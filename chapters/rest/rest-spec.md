# REST Specifications {#sec:rest-specs}

RESTful services have undoubtedly become the de-facto software
architectural style for creating Web services. A REST API specification
would define the attributes and constraints to be used in the web
service. There have been multiple specifications that have been in use
such as [OpenAPI (formally called Swagger)](https://github.com/OAI/OpenAPI-Specification) 
[@oai-spec], [RAML](https://raml.org/) [@raml-spec], [tinyspec](https://github.com/Ajaxy/tinyspec)
[@tinyspec], and [API Blueprint](https://apiblueprint.org/) [@apiblue-spec].


   
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

OAS 3.0 key definitions are depicted in @fig:oas3-spec

![Components of OAS 3.0 [Source](https://blog.readme.io/an-example-filled-guide-to-swagger-3-2/)](images/openapi3.png){#fig:oas3-spec}

The basic structure of the definitions would look like this. The sample REST 
service exposes *http://localhost:8080/cloudmesh* basepath. Under that base path, an endpoint has been exposed as *cloudmesh/cpu*, which would return CPU 
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
  description: 
      A simple service to get cpuinfo as an example of using OpenAPI 3.0
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

When using introspection for REST services (using Connexion), we would need to point to the operation that would ultimately carry out the request. This operation is specified by the *operationID*.

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

When a request is sent with a body, such as *POST*, that is
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

* HTTP authentication: Basic, Bearer, and others.
* API key as a header or query parameter or in cookies
* OAuth2
* OpenID Connect Discovery




## RAML

[RAML](https://raml.org/) [@raml-spec] (RESTful API Modeling Language) is a 
specification proposed in 2013, and it is based on YAML format. The specification is managed by the RAML Worker Group. It initially came out as a proprietary vendor language (specification) but later was open-sourced. As of Sep 2019, the 
latest specification is [RAML 1.0](https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md)
[@raml_spec_1]. 

Following is an example RAML specification from the [RAML.org](https://github.com/raml-org/raml-examples/blob/master/helloworld/helloworld.raml) 

```yaml
#%RAML 1.0
title: Hello world # required title

/helloworld: # optional resource
  get: # HTTP method declaration
    responses: # declare a response
      200: # HTTP status code
        body: # declare the content of the response
          application/json: # media type
            type: | # structural definition of a response (schema or type)
              {
                "title": "Hello world Response",
                "type": "object",
                "properties": {
                  "message": {
                    "type": "string"
                  }
                }
              }
            example: | # example of how a response looks
              {
                "message": "Hello world"
              }
```

In the current context, the industry seems to be adopting OpenAPI more than 
RAML. Consequently, some of the main contributors of RAML, such as MuleSoft, have joined the Open API Initiative since 2017. Hence, it is safe to conclude that 
Open API would be the dominant REST API specification in the web services domain.

Furthermore, there are tools available to switch between the specifications, 
such as [RAML Web API Parser](https://github.com/raml-org/webapi-parser), which can convert RAML to Open API and vice-versa. 


## API Blueprint 

[API Blueprint](https://apiblueprint.org/) [@apiblue-spec] is another specification available currently which uses Markdown syntax. As of Sep 2019 
the latest version available is 1A-rev9.



## JsonAPI

As the name suggests, [JSON API](https://jsonapi.org)[@jsonapi] attempts to leverage web services specifications using JSON format. It reached a stable 
version 1.0 in May 2015, but there have been no revisions since then.


## Tinyspec

[Tinyspec](https://github.com/Ajaxy/tinyspec)[@tinyspec] is a lightweight 
alternative to Open API. It has not been able to enter into the mainstream. 

## Tools

There are a number of tools available in the REST Web services specification domain. A classification of REST tools can be found in the [@sec:rest_classification]
section. 

### Connexion

[Connexion](https://github.com/zalando/connexion)[@connexion] is one such tool that is based on Open API, and it is widely used in the Python environment. This framework allows users to define Web services in Open API and then map those services to Python functions conveniently. We would be using Connexion when we create REST services using introspection [@sec:openapi-introspection].

Here is an example from the [Connexion official website](https://github.com/zalando/connexion/blob/master/examples/openapi3/helloworld/openapi/helloworld-api.yaml) 
[@connexion]. 

```yaml
openapi: "3.0.0"

info:
  title: Hello World
  version: "1.0"
servers:
  - url: http://localhost:9090/v1.0

paths:
  /greeting/{name}:
    post:
      summary: Generate greeting
      description: Generates a greeting message.
      operationId: hello.post_greeting
      responses:
        200:
          description: greeting response
          content:
            text/plain:
              schema:
                type: string
                example: "hello dave!"
      parameters:
        - name: name
          in: path
          description: Name of the person to greet.
          required: true
          schema:
            type: string
            example: "dave"
```

This service would map to the following *post_greeting* Python function. 

```python
import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
    app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()
```

