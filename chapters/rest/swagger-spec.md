# OpenAPI Specification

Swagger provides through its specification the definition of REST
services through a YAML or JSON document.

When following the API-specification-first approach to define and
develop a RESTful service, the first and foremost step is to define the
API conforming to the OpenAPI specification, and then using codegen
tools to conveniently generate server side stub code, client code,
documentations, in the language you desire. In Section
[REST Service Generation with OpenAPI](#rest-service-generation-with-openapi)
we have introduced the codegen tool
and how to use that to generate server side and client side code and
documentation. In this
Section [The Virtual Cluster example API Definition](#the-virtual-cluster-example-api-definition)
we will use a slightly more complex example
to show how to define an API following the OpenAPI 2.0 specification.
The example is to retrieve virtual cluster (VC) object from the server.

The OpenAPI Specification is formerly known as Swagger RESTful API
Documentation Specification. It defines a specification to describe and
document a RESTful service API. It is also known under version 3.0 of
swagger. However, as the tools for 3.0 are not yet completed, we will
continue for now to use version swagger 2.0, till the transition has
been completed. This is especially of importance, as we need to use the
swagger codegen tool, which currently support only up to specification
v2. Hence we are at this time using OpenAPI/Swagger v2.0 in our example.
There are some structure and syntax changes in v3, while the essence is
very similar. For more details of the changes between v3 and v2, please
refer to A document published on the Web titled [Difference between
OpenAPI 3.0 and Swagger
2.0](https://blog.readme.io/an-example-filled-guide-to-swagger-3-2/).

You can write the API definition in json for yaml format. Let us discuss
this format briefly and focus on yaml as it is easier to read and
maintain.

On the root level of the yaml document we see fields like *swagger*,
*info*, and so on. Among these fields, ***swagger***, ***info***, and
***path*** are **required**. Their meaning is as follows:

swagger

:   specifies the version number. IN our case a string value '2.0' is
    used as we are writing the definition conforming to the v2.0
    specification.

info

:   defines metadata information related to the API. E.g., the API
    *version*, *title* and *description*, *termsOfService* if
    applicable, *contact* information and *license*, etc. Among these
    attributes, ***version*** and ***title*** are required while others
    are optional.

path

:   defines the actual endpoints of the exposed RESTful API service.
    Each endpoint has a *field pattern* as the key, and a *Path Item
    Object* as the value. In this example we have defined */vc* and
    */vc/{id}* as the two service endpoints. They will be part of the
    final service URL, appended after the service *host* and *basePath*,
    which will be explained later.

Let us focus on the *Path Item Object*. It contains one or more
supported *operations* on the service endpoint. An *operation* is keyed
by a valid HTTP operation verb, e.g., one of **get**, **put**, **post**,
**delete**, or **patch**. It has a value of *Operation Object* that
describes the operations in more detail.

The *Operation Object* will always **require** a *Response Object*. A
*Response Object* has a *HTTP status code* as the key, e.g., **200** as
successful return; **40X** as authentication and authorization related
errors; and **50x** as other server side servers. It can also has a
default response keyed by **default** for undeclared http status return
code. The *Response Object* value has a **required** *description*
field, and if anything is returned, a *schema* indicating the object
type to be returned, which could be a primitive type, e.g., *string*, or
an *array* or customized *object*. In case of *object* or an *array* of
*object*, use *\$ref* to point to the definition of the object. In this
example, we have

      $ref: "#/definitions/VC"

to point to the *VC* definition in the *definitions* section in the same
specification file, which will be explained later.

Besides the required field, the *Operation Object* **can** have
*summary* and *description* to indicate what the operation is about; and
*operationId* to uniquely identify the operation; and *consumes* and
*produces* to indicate what MIME types it expects as input and for
returns, e.g., *application/json* in most modern RESTful APIs. It can
further specify what input parameter is expected using *parameters*,
which requires a *name* and *in* fields. *name* specifies the name of
the parameter, and *in* specifies from where to get the parameter, and
its possible values are *query*, *header*, *path*, *formData* or *body*.
In this example in the */vc/{id}* path we obtain the *id* parameter from
the URL path wo it has the *path* value. When the *in* has *path* as its
value, the *required* field is required and has to be set as *true*;
when the *in* has value other than *body*, a *type* field is required to
specify the type of the parameter.

While the three root level fields mentioned above are required, in most
cases we will also use other optional fields.

host

:   to indicate where the service is to be deployed, which could be
    *localhost* or a valid IP address or a DNS name of the host where
    the service is to be deployed. If other port number other than *80*
    is to be used, write the port number as well, e.g.,
    *localhost:8080*.

schemas

:   to specify the transfer protocol, e.g, *http* or *https*.

basePath

:   to specify the common base URL to be append after the *host* to form
    the base path for all the endpoints, e.g., */api* or */api/1.0/*. In
    this example with the values specified we would have the final
    service endpoints *http://localhost:8080/api/vcs* and
    *http://localhost:8080/api/vc/{id}* by combining the *schemas*,
    *host*, *basePath* and *paths* values.

consumes and produces

:   can also be specified on the top level to specify the default MIME
    types of the input and return if most *paths* and the defined
    operations have the same.

definitions

:   as used in in the *paths* field, in order to point to a customized
    object definition with a *\$ref* keyword.

The *definitions* field really contains the object definition of the
customized objects involved in the API, similar to a class definition in
any Object Oriented programming language. In this example, we defined a
*VC* object, and hierarchically a *Node* object. Each object defined is
a type of *Schema Object* in which many field could be used to specify
the object (see details in the REF link at top of the document), but the
most frequently used ones are:

type

:   to specify the type, and in the customized definition case the value
    is mostly *object*.

required

:   field to list the names of the required attributes of the object.

properties

:   has the detailed information of each attribute/property of the
    object, e.g, *type*, *format*. It also supports hierarchical object
    definition so a property of one object could be another customized
    object defined elsewhere while using *schema* and *\$ref* keyword to
    point to the definition. In this example we have defined a *VC*, or
    virtual cluster, object, while it contains another object definition
    of

Node

:   as part of a cluster.

## The Virtual Cluster example API Definition

### Terminology

VC

:   A virtual cluster, which has one Front-End (FE) management node and
    multiple compute nodes. A VC object also has *id* and *name* to
    identify the VC, and *nnodes* to indicate how many compute nodes it
    has.

FE

:   A management node from which to access the compute nodes. The FE
    node usually connects to all the compute nodes via private network.

Node

:   A computer node object that the info *ncores* to indicate number of
    cores it has, and *ram* and *localdisk* to show the size of RAM and
    local disk storage.

### Specification

    swagger: "2.0"
    info: 
      version: "1.0.0"
      title: "A Virtual Cluster"
      description: "Virtual Cluster as a test of using swagger-2.0 specification and codegen"
      termsOfService: "http://swagger.io/terms/"
      contact: 
        name: "IU ISE software and system team"
      license: 
        name: "Apache"
    host: "localhost:8080"
    basePath: "/api"
    schemes: 
      - "http"
    consumes: 
      - "application/json"
    produces: 
      - "application/json"
    paths: 
      /vcs: 
        get: 
          description: "Returns all VCs from the system that the user has access to"
          produces: 
            - "application/json"
          responses: 
            "200":
              description: "A list of VCs."
              schema: 
                type: "array"
                items: 
                  $ref: "#/definitions/VC"
      /vcs/{id}:
        get: 
          description: "Returns all VCs from the system that the user has access to"
          operationId: getVCById
          parameters:
            - name: id
              in: path
              description: ID of VC to fetch
              required: true
              type: string
          produces: 
            - "application/json"
          responses: 
            "200":
              description: "The vc with the given id."
              schema: 
                $ref: "#/definitions/VC"
            default:
              description: unexpected error
              schema:
                $ref: '#/definitions/Error'
    definitions:
      VC: 
        type: "object"
        required: 
          - "id"
          - "name"
          - "nnodes"
          - "FE"
          - "computes"
        properties: 
          id: 
            type: "string"
          name: 
            type: "string"
          nnodes:
            type: "integer"
            format: "int64"
          FE:
            type: "object"
            schema:
              $ref: "#/definitions/Node"
          computes:
            type: "array"
            items:
              $ref: "#/definitions/Node"
          tag: 
            type: "string"
      Node:
        type: "object"
        required:
          - "ncores"
          - "ram"
          - "localdisk"
        properties:
          ncores:
            type: "integer"
            format: "int64"
          ram:
            type: "integer"
            format: "int64"
          localdisk:
            type: "integer"
            format: "int64"
      Error:
        required:
        - code
        - message
        properties:
          code:
            type: integer
            format: int32
          message:
            type: string

## References

[The official OpenAPI 2.0
Documentation](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md)
