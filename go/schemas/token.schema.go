package schemas

// RefreshTokenDetails contains the schema about the refresh token
type RefreshTokenDetails struct {
	UserID          uint64
	AccessTokenUUID string
}
