# Open API :o: :question: {#sec:go-openapi}

We have a large section previously on openapi,
what needs to be done here is to showcase how to generate go
from swagger codegen or other tool and use it. Please see @sec:swagger


## serve specification UI


Most basic use-case: serve a UI for your spec:

```bash
swagger serve https://raw.githubusercontent.com/swagger-api/swagger-spec/master/examples/v2.0/json/petstore-expanded.json
```

## validate a specification

```go
swagger validate https://raw.githubusercontent.com/swagger-api/swagger-spec/master/examples/v2.0/json/petstore-expanded.json
```

## Generate a Go OpenAPI server

:warning: this is incorrect :o:
```go
swagger generate server [-f ./swagger.json] -A [application-name [--principal [principal-name]]
```

## generate a Go OpenAPI client

:warning: this is incorrect :o:

```go
swagger generate client [-f ./swagger.json] -A [application-name [--principal [principal-name]]
```

## generate a spec from the source

:warning: this is put here without explanation

```go
swagger generate spec -o ./swagger.json
```

## generate a data model

:warning: this is put here without explanation

```go
swagger generate model --spec={spec}
```


## other editors

* [KaiZen-OpenAPI-Editor](https://github.com/RepreZen/KaiZen-OpenAPI-Editor)- Full-featured Eclipse editor for OpenAPI 2.0 and 3.0, also available on Eclipse Marketplace.
* [Atom/linter-swagger](https://atom.io/packages/linter-swagger) - This plugin for Atom Linter will lint Swagger 2.0 specifications or OpenAPI 3.0, both JSON and YAML using swagger-parser node package.
* [Swagger Editor](https://github.com/swagger-api/swagger-editor) - Design, describe, and document your API on the first open source editor fully dedicated to OpenAPI-based APIs.
* [RepreZen API Studio](https://www.reprezen.com/) - RepreZen API Studio is an integrated workbench that brings API-first design into focus for your whole team, harmonizes your API designs, and generates APIs that click into client apps.
* [Apicurio Studio](http://www.apicur.io/) A standalone API design studio that can be used to create new or edit existing API designs.
* [SwaggerHub](https://swagger.io/tools/swaggerhub/) - API design and documentation platform to improve collaboration, standardize development workflow and centralize their API discovery and consumption.
* [Senya Editor](https://senya.io/) - Design API specifications fast and effectively​ in your favorite JetBrains IDE.


# Create an Echo service using Swagger and Go

In this tutorial, we will create a micro service using Swagger and Go. This service does nothing but echos the message sent from users.

## Dependencies

Some dependencies are required to install before proceeding.

- github.com/go-swagger/go-swagger/cmd/swagger
- github.com/go-openapi/runtime
- github.com/docker/go-units
- github.com/go-openapi/loads
- github.com/go-openapi/validate

These dependencies can be installed via command lines:

```bash
go get -u -v github.com/go-swagger/go-swagger/cmd/swagger
go get -u -v github.com/go-openapi/runtime
go get -u -v github.com/docker/go-units
go get -u -v github.com/go-openapi/loads
go get -u -v github.com/go-openapi/validate
```

## Initialize a Golang project

Create a new folder named `hello-swagger` under `~/go/src`, and a folder named `swagger` under `hello-swagger`. Create `main.go` under `hello-swagger` and `swagger.yml` under `swagger` folder. The structure of the project should look like this:

```
hello-swagger/
  swagger/
    swaggger.yml
  main.go
```

## Define APIs and generate code in Go

Here is the code of `swagger.yml`:

```YAML
swagger: "2.0"
info:
  title: "Echo"
  version: "0.0.1"
paths:
  /echo:
    get:
      operationId: echo
      produces:
        - "application/json"
      parameters:
        - name: "msg"
          in: "query"
          required: true
          type: "string"
      responses:
        200:
          description: "echo message"
          schema:
            type: object
            properties:
              msg:
                type: string
```

To generate Go code run this command:

```bash
~/go/bin/swagger generate server --target ./swagger --spec ./swagger/swagger.yml --exclude-main --name=echo
```

The command will generate Go code and put them under the `swagger` folder. Once there is a new folder named `restapi`, this step is successful.

## Implement the functionality

Now we can create our restapi server and implement the request handler in Go.

Modify the `main.go` so the the content looks like this:

```go
package main

import (
	"github.com/go-openapi/loads"
	"github.com/go-openapi/runtime/middleware"
	"hello-swagger/swagger/restapi"
	"hello-swagger/swagger/restapi/operations"
	"log"
)

func main() {
	log.Println("Starting...")

	swaggerSpec, err := loads.Analyzed(restapi.SwaggerJSON, "")

	if err != nil {
		log.Fatalln(err)
	}

	api := operations.NewEchoAPI(swaggerSpec)
	server := restapi.NewServer(api)
	defer server.Shutdown()

	server.Port = 8080

	api.EchoHandler = operations.EchoHandlerFunc(
		func(params operations.EchoParams) middleware.Responder {
			response := params.Msg
			payload := operations.EchoOKBody{Msg: response}
			return operations.NewEchoOK().WithPayload(&payload)
		})

	if err := server.Serve(); err != nil {
		log.Fatalln(err)
	}
}
```

## Run and test the server

We use `go` command to run, which compile the code and run the program. Once the program is been started, some logs are print out in the console like:

```
2019/02/04 17:06:24 Starting...
2019/02/04 17:06:24 Serving echo at http://[::]:8080
```

Once the server is listening at 8080, we can run `curl` command to do some tests:

```bash

curl http://localhost:8080/echo\?msg\=Hello
# {"msg":"Hello"}

curl http://localhost:8080/echo\?msg\=World
# {"msg":"World"}

```



## References

* [go-swagger documentation](https://goswagger.io/)
* [OpenAPI.Tools](http://openapi.tools)
