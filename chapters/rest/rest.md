# REST {#sec:rest}


---

**:mortar_board: Learning Objectives**

* Understand REST Servioces.
* Understand OpenAPI.
* Develop REST services in Python using Eve.
* Develop REST services in Python using OpenAPI with swagger.

---


## Overview of REST

Test short refid.
This should bring up the [python intro](#s-python-intro).
This should bring up the [graphql](#s-graphql).

This section is accompanied by a video about REST.

[:clapper: REST 36:02](https://youtu.be/xjFuA6q5N_U)

REST stands for **RE**presentational **S**tate **T**ransfer. REST is an
architecture style for designing networked applications. It is based on
stateless, client-server, cacheable communications protocol. In contrast
to what some others write or say, REST is not a *standard*. Although not
based on http, in most cases, the HTTP protocol is used. In that case,
RESTful applications use HTTP requests to (a) post data while creating
and/or updating it, (b) read data while making queries, and (c) delete
data.

REST was first introduced in a thesis from Fielding:

* <https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>

Hence REST can use HTTP for the four CRUD operations:

-   **C**reate resources

-   **R**ead resources

-   **U**pdate resources

-   **D**elete resources

As part of the HTTP protocol we have methods such as GET, PUT, POST, and
DELETE. These methods can than be used to implement a REST service. This
is not surprising as the HTTP protocol was explicitly designed to
support these operations. As REST introduces collections and items we
need to implement the CRUD functions for them. We distinguish single
resources and collection of resources. The semantics for accessing them
is explained next illustrating how to implement them with HTTP methods
(see <https://en.wikipedia.org/wiki/Representational_state_transfer>).

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

PUST

:   Replace the addressed member of the collection, or if it does not
    exist, create it.

POST

:   Not generally used. Treat the addressed member as a collection in
    its own right and create a new entry within it.

DELETE

:   Delete the addressed member of the collection.

### REST Tool Classification

Due to the well defined structure that REST provides a number of tools
have been created that manage the creation of the specification for rest
services and their programming. We distinguish several different
categories:

REST programming language support:

:   These tools and services are targeting a particular programming
    language. Such tools include Eve which we will explore in more
    detail.

REST documentation based tools:

:   These tools are primarily focusing on documenting REST
    specifications. Such tools include Swagger, which we will explore in
    more detail.

REST design support tools:

:   These tools are used to support the design process of developing
    REST services while abstracting on top of the programming languages
    and define reusable specifications that can be used to create
    clients and servers for particular technology targets. Such tools
    include also swagger as additional tools are available that can
    generate code from swagger specifications, which we will explore in
    more detail.





