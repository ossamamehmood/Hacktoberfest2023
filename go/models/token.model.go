package models

import "time"

// Sessions is a struct that represents the sessions table in the database which is used to store details
// about the sessions that are provided to the user
type Sessions struct {
	TokenID   string `gorm:"primaryKey"`
	UserID    uint64 `gorm:"not null"`
	IPAddress string
	Location  string
	Device    string
	OS        string
	LoginAt   time.Time `gorm:"autoCreateTime:true;not null"`
	ExpiresAt int64     `gorm:"not null"`
}
