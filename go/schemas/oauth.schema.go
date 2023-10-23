package schemas

// BasicOAuthProvider contains all the feilds realted to oauth providers
type BasicOAuthProvider struct {
	ID       string
	Name     string
	Username string
	Email    *string
	PhotoURL string
}

// Github struct contains the schema of the data that is provided by Github
type Github struct {
	ID        int     `json:"id"`
	Name      string  `json:"name"`
	Username  string  `json:"login"`
	AvatarURL string  `json:"avatar_url"`
	Email     *string `json:"email"`
}

// GetEmailFromPayload is a fucntion to get the Email from the payload that is received from Github
func (Github) GetEmailFromPayload(payload map[string]interface{}) *string {
	if email, ok := payload["email"].(*string); ok && email != nil {
		return email
	}

	return nil
}
