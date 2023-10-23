package initializers

import (
	"context"

	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/redis/go-redis/v9"
)

// Redis contains connections to all the Redis instances
type Redis struct {
	RS *redis.Client
}

func connnect(url string) *redis.Client {
	opt, err := redis.ParseURL(url)
	if err != nil {
		log.Errorf(err, nil)
	}

	r := redis.NewClient(opt)
	if err = r.Ping(context.Background()).Err(); err != nil {
		log.Errorf(err, nil)
	}

	return r
}

// InitRedis is a function that is used to intialize the Redis connection
func (h *H) InitRedis(env *config.Env) {
	h.R = &Redis{
		RS: connnect(env.RedisSessionURL),
	}
}
