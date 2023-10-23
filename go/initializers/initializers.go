// Package initializers contains connections to various thrid party apis
package initializers

import "github.com/VinukaThejana/go-utils/logger"

var log logger.Logger

// H contains connections to various thrid party services
type H struct {
	S  *Storage
	DB *DB
	R  *Redis
}
