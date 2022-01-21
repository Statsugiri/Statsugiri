package main

import (
	log "github.com/sirupsen/logrus"
	"github.com/kelvinkoon/babiri_v2/configs"
	"github.com/kelvinkoon/babiri_v2/routes"
	"github.com/kelvinkoon/babiri_v2/middleware"
	"github.com/gorilla/mux"
	"net/http"
)

func main() {
	// Configure router 
    router := mux.NewRouter()
	router.Use(middleware.HeaderMiddleware)

    // Connect to database
    configs.ConnectDB()

    // Configure routes
    routes.TeamRoute(router) 

    log.Fatal(http.ListenAndServe(":3000", router))
}
