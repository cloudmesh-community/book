# HATEOAS

In the previous section we discussed the basic concepts about RESTful
web service. Next we introduce you to the concept of HATEOAS

HATEOAS stands for Hypermedia as the Engine of Application State and
this is enabled by the default configuration within Eve. It is useful to
review the terminology and attributes used as part of this
configuration. HATEOS explains how REST API endpoints are defined and it
provides a clear description on how the API can be consumed through
these terms:

_links

:   Links describe the relation of current resource being accessed to
    the rest of the resources. It is like if we have a set of links to
    the set of objects or service endpoints that we are referring in the
    RESTful web service. Here an endpoint refers to a service call which
    is responsible for executing one of the CRUD operations on a
    particular object or set of objects. More on the links, the links
    object contains the list of serviceable API endpoints or list of
    services. When we are calling a GET request or any other request, we
    can use these service endpoints to execute different queries based
    on the user purpose. For instance, a service call can be used to
    insert data or retrieve data from a remote database using a REST API
    call. About databases we will discuss in detail in another chapter.

title

:   The title in the rest endpoint is the name or topic that we are
    trying to address. It describes the nature of the object by a single
    word. For instance student, bank-statement, salary,etc can be a
    title.

parent

:   The term parent refers to the very initial link or an API
    endpoint in a particular RESTful web service. Generally this is
    denoted with the primary address like http://example.com/api/v1/.

href

:   The term href refers to the url segment that we use to access the
    a particular REST API endpoint. For instance "student?page=1" will
    return the first page of student list by retrieving a particular
    number of items from a remote database or a remote data source. The
    full url will look like this,
    "http://www.exampleapi.com/student?page=1".

In addition to these fields eve will automatically create the follwoing
information when resources are created as showcased ot

* <http://python-eve.org/features.html>

| Field    |    Description|
| :------ | :------- |
|  `_created` |  item creation date.
|  `_updated` |  item last updated on.
|  `_etag`    |  ETag, to be used for concurrency control and conditional requests.
|  `_id`      |  unique item key, also needed to access the individual item endpoint.

Pagenation information can be included in the `_meta` field.

## Filtering

Clients can submit query strings to the rest service to retrieve
resources based on a filter. This also allows sorting of the results
queried. One nice feature about using mongo as a backend database is
that Eve not only allows python conditional expressions, but also mongo
queries.

A number of examples to conduct such queries include:

    $ curl -i -g http://eve-demo.herokuapp.com/people?where={%22lastname%22:%20%22Doe%22}

A python expression

    $ curl -i http://eve-demo.herokuapp.com/people?where=lastname=="Doe"

## Pretty Printing

Pretty printing is typically supported by adding the parameter `?pretty`
or `?pretty=1`

If this does not work you can always use python to beautify a json
output with

    $ curl -i http://localhost/people?pretty

or

    $ curl -i http://localhost/people | python -m json.tool

## XML

If for some reason you like to retrieve the information in XML you can
specify this for example through curl with an Accept header

    $ curl -H "Accept: application/xml" -i http://localhost
