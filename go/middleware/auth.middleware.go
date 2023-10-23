package middleware

import (
	"strings"

	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/utils"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/log"
)

// Auth related middleware actions
type Auth struct {
	H   *initializers.H
	Env *config.Env
}

// CheckAuth is a middleware to check wether the users are authenticated or not
func (a *Auth) CheckAuth(c *fiber.Ctx) error {
	h := a.H
	env := a.Env

	var accessToken string
	authorization := c.Get("Authorization")

	if strings.HasPrefix(authorization, "Bearer ") {
		accessToken = strings.TrimPrefix(authorization, "Bearer ")
	} else {
		if c.Cookies("access_token") != "" {
			accessToken = c.Cookies("access_token")
		} else {
			return c.Status(fiber.StatusForbidden).JSON(response{
				Status: errors.ErrAccessTokenNotProvided.Error(),
			})
		}
	}

	if accessToken == "" {
		return c.Status(fiber.StatusForbidden).JSON(response{
			Status: errors.ErrAccessTokenNotProvided.Error(),
		})
	}

	_, err := utils.Token{}.ValidateAccessToken(h, accessToken, env.AccessTokenPublicKey)
	if err != nil {
		if err == errors.ErrUnauthorized {
			return c.Status(fiber.StatusUnauthorized).JSON(response{
				Status: errors.ErrUnauthorized.Error(),
			})
		}

		if ok := (errors.CheckTokenError{}.Expired(err)); ok {
			return c.Status(fiber.StatusUnauthorized).JSON(response{
				Status: errors.ErrAccessTokenExpired.Error(),
			})
		}

		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	sessionCookie := c.Cookies("session")
	if sessionCookie == "" {
		return c.Status(fiber.StatusUnauthorized).JSON(response{
			Status: errors.ErrUnauthorized.Error(),
		})
	}

	session, err := utils.Token{}.ValidateSessionToken(sessionCookie, env.SessionTokenSecret)
	if err != nil {
		if err == errors.ErrBadRequest {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrBadRequest.Error(),
			})
		}

		if ok := (errors.CheckTokenError{}.Expired(err)); !ok {
			return c.Status(fiber.StatusUnauthorized).JSON(response{
				Status: errors.ErrAccessTokenExpired.Error(),
			})
		}

		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	user, err := utils.SessionToken{}.GetUserDetails(session)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	utils.Session{}.Add(c, user)

	return c.Next()
}
