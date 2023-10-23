// Package errors contains all the errrors that should be handled
package errors

import "fmt"

var (
	//revive:disable
	ErrInternalServerError       = fmt.Errorf("internal_server_error")
	ErrUnauthorized              = fmt.Errorf("unauthorized")
	ErrAccessTokenNotProvided    = fmt.Errorf("access_token_not_provided")
	ErrBadRequest                = fmt.Errorf("bad_request")
	ErrIncorrectCredentials      = fmt.Errorf("incorrect_credentials")
	ErrRefreshTokenExpired       = fmt.Errorf("refresh_token_expired")
	ErrAccessTokenExpired        = fmt.Errorf("access_token_expired")
	ErrUsernameAlreadyUsed       = fmt.Errorf("username_already_used")
	ErrEmailAlreadyUsed          = fmt.Errorf("email_already_used")
	ErrEmailConfirmationExpired  = fmt.Errorf("email_confirmation_expired")
	ErrHaveAnAccountWithTheEmail = fmt.Errorf("already_have_an_account")
	ErrAddAUsername              = fmt.Errorf("add_a_username")
	ErrKeyAlreadyUsed            = fmt.Errorf("key_already_used")
	ErrKeyDoesNotExsist          = fmt.Errorf("key_does_not_exsist")
	Okay                         = "okay"
	//revive:enable
)

// CheckTokenError is a struct to check token related errors
type CheckTokenError struct{}

// Expired is a function to check wether the token has expired
func (CheckTokenError) Expired(err error) bool {
	if err.Error() == "token has invalid claims: token is expired" {
		return true
	}

	return false
}
