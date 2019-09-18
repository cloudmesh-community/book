# REST Specifications {#sec:rest-specs}

RESTful services have undoubtedly become the de-facto software
architectural style for creating Web services. A REST API specification
would defines the attributes and constraints to be used in the web
service. There have been multiple specifications that have been in use
such as [OpenAPI (formally called Swagger)](https://github.com/OAI/OpenAPI-Specification) 
[@oai-spec], [RAML](https://raml.org/) [@raml-spec], and [API
Blueprint](https://apiblueprint.org/) [@apiblue-spec].


   
## OPENAPI

Over the years, Open API specification has become the most popular with
a much larger community behind it. Therefore, this section would focus
on the latest specification, [OpenAPI 3.0 (OAS
3.0)](https://swagger.io/blog/news/announcing-openapi-3-0/) [@oai3-spec].

According to the [OAS
documentation](https://swagger.io/docs/specification/about/) [@oai-docs], it 
allows users to,

* Describe endpoints and operations on each endpoint
* Specify operation parameters, inputs, and outputs for each operation 
* Handle authentication 
* Describe contact, license, terms of use and other information  

API specifications can be written in YAML or JSON. OAS also comes with a
rich toolkit that includes 
[Swagger Editor](http://editor.swagger.io/) [@swagger-editor],
[Swagger UI](https://swagger.io/swagger-ui/) [@swagger-ui] and [Swagger
Codegen](https://github.com/swagger-api/swagger-codegen) [@swagger-codegen], 
that creates an end-to-end development environment, even for the users who are 
new to OAS.

Section [OpenAPI Specification](#openapi-spec) details more on the OAS 2.0 
specification.

### Open API 3.0 Specification (OAS 3.0) 

OAS 3.0 key definitions can be depicted in the following figure.  

![Components of OAS 3.0 [Source](https://blog.readme.io/an-example-filled-guide-to-swagger-3-2/)](images/openapi3.png){#fig:oas3-spec}

Basic structure of the definitions would look like this. The sample REST 
service, exposes *http://localhost:8080/cloudmesh* basepath. Under that base 
path, an endpoint has been exposed as *cloudmesh/cpu* which would return CPU 
information of the server. It uses a predefined schema to return the results, 
which is defined under the *components/schemas*. See the Section [OpenAPI REST 
Service via Introspection](#sec:openapi-introspection}) for the detailed example. 

```yaml
openapi: 3.0.2
info:
  title: cpuinfo
  description: A simple service to get cpuinfo as an example of using OpenAPI 3.0
  license:
    name: Apache 2.0
  version: 0.0.1

servers:
  - url: http://localhost:8080/cloudmesh

paths:
  /cpu:
    get:
      summary: Returns cpu information of the hosting server
      operationId: cpu.get_processor_name
      responses:
        '200':
          description: cpu info
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/cpu"

components:
  schemas:
    cpu:
      type: "object"
      required:
        - "model"
      properties:
        model:
          type: "string"
```

#### Definitions 

**Metadata**:

OAS 3.0 requires a specification definition at the start under the
*openapi* field.

```yaml
openapi: 3.0.2
```

Next, metadata can be specified under *info* field such as *title*,
*version*, *description*, etc. Additionally, license, contact
information can also be specified. *tile* and *version* are mandatory
fields under *info*.

```yaml
info:
  title: cpuinfo
  description: A simple service to get cpuinfo as an example of using OpenAPI 3.0
  license:
    name: Apache 2.0
  version: 0.0.1
```


**Servers**:

The *servers* section defines the server URLs with the basepath.
Optionally, a *description* can be added.

```yaml
servers:
  - url: http://localhost:8080/cloudmesh
    description: Cloudmesh server basepath 
``` 


**Paths**:

The *paths* section specifies all the endpoints exposed by the API and
the HTTP operations supported by these endpoints.

```yaml
paths:
  /cpu:
    get:
      summary: Returns cpu information of the hosting server
      operationId: cpu.get_processor_name
      responses:
        '200':
          description: cpu info
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/cpu"
```

**Operation ID**:
When using introspection for REST services, we would need to point to the 
operation that would ultimately carry out the request. This operation is 
specified by the *operationID*.

```yaml
...
paths:
  /cpu:
...
      operationId: cpu.get_processor_name
``` 


**Parameters**:

If the service endpoint accepts URL parameters (ex:
*/cpu/cache/{cache_level}* or */cpu?arch=x86*), headers or cookies,
those can also be specified under a *path*.

```yaml
paths:
  /cpu/cache/{cache_level}:
    get:
      summary: Returns the cache size of the specified level 
      parameters:
        - name: cache_level
          in: path
          required: true
          description: Parameter description in CommonMark or HTML.
          schema:
            type : string
            minimum: 1
      responses: 
        '200':
          description: OK
``` 
 
**Request Body**:

When a request is sent with a body, such as *POST*, that will be
specified in the *requestBody* under a *path*.

```yaml
paths:
  /upload:
    post:
      summary: upload input
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses: 
        '200':
          description: OK
```

**Responses**:

For each path, *responses* can be specified with the corresponding
status codes such as 200 OK or 404 Not Found. A response may return a
response body, that can be defined under *content*.

```yaml
...
paths:
  /cpu:
...
        responses:
            '200':
              description: cpu info
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/cpu"
``` 

**Schemas**:

The *components/schemas* section allows users to define schemas for
inputs or outputs that can be referenced via *$ref* tag.

```yaml
...
paths:
  /cpu:
...
      responses:
        '200':
          description: cpu info
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/cpu"

...

components:
  schemas:
    cpu:
      type: "object"
      required:
        - "model"
      properties:
        model:
          type: "string"
```

**Authentication**:

Under the *components* sections, *securitySchemes* can also be specified
such as Basic Auth.

```yaml
components:
  securitySchemes:
    BasicAuth:
      type: http
      scheme: basic

security:
  - BasicAuth: []
```

According to the current OAS 3.0, supported authentication methods are, 

* HTTP authentication: Basic, Bearer, and so on.
* API key as a header or query parameter or in cookies
* OAuth2
* OpenID Connect Discovery




## RAML

[:o2:] under development

paragraph with intro, pointer to example, 

point out that OpenAPI seem to have even RAML people as so OpenAPI seems
the one we want to use and not RAML

there are tools to convert this.

## Tinyspec
[:o2:] under development

Is this even useful?

* <https://www.toptal.com/api-developers/5-new-things-rest-specification> [:o2:]

## JsonAPI
[:o2:] under development

* <https://jsonapi.org/> [:o2:]
* <https://jsonapi.org/format/> [:o2:]


## Tools
[:o2:] under development

[:o2:] see in rest.md, the link to resttools, put this here also


### Conexion
[:o2:] under development

* <https://github.com/zalando/connexion> [:o2:]
* <https://github.com/zalando/connexion/tree/master/examples/openapi3/helloworld/openapi> [:o2:]
