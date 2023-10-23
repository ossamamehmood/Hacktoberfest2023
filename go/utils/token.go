package utils

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"strconv"
	"time"

	"github.com/VinukaThejana/link-shortner/backend/errors"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/models"
	"github.com/VinukaThejana/link-shortner/backend/schemas"
	"github.com/gofiber/fiber/v2/log"
	"github.com/golang-jwt/jwt/v5"
	"github.com/google/uuid"
	"gorm.io/gorm"
)

// Token contains all the token related operations
type Token struct{}

// TokenDetails is a struct that contains details that should be included in the token
type TokenDetails struct {
	Token     *string
	TokenUUID string
	UserID    uint64
	ExpiresIn *int64
}

// CreateRefreshToken is a function that is used to create a refresh token
func (Token) CreateRefreshToken(h *initializers.H, userID uint64, privateKey string, ttl time.Duration, reqData struct {
	IPAddress       string
	Location        string
	Device          string
	OS              string
	AccessTokenUUID string
},
) (*TokenDetails, error) {
	var refreshTokenDetails schemas.RefreshTokenDetails

	uid, err := uuid.NewUUID()
	if err != nil {
		return nil, err
	}

	now := time.Now().UTC()
	td := &TokenDetails{
		ExpiresIn: new(int64),
		Token:     new(string),
	}

	*td.ExpiresIn = now.Add(ttl).Unix()
	td.TokenUUID = uid.String()
	td.UserID = userID

	decodedPrivateKey, err := base64.StdEncoding.DecodeString(privateKey)
	if err != nil {
		return nil, err
	}

	key, err := jwt.ParseRSAPrivateKeyFromPEM(decodedPrivateKey)
	if err != nil {
		return nil, err
	}

	claims := make(jwt.MapClaims)
	claims["sub"] = userID
	claims["token_uuid"] = td.TokenUUID
	claims["exp"] = td.ExpiresIn
	claims["iat"] = now.Unix()
	claims["nbf"] = now.Unix()

	*td.Token, err = jwt.NewWithClaims(jwt.SigningMethodRS256, claims).SignedString(key)
	if err != nil {
		return nil, err
	}

	refreshTokenDetails = schemas.RefreshTokenDetails{
		UserID:          userID,
		AccessTokenUUID: reqData.AccessTokenUUID,
	}

	tokenVal, err := json.Marshal(refreshTokenDetails)
	if err != nil {
		return nil, err
	}

	err = h.DB.DB.Create(&models.Sessions{
		UserID:    userID,
		TokenID:   uid.String(),
		IPAddress: "",
		Location:  "",
		OS:        "",
		Device:    "",
		LoginAt:   time.Now().UTC(),
		ExpiresAt: *td.ExpiresIn,
	}).Error
	if err != nil {
		return nil, err
	}

	ctx := context.TODO()
	h.R.RS.Set(ctx, td.TokenUUID, string(tokenVal), time.Unix(*td.ExpiresIn, 0).Sub(now))

	return td, nil
}

// CreateAccessToken is a function that is used to create access tokens
func (Token) CreateAccessToken(h *initializers.H, userID uint64, privateKey string, ttl time.Duration) (*TokenDetails, error) {
	uid, err := uuid.NewUUID()
	if err != nil {
		return nil, err
	}

	now := time.Now().UTC()
	td := &TokenDetails{
		ExpiresIn: new(int64),
		Token:     new(string),
	}

	*td.ExpiresIn = now.Add(ttl).Unix()
	td.TokenUUID = uid.String()
	td.UserID = userID

	decodedPrivateKey, err := base64.StdEncoding.DecodeString(privateKey)
	if err != nil {
		return nil, err
	}

	key, err := jwt.ParseRSAPrivateKeyFromPEM(decodedPrivateKey)
	if err != nil {
		return nil, err
	}

	claims := make(jwt.MapClaims)
	claims["sub"] = userID
	claims["token_uuid"] = td.TokenUUID
	claims["exp"] = td.ExpiresIn
	claims["iat"] = now.Unix()
	claims["nbf"] = now.Unix()

	*td.Token, err = jwt.NewWithClaims(jwt.SigningMethodRS256, claims).SignedString(key)
	if err != nil {
		return nil, err
	}

	ctx := context.TODO()
	h.R.RS.Set(ctx, td.TokenUUID, userID, time.Unix(*td.ExpiresIn, 0).Sub(now))

	return td, nil
}

// ValidateRefreshToken is a function that is used to validate the refresh token
func (Token) ValidateRefreshToken(h *initializers.H, token, publicKey string) (*TokenDetails, *schemas.RefreshTokenDetails, error) {
	td, val, err := validateToken(h, token, publicKey)
	if err != nil {
		return nil, nil, err
	} else if val == nil {
		return nil, nil, errors.ErrInternalServerError
	}

	var refreshTokenDetails schemas.RefreshTokenDetails
	err = json.Unmarshal([]byte(*val), &refreshTokenDetails)
	if err != nil {
		return nil, nil, errors.ErrInternalServerError
	}

	if refreshTokenDetails.UserID == td.UserID {
		return td, &refreshTokenDetails, nil
	}

	return nil, nil, errors.ErrUnauthorized
}

// ValidateAccessToken is a function  that is used to validate the access token
func (Token) ValidateAccessToken(h *initializers.H, token, publicKey string) (*TokenDetails, error) {
	td, val, err := validateToken(h, token, publicKey)
	if err != nil {
		return nil, err
	} else if val == nil {
		return nil, errors.ErrInternalServerError
	}

	userID, err := strconv.ParseUint(*val, 10, 64)
	if err != nil {
		return nil, errors.ErrInternalServerError
	}

	if userID == td.UserID {
		return td, nil
	}

	return nil, errors.ErrUnauthorized
}

// DeleteToken the given access token and the refresh token
func (Token) DeleteToken(h *initializers.H, refreshTokenUUID, accessTokenUUID string) error {
	err := h.DB.DB.Delete(&models.Sessions{
		TokenID: refreshTokenUUID,
	}).Error
	if err != nil {
		if err == gorm.ErrRecordNotFound {
			return errors.ErrUnauthorized
		}

		return err
	}

	ctx := context.TODO()
	pipe := h.R.RS.Pipeline()
	pipe.Del(ctx, refreshTokenUUID)
	pipe.Del(ctx, accessTokenUUID)
	_, err = pipe.Exec(ctx)
	if err != nil {
		return err
	}

	return nil
}

func validateToken(h *initializers.H, token, publicKey string) (*TokenDetails, *string, error) {
	decodedPublicKey, err := base64.StdEncoding.DecodeString(publicKey)
	if err != nil {
		return nil, nil, err
	}

	key, err := jwt.ParseRSAPublicKeyFromPEM(decodedPublicKey)
	if err != nil {
		return nil, nil, err
	}

	parsedToken, err := jwt.Parse(token, func(t *jwt.Token) (interface{}, error) {
		if _, ok := t.Method.(*jwt.SigningMethodRSA); !ok {
			return nil, fmt.Errorf("Unexpected method : %s", t.Header["alg"])
		}

		return key, nil
	})
	if err != nil {
		return nil, nil, err
	}

	claims, ok := parsedToken.Claims.(jwt.MapClaims)
	if !ok || !parsedToken.Valid {
		return nil, nil, fmt.Errorf("Validate : invalid token")
	}

	userID, err := strconv.ParseUint(fmt.Sprint(claims["sub"]), 10, 64)
	if err != nil {
		return nil, nil, err
	}

	td := &TokenDetails{
		TokenUUID: fmt.Sprint(claims["token_uuid"]),
		UserID:    userID,
	}

	ctx := context.TODO()
	val := h.R.RS.Get(ctx, td.TokenUUID).Val()
	if val == "" {
		return nil, nil, errors.ErrUnauthorized
	}

	return td, &val, nil
}

// CreateSessionToken is a function that is used to create a new session token for the user
func (Token) CreateSessionToken(user *schemas.User, privateKey string, ttl time.Duration) (*TokenDetails, error) {
	if user == nil {
		return nil, fmt.Errorf("no user was provided")
	}

	uid, err := uuid.NewUUID()
	if err != nil {
		return nil, err
	}

	now := time.Now().UTC()
	td := &TokenDetails{
		ExpiresIn: new(int64),
		Token:     new(string),
	}

	*td.ExpiresIn = now.Add(ttl).Unix()
	td.TokenUUID = uid.String()
	td.UserID = user.ID

	claims := make(jwt.MapClaims)
	claims["sub"] = user.ID
	claims["token_uuid"] = td.TokenUUID
	claims["exp"] = td.ExpiresIn
	claims["iat"] = now.Unix()
	claims["nbf"] = now.Unix()
	claims["name"] = user.Name
	claims["username"] = user.Username
	claims["photo_url"] = user.PhotoURL
	claims["email"] = user.Email
	claims["role"] = user.Role
	claims["provider"] = user.Provider
	claims["provider_id"] = user.ProviderID

	*td.Token, err = jwt.NewWithClaims(jwt.SigningMethodHS256, claims).SignedString([]byte(privateKey))
	if err != nil {
		return nil, err
	}

	return td, nil
}

// ValidateSessionToken is a function that is used to validate the session token
func (Token) ValidateSessionToken(tokenStr, privateKey string) (*jwt.Token, error) {
	token, err := jwt.Parse(tokenStr, func(t *jwt.Token) (interface{}, error) {
		if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("Unexpected signing method")
		}

		return []byte(privateKey), nil
	})
	if err != nil {
		return nil, err
	}

	return token, nil
}

// SessionToken is a function that conatins actions related to the user session token
type SessionToken struct{}

// GetUserDetails is a function that allows to get the user details from the session token
func (SessionToken) GetUserDetails(token *jwt.Token) (user *schemas.User, err error) {
	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return nil, fmt.Errorf("Error getting the claims from the token")
	}
	userID := uint64(claims["sub"].(float64))
	if err != nil {
		return nil, err
	}

	return &schemas.User{
		ID:         userID,
		Username:   claims["username"].(string),
		Name:       claims["name"].(string),
		Email:      claims["email"].(string),
		PhotoURL:   claims["photo_url"].(string),
		Role:       claims["role"].(string),
		Provider:   claims["provider"].(string),
		ProviderID: claims["provider_id"].(string),
	}, nil
}

// DeleteExpiredTokens is a function that is used to delete expired tokens as a background task
func (Token) DeleteExpiredTokens(h *initializers.H, userID uint64) {
	var sessions []models.Sessions
	err := h.DB.DB.Where("user_id = ? AND expires_at <= ?", userID, time.Now().UTC().Unix()).Error
	if err != nil {
		log.Error(err, nil)
		return
	}

	if len(sessions) == 0 {
		return
	}

	err = h.DB.DB.Where("1 = 1").Delete(&sessions).Error
	if err != nil {
		log.Error(err, nil)
		return
	}

	return
}
