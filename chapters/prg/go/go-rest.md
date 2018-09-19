# Go REST :o: {#s-go-rest}

TODO: we have many pages on rest ... 

## REST

Representational State Transfer (REST) is an architectural style that defines a set of constraints to be used for creating web services. Web Services that conform to the REST architectural style, or RESTful web services, provide interoperability between computer systems on the Internet. REST-compliant web services allow the requesting systems to access and manipulate textual representations of web resources by using a uniform and predefined set of stateless operations. Other kinds of web services, such as SOAP web services, expose their own arbitrary sets of operations.

# RESTful architectures and implementations bring the following characteristics/benefits to organizations:

* Ease of integration - RESTful applications can be easily integrated in the web as they use HTTP methods explicitly
* Increased Scalability - RESTful interactions are stateless and caching semantics are built into the protocol). 
* Evolvability - All resources are identified by URIs which provides a simple way to deal with the evolution of a system. 
* Reliability - RESTful systems typically achieve reliability through idempotent operations.
* Security - RESTful systems can achieve security through both the transport layer (SSL) and a variety of message-level mechanisms.
* Transfer XML, JavaScript Object Notation (JSON)




Gorilla is a web toolkit for the Go programming language. Currently these packages are available:

* gorilla/context stores global request variables.
* gorilla/mux is a powerful URL router and dispatcher.
* gorilla/reverse produces reversible regular expressions for regexp-based muxes.
* gorilla/rpc implements RPC over HTTP with codec for JSON-RPC.
* gorilla/schema converts form values to a struct.
* gorilla/securecookie encodes and decodes authenticated and optionally encrypted cookie values.
* gorilla/sessions saves cookie and filesystem sessions and allows custom session backends.
* gorilla/websocket implements the WebSocket protocol defined in RFC 6455.

# A Basic Web Server
A RESTful service starts with fundamentally being a web service first. Here is a really basic web server that responds to any requests by simply outputting the request url:

```go
package main

import (
    "fmt"
    "html"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
    })

    log.Fatal(http.ListenAndServe(":8080", nil))

}
```


Running this example will spin up a server on port 8080, and can be accessed at http://localhost:8080


# Adding a Router
While the standard library comes with a router, I find that most people are confused about how it works. I’ve used a couple of third party routers in my projects. Most notably I’ve used the [mux router](http://www.gorillatoolkit.org/pkg/mux) from the [Gorilla Web Toolkit](http://www.gorillatoolkit.org/).

Another popular router is from Julien Schmidt called [httprouter](https://github.com/julienschmidt/httprouter).

```go
package main

import (
    "fmt"
    "html"
    "log"
    "net/http"

    "github.com/gorilla/mux"
)

func main() {

    router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/", Index)
    log.Fatal(http.ListenAndServe(":8080", router))
}

func Index(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
```

To run this example, you will now need to execute the following command:

```bash
go get
```

This will retrieve the Gorilla Mux package from GitHub at “github.com/gorilla/mux”

The above example creates a basic router, adds the route / and assigns the Index handler to run when that endpoint is called. You will also notice now that before we could ask for http://localhost:8080/foo and that worked. That will no longer work now as there is no route defined. Only http://localhost:8080 will be a valid response.

# Creating Some Basic Routes

Now that we have a router in place, it is time to create some more routes.

Let’s assume that we are going to create a basic ToDo app.

```go
package main

import (
    "fmt"
    "log"
    "net/http"

    "github.com/gorilla/mux"
)

func main() {

    router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/", Index)
    router.HandleFunc("/todos", TodoIndex)
    router.HandleFunc("/todos/{todoId}", TodoShow)

    log.Fatal(http.ListenAndServe(":8080", router))
}

func Index(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Welcome!")
}

func TodoIndex(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Todo Index!")
}

func TodoShow(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    todoId := vars["todoId"]
    fmt.Fprintln(w, "Todo show:", todoId)
}
```

We have now added two more endpoints (or routes)

This is the Todo Index route: http://localhost:8080/todos

THis is the Todo Show route: http://localhost:8080/todos/{todoId}

This is the beginning of a RESTful design.

Pay close attention to the last route where we added a variable in the route, called todoId: http://localhost:8080/todos/{todoId}

This will allow us to pass in id’s to the route and respond with the proper records.


# References
[Making a RESTful JSON API in Go](https://thenewstack.io/make-a-restful-json-api-go/)



