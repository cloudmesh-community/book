# Open API

## swagger
Swagger is a simple yet powerful representation of your RESTful API.
With the largest ecosystem of API tooling on the planet, thousands of developers are supporting Swagger in almost every modern programming language and deployment environment.
With a Swagger-enabled API, you get interactive documentation, client SDK generation and discoverability. We created Swagger to help fulfill the promise of APIs.
## features of GO swagger 
* Generates a server from a swagger specification
* Generates a client from a swagger specification
* Supports most features offered by jsonschema and swagger, including polymorphism
* Generates a swagger specification from annotated go code
* Additional tools to work with a swagger spec
* Great customization features, with vendor extensions and customizable templates
* Our focus with code generation is to produce idiomatic, fast go code, which plays nice with golint, go vet etc.

go-swagger brings to the go community a complete suite of fully-featured, high-performance, API components to work with a Swagger API: server, client and data model.

## installing 
go-swagger is available as binary or docker releases as well as from source: more details.
## use cases 
## serve specification UI 
Most basic use-case: serve a UI for your spec:
```go
swagger serve https://raw.githubusercontent.com/swagger-api/swagger-spec/master/examples/v2.0/json/petstore-expanded.json
```
## validate a specification 
## generate an API server 
## generate an API client 
## generate a spec from the source 

## other editors 

* KaiZen-OpenAPI-Editor - Full-featured Eclipse editor for OpenAPI 2.0 and 3.0, also available on Eclipse Marketplace.
* Atom/linter-swagger - This plugin for Atom Linter will lint Swagger 2.0 specifications or OpenAPI 3.0, both JSON and YAML using swagger-parser node package.
* Swagger Editor - Design, describe, and document your API on the first open source editor fully dedicated to OpenAPI-based APIs.
* RepreZen API Studio - RepreZen API Studio is an integrated workbench that brings API-first design into focus for your whole team, harmonizes your API designs, and generates APIs that click into client apps.
* Apicurio Studio - A standalone API design studio that can be used to create new or edit existing API designs.
* SwaggerHub - API design and documentation platform to improve collaboration, standardize development workflow and centralize their API discovery and consumption.
* Senya Editor - Design API specifications fast and effectively​ in your favorite JetBrains IDE.
# References
* [go-swagger documentation](https://goswagger.io/)
* OpenAPI.Tools
