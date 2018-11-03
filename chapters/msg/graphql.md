# GraphQL {#s-graphql}

---

**:mortar_board: Learning Objectives**

* Learn about GraphQL
* Develop a GraphQL Server in Python

---

## Introduction

[GraphQL]{.index} is a data query language developed by Facebook.

GraphQL allows clients to request they need while specifing attributes
in the query without thinking
much about the API implementation. It simplifies access and reduces traffic
as the application has control over the data it needs and
its format. Hence GraphQL reduces the network traffic as 
only the necessary data is transfered from server to client.

Unlike REST APIs, which require often loading data via multiple
queries, GraphQL can get typically all the data in a single
request. GraphQL APIs are defined in terms of types and fields. Types
help GraphQL to ensure that client only asks for what is possible and
in case of faults, provides clear and helpful errors.

Initially GraphQL was implemented in JavaScript. Today there are
several other implementations in different languages available.  To
show case how to use GraphQL, we will explore the *graphql-python*
implementation in this chapter. The official documentation of GraphQL
is available at [@graphql-learn]

## Prerequisites

Before we start we need to install a number of tools that we use
throughout the chapter

### Install Graphene

In this chapter, we will use [Graphene](https://graphene-python.org/) 
which is a library for implementing GraphQL APIs in Python. Use `pip`
to install [Graphene]{.index}

```bash
$ pip install graphene==2.0.1 graphene-django==2.0.0
```

### Install Django

For the purpose of demonstrating in this chapter, we will use Django as 
Python web framework.  Django is a popular Python web framework which 
already comes with a lot of boilerplate code. It is mature and has a very
large community.  It has inbuilt support for Object Relational Mapping
which is based on Database Code-First approach. Please refer
[@www-djangoproject] for more Django information.
Use `pip` to install Django

```bash 
$ pip install django==2.0.2 django-filter==1.1.0
```

### Install GraphiQL

In case you prefer to use a browser interface which could be useful
for debugging purposes a number of GraphQL browsers are available. A
free version is GraphiQL. It is an IDE(Interactive Development
Environment) for GraphQL where you can run a *GraphQL Query*. There
are many implementations of *GraphiQL* available. For this chapter we
will use [GraphiQL](https://github.com/skevy/graphiql-app). You can
download the *GraphiQL* installation files specific to your OS from
[GraphiQL Releases](https://github.com/skevy/graphiql-app/releases).

For MacOS, you can even use `homebrew` to install it

```bash
brew cask install graphiql
```

Commercial GraphQL browsers are available from 

* [Insomnia](https://insomnia.rest/graphql/)
* [Altair](https://altair.sirmuel.design/)


## GraphQL type system and schema

To get started with GraphQL we will first explore the GraphQL type system
and schema creation.

### Type System

In GraphQL a query is what a client requests from the GraphQL
server. The result will be obtained in a *structure* defined by *type*
and *schema*. Thus, the client will know ahead of time what it is
going to get as result as part of a well formed response. For this to
work, the data is often assumed to be structured data.

To demonstrate the type system we will use a simple example while looking
at authors and co-authors of papers. We represent in this example a
database that contains a number of authors. Each author has a
publication count and a number of coauthors that are identified by
name. We assume for this simple example that all author names are
unique.

Here is how a simple GraphQL query would look like

```graphql
{
    author {
        name 
        publication_count
        coauthors {
            name
        }
    }
}
```

The response is

```json
{
    "author": {
        "name": "John Doe",
        "publication_count": 25,
        "coauthors": [
            {
                "name": "Mary Jane"
            },
            {
                "name": "David Miller"
            }
        ]
    }
}
```

For this to work, we need to define the types that are going to be
honored by the GraphQL service so that when a query is received by the
server, it is first validated against a schema that defines the types
contained within the GraphQL service.

Hence, types must be defined as part of each GraphQL service. They are
defined with the GraphQL schema language which is programming language
agnostic. An example of a GraphQL type is:

```graphql
type Author {
    name: String!
    publication_count: Int
    coauthors: [Author!]!
}
```

Here we define the type author with three fields `name`,
`publication`, and `coauthors`.  Note that the `!` indicates a field
value, that cannot be null and must have a defined value. `[Author!]!`
means that an array is returned, but that array cannot be null and
also none of the items in the array can be null.

### Scalar Types

GraphQL supports the following scalar types:

* `String`: UTF8 characters
* `Int`: 32 bit signed integer
* `Float`: Double precision floating point value
* `Boolean`: true or false
* `ID`: Represents a unique identifier which can be used as a key to
  fetch the object

### Enumeration Types

`enum` is a scalar type which defines restricted set of values.
When a GraphQL schema defines a field of `enum` type, we
expect that the field's value be of the type `enum` including only the
values that are included in that enumeration. An
example of an `enum` type is

```graphql
enum ContainerType {
    Docker
    Kubernetes
    DockerSwarm
}
```

### Interfaces

Similar to common programming languages, the GraphQL type system also
supports an `interface`. Interfaces allow us to assure that certain
fields are part of the definition of a type.  When a type implements
an `interface`, it needs to specify all the fields that are defined
through the `interface`.

We will illustrate this in the following example, where we define
simple `ComputeService` interface type. This `interface` declares
`id`, `name` and `memory` fields. This means that a `Container` and a
`VirtualMachine` both of which implement `ComputeService`, must have
the fields defined in the `interface`. They may or may not have
additional fields like we demonstrate in our example with the field
`systemType` of type `ContainerType` in case of `Container` and field
`systemType` of type `VMBackend` in case of the `VirtualMachine`.

```graphql
interface ComputeService {
    id: ID!
    name: String!
    memory: Int!
}

type Container implements ComputeService {
    id: ID!
    name: String!
    memory: Int!
    systemType: ContainerType!
}

type VirtualMachine implements ComputeService {
    id: ID!
    name: String!
    memory: Int!
    systemType: VMBackend!
}
```

### Union Types

As the name suggests a `union` type represents the union of two or
more types. The following example shows how we can define a `union`
type. As you can see we use the `|` character to indicate the union
operator.

```graphql
union ComputeType = Container | VirtualMachine
```

Now when we write a GraphQL query to get the `ComputeType`
information, we can ask some of the common fields and some of the
specific fields conditionally. In the next example we request
`AllComputeTypes` with common fields like `id`, `name` and fields
specific to either `VirtualMachine` or `Container`.

```graphql
{
    AllComputeTypes {
        id
        name
        ... on VirtualMachine {
            user
        }
        ... on Container {
            type
        }
    }
}
```

## GraphQL Query

An application asks for data from server in form of a GraphQL *query*. 
A GraphQL query can have different fields and arguments and in this 
section we describe how to use them.

### Fields

A very simple definition of a query is to ask for specific fields that
belong to an object stored in GraphQL.

In the next examples we will use data related to repositories in github.

When asking the query

```graphql
{
    repository {
        name
    }
}
```

we obtain the following response

```json
{
    "data": {
        "repository": {
            "name": "cm"
        }
    }
}
```

As we can see the response data format looks exactly like the query. This
way a client knows exactly what data it has to consume. In the
previous example, the `name` field returns the data of type
`String`. Clients can also ask for an object representing any match
within the GraphQL database.

For example following query

```graphql
{
    community {
        name
        repositories {
            name
        }
    }
}
```

returns the response

```json
{
    "data": {
        "community": {
            "name": "cloudmesh-community",
            "repositories": [{
                "name": "S.T.A.R boat"
            }, {
                "name": "book"
            }]
        }
    }
}
```

### Arguments

As you may already know in REST services you can pass parameters as
part of a request via query parameters through *GET* or a request body
through *POST*. However in GraphQL, for every field, you provide an
argument restricting the data returned to only the information that
you need. This reduces the traffic for returning the information that
is needed without doing the postprocessing on the client. These
restricting arguments can be of scalar type, enumeration type and
others.

Let us look at an example of a query where we only ask for first 3
repositories in cloudmesh community

```graphql
{
    repositories(first: 3) {
        name
        url
    }
}
```

The response will be similar to

```json
{
    "data": {
        "repositories": [{
            "name": "boat",
            "url": "https://github.com/cloudmesh-community/boat"
        }, {
            "name": "book",
            "url": "https://github.com/cloudmesh-community/book"
        }, {
            "name": "case",
            "url": "https://github.com/cloudmesh-community/case"
        }]
    }
}
```

### Fragments

Fragments allow us to reuse portions of a query. Let us look at the
following complex query, which includes repetitive fields:

```graphql
{
    boatRepositoryExample: repository(name: boat) {
        name
        full_name
        url
        description
    }
    cloudRepositoryExample: repository(name: cm) {
        name
        full_name
        url
        description
    }
}
```

As the query gets bigger and more complex, we can use a `fragment` to split
it into smaller chunks.  This `fragment` can then be re-used, which
can significantly reduce the query size and also make it more
readable.

A `fragment` can be defined as

```graphql
fragment repositoryInfo on Repository {
    name
    full_name
    url
    description
}
```

and can be used in a query like this

```graphql
{
    boatRepositoryExample: repository(name: boat) {
        ...repositoryInfo
    }
    cloudRepositoryExample: repository(name: cm) {
        ...repositoryInfo
    }
}
```

The response for this query will look like

```json
{
    "data": {
        "boatRepositoryExample": {
            "name": "boat",
            "fullName": "cloudmesh-community/boat",
            "url": "https://github.com/cloudmesh-community/boat",
            "description": "S.T.A.R. boat"
        },
        "cloudRepositoryExample": {
            "name": "cm",
            "fullName": "cloudmesh-community/cm",
            "url": "https://github.com/cloudmesh-community/cm",
            "description": "Cloudmesh v4"
        }
    }
}
```

### Variables

Variables are used to pass dynamic values to queries. Instead of
passing hard-coded values to a query, variables can be defined for
these values.  Now these variables can be passed to queries.

Variables can be passed to GraphQL queries directly through
commandline. Please note that we pretty print the json output with
python's `json.tool`. So it is not actually part of the querry, but
convenient to format the output. Try to see the difference with and
without the pipe to `json.tool`

```bash
curl -X POST \
-H "Content-Type: application/json;" \
-d '{"query": "{ repository (name: $name) { name url } }", "variables": \
{ "name": "book" }}' \
http://localhost:8000/graphql/ | python -m json.tool
```

In case you use GraphiQL, variables can be defined in the *Query
Variables* panel at left bottom of the *GraphiQL* client. It is
defined as a JSON object and this is how it looks like

```json
{
    "name": "book"
}
```

and it can be used in the query like this

```graphql
{
    repository(name: $name) {
        name
        url
    }
}
```

which will result in the response 

```json
{
    "data": {
        "repository": {
            "name": "book",
            "url": "https://github.com/cloudmesh-community/book"
        }
    }
}
```

### Directives

Directives are used to change the structure of queries at runtime
using variables. Directives provide a way to describe additional
options to GraphQL executors. Currently the core GraphQL specification
supports two directives

* `@skip (if: Boolean)` - It skips the field if argument is true
* `@Include (if: Boolean)` - It includes the field if argument is true

To demonstrate its usage, we define the variable `isAdmin` and assign
a value of `true` to it.

```json
{
    "isAdmin": true
}
```

This variable is passed as an argument `showOwnerInfo` to the query. 
This argument is in turn passed to `@include` directive to determine 
whether to include the `ownerInfo` sub-query.

```graphql
{
    repositories(showOwnerInfo: $isAdmin) {
        name
        url
        ownerInfo @Include(if: $showOwnerInfo) {
            name
        }
    }
}
```

Since we have defined `showOwnerInfo` as `true`, the response 
includes `ownerInfo` data.

```json
{
    "data": {
        "repositories": [{
            "name": "book",
            "url": "https://github.com/cloudmesh-community/book",
            "ownerInfo": {
                "name": "cloudmesh-community"
            }
        }]
    }
}
```

### Mutations

Mutations are used to modify the server side data. To demonstrate this,
let us look at the query and the data to be passed along with it

```graphql
mutation CreateRepositoryForCommunity($community: Community!, $repository: Repository!) {
    createRepository(community: $community, repository: $repository) {
        name
        url
    }
}
```

```json
{
    "community": "cloudmesh-community",
    "repository": {
        "name": "cm-burn",
        "url": "https://github.com/cloudmesh-community/cm-burn"
    }
}
```

The response will be as follow, indicating that a repository has been added.

```json
{
    "data": {
        "createRepository": {
            "name": "cm-burn",
            "url": "https://github.com/cloudmesh-community/cm-burn"
        }
    }
}
```

### Query Validation

GraphQL is a language with strong type system. So requesting and providing
wrong data will generate an error.

For example the query

```graphql
{
    repositories {
        name
        url
        type
    }
}
```

will give the response

```json
{
    "errors": [{
        "message": "Cannot query field \"type\" on type \"Repository\".",
        "locations": [{
            "line": 5,
            "column": 3
        }]
    }]
}
```

In an application we need to validate the user input. If it is invalid
we can use the `GraphQLError` class or Python exceptions to raise
validation errors.

Let us take an example of mutation query. We want to validate whether 
repository name is empty or not. We can use `GraphQLError` to raise 
validation error from our mutation function like this

```python
def mutate(self, info, url, name, full_name, description):
    if not name:
        raise GraphQLError('Repository name is required')
    repository = Repository(url=url, name=name, full_name=full_name, description=description)
    repository.save()
```

## GraphQL in Python

We will cover a basic server implementation with schema and queries 
to fetch and mutate data. 

To develop a GraphQL server in Python we will use `Django` as Python
web framework and the `Graphene` library which alllows us to develop
GraphQL APIs. Naturally other frameworks such as Flask could be used,
but for this example we focus on Django. The installation for Graphene
and Django been already described at the beginning of this chapter.
Our example is located in the book repository which you can clone with

```bash
$ git clone https://github.com/cloudmesh-community/book.git
```

The example itself is located in the directory

* [book/examples/graphql/cloudmeshrepo](https://github.com/cloudmesh-community/book/tree/master/examples/graphql/cloudmeshrepo) - A graphql server example with local database

To execute the example you need to go in the specific
directory. Thus, for  `cloudmeshrepo` say

```bash
$ cd book/examples/graphql/cloudmeshrepo
```

Then you can execute following steps

```bash
$ pip install django-graphql-jwt==0.1.5
$ python manage.py migrate
$ python manage.py runserver
```

The last command will start a server on localhost and you can access
it at

* <http://localhost:8000>

It will show you a graphical interface based on *GraphiQL*, allowing
you to execute your queries in it.

## Developing your own GraphQL Server

If you want to create GraphQL server while using django as the web 
server backend yourself, you can start with following steps

```bash
$ mkdir -p example/graphql
$ cd example/graphql
$ pip install django-graphql-jwt==0.1.5
$ django-admin startproject cloudmeshrepo
$ cd cloudmeshrepo
$ python manage.py migrate
$ python manage.py runserver
```

The last command will start a server on the localhost and you can
access it at the URL

* <http://localhost:8000>

It will show you the welcome page for django. Now open the file

`cloudmeshrepo/cloudmeshrepo/settings.py`

file under folder and append following to
`INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    # After the default packages
    'graphene_django',
)
```

At the end of `settings.py` add following line

```python
GRAPHENE = {
    'SCHEMA': 'cloudmeshrepo.schema.schema',
}
```

### GraphQL server implementation

Clients can request for data to GraphQL server via GraphQL queries. 
They can also use mutations to insert data into GraphQL server's database.
Django follows the principle of separating different modules in a project 
into apps. For this example, we will have two apps, one for Users and 
one for Repositories. For the demo purpose, we have decided not use 
backend such as MongoDB but instead we will use SQLite.

Django provides `startapp` utility to create blank app with some 
biolerplate code.

Go to the root dir of project and execute the following command which
will create an app for repository.

```bash
python manage.py startapp repository
```

Now open `Repositories/models.py` and add the `Repository` model class.

```python
class Repository(models.Model):
    url = models.URLField()
    name = models.TextField(blank=False)
    full_name = models.TextField(blank=False)
    description = models.TextField(blank=True)
```

Now open the file `cloudmeshRepository/settings.py` and append
following line into INSTALLED_APPS

```python
INSTALLED_APPS = (
    # After the graphene_django app
    'Repositories',
)
```

Go to root folder and execute following commands. It will create table
for new model

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Naturally, for us to demonstrate the server, we need to ingest some
data into the server. We can easily do this with the django shell
while calling

```bash
$ python manage.py shell
```

Inside the shell, execute following command to create some example
data. We have taken this data from github's API and used the
repositories in the cloudmesh community at

* <https://api.github.com/users/cloudmesh-community/repos>.

You could use either `wget` or `curl` command to download this data
through shell. As this data is huge, we have used a small subset for
this example. You can have a python script, shell script or any other
program to clean and remodel the data as per your need; the
implementation details for the cleaning process is out of scope for
this chapter.

```python
from Repositories.models import Repository
Repository.objects.create(
    name="boat",
    full_name="cloudmesh-community/boat",
    url="https://github.com/cloudmesh-community/boat",
    description="S.T.A.R. boat")
Repository.objects.create(
    name="book",full_name="cloudmesh-community/book",
    url="https://github.com/cloudmesh-community/book",
    description="Gregor von Laszewski")
Repository.objects.create(name="cm",
    full_name="cloudmesh-community/cm",
    url="https://github.com/cloudmesh-community/cm",
    description="Cloudmesh v4")
Repository.objects.create(name="cm-burn",
    full_name="cloudmesh-community/cm-burn",
    url="https://github.com/cloudmesh-community/cm-burn",
    description="Burns many SD cards so we can build a Raspberry PI cluster")
exit()
```

Now create the file `Repositories/schema.py` with the following
code. The code will create a custom type `Repository` and query with a
[*resolver function*]{#s-graphql-resolver} for Repositories.  The GraphQL server uses
a resolver function to resolve the incoming queries. Queries can respond
to only those fields or entities of schema for which resolver function
has been defined. A `Resolver` function's responsibility is to return data
for that specific field or entity.  We will create one for
Repositories list. When you query repositories, resolver function will
return all the repositories objects from database.

```python
import graphene
from graphene_django import DjangoObjectType

from .models import Repository

class RepositoryType(DjangoObjectType):
    class Meta:
        model = Repository

class Query(graphene.ObjectType):
    Repositories = graphene.List(RepositoryType)

    def resolve_Repositories(self, info, **kwargs):
        return Repository.objects.all()
```

Next create the file `cloudmeshRepository/schema.py` with following
code. It just inherits the query defined in Repositories app. This way we
are able to isolate schema to their apps.

```python
import graphene
  
import Repositories.schema


class Query(Repositories.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
```

### GraphQL Server Querying

Next, we create a Schema  and use it within *GraphiQL* which is a
playground for GraphQL queries. Open the file `cloudmeshrepository/urls.py` and
append the following code

```python
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

Start your server using the command

```bash
$ python manage.py runserver
```

Now open in your browser the URL

* <http://localhost:8000/graphql>

You will see *GraphiQL* window. In the left pane you
can add queries. Let us add the following query

```graphql
{
  repositories {
    name
    fullName
    url
    description
  }
}
```

In the right pane you will see following output

```json
{
  "data": {
    "repositories": [
      {
        "name": "boat",
        "fullName": "cloudmesh-community/boat",
        "url": "https://github.com/cloudmesh-community/boat",
        "description": "S.T.A.R. boat"
      },
      {
        "name": "book",
        "fullName": "cloudmesh-community/book",
        "url": "https://github.com/cloudmesh-community/book",
        "description": "Gregor von Laszewski"
      },
      {
        "name": "cm",
        "fullName": "cloudmesh-community/cm",
        "url": "https://github.com/cloudmesh-community/cm",
        "description": "Cloudmesh v4"
      },
      {
        "name": "cm-burn",
        "fullName": "cloudmesh-community/cm-burn",
        "url": "https://github.com/cloudmesh-community/cm-burn",
        "description": "Burns many SD cards so we can build a Raspberry PI cluster"
      }
    ]
  }
}
```

### Mutation example

Similar to a query, you can add a mutation to create your own data. To
achieve this, add a
`CreateRepository` class for new repository object which will inherit
from graphene's Mutation class. This class will accept a new
repository as 
an argument. Please see the following code snippet which is
added to `repositories/models.py`.


```python
class CreateRepository(graphene.Mutation):
    url = graphene.String()
    name = graphene.String()
    full_name = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        name = graphene.String()
        full_name = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, name, full_name, description):
        repository = Repository(url=url, name=name,
                                full_name=full_name,
                                description=description)
        repository.save()

        return CreateRepository(url=repository.url,
            name=repository.name,
            full_name=repository.full_name,
            description=repository.description)
```

Similar to A Query, add a `Mutation` class in the repository's schema in
`repositories/schema.py`.

```python
class Mutation(graphene.ObjectType):
    create_repository = CreateRepository.Field()
```

Now you can run the following mutation on *GraphiQL* to add a new repository

```graphql
mutation {
  createRepository (
    url: "https://github.com/cloudmesh-community/repository-test",
    name: "repository-test",
    fullName: "cloudmesh-community/repository-test",
    description: "Test repository"
  ) {
    url
    name
    fullName
    description
  }
}
```

This will insert a new repository *repository-test* and also 
immediately return its inserted data fields (`url`, `name`, `fullName`,
`description`).

```json
{
  "data": {
    "createRepository": {
      "url": "https://github.com/cloudmesh-community/repository-test",
      "name": "repository-test",
      "fullName": "cloudmesh-community/repository-test",
      "description": "Test repository"
    }
  }
}
```

### GraphQL Authentication

There a number of ways to add authentication to your GraphQL server

* We can add a REST API endpoint which will take care of
  authenticating the user and only the logged in users can make
  GraphQL queries. This method can also be used to restrict only a
  subset of GraphQL queries. This is ideal for existing applications,
  which have REST endpoints, and which are trying to migrate over to
  GraphQL.
* We can add basic authentication to the GraphQL server which will
  just accept credentials in raw format and once authenticated, logged
  in user can start GraphQL querying
* We can add JSON Web Token authentication to GraphQL server, since
  most of the applications these days are stateless.

### JSON Web Token Authentication

Next we focus on the JSON web token (JWT) authentication. It is tyically
prefered as it provides a more secure and sophisticated way of
authentication. As part of the authentication process, a client has to
provide a username and a password. A limited life time token is
generated that is used during the authentication process.  Once the token
is generated, it needs to be provided with each subsequent GraphQL API
call to assure the authentication is valid.

JWT tokens are bearer tokens which need to be passed in HTTP
authorization header. JWT tokens are very safe against CSRF attacks
and are trusted and verified since they are digitally signed.

The advantage of using frameworks such as the python implementation of
GraphQL is that it can leverage existing authentication modules, so we
do not have to develop them ourselves. One such module is *JSON Web
Token Authentication* or *JWT Authentication.  To use this module,
please add it to the `settings.py` file as follows

```python
MIDDLEWARE = [
    'graphql_jwt.middleware.JSONWebTokenMiddleware',
[

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

Add the Token mutation to `cloudmeshrepo/schema.py`.

```python
class Mutation(users.schema.Mutation, repositories.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
```

Run the server using `runserver` command and fire the token mutation 
providing username and password. You can either run this mutation on 
*GraphiQL* or using `curl` command.

For *GraphiQL* run this on query panel.

```graphql
mutation {
  tokenAuth (username:"user1", password:"Testing123") {
    token
  }
}
```

Or if you are on bash shell, use this `curl` command

```bash
curl -X POST \
-H "Content-Type: application/json;" \
-d '{"query": "{ mutation { tokenAuth (username: \"user1\", ' \
' password:\"Testing123\") { token } } }"}' \
http://localhost:8000/graphql/ | python -m json.tool
```

This will create a token for us to use in our subsequent calls.

```json
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1.... (cut to fit in line)"
    }
  }
}
```

The JWT library comes with a built-in directive called *login_required*.
You can add this to any of your Query resolvers to prevent
unauthenticated access. We have annotated it to the `resolve_repositories` which
means it will throw authentication error to query which does not have 
JWT token passed. Whenever a valid JWT token is present in the query, it is
considered as authenticated or logged in request, and data will be served
only to these queries.

```python
from graphql_jwt.decorators import login_required
...

class Query(graphene.ObjectType):
    repositories = graphene.List(RepositoryType)

    @login_required
    def resolve_repositories(self, info, **kwargs):
        return Repository.objects.all()
```

Now if you try to query our repositories from GraphQL, you will see this error

```json
{
  "errors": [
    {
      "message": "You do not have permission to perform this action",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "repositories"
      ]
    }
  ],
  "data": {
    "repositories": null
  }
}
```

Henceforth you need to pass token with every repository query. This token
needs to be passed as header. Unfortunately, the *GraphiQL* UI client does not
support this. Hence you can use either a curl query from command line
or more advanced GraphQL clients that support authentication.

#### Using Authentication with Curl

To use authentication with curl, you can pass the token to the
command. For simplicity we created a TOKEN environment variable in with
we stor the token so it is easier for us to refer to it in our
examples.

```bash
export TOKEN=eyJ0eXAiOiJKV1.... (cut to fit in line)
curl -X POST \
-H "Content-Type: application/json;" \
-H "Authorization: JWT $TOKEN" \
-d '{"query": "{ repositories { url } }"}' \
http://localhost:8000/graphql/  | python -m json.tool
```

The result obtained from running this command is: 

```json
{"data":{"repositories":[
  {"url":"https://github.com/cloudmesh-community/boat"},
  {"url":"https://github.com/cloudmesh-community/book"},
  {"url":"https://github.com/cloudmesh-community/cm"},
  {"url":"https://github.com/cloudmesh-community/cm-burn"},
  {"url":"https://github.com/cloudmesh-community/vineet-test-1"},
  {"url":"https://github.com/cloudmesh-community/vineet-test"}
  ]}
}
```

#### Expiration of JWT tokens

JWT tokens have a time-to-life and expire after a while. This is
controlled by the 
GraphQL server and is usually communicated to the client in
transparent documented fashion.

If the token is about to expire, you can call the `refreshToken`
mutation to refresh the Token and to return the refreshed token to the
client. However, if the token has already expired we will need to
request a new token by calling `tokenAuth` mutation.

More information about JWT tokens can be found at [@jwt-tokens] and
the GraphQL authentication page at [@medium-graphql].

### GitHub API v4

GraphQL has made already an impact in the cloud services community. In
addition to Facebook, Twitter and Pinterest, *Github* is now also providing 
a GraphQL interface, making it an ideal example for us.

GitHub has implemented as part of its API v4 also GraphQL which allows you to query
or mutate data of repositories that you can access via
`github.com`. To demonstrate its use, we will use *GraphiQL*.

To access the information, we need an OAuth token to access GitHub
API. You can generate an OAuth token by following the steps listed at 

* <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>

Next we demonstrate the use of Github within a GraphQL browser called 
Open *GraphiQL*. First you need to click edit headers at upper-right
corner and add a new header with key *Authorization* and value *Bearer
your_token*.

Next you enter the URL 

* <https://api.github.com/graphql>

in the GraphQL endpoint textbox and keep the method as *POST* only. To
test if the changes have been applied successfully you can use the
query

```graphql
query {
  viewer {
    login
    name
  }
}
```

The query gives the following response 

```json
{
  "data": {
    "viewer": {
      "login": "*Your GitHub UserId*",
      "name": "*Your Full Name*"
    }
  }
}
```

To get a list of our own repositories add following query

```graphql
query($number_of_repositories:Int!) {
  viewer {
    name
     repositories(last: $number_of_repositories) {
       nodes {
         name
       }
     }
   }
}
```

To limit the responses we can define a 
use the variable `number_of_repositories`

```json
{
   "number_of_repositories": 3
}
```

The query gives the following response

```json
{
  "data": {
    "viewer": {
      "name": "*your name*",
      "repositories": {
        "nodes": [
          {
            "name": "*Repository 1*"
          },
          {
            "name": "*Repository 2*"
          },
          {
            "name": "*Repository 3*"
          }
        ]
      }
    }
  }
}
```

To add a comment using mutation we need to get the issue `id` with the
query

```graphql
{
  repository(owner:"MihirNS", name:"Temp_Repository") {
    issue(number: 1) {
      id
    }
  }
}
```

The query gives the following response 

```json
{
  "data": {
    "repository": {
      "issue": {
        "id": "MDU6SXNzdWUzNjUxMDIwOTE="
      }
    }
  }
}
```

Now we can use the id as `subjectId` for mutation to add a comment to an
issue with the query

```graphql
mutation AddComment {
  addComment(input:{subjectId:"MDU6SXNzdWUzNjUxMDIwOTE=",body:"This comment is done using GitHub API v4"}) {
  	commentEdge {
      node {
        repository{
          nameWithOwner
        }
        url
      }
    }
  }
}
```

The query gives the following response

```json
{
  "data": {
    "addComment": {
      "commentEdge": {
        "node": {
          "repository": {
            "nameWithOwner": "MihirNS/Temp_Repository"
          },
          "url": "https://github.com/MihirNS/Temp_Repository/issues/1#issuecomment-425620312"
        }
      }
    }
  }
}
```

## Dynamic Queries with GraphQL

The previous examples served data to and from a database. However,
often we need to access dynamic data that is provided through function
or system calls.

For this reason we like you to be reminded about the Section
describing the [resolver function](#s-graphql-resolver).
It allows us to add functions on the server side that return the data
from various data sources.

It is similar in nature than our example in the REST OpenAPI section,
where we associate call backs that execute dynamic operations.  More
information about the functionality in REST is provided in the Section
[OpenAPI Specification](#s-openapi-spec) as part of the [path
definition](#s-openapi-path).


## Advantages of Using GraphQL

Unlike REST APIs, only the required data is fetched minimizing the
data transferred over network.

Seperation of concern is achieved
between client and server. Client requests data entities with fields
needed for the UI in one query request while server knows about the
data structure and how to resolve the data from its sources which
could be database, web service, microservice, external APIs, etc.

Versioning is simpler than REST, since we only have to take care of it
when we want to remove any of the fields. We can even introduce the
property of a deprecated field for a while to inform the service
users. At a later time the field could be entirely be removed.

```graphql
type Car {
    id: ID!
    make: String
    description: String @deprecated(reason: "Field is deprecated!")
}
``` 

  
## Disadvantages of Using GraphQL

GraphQL query can get very complex. A client may not necessarily know
how expensive the queries can be for server to go and gather the
data. This can be overcome by limiting, for example, the query depth
and recursion.

Caching gets pretty tricky and messy in case of GraphQL. In REST, you
can have separate API url for each resource requested, caching can be
done at this resource level. However, in GraphQL you can have
different queries but they can operate over a single API url. This
means that caching needs to be done at the field level introducing
additional complexity.


## Conclusion

GraphQL is gaining momentum as growing and the integration into
services such as Github, Pinterest, Intuit, Coursera,
and Shopify, demonstrates this. Many GraphQL editors, IDEs
and packages have recently been developed.

In general there are several reasons to use GraphQL due to its
simplicity and flexibility. It also fits well with the microservices
architecture which is a new trend in cloud architectures.  With that
being said, REST APIs still have it is own place and may prove better
choice in certain use cases. Both REST and GraphQL have some tradeoffs
which need to be understood before making a choice between the one or
the other. Github shows that both can be used.

### Resources

* Official documentation of Github API v4 is available at [@github-v4]
* More GraphQL Python examples available at [@www-howtographql]

## Excersises

E.GraphQL.1:

> The chapter shows you how to develop a GraphQL server with
> Django. Instead of Django we like you to use Flask. Develop a
> documented section showcasing this. Use the resolver class to
> demonstrate a dynamic information example such as the cpu type.
> Showcase integration with mongoengine and dynamic information
> retrieval form another information source.
>
> See an example
>
> * <https://github.com/graphql-python/graphene-mongo/tree/master/examples/flask_mongoengine>
> * <https://graphene-mongo.readthedocs.io/en/latest/tutorial.html>

E.GraphQL.2:

> Develop a GraphQL server and client that queries your CPU
> information through a dynamic query using a resolver

E.GraphQL.3: OpenStack VMS

> Develop a GraphQL server that returns the information of running
> virtual machines on OpenStack
> 

E.GraphQL.4: OpenStack Azure

> Develop a GraphQL server that returns the information of running
> virtual machines on OpenStack
> 

E.GraphQL.5: OpenStack Aws

> Develop a GraphQL server that returns the information of running
> virtual machines on OpenStack
>

E.GraphQL.6: Cloud Service

> Pick a Cloud Service and develop a GraphQL interface for it.

E.GraphQL.7: Cloudmesh

> Develop a cloudmesh framework that uses all clouds above while
> returning the information of all running VMS in a Web page. YOu are
> allowed to make the Web page beautiful with HTML5 and/or JavaScript
> if you have the background to do so. Contact Gregor if you like to
> work on this for your project.
>


