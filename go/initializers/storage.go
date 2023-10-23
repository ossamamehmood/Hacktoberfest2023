package initializers

import (
	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/gofiber/storage/redis"
)

// Storage contains the connection to the Redis ratelimiter storage
type Storage struct {
	S *redis.Storage
}

// InitStorage intialize connection to the Redis ratelimiting storage
func (h *H) InitStorage(env *config.Env) {
	store := redis.New(redis.Config{
		Username: env.RedisRatelimiterUsername,
		Password: env.RedisRatelimiterPassword,
		Host:     env.RedisRatelimiterHost,
		Port:     env.RedisRatelimiterPort,
	})

	h.S = &Storage{
		S: store,
	}
}
