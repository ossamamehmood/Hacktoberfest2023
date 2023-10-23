package models

import "time"

// User is a struct representing the user table in the datbase which contians information
// about the reigstred users that are in the platform
type User struct {
	ID         uint64     `gorm:"primaryKey;autoIncrement:true"`
	Name       string     `gorm:"type:varchar(100);not null"`
	Username   string     `gorm:"type:varchar(100);uniqueIndex;not null"`
	PhotoURL   string     `gorm:"type:varchar(200);not null"`
	Email      string     `gorm:"type:varchar(200);index"`
	Role       *string    `gorm:"type:varchar(50);default:'user';not null"`
	Provider   *string    `gorm:"type:varchar(50);default:'local';not null"`
	ProviderID string     `gorm:"type:varchar(100)"`
	Verified   *bool      `gorm:"not null;default:false"`
	CreatedAt  *time.Time `gorm:"autoCreateTime:true;not null"`
	UpdatedAt  *time.Time `gorm:"autoUpdateTime:true;not null"`

	Sessions []Sessions `gorm:"foreignKey:UserID"`
	Links    []Link     `gorm:"foreignKey:UserID"`
}

const (
	// revive:disable
	GithubProvider = "github"
	// revive:enable
)
