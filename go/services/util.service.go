package services

import (
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"gorm.io/gorm"
)

// Paginate is a function to paginate the queries
func Paginate(h *initializers.H, page, limit int) func(db *gorm.DB) *gorm.DB {
	return func(db *gorm.DB) *gorm.DB {
		offset := (page - 1) * limit
		return db.Offset(offset).Limit(limit + 1)
	}
}
