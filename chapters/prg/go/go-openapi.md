# Open API :o: :question:

:warning: We have a large section previously on openapi, 
what needs to be done here is to showcase how to generate go 
from swagger codegen or other tool and use it


## serve specification UI 

Most basic use-case: serve a UI for your spec: 
```go 
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

## References

* [go-swagger documentation](https://goswagger.io/)
* [OpenAPI.Tools](http://openapi.tools)
