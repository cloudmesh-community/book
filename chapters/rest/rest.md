# REST {#sec:rest}

---

![](images/learning.png) **Learning Objectives**

* Understand REST Servioces.
* Understand OpenAPI.
* Develop REST services in Python using Eve.
* Develop REST services in Python using OpenAPI with swagger.

---


## Overview of REST

This section is accompanied by a video about REST in which we present
some additional information.

[![Video](images/video.png) REST 36:02](https://youtu.be/xjFuA6q5N_U)

REST stands for **RE**presentational **S**tate **T**ransfer. REST is an
architecture style for designing networked applications. It is based on
stateless, client-server, cacheable communications protocol. In contrast
to what some others write or say, REST is not a *standard*. Although not
based on http, in most cases, the HTTP protocol is used. In that case,
RESTful applications use HTTP requests to (a) post data while creating
and/or updating it, (b) read data while making queries, and (c) delete
data.

REST was first introduced in a [thesis from Roy T. Fielding](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
[@fielding2000architectural].

Hence REST can use HTTP for the four CRUD operations:

* **C**reate resources
* **R**ead resources
* **U**pdate resources
* **D**elete resources

As part of the HTTP protocol we have methods such as GET, PUT, POST, and
DELETE. These methods can than be used to implement a REST service. This
is not surprising as the HTTP protocol was explicitly designed to
support these operations. As REST introduces collections and items we
need to implement the CRUD functions for them. We distinguish single
resources and collection of resources. The semantics for accessing them
is explained next illustrating how to implement them with HTTP methods
(See [REST on Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)
[@restwiki]).

### Collection of Resources

Let us assume the following URI identifies a collection of resources

`http://.../resources/`

than we need to implement the following CRUD methods:

GET

:   List the URIs and perhaps other details of the collections members

PUT

:   Replace the entire collection with another collection.

POST

:   Create a new entry in the collection. The new entry's URI is
    assigned automatically and is usually returned by the operation.

DELETE

:   Delete the entire collection.

### Single Resource

Let us assume the following URI identifies a single resource in a
collection of resources

`http://.../resources/item42`

than we need to implement the following CRUD methods:

GET

:   Retrieve a representation of the addressed member of the collection,
    expressed in an appropriate internet media type.

PUT

:   Replace the addressed member of the collection, or if it does not
    exist, create it.

POST

:   Not generally used. Treat the addressed member as a collection in
    its own right and create a new entry within it.

DELETE

:   Delete the addressed member of the collection.

### REST Tool Classification {#sec:rest_classification}

Due to the well defined structure that REST provides a number of tools
have been created that manage the creation of the specification for rest
services and their programming. We distinguish several different
categories:

REST Specification Frameworks:

: These are frameworks that help defining rest servicice through
  specifications to generate REST services in a language and framework
  independent way. This includes for example Swagger 2.0 [@swagger2spec],
  OpenAPI 3.0 [@oai-spec], and RAML [@raml-spec].

REST programming language support:

: These tools and services are targeting a particular programming
  language. Such tools include Python Restful [:o2:], Flask Rest [@flaskrestful],
  and Django Rest Services [@djangorest], some of which we will explore in more
  detail.

REST documentation based tools:

: These tools are primarily focusing on documenting REST specifications.
  Such tools include Swagger [@swagger], which we will explore in more 
  detail.

REST design support tools:

: These tools are used to support the design process of developing
  REST services while abstracting on top of the programming languages
  and define reusable specifications that can be used to create
  clients and servers for particular technology targets. Such tools
  include also swagger [@swagger] as additional tools are available that can
  generate code from OpenAPI specifications [@swagger-codegen], which we will 
  explore in more detail.

A list of such efforts is available at [OpenAPI Tools](https://openapi.tools/)
[@openapitools]


