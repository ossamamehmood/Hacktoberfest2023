package controllers

import (
	"context"
	"encoding/json"
	"time"

	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/utils"
	"github.com/gofiber/fiber/v2"
	"github.com/redis/go-redis/v9"
)

// Auth is a struct containing the Auth controllers
type Auth struct {
	H   *initializers.H
	Env *config.Env
}

// RefreshToken is a function that is used to refresh the access token by providing the refresh token
func (a *Auth) RefreshToken(c *fiber.Ctx) error {
	h := a.H
	env := a.Env

	refreshToken := c.Cookies("refresh_token")
	if refreshToken == "" {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	tokenClaims, _, err := utils.Token{}.ValidateRefreshToken(h, refreshToken, env.RefreshTokenPublicKey)
	if err != nil {
		if err == errors.ErrUnauthorized {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: err.Error(),
			})
		}

		if ok := (errors.CheckTokenError{}.Expired(err)); !ok {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrRefreshTokenExpired.Error(),
			})
		}

		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	ctx := context.TODO()

	data := h.R.RS.Get(ctx, tokenClaims.TokenUUID).Val()
	if data == "" {
		return c.Status(fiber.StatusUnauthorized).JSON(response{
			Status: errors.ErrUnauthorized.Error(),
		})
	}
	var payload struct {
		UserID          string `json:"UserID"`
		AccessTokenUUID string `json:"AccessTokenUUID"`
	}
	err = json.Unmarshal([]byte(data), &payload)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}
	err = h.R.RS.Del(ctx, payload.AccessTokenUUID).Err()
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	accessTokenDetails, err := utils.Token{}.CreateAccessToken(h, tokenClaims.UserID, env.AccessTokenPrivateKey, env.AccessTokenExpires)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	payloadByte, err := json.Marshal(payload)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	err = h.R.RS.Set(ctx, tokenClaims.TokenUUID, string(payloadByte), redis.KeepTTL).Err()
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
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

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// Logout is a function that is used to logout the user from the application
func (a *Auth) Logout(c *fiber.Ctx) error {
	h := a.H
	env := a.Env

	state := c.Query("state")
	if state == "" {
		state = env.FrontEndDomain
	}

	refreshToken := c.Cookies("refresh_token")
	if refreshToken == "" {
		return c.Redirect(state)
	}

	tokenDetails, tokenValue, err := utils.Token{}.ValidateRefreshToken(h, refreshToken, env.RefreshTokenPublicKey)
	if err != nil {
		if err == errors.ErrUnauthorized {
			return c.Redirect(state)
		}

		if ok := (errors.CheckTokenError{}.Expired(err)); !ok {
			return c.Redirect(state)
		}

		log.Error(err, nil)
		return c.Redirect(state)
	}

	err = utils.Token{}.DeleteToken(h, tokenDetails.TokenUUID, tokenValue.AccessTokenUUID)
	if err != nil {
		log.Error(err, nil)
		return c.Redirect(state)
	}

	expired := time.Now().Add(-time.Hour * 24)

	c.Cookie(&fiber.Cookie{
		Name:    "access_token",
		Value:   "",
		Expires: expired,
	})
	c.Cookie(&fiber.Cookie{
		Name:    "refresh_token",
		Value:   "",
		Expires: expired,
	})
	c.Cookie(&fiber.Cookie{
		Name:    "session",
		Value:   "",
		Expires: expired,
	})

	return c.Redirect(state)
}
