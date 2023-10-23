// Link shortner backend
package main

import (
	"flag"
	"fmt"
	"time"

	"github.com/VinukaThejana/go-utils/logger"
	"github.com/VinukaThejana/link-shortner/backend/config"
	"github.com/VinukaThejana/link-shortner/backend/controllers"
	"github.com/VinukaThejana/link-shortner/backend/initializers"
	"github.com/VinukaThejana/link-shortner/backend/middleware"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"github.com/gofiber/fiber/v2/middleware/limiter"
	fiberLogger "github.com/gofiber/fiber/v2/middleware/logger"
	"github.com/gofiber/fiber/v2/middleware/monitor"
)

var (
	log logger.Logger

	env config.Env
	h   initializers.H

	authM middleware.Auth

	auth  controllers.Auth
	oauth controllers.OAuth
	user  controllers.User
	links controllers.Links
)

func init() {
	env.Load()

	h.InitStorage(&env)
	h.InitDB(&env)
	h.InitRedis(&env)

	authM = middleware.Auth{
		H:   &h,
		Env: &env,
	}

	auth = controllers.Auth{
		H:   &h,
		Env: &env,
	}
	oauth = controllers.OAuth{
		H:   &h,
		Env: &env,
	}
	user = controllers.User{
		H:   &h,
		Env: &env,
	}
	links = controllers.Links{
		H:   &h,
		Env: &env,
	}
}

func main() {
	enableMigrations := flag.Bool("migrate", false, "Migrate the schema to the database")
	flag.Parse()
	if enableMigrations != nil && *enableMigrations {
		h.Migrate()
		return
	}

	app := fiber.New()

	app.Use(fiberLogger.New())
	app.Use(cors.New(cors.Config{
		AllowHeaders:     "Origin, Content-Type, Accept",
		AllowOrigins:     env.FrontEndDomain,
		AllowCredentials: true,
		AllowMethods:     "*",
	}))
	app.Use(limiter.New(limiter.Config{
		Max:        100,
		Expiration: 1 * time.Minute,
		KeyGenerator: func(c *fiber.Ctx) string {
			return c.IP()
		},
		LimitReached: func(c *fiber.Ctx) error {
			return c.SendStatus(fiber.StatusTooManyRequests)
		},
		SkipFailedRequests:     false,
		SkipSuccessfulRequests: false,
		LimiterMiddleware:      limiter.SlidingWindow{},
		Storage:                h.S.S,
	}))
	app.Get("/metrics", monitor.New(monitor.Config{
		Title: "auth",
	}))

	authG := app.Group("/auth")
	authG.Get("/login", oauth.RedirectToGitHubOAuthFlow)
	authG.Get("/logout", auth.Logout)
	authG.Get("/refresh", auth.RefreshToken)

	oauthG := app.Group("/oauth")
	oauthG.Get("/callback/github", oauth.GithubOAuthCalback)
	oauthG.Get("/login/github", oauth.RedirectToGitHubOAuthFlow)

	userG := app.Group("/user", authM.CheckAuth)
	userG.Get("/me", user.GetMe)
	userG.Route("/update", func(router fiber.Router) {
		router.Post("/email", user.UpdateEmail)
		router.Post("/username", user.UpdateUsername)
		router.Post("/name", user.UpdateName)
	})

	linksG := app.Group("/links", authM.CheckAuth)
	linksG.Get("/", links.GetLinks)
	linksG.Post("/new", links.New)
	linksG.Route("/delete", func(router fiber.Router) {
		router.Post("/", links.DeleteLink)
		router.Post("/all", links.DeleteLinks)
	})
	linksG.Route("/update", func(router fiber.Router) {
		router.Post("/", links.Update)
		router.Post("/key", links.UpdateKey)
		router.Post("/url", links.UpdateURL)
	})

	checkG := app.Group("/check")
	checkG.Route("/users", func(router fiber.Router) {
		router.Post("/username", user.CheckUsername)
	})
	checkG.Route("/links", func(router fiber.Router) {
		router.Post("/key", links.CheckKey)
	})

	log.Errorf(app.Listen(fmt.Sprintf(":%s", env.Port)), nil)
}
