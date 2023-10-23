package controllers

import (
	"fmt"
	"net/url"

	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/schemas"
	"github.com/VinukaThejana/link-shortner/backend/services"
	"github.com/VinukaThejana/link-shortner/backend/utils"
	"github.com/gofiber/fiber/v2"
)

// OAuth contains oauth releated controllers
type OAuth struct {
	H   *initializers.H
	Env *config.Env
}

// RedirectToGitHubOAuthFlow redirect the user to the Github reidrect URL to login with Github
func (o *OAuth) RedirectToGitHubOAuthFlow(c *fiber.Ctx) error {
	env := o.Env

	options := url.Values{
		"client_id":    []string{env.GithubClientID},
		"redirect_url": []string{env.GithubRedirectURL},
		"scope":        []string{"user:email"},
		"state":        []string{env.GithubFromURL},
	}

	githubRedirectURL := fmt.Sprintf("%s?%s", env.GithubRootURL, options.Encode())
	return c.Redirect(githubRedirectURL)
}

// GithubOAuthCalback is a function that is used by Github to provide a unique code for the user who just tried
// to login
func (o *OAuth) GithubOAuthCalback(c *fiber.Ctx) error {
	h := o.H
	env := o.Env

	code := c.Query("code")
	if code == "" {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	state := c.Query("state")
	if state == "" {
		state = env.FrontEndDomain
	} else if state == env.Domain {
		state = env.FrontEndDomain
	}

	accessToken, err := utils.OAuth{}.GetGithubAccessToken(code, env)
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	userDetails, err := utils.OAuth{}.GetGithubUser(*accessToken)
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	fmt.Println(*userDetails, userDetails.ID)

	githubS := services.Github{H: h}

	user, err := githubS.GithubOAuth(*userDetails)
	if err != nil {
		if err != errors.ErrBadRequest {
			log.Error(err, nil)
		}

		return c.Redirect(state)
	}

	go func() {
		utils.Token{}.DeleteExpiredTokens(h, user.ID)
	}()

	accessTokenDetails, err := utils.Token{}.CreateAccessToken(h, user.ID, env.AccessTokenPrivateKey, env.AccessTokenExpires)
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	refreshTokenDetails, err := utils.Token{}.CreateRefreshToken(h, user.ID, env.RefreshTokenPrivateKey, env.RefreshTokenExpires, struct {
		IPAddress       string
		Location        string
		Device          string
		OS              string
		AccessTokenUUID string
	}{
		AccessTokenUUID: accessTokenDetails.TokenUUID,
	})
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	sessionTokenDetails, err := utils.Token{}.CreateSessionToken(schemas.FilterUserRecord(user), env.SessionTokenSecret, env.RefreshTokenExpires)
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	c.Cookie(&fiber.Cookie{
		Name:     "access_token",
		Value:    *accessTokenDetails.Token,
		Path:     "/",
		MaxAge:   env.AccessTokenMaxAge * 60,
		Secure:   false,
		HTTPOnly: false,
		Domain:   "localhost",
	})

	c.Cookie(&fiber.Cookie{
		Name:     "refresh_token",
		Value:    *refreshTokenDetails.Token,
		Path:     "/",
		MaxAge:   env.RefreshTokenMaxAge * 60,
		Secure:   false,
		HTTPOnly: true,
		Domain:   "localhost",
	})

	c.Cookie(&fiber.Cookie{
		Name:     "session",
		Value:    *sessionTokenDetails.Token,
		Path:     "/",
		MaxAge:   env.RefreshTokenMaxAge * 60,
		Secure:   false,
		HTTPOnly: false,
		Domain:   "localhost",
	})

	return c.Redirect(state)
}
