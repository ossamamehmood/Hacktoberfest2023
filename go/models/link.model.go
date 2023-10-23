package models

// Link represents the Link table in the database which represents all the links that the user have shortned
type Link struct {
	ID     uint64 `gorm:"primaryKey;autoIncrement:true"`
	UserID uint64 `gorm:"not null,index"`
	URL    string `gorm:"type:varchar(255);not null"`
	Key    string `gorm:"type:varchar(100);uniqueIndex;not null"`
}
