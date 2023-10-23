package controllers

import (
	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/models"
	"github.com/VinukaThejana/link-shortner/backend/services"
	"github.com/VinukaThejana/link-shortner/backend/utils"
	"github.com/gofiber/fiber/v2"
	"gorm.io/gorm"
)

// User contains all the user related controllers
type User struct {
	H   *initializers.H
	Env *config.Env
}

// GetMe is a function to get the user details of the currently logged in user
func (u *User) GetMe(c *fiber.Ctx) error {
	user, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(user)
}

// CheckUsername is a function to check wether the username is availale or not
func (u *User) CheckUsername(c *fiber.Ctx) error {
	h := u.H

	var payload struct {
		Username string `json:"username"`
	}

	if err := c.BodyParser(&payload); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	type response struct {
		Available bool `json:"available"`
	}

	userS := services.User{H: h}

	available, err := userS.IsUsernameAvailable(payload.Username)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Available: false,
		})
	}

	return c.Status(fiber.StatusOK).JSON(response{
		Available: available,
	})
}

// UpdateEmail is a function that is used to update the email of the user
func (u *User) UpdateEmail(c *fiber.Ctx) error {
	h := u.H
	env := u.Env

	var payload struct {
		Email string `json:"email" validate:"required,email"`
	}

	if err := c.BodyParser(&payload); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	if ok := log.Validate(payload); !ok {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	var user models.User
	err := h.DB.DB.First(&user, "email = ?", payload.Email).Error
	if err != nil {
		if err != gorm.ErrRecordNotFound {
			log.Error(err, nil)
			return c.Status(fiber.StatusInternalServerError).JSON(response{
				Status: errors.ErrInternalServerError.Error(),
			})
		}

		return c.Status(fiber.StatusOK).JSON(response{
			Status: errors.ErrEmailAlreadyUsed.Error(),
		})
	}

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	verifed := true
	err = h.DB.DB.Model(&models.User{}).Where(&models.User{ID: userD.ID}).Updates(models.User{
		Email:    payload.Email,
		Verified: &verifed,
	}).Error
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	userD.Email = payload.Email
	sessionTokenDetails, err := utils.Token{}.CreateSessionToken(userD, env.SessionTokenSecret, env.RefreshTokenExpires)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	c.Cookie(&fiber.Cookie{
		Name:     "session",
		Value:    *sessionTokenDetails.Token,
		Path:     "/",
		MaxAge:   env.RefreshTokenMaxAge * 60,
		Secure:   false,
		HTTPOnly: false,
		Domain:   "localhost",
	})

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// UpdateUsername is a function to change the username of the username to another valid username
func (u *User) UpdateUsername(c *fiber.Ctx) error {
	h := u.H

	var payload struct {
		Username string `json:"username" validate:"required,min=3,max=15"`
	}

	if err := c.BodyParser(&payload); err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	if ok := log.Validate(payload); !ok {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	userS := services.User{H: h}

	available, err := userS.IsUsernameAvailable(payload.Username)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	if !available {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrUsernameAlreadyUsed.Error(),
		})
	}

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	err = h.DB.DB.Model(&models.User{}).Where(&models.User{ID: userD.ID}).Update("username", payload.Username).Error
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// UpdateName is a function to update the name of the user
func (u *User) UpdateName(c *fiber.Ctx) error {
	h := u.H

	var payload struct {
		Name string `json:"name" validate:"required,min=3,max=50"`
	}

	if err := c.BodyParser(&payload); err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	if ok := log.Validate(payload); !ok {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	err = h.DB.DB.Model(&models.User{}).Where(&models.User{
		ID: userD.ID,
	}).Update("name = ?", payload.Name).Error
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}
	userD.Name = payload.Name

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}
