package schemas

import (
	"github.com/VinukaThejana/link-shortner/backend/models"
)

// User contians the most essential details of the user that should be available to the public
type User struct {
	ID         uint64 `json:"id"`
	Name       string `json:"name"`
	Username   string `json:"username"`
	Email      string `json:"email"`
	PhotoURL   string `json:"photo_url"`
	Role       string `json:"role"`
	Provider   string `json:"provider"`
	ProviderID string `json:"provider_id"`
}

// FilterUserRecord filter the user data that is fetched from the database so that it is in the
// most user secure way possible
func FilterUserRecord(user models.User) *User {
	return &User{
		ID:         user.ID,
		Name:       user.Name,
		Username:   user.Username,
		PhotoURL:   user.PhotoURL,
		Email:      user.Email,
		Role:       *user.Role,
		Provider:   *user.Provider,
		ProviderID: user.ProviderID,
	}
}
