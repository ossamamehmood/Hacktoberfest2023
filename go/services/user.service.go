package services

import (
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/models"
	"gorm.io/gorm"
)

// User is a struct that contains user related services
type User struct {
	H *initializers.H
}

// IsUsernameAvailable is a function that is used to check if wether a given username is available or not
// within the platform
//
// returns `true`  - if the username is free to use
//
// returns `false` - if the username is not free to use
func (u *User) IsUsernameAvailable(username string) (bool, error) {
	var user models.User
	err := u.H.DB.DB.Select("username").Where(&models.User{Username: username}).First(&user).Error
	if err != nil {
		if err != gorm.ErrRecordNotFound {
			return false, err
		}

		return true, nil
	}

	return false, nil
}

// IsEmailAvailable is a fucntion to check wether the email address is available and wether the concerned email address is verified or not
//
// returns `true`  - if the email is free to use
//
// returns `false` - if the email is not free to use
func (u *User) IsEmailAvailable(email string) (id *uint64, isAvailable bool, isVerified bool, provider *string, err error) {
	var user models.User
	err = u.H.DB.DB.Select("id", "email", "verified").Where(&models.User{Email: email}).First(&user).Error
	if err != nil {
		if err != gorm.ErrRecordNotFound {
			return nil, false, false, nil, err
		}

		return nil, true, false, nil, nil
	}

	return &user.ID, false, *user.Verified, user.Provider, nil
}

// Create is a function that is used to create a newUser in the database
func (u *User) Create(user models.User) (newUser models.User, err error) {
	newUser = user
	err = u.H.DB.DB.Create(&newUser).Error
	if err != nil {
		return models.User{}, err
	}

	return newUser, nil
}
