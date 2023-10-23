package controllers

import (
	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/services"
	"github.com/VinukaThejana/link-shortner/backend/utils"
	"github.com/gofiber/fiber/v2"
	"github.com/lithammer/shortuuid/v4"
	"gorm.io/gorm"
)

// Links contains all the operations that are related to links
type Links struct {
	H   *initializers.H
	Env *config.Env
}

// CheckKey is a function that is used to check wether a given key is used previously
// in the database
func (l *Links) CheckKey(c *fiber.Ctx) error {
	h := l.H

	var payload struct {
		Key string `json:"key" validate:"required,min=3,max=20"`
	}

	type res struct {
		Available bool `json:"available"`
	}

	if err := c.BodyParser(&payload); err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusBadRequest).JSON(res{
			Available: false,
		})
	}

	if ok := log.Validate(payload); !ok {
		return c.Status(fiber.StatusBadRequest).JSON(res{
			Available: false,
		})
	}

	regex := utils.Regex{}
	if !regex.IsKeyValid(payload.Key) {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	linkS := services.Link{
		H: h,
	}

	ok, err := linkS.IsKeyAvailable(payload.Key)
	if err != nil {
		log.Error(err, nil)
		c.Status(fiber.StatusInternalServerError).JSON(res{
			Available: false,
		})
	}

	return c.Status(fiber.StatusOK).JSON(res{
		Available: ok,
	})
}

// New create a new link with the key or without the key
func (l *Links) New(c *fiber.Ctx) error {
	h := l.H

	var payload struct {
		Link string `json:"link" validate:"required,url"`
		Key  string `json:"key" validate:"omitempty,min=2,max=25"`
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

	if payload.Key != "" {
		regex := utils.Regex{}
		if !regex.IsKeyValid(payload.Key) {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrBadRequest.Error(),
			})
		}
	}

	linkS := services.Link{H: h}
	key := ""

	if payload.Key == "" {
		for i := 1; i <= 4; i++ {
			newKey := shortuuid.New()
			ok, err := linkS.IsKeyAvailable(newKey)
			if err != nil {
				log.Error(err, nil)
				break
			}

			if ok {
				key = newKey
				break
			}
		}

		if key == "" {
			return c.Status(fiber.StatusInternalServerError).JSON(response{
				Status: errors.ErrInternalServerError.Error(),
			})
		}
	} else {
		ok, err := linkS.IsKeyAvailable(payload.Key)
		if err != nil {
			log.Error(err, nil)
			return c.Status(fiber.StatusInternalServerError).JSON(response{
				Status: errors.ErrInternalServerError.Error(),
			})
		}

		if !ok {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrKeyAlreadyUsed.Error(),
			})
		}

		key = payload.Key
	}

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	err = linkS.Create(userD, payload.Link, key)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"status": errors.Okay,
		"key":    key,
		"url":    payload.Link,
	})
}

// GetLinks is a function to get all the links created by the user
func (l *Links) GetLinks(c *fiber.Ctx) error {
	h := l.H

	page := c.QueryInt("page", 1)
	limit := c.QueryInt("limit", 10)

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	linkS := services.Link{H: h}

	links, err := linkS.GetLinks(userD, page, limit)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	if len(links) == limit+1 {
		links = links[:len(links)-1]
		return c.Status(fiber.StatusOK).JSON(fiber.Map{
			"data":     links,
			"nextPage": page + 1,
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"data":     links,
		"nextPage": nil,
	})
}

// DeleteLink is a function to delete a link with a given key
func (l *Links) DeleteLink(c *fiber.Ctx) error {
	h := l.H

	var payload struct {
		Key string `json:"key" validate:"required,min=3"`
	}

	if err := c.BodyParser(&payload); err != nil {
		log.Error(err, nil)
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

	linkS := services.Link{H: h}
	err = linkS.DeleteLink(userD, payload.Key)
	if err != nil {
		if err == gorm.ErrRecordNotFound {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrKeyDoesNotExsist.Error(),
			})
		}

		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// DeleteLinks is a function that is used to delete all the links that belong to the user
func (l *Links) DeleteLinks(c *fiber.Ctx) error {
	h := l.H

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	linkS := services.Link{H: h}
	err = linkS.DeleteLinks(userD)
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

// Update is a function to update the Link and the Key in the database
func (l *Links) Update(c *fiber.Ctx) error {
	h := l.H

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	var payload struct {
		InitialKey string `json:"initial_key" validate:"required,min=2,max=25"`
		NewKey     string `json:"new_key" validate:"required,min=2,max=25"`
		URL        string `json:"url" validate:"required,url"`
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

	regex := utils.Regex{}
	if !regex.IsKeyValid(payload.InitialKey) || !regex.IsKeyValid(payload.NewKey) {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	linkS := services.Link{
		H: h,
	}

	err = linkS.Update(userD, payload.InitialKey, payload.NewKey, payload.URL)
	if err != nil {
		log.Error(err, nil)
		if err == gorm.ErrRecordNotFound {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrBadRequest.Error(),
			})
		}

		if err == gorm.ErrDuplicatedKey {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrKeyAlreadyUsed.Error(),
			})
		}

		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// UpdateKey is a function that is used to update the shortned key of the link
func (l *Links) UpdateKey(c *fiber.Ctx) error {
	h := l.H

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	var payload struct {
		InitialKey string `json:"initial_key" validate:"required,min=2,max=25"`
		NewKey     string `json:"new_key" validate:"required,min=2,max=25"`
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

	regex := utils.Regex{}
	if !regex.IsKeyValid(payload.InitialKey) || !regex.IsKeyValid(payload.NewKey) {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	linkS := services.Link{
		H: h,
	}

	err = linkS.UpdateKey(userD, payload.InitialKey, payload.NewKey)
	if err != nil {
		log.Error(err, nil)
		if err == gorm.ErrRecordNotFound {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrBadRequest.Error(),
			})
		}

		if err == gorm.ErrDuplicatedKey {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrKeyAlreadyUsed.Error(),
			})
		}

		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})

	}

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}

// UpdateURL is a function that is used to update the URL of the shortned link that is saved in the datbase
func (l *Links) UpdateURL(c *fiber.Ctx) error {
	h := l.H

	userD, err := utils.Session{}.Get(c)
	if err != nil {
		log.Error(err, nil)
		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	var payload struct {
		Key string `json:"key" validate:"required,min=2,max=25"`
		URL string `json:"url" validate:"required,url"`
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

	regex := utils.Regex{}
	if !regex.IsKeyValid(payload.Key) {
		return c.Status(fiber.StatusBadRequest).JSON(response{
			Status: errors.ErrBadRequest.Error(),
		})
	}

	linkS := services.Link{
		H: h,
	}

	err = linkS.UpdateURL(userD, payload.Key, payload.URL)
	if err != nil {
		log.Error(err, nil)
		if err == gorm.ErrRecordNotFound {
			return c.Status(fiber.StatusBadRequest).JSON(response{
				Status: errors.ErrBadRequest.Error(),
			})
		}

		return c.Status(fiber.StatusInternalServerError).JSON(response{
			Status: errors.ErrInternalServerError.Error(),
		})
	}

	return c.Status(fiber.StatusOK).JSON(response{
		Status: errors.Okay,
	})
}
