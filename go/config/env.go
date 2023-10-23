package config

import (
	"time"

	"github.com/spf13/viper"
)

// Env contains the env variables that are used throughout the backend
type Env struct {
	Domain         string `mapstructure:"DOMAIN" validate:"required"`
	FrontEndDomain string `mapstructure:"FRONT_END_DOMAIN" validate:"required"`
	Port           string `mapstructure:"PORT" validate:"required"`

	DSN string `mapstructure:"DSN" validate:"required"`

	RedisRatelimiterUsername string `mapstructure:"REDIS_RATELIMITER_USERNAME" validate:"required"`
	RedisRatelimiterPassword string `mapstructure:"REDIS_RATELIMITER_PASSWORD" validate:"required"`
	RedisRatelimiterHost     string `mapstructure:"REDIS_RATELIMITER_HOST" validate:"required"`
	RedisRatelimiterPort     int    `mapstructure:"REDIS_RATELIMITER_PORT" validate:"required"`

	RedisSessionURL string `mapstructure:"REDIS_SESSION_URL" validate:"required"`

	GithubClientID     string `mapstructure:"GITHUB_CLIENT_ID" validate:"required"`
	GithubClientSecret string `mapstructure:"GITHUB_CLIENT_SECRET" validate:"required"`
	GithubRedirectURL  string `mapstructure:"GITHUB_REDIRECT_URL" validate:"required"`
	GithubFromURL      string `mapstructure:"GITHUB_FROM_URL" validate:"required"`
	GithubRootURL      string `mapstructure:"GITHUB_ROOT_URL" validate:"required"`

	AccessTokenPrivateKey string        `mapstructure:"ACCESS_TOKEN_PRIVATE_KEY" validate:"required"`
	AccessTokenPublicKey  string        `mapstructure:"ACCESS_TOKEN_PUBLIC_KEY" validate:"required"`
	AccessTokenExpires    time.Duration `mapstructure:"ACCESS_TOKEN_EXPIRED_IN" validate:"required"`
	AccessTokenMaxAge     int           `mapstructure:"ACCESS_TOKEN_MAXAGE" validate:"required"`

	RefreshTokenPrivateKey string        `mapstructure:"REFRESH_TOKEN_PRIVATE_KEY" validate:"required"`
	RefreshTokenPublicKey  string        `mapstructure:"REFRESH_TOKEN_PUBLIC_KEY" validate:"required"`
	RefreshTokenExpires    time.Duration `mapstructure:"REFRESH_TOKEN_EXPIRED_IN" validate:"required"`
	RefreshTokenMaxAge     int           `mapstructure:"REFRESH_TOKEN_MAXAGE" validate:"required"`

	SessionTokenSecret string `mapstructure:"SESSION_TOKEN_SECRET" validate:"required"`
}

// Load is a function that loads all the env variables from relevant files and the enviroment to the env variable
func (e *Env) Load() {
	viper.AddConfigPath(".")
	viper.SetConfigFile(".env")

	viper.AutomaticEnv()
	err := viper.ReadInConfig()
	if err != nil {
		log.Errorf(err, nil)
	}

	err = viper.Unmarshal(&e)
	if err != nil {
		log.Errorf(err, nil)
	}

	log.Validatef(e)
}
