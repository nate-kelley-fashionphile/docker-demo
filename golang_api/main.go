package main

import (
    "os"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

func main() {

    e := echo.New()

    e.Use(middleware.Logger())
    e.Use(middleware.Recover())

    e.GET("/", func(c echo.Context) error {
        return c.JSON(200, struct{ Message string `json:"message"` }{Message: "Hello World from GoLang"})
    })

    httpPort := os.Getenv("HTTP_PORT")
    if httpPort == "" {
        httpPort = "8080"
    }

    e.Logger.Fatal(e.Start(":" + httpPort))
}
