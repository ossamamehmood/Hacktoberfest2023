package utils

import (
	"github.com/VinukaThejana/link-shortner/backend/schemas"
	"github.com/gofiber/fiber/v2"
)

// Session is to maintain the session of the current user
type Session struct{}

// Add add the user details to the fiber ctx session
func (Session) Add(c *fiber.Ctx, user *schemas.User) {
	if user == nil {
		return
	}

	c.Locals("id", user.ID)
	c.Locals("name", user.Name)
	c.Locals("username", user.Username)
	c.Locals("photoURL", user.PhotoURL)
	c.Locals("email", user.Email)
	c.Locals("role", user.Role)
	c.Locals("provider", user.Provider)
	c.Locals("providerID", user.ProviderID)
	return
}

// Get the user from the go fiber ctx session
func (Session) Get(c *fiber.Ctx) (*schemas.User, error) {
	userID := c.Locals("id").(uint64)

	return &schemas.User{
		ID:         userID,
		Name:       c.Locals("name").(string),
		Username:   c.Locals("username").(string),
		PhotoURL:   c.Locals("photoURL").(string),
		Email:      c.Locals("email").(string),
		Role:       c.Locals("role").(string),
		Provider:   c.Locals("provider").(string),
		ProviderID: c.Locals("providerID").(string),
	}, nil
}
