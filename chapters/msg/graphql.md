# GraphQL :o:

## Introduction

GraphQL is a data query language developed by Facebook.

GraphQL allows clients to request data they need without thinking
about the API implementation. It makes application devlopment fast and
stable because the application has control over the data it needs and
its format. The benefit of GraphQL is also to reduce network I/O since
only the necessary data is transfered from server to client.

Unlike REST APIs, which require loading data via multiple URLs,
GraphQL can get all data, that application needs, in a single
request. GraphQL APIs are defined in terms of types and fields. Types
help GraphQL to ensure that client only asks for what is possible and
in case of faults, provides clear and helpful errors.

Initially GraphQL was implemented in JavaScript. Today there are
several other implementations in different language available of
GraphQLs. We will explore the *graphql-python* implementation in this
chapter. The official documentation of GraphQL is available at
[@graphql-learn]

## GraphQL type system and schema

To get started with GraphQL we will first explore GraphQL type system
and schema creation.

### Type System

In GraphQL a query is what client requests from the GraphQL server. The
result will be obtained in a structure defined by type and schema. It
means client will know ahead of time what it is going to get as
result. For this to work, the data is often assumed to be structured
data.

To demonstrate the type system we use a simple example while looking
at authors and co-authors of papers. We represent in this example a
database that contains a number of authors. each author has a
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
honored by the GraphQL service so that when a query is recieved by the
server, it is first validated to a schema that defines the types
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

Note that the `!` indicates a field value, that cannot be null and
must have a defined value. `[Author!]!` means that an array is
returned, but that array cannot be null and also none of the items
in the array can be null.


### Scalar Types

GraphQL supports the following scalar types:

* `String`: UTF8 characters
* `Int`: 32 bit signed integer
* `Float`: Double precision floating point value
* `Boolean`: true or false
* `ID`: Represents a unique identifier which can be used as a key to
  fetch the object

### Enumeration Types

`enum` is also a scalar type which define a certain set of restricted
values. When a GraphQL schema defines a field of `enum` type, we
expect that the field's value be of the type `enum` values only. An
example of an `enum` type is

```graphql
enum ContainerTYpe {
    Docker
    Kubernetes
    DockerSwarm
}
```

### Interfaces

Similar to any programming language, the GraphQL type system also
supports `interface`. When a type implements an `interface`, it needs
to specify all the fields that are defined through the `interface`.

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

As the name suggests, `union` type represent the union of two or more
types. Here is how we can define a `union` type. As you can see we use
the `|` charater to indicate the union operator.

```graphql
union ComputeType = Container | VirtualMachine
```

Now when we write a GraphQL query to fetch the `ComputeType`
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

In the next examples we use data related to repositories in github.

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

As we see the response data, format looks exactly like the query. This
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

Lets look at an example of a query where we only ask for first 3
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

Lets say for example we have a complex query, which has repetitive 
fields in it.

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

As the query gets bigger and complex, we can use `fragment` to split
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
commandline.

```bash
curl -X POST \
-H "Content-Type: application/json;" \
-d '{"query": "{ repository (name: $name) { name url } }", "variables": \
{ "name": "book" }}' \
http://localhost:8000/graphql/
```

Variables can be defined in the *Query Variables* panel at left bottom
of the *GraphiQL* client, which is an IDE(Interactive Development
Environment) for GraphQL. There are many implementations of *GraphiQL*
available. For this chapter we will use
[GraphiQL](https://github.com/skevy/graphiql-app).  Its usage is
discussed later in this chapter.

A variable is defined as a json object and this is how it looks like

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

which will fetch response 

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
options to GraphQL executors. Currently core GraphQL specification
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

Mutations are used to modify server side data. To demonstrate this,

let us look at the query and data to be passed along with it

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

which will give response

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

In application we need to validate user input. If it is invalid we can
use `GraphQLError` class or Python exceptions to raise validation
errors.

## GraphQL in Python :o:

In this example we will implement a GraphQL server in Python. For this
we will use [Graphene](https://graphene-python.org/) which is a
library for implementing GraphQL APIs in Python. We will cover a basic
server implementation with schema and queries to fetch and mutate
data.

To develop a GraphQL server in Python we will create virtual
environment for project to keep all the dependencies isolated from
other projects and system. To do so please follow the deplyment of a
virtualenv as discussied in the Python section or if you use Python 3
you could also use `venv`.

We have two examples that are located in the book repository which you
can clone with

```bash
$ git clone https://github.com/cloudmesh-community/book
```

The examples itself are located in the directories

* [book/examples/graphql/cloudmeshrepo](https://github.com/cloudmesh-community/book/tree/master/examples/graphql/cloudmeshrepo) - A graphql server example with local database
* [book/examples/graphql/github](https://github.com/cloudmesh-community/book/tree/master/examples/graphql/github) - A graphql server example using GitHub API v3

To execute the examples you need to go in the specific
directory. Thus, for  `cloudmeshrepo` say

```bash
$ cd book/examples/graphql/cloudmeshrepo
```

and for the github example execute

```bash
cd book/examples/graphql/github
```

Then you can execute following steps

```bash
$ pip install graphene==2.0.1 graphene-django==2.0.0 
$ pip install django==2.0.2 django-filter==1.1.0
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

If you want to create GraphQL server while using django as the server
backend yourself, you can start with following steps

```bash
$ mkdir -p example/graphql
$ cd example/graphql
$ pip install graphene==2.0.1 graphene-django==2.0.0 
$ pip install django==2.0.2 django-filter==1.1.0
$ pip install django-graphql-jwt==0.1.5
$ django-admin startproject cloudmeshrepository
$ cd cloudmeshrepository
$ python manage.py migrate
$ python manage.py runserver
```

The last command will start a server on th localhost and you can
access it at the URL

* <http://localhost:8000>

It will show you the welcome page for django. Now open the file

:o: this seems wrong I thought we want to develop this ourselfs. The
description does not match the example.

`cloudmeshrepo/cloudmeshrepo/settings.py`


file under folder and append following to
INSTALLED_APPS

```python
INSTALLED_APPS = (
    # After the default packages
    'graphene_django',
)
```

And at the end of settings.py add following line

```python
GRAPHENE = {
    'SCHEMA': 'cloudmeshrepo.schema.schema',
}
```

### Django for GraphQL

:o: i am confused, now we do this again?

For the purpose of this example, we will use Django as Python web
framework.  Django is a popular Python web framework which already
comes with a lot of boilerplate code. It is mature and has a very
large community.  It has inbuilt support for Object Relational Mapping
which is based on Database Code-First approach. Please refer
[@www-djangoproject] for more Django information.

### GraphQL server implementation :o:

Django seperates project into apps. Here we will have one app for
Users and one for Repos. Django provides support for SQLite so we will
use that for demo.

Go to root dir of project and execute following command

```bash
python manage.py startapp repository
```

Open Repositories/models.py and add following line

```python
class Repository(models.Model):
    url = models.URLField()
    name = models.TextField(blank=False)
    full_name = models.TextField(blank=False)
    description = models.TextField(blank=True)
```

Now open cloudmeshRepository/settings.py and append following line into
INSTALLED_APPS

```python
INSTALLED_APPS = (
    # After the graphene_django app
    'Repositories',
)
```

Go to root folder and execute following commands. It will create table
for new modeld

```bash
python manage.py makemigrations
python manage.py migrate

python manage.py shell
```

Last command will open Python shell. Execute following command inside
that shell to create some data. following example data we got from
github's API https://api.github.com/users/cloudmesh-community/repos.

:o: TODO: reformat to 80 lines if possible

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

Now create Repositories/schema.py with following code. This will
introduce custom type of Repository and query with resolver for
Repositories.

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

Create cloudmeshRepository/schema.py with following code. It just
inherits query defind in Repositories app. This way we are able to
isolate schema to their apps.

```python
import graphene
  
import Repositories.schema


class Query(Repositories.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
```
### GraphQL Server Querying :o:

Schema is created now to query it we will use *GraphiQL* which is
playground for GraphQL queries. Open cloudmeshrepository/urls.py and
append following code

```python
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```

Start your server using following command

```bash
python manage.py runserver
```

Now open the URL

* <http://localhost:8000/graphql>

in your broweser. You will see *GraphiQL*. In the left pane add the
following query

```graphql
{
  repositoriess {
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

### Mutation example :o:

Similar to a query you can add mutation to create your own data. Add a
`CreateRepository` class for new repository object which will inherit
from graphene's Mutation class. This class will accept new repository
properties as arguments. Please see the following code snippet

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

Similar to Query, add `Mutation` class in repository's schema.

```python
class Mutation(graphene.ObjectType):
    create_repository = CreateRepository.Field()
```

Now you can run the following mutation on *GraphiQL* to add a new repository

```graphql
mutation {
  createRepository (
    url: "https://github.com/cloudmesh-community/vineet-test",
    name: "vineet-test",
    fullName: "cloudmesh-community/vineet-test",
    description: "Test repository"
  ) {
    url
    name
    fullName
    description
  }
}
```

And this will not just create a new repository but also get the newly 
added repository

```json
{
  "data": {
    "createRepository": {
      "url": "https://github.com/cloudmesh-community/vineet-test",
      "name": "vineet-test",
      "fullName": "cloudmesh-community/vineet-test",
      "description": "Test repository"
    }
  }
}
```

### GraphQL Authentication :o:

There a few ways to add authentication to your GraphQL server

* Add a REST API endpoint which will take care of authenticating the
  user and only the logged in users can make GraphQL queries. This
  method can also be used to restrict only a subset of GraphQL
  queries. This is ideal for existing applications, which have REST
  endpoints, and which are trying to migrate over to GraphQL.
* Add basic authentication to GraphQL server which will just accept
  credentials in raw format and once authenticated, logged in user can
  start GraphQL querying
* Add JSON Web Token authentication to GraphQL server, since most of
  the applications these days are stateless.

### JSON Web Authentication :o:

This is a more secure and sophisticated way of authentication. Client
has to provide username and password to mutate a token which has
limited expiry time. Once token is generated, it needs to be provided
with each subsequent GraphQL api calls which indicates GraphQL server
of authenticated requests.

To enable JWT authentication in your GraphQL server, you need to
install django-graphql-jwt. You can add this settings to settings.py
file.

```python
MIDDLEWARE = [
    'graphql_jwt.middleware.JSONWebTokenMiddleware',
[
```

```python
AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

Add the Token mutation

```python
class Mutation(users.schema.Mutation, repositories.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
```

Run the server and fire the token mutation providing username and password.

```graphql
mutation {
  tokenAuth (username:"user1", password:"Testing123") {
    token
  }
}
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

JWT library comes with inbuilt directive called *login_required*
You can add this any of your Query resolver to prevent unauthenticated access.

```python
from graphql_jwt.decorators import login_required

...

class Query(graphene.ObjectType):
    repositories = graphene.List(RepositoryType)

    @login_required
    def resolve_repositories(self, info, **kwargs):
        return Repository.objects.all()
```

Now if you try to query repositories from GraphQL, you will see this error

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

Henceforth you need to pass token with every repositories query. This token
needs to be passed as header which the *GraphiQL* ui client does not
support. Hence you can use either of these 2 ways

* curl command 

```bash
export TOKEN=eyJ0eXAiOiJKV1.... (cut to fit in line)
curl -X POST \
-H "Content-Type: application/json;" \
-H "Authorization: JWT $TOKEN" \
-d '{"query": "{ repositories { url } }"}' \
http://localhost:8000/graphql/
```

Result obtained from running this command: 

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

Clearly as you can see the output is not well formatted and hence not
the preferred way.

* Install GraphQL client like [Insomnia](https://insomnia.rest/graphql/), [Altair](https://altair.sirmuel.design/) or [GraphiQL](https://github.com/skevy/graphiql-app).
  Advantage of using these clients is that they are much user 
  friendly and provide a well formatted json output.

JWT tokens are bearer tokens which need to be passed in HTTP
authorization header. JWT tokens are very safe against CSRF attacks
and are trusted and verified since they are digitally signed.

JWT tokens can have expiry period. Typically, GraphQL server host 
provides the token expiry information to client through some kind of 
documentation. If the token is about to be expired, you can call `refreshToken` 
mutation and the response would be a refreshed token. However if the token 
has already expired then you can again request a new token by calling 
`tokenAuth` mutation.

Find more about JWT tockens at [@jwt-tockens] and GraphQL
authentication at [@medium-graphql]

Examples for GraphQL are available at:

* <https://github.com/cloudmesh-community/book/tree/master/examples/graphql> and [@www-howtographql]

### GitHub API v4 :o:

GitHub has implemented API v4 using GraphQL which allows you to query
or mutate data of repositories for which you have access. To access GitHub API v4
first we need to install [GraphiQL](https://github.com/skevy/graphiql-app).

For MacOS

```bash
brew cask install graphiql
```

* Now we need OAuth token to access GitHub API. You can generate OAuth
  token by following steps mentioned at
  https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
* Open *GraphiQL* app and click edit headers at upper-right corner. Add
  new header with key *Authorization* and value *Bearer your_token*
* Enter *https://api.github.com/graphql* in GraphQL endpoint textbox
* Keep method as *POST* only

To test the changes add following query

```graphql
query {
  viewer {
    login
    name
  }
}
```

which gives response

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

To get your repositories add following query

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

and define variables used in query

```json
{
   "number_of_repositories": 3
}
```

it gives following response

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

To add a comment using mutation we need to get issue id 

For example query

```graphql
{
  repository(owner:"MihirNS", name:"Temp_Repository") {
    issue(number: 1) {
      id
    }
  }
}
```

it gives following response

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

Now we can use this id as subjectId for mutation to add comment to an
issue,

For query

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

it gives following response

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

Official documentation of Github API v4 is available at [@github-v4]

## Advantages and Disadvantages of Using GraphQL :o:

### Advantages :o:

* Unlike REST APIs, only the required data is fetched, nothing more
  nothing less, which minimizes the data transferred over network
* Seperation of concern is achieved between client and server. Client
  requests data entities with fields needed for the UI in one query
  request while server knows about the data structure and how to
  resolve the data from its sources which could be database, web
  service, microservice, external APIs, etc.
* Versioning is simpler than REST, since we only have to take care of
  it when we want to remove any of the fields. Even then we can first
  mark the field to be removed as deprecated. And later on, this field
  can be removed when not many clients are using it.

```graphql
type Car {
    id: ID!
    make: String
    description: String @deprecated(reason: "Field is deprecated!")
}
``` 

* GraphQL is gaining momentum as its community, support and enthusiasm
  is growing. Many GraphQL editors, IDEs and packages are getting
  added day by day.
  
### Disadvantages :o:

* GraphQL query can get very complex. Client may not necessarily know
  how expensive the queries can be for server to go and gather the
  data. This can be overcome by limiting the query depth, recursion,
  etc.
* Caching gets pretty tricky and messy in case of GraphQL. In REST,
  you can have seperate API url for each resource requested, caching
  can be done at this resource level. However in GraphQL you can have
  different queries but they can operate over a single API url. This
  means that caching needs to be done at the field level rather, and
  hence it is difficult.


## Conclusion :o:

In general there are many reasons to have GraphQL in our software
ecosystem. Beauty of it lies in the flexibility and extensiveness it
provides and also fits well with the microservices architecture which
many are moving towards. Already big players like Github, Pinterest,
Intuit, Coursera, Shopify, etc. are using it.  With that being said,
REST APIs still have it is own place and may prove better choice in
certain use cases. Both REST and GraphQL have some tradeoffs which
need to be understood before being considered.
