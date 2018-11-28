# Go REST {#s-go-rest}

Go is a new powerful language and there are many frameworks from lightweight to full featured that support building RESTful APIs.

1. [Revel](https://github.com/revel/revel) A high-productivity web framework for the Go language.

2. [Gin](https://gin-gonic.github.io/gin/) The fastest full-featured web framework for Golang. Crystal clear.

3. [Martini](https://github.com/olebedev/martini) Classy web framework for Go

4. [Web.go](https://github.com/hoisie/web) The easiest way to create web applications with Go

List here the rest services tutorials for frameworks

* <https://nordicapis.com/7-frameworks-to-build-a-rest-api-in-go/>
* with mongo <https://hackernoon.com/build-restful-api-in-go-and-mongodb-5e7f2ec4be94>
* <https://tutorialedge.net/golang/consuming-restful-api-with-go/>
* <https://thenewstack.io/make-a-restful-json-api-go/>
* [Making a RESTful JSON API in Go](https://thenewstack.io/make-a-restful-json-api-go/)

## Gorilla

* <https://www.codementor.io/codehakase/building-a-restful-api-with-golang-a6yivzqdo>

Gorilla is a web toolkit for the Go programming language. Currently
these packages are available:

* gorilla/context stores global request variables.
* gorilla/mux is a powerful URL router and dispatcher.
* gorilla/reverse produces reversible regular expressions for regexp-based muxes.
* gorilla/rpc implements RPC over HTTP with codec for JSON-RPC.
* gorilla/schema converts form values to a struct.
* gorilla/securecookie encodes and decodes authenticated and optionally encrypted cookie values.
* gorilla/sessions saves cookie and filesystem sessions and allows custom session backends.
* gorilla/websocket implements the WebSocket protocol defined in RFC 6455.


## REST, RESTful

REST is an acronym for Representational State Transfer. It is a web standards architecture and HTTP Protocol. The REST protocol, decribes six (6) constraints:

1. Uniform Interface
1. Cacheable
1. Client-Server
1. Stateless
1. Code on Demand
1. Layered System

## Router

Package gorilla/mux implements a request router and dispatcher for matching incoming requests to their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard http.ServeMux, mux.Router matches incoming requests against a list of registered routes and calls a handler for the route that matches the URL or other conditions. The main features are:

We'll need to use a mux to route requests, so we need a Go package for that (mux stands for HTTP request multiplexer which matches an incoming request to against a list of routes (registered)). In the rest-api directory, let's require the dependency (package rather). More examples are here: https://github.com/gorilla/mux#examples

```
rest-api$ go get github.com/gorilla/mux
```

```go
package main

import (
    "encoding/json"
    "log"
    "net/http"
    "github.com/gorilla/mux"
)

// our main function
func main() {
    router := mux.NewRouter()
    router.HandleFunc("/people", GetPeople).Methods("GET")
    router.HandleFunc("/people/{id}", GetPerson).Methods("GET")
    router.HandleFunc("/people/{id}", CreatePerson).Methods("POST")
    router.HandleFunc("/people/{id}", DeletePerson).Methods("DELETE")
    log.Fatal(http.ListenAndServe(":8000", router))
}
```

Packages are explained here:
* fmt is what we'll be using to print to STDOUT (the console)
* log is used to log when the server exits
* encoding/json is for creating our JSON responses
* net/http will give us the representations of HTTP requests, responses, and be responsible for running our server
* github.com/gorilla/mux will be our router that will take requests and decide what should be done with them

## Full code

```go
package main

import (
    "encoding/json"
    "github.com/gorilla/mux"
    "log"
    "net/http"
)

// The person Type (more like an object)
type Person struct {
    ID        string   `json:"id,omitempty"`
    Firstname string   `json:"firstname,omitempty"`
    Lastname  string   `json:"lastname,omitempty"`
    Address   *Address `json:"address,omitempty"`
}
type Address struct {
    City  string `json:"city,omitempty"`
    State string `json:"state,omitempty"`
}

var people []Person

// Display all from the people var
func GetPeople(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(people)
}

// Display a single data
func GetPerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    for _, item := range people {
        if item.ID == params["id"] {
            json.NewEncoder(w).Encode(item)
            return
        }
    }
    json.NewEncoder(w).Encode(&Person{})
}

// create a new item
func CreatePerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    var person Person
    _ = json.NewDecoder(r.Body).Decode(&person)
    person.ID = params["id"]
    people = append(people, person)
    json.NewEncoder(w).Encode(people)
}

// Delete an item
func DeletePerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    for index, item := range people {
        if item.ID == params["id"] {
            people = append(people[:index], people[index+1:]...)
            break
        }
        json.NewEncoder(w).Encode(people)
    }
}

// main function to boot up everything
func main() {
    router := mux.NewRouter()
    people = append(people, Person{ID: "1", Firstname: "John", Lastname: "Doe", Address: &Address{City: "City X", State: "State X"}})
    people = append(people, Person{ID: "2", Firstname: "Koko", Lastname: "Doe", Address: &Address{City: "City Z", State: "State Y"}})
    router.HandleFunc("/people", GetPeople).Methods("GET")
    router.HandleFunc("/people/{id}", GetPerson).Methods("GET")
    router.HandleFunc("/people/{id}", CreatePerson).Methods("POST")
    router.HandleFunc("/people/{id}", DeletePerson).Methods("DELETE")
    log.Fatal(http.ListenAndServe(":8000", router))
}
```
