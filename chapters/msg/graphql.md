# GraphQL :o:

:o: TODO: use full sentences, there are several ocasions where a
sentence seems incomplete. such as Examples available at I will fix
that pariculare example, but can you fix the other sentences ...

:o: you switch examples, between car and employee, i suggest to make
examples consistent :o: why not use the example computer and you do ip
adresses, and OS, and things like that relating it to cloud.


## Introduction

GraphQL is a data query language developed by Faceboo%k. 

GraphQL allows clients to request data they need without thinking
about the API implementation. It makes application devlopment fast and
stable because the application has control over the data it needs and
its format. The benefit of Graphql is also to reduce network I/O since
only the necessary data is transfered from server to client.

Unlike REST APIs, which require loading data via multiple URLs, GraphQL
can get all data, that application needs, in a single request. GraphQL APIs
are defined in terms of types and fields. Types help GraphQL to ensure
that client only asks for what is possible and in case of faults,
provides clear and helpful errors.

Initially GraphQL was implemented in JavaScript. Today there are
several other implementations in different language available of
GraphQLs. We will explore the *graphql-python* implementation in this
chapter. The GraphQL official documentation is available at
[@graphql-learn]


## GraphQL type system and schema

To get started with GraphQL we will first explore GraphQL type system
and schema creation.

### Type System

In GraphQL a query is what we request from the graphql server. The
result will be obtained in a structure defined by type and schema. It
means we will know ahead of time what we are going to get as
result. For this to work, the data is often assumed to be structured
data.

To demonstrate the type system we use a simple example while looking
at authors and co-authors of papers. We represent in this example a
database that containes a number of authors. each author has a
publication count and a number of coauthors that are identified by
name. We assume for this simple example that all author names are unique.

Here is how a simple graphQL query would look like

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
honored by the graphql service so that when a query is recieved by the
server, it is first validated to a schema that defines the types
contained within the graphql service.

Hence, types must be defined as part of each graphql service. They are
defined with the graphql schema language which is programming language
agnostic. An example of a graphql type is:

```graphql
type author {
    name: String!
    publication_count: Int
    coauthors: [author!]!
}
```

Note that the `!` indicates a field value, that cannot be null and
must have a defined value. `[author!]!` means that an array is
returned, but that array cannot be null and also none of the items
in the array can be null.


### Scalar Types

Graphql supports the following scalar types:

* `String`: UTF8 characters
* `Int`: 32 bit signed integer
* `Float`: Double precision floating point value
* `Boolean`: true or false
* `ID`: Represents a unique identifier which can be used as a key to fetch the object

### Enumeration Types

:o: the car example needs to be replaced with a compute resourec
example

`Enums` also are scalar types which define a certain set of restricted
values. When a graphql schema defines a field of enum type, we expect
that the field's value be of the type enum values only. An example of
an enum type is

```graphql
enum ContainerTYpe {
    Docker
    Kubernetes
    DockerSwarm
}
```

### Interfaces

Similar to any programming language, the graphql type system also supports
interfaces. When a type implements an interface, it needs to specify all the
fields that are defined through the interface.

We illustrate this in the following example, where we define simple
`ComputeService` interface type. This interface declares `Id`, `Name`
and `Memory` fields. This means that a `Container` and a `VirtualMachine` both
of which implement `ComputeService`, and must have the fields defined in the
interface. They may or may not have additional fields like we
demonstrate in our example with the field `ContainerBackend` in case of Container
and `VMBAckend` in case of the `VirtualMachine`.

```graphql
interface ComputeService {
    Id: ID!
    Name: String!
    Memory: Int!
}

type Container implements ComputeService {
    Id: ID!
    Name: String!
    Memory: Int!
    Type: ContainerType!
}

type VirtualMachine implements Vehicle {
    Id: ID!
    Name: String!
    Memory: Int!
    User: String!
}
```

where user indocates the name of the user to log into this vm.

### Union Types

As the name suggests, union types represent the union of two or more
types. Here is how we can define a union type. As you can see we use
the `|` charater to indicate the union operator.

```graphql
union COmputeType = Container | VirtualMachine
```

Now when we write a graphql query to fetch the `ComputeType`
information, we can ask some of the common fields and some of the
specific fields conditionally. In the next example we request
`AllComputeTypes` with common fields like `Id`, `Name` and fields
specific to either `VirtualMachine` or `Container`.

```graphql
{
    AllComputeTypes {
        Id
        Name
        ... on VirtualMachine {
            User
        }
        ... on Container {
            Type
        }
    }
}
```

## GraphQL Query

An application asks for data from server in form of a GraphQL *query*. 
A GraphQL query can have different fields and arguments and in this 
section we describe how to use them.

### Fields

A very simple definition of a query is to ask for specific fields
that belong to an object stored in graphQL.

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
way a client knows exactly what data it has to consume. In the previous
example, the `name` field returns the data of type `String`. Clients can 
also ask for an object representing any match within the graphQL database.

For example the query

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

### Arguments :o:

As you may already know in REST services you can pass parameters as 
part of a request via query parameters through *GET* or a request body 
thorough *POST*. However in GraphQL, for every field, you provide an 
argument restricting the data returned to only the information that you
need. This reduces the traffic for returning the information that is
needed without doing the postprocessing on the client. These
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

As the query gets bigger and complex, we can use *Fragments* to split 
it into smaller chunks.  These fragments can then be re-used which can 
significantly reduce the query query size and also make it more readable. 

A Fragment can be defined as

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

### Variables :o:

:o: this section needs to be improved as it can not be understood by a
non graphql expert. for example the term interpolate is not defined.

Variables are used to pass dynamic values to queries. Instead of passing 
hard-coded values to a query, variables can be defined for these values. 
Now these variables can be passed to queries.

**Variables can be defined in the Query variables panel at left bottom of 
the graphiql client**. The variable is defined as a json object and this 
is how it looks like

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

### Directives :o:

Directives are used to change the structure of queries at runtime using
variables. Directives provide a way to describe additional options to 
graphql executors. Currently core graphql specification supports two 
directives 

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
use GraphQLError class or python exceptions to raise validation errors.

## Django for graphQL

Django is a very popular python web framework which includes a lot of
boilerplate code. Due to this its footprint is larger than other
services, such as Flask, but provide a lot of build in features. Django is
mature and has a larger community than that of flask.
Django has inbuilt support for Object Relational Mapping
which is based on Database Code-First approach. Please refer
[@www-djangoproject] for more Django information. Database suport
however can also be easily added to falsk through plugins.

:o: the purpose of this section is unclear at this time. Django nd
flask have advantages and disadvantages.

## GraphQL-python (Graphene) Example :o:

:o: In this example we will ... intro missing

To start with GraphQL server implementation in python we will create
virtual environment for project to keep all the dependencies isolated
from other projects and system. To leave it execute *deactivate*
command in shell. Always remember to activate virtual environment.

* :o: TODO: mkdir -p  example/graphql
* :o: TODO: whould we just do a wget or culr on the git example dir
  and cd into it?
* :o: TODO: you remind me that venv is now part of python 3, so we
  could do an alternative install of python 3 with altinstall and
  document that in the python section instead of using pyenv

```bash
mkdir -p example/graphql
cd example/graphql
python3 -m venv venv
source venv/bin/activate
```

Now the project has been changed to (venv) so it means we are in
virtual environment. Execute following commands

```bash
pip install graphene==2.0.1 graphene-django==2.0.0 
pip install django==2.0.2 django-filter==1.1.0
pip install django-graphql-jwt==0.1.5
django-admin startproject cloudmeshrepository
cd cloudmeshrepository
python manage.py migrate
python manage.py runserver
```

Last command will start server on localhost and you can access it at

* <http://localhost:8000>

URL. It will show you welcome page for django. Now open settings.py
file under cloudmeshrepo/cloudmeshrepo folder and append following to
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

### GraphQL server implementation :o:

Now django seperates project into apps. Here we will have one app for
Users and one for Repos. Django provides support for SQLite so we will
use that for demo.

Go to root dir of project and execute following command

```bash
python manage.py startapp repos
```

Open repos/models.py and add following line

```python
class Repo(models.Model):
    url = models.URLField()
    name = models.TextField(blank=False)
    full_name = models.TextField(blank=False)
    description = models.TextField(blank=True)
```

Now open cloudmeshrepo/settings.py and append following line into
INSTALLED_APPS

```python
INSTALLED_APPS = (
    # After the graphene_django app
    'repos',
)
```

Go to root folder and execute following commands. It will create table
for new modeld

```bash
python manage.py makemigrations
python manage.py migrate

python manage.py shell
```

Last command will open python shell. Execute following command inside
that shell to create some data. following example data we got from
github's API https://api.github.com/users/cloudmesh-community/repos.

:o: TODO: reformat to 80 lines if possible

```python
from repos.models import Repo
Repo.objects.create(
    name="boat",
    full_name="cloudmesh-community/boat",
    url="https://github.com/cloudmesh-community/boat",
    description="S.T.A.R. boat")
Repo.objects.create(
    name="book",full_name="cloudmesh-community/book",
    url="https://github.com/cloudmesh-community/book",
    description="Gregor von Laszewski")
Repo.objects.create(name="cm",
    full_name="cloudmesh-community/cm",
    url="https://github.com/cloudmesh-community/cm",
    description="Cloudmesh v4")
Repo.objects.create(name="cm-burn",
    full_name="cloudmesh-community/cm-burn",
    url="https://github.com/cloudmesh-community/cm-burn",
    description="Burns many SD cards so we can build a Raspberry PI cluster")
exit()
```

Now create repos/schema.py with following code. This will introduce
custom type of Repo and query with resolver for repos.

```python
import graphene
from graphene_django import DjangoObjectType

from .models import Repo


class RepoType(DjangoObjectType):
    class Meta:
        model = Repo


class Query(graphene.ObjectType):
    repos = graphene.List(RepoType)

    def resolve_repos(self, info, **kwargs):
        return Repo.objects.all()
```

Create cloudmeshrepo/schema.py with following code. It just inherits
query defind in repos app. This way we are able to isolate schema to
their apps.

```python
import graphene
  
import repos.schema


class Query(repos.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
```
### Querying implemented GraphQL server :o:

Schema is created now to query it we will use GraphiQL which is
playground for graphql queries. Open cloudmeshrepo/urls.py and append
following code

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

in your broweser. You will see GraphiQL. In the left pane add the
following query

```graphql
{
  repos {
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
    "repos": [
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
*Create* class for new repo object which will inherit from graphene's
Mutation class. This class will accept new repo properties as
Arguments. Please see the following code snippet

```python
class CreateRepo(graphene.Mutation):
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
        repo = Repo(url=url, name=name, full_name=full_name, description=description)
        repo.save()

        return CreateRepo(url=repo.url, name=repo.name, full_name=repo.full_name, description=repo.description)
```

Similar to Query, add Mutation class in repo's schema.

```python
class Mutation(graphene.ObjectType):
    create_repo = CreateRepo.Field()
```

Now you can run the following mutation on graphiql to add a new repo

```graphql
mutation {
  createRepo (
    url: "https://github.com/cloudmesh-community/vineet-test",
    name: "vineet-test",
    fullName: "cloudmesh-community/vineet-test",
    description: "Test repo"
  ) {
    url
    name
    fullName
    description
  }
}
```

And this will not just create a new repo but also get the newly added repo

```json
{
  "data": {
    "createRepo": {
      "url": "https://github.com/cloudmesh-community/vineet-test",
      "name": "vineet-test",
      "fullName": "cloudmesh-community/vineet-test",
      "description": "Test repo"
    }
  }
}
```

### GraphQL Authentication :o:

There a few ways to add authentication to your graphql server

* Add a REST Api endpoint which will take care of authenticating the
  user and only the logged in users can make graphql queries. This
  method can also be used to restrict only a subset of graphql
  queries. This is ideal for existing applications, which have REST
  endpoints, and which are trying to migrate over to graphql.
* Add basic authentication to graphql server which will just accept
  credentials in raw format and once authenticated, logged in user can
  start graphql querying
* Add JSON Web Token authentication to graphql server, since most of
  the applications these days are stateless.

### JSON Web Authentication :o:

This is a more secure and sophisticated way of authentication. Client
has to provide username and password to mutate a token which has
limited expiry time. Once token is generated, it needs to be provided
with each subsequent graphql api calls which indicates graphql server
of authenticated requests.

To enable JWT authentication in your graphql server, you need to
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
class Mutation(users.schema.Mutation, repos.schema.Mutation, graphene.ObjectType):
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
    repos = graphene.List(RepoType)

    @login_required
    def resolve_repos(self, info, **kwargs):
        return Repo.objects.all()
```

Now if you try to query repos from graphql, you will see this error

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
        "repos"
      ]
    }
  ],
  "data": {
    "repos": null
  }
}
```

Henceforth you need to pass token with every repos query. This token
needs to be passed as header which the graphiql ui client does not
support. Hence you can use either of these 2 ways

:o: :TODO: could we not put the token in an env variable and use that,
or have a secript that does find the token from the file that you use
earlier?

* curl command 

```bash
export TOKEN=eyJ0eXAiOiJKV1.... (cut to fit in line)
curl -X POST \
-H "Content-Type: application/json;" \
-H "Authorization: JWT $TOKEN" \
-d '{"query": "{ repos { url } }"}' \
http://localhost:8000/graphql/
```

Result obtained from running this command: 

```
{"data":{"repos":[
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

* Install graphql client like Insomnia or Altair Advantage of using
  these clients is that they are much user friendly and provide a well
  formatted json output.

JWT tokens are bearer tokens which need to be passed in HTTP
authorization header. JWT tokens are very safe against CSRF attacks
and are trusted and verified since they are digitally signed.

Find more about JWT tockens at [@jwt-tockens] and graphql
authentication at [@medium-graphql]

Examples for graphql are available at:

* <https://github.com/cloudmesh-community/book/tree/master/examples/graphql/> and [@www-howtographql]

To use them please do:

```bash
$ mkdir -p cloudmesh-community/example
$ cd cloudmesh-community/example
$ wget https://github.com/cloudmesh-community/book/tree/master/examples/graphql
$ cd grpahql
```

### GitHub API v4 :o:

GitHub has implemented API v4 using graphql which allows you to query
or mutate data for which you have access. To access GitHub API v4
first we need to install [GraphiQL](https://github.com/skevy/graphiql-app).

For MacOS

```bash
brew cask install graphiql
```

* Now we need OAuth token to access GitHub API. You can generate OAuth
  token by following steps mentioned at
  https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
* Open GraphiQL app and click edit headers at upper-right corner. Add
  new Header with key "Authorization" and value "Bearer *your token*"
* Enter "https://api.github.com/graphql" in GraphQL Endpoint textbox
* Keep method as "POST" only

To test the changes add following query

```graphql
query {
  viewer {
    login
    name
  }
}
```

Response

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

To get your repos add following query

```graphql
query($number_of_repos:Int!) {
  viewer {
    name
     repositories(last: $number_of_repos) {
       nodes {
         name
       }
     }
   }
}
```

Define variables

```json
{
   "number_of_repos": 3
}
```

Response

```json
{
  "data": {
    "viewer": {
      "name": "*your name*",
      "repositories": {
        "nodes": [
          {
            "name": "*Repo 1*"
          },
          {
            "name": "*Repo 2*"
          },
          {
            "name": "*Repo 3*"
          }
        ]
      }
    }
  }
}
```

To add a comment using mutation we need to get issue id 

Query

```graphql
{
  repository(owner:"MihirNS", name:"Temp_Repo") {
    issue(number: 1) {
      id
    }
  }
}
```

Response

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

Query

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

Response

```json
{
  "data": {
    "addComment": {
      "commentEdge": {
        "node": {
          "repository": {
            "nameWithOwner": "MihirNS/Temp_Repo"
          },
          "url": "https://github.com/MihirNS/Temp_Repo/issues/1#issuecomment-425620312"
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

* Graphql is gaining momentum as its community, support and enthusiasm
  is growing. Many graphql editors, IDEs and packages are getting
  added day by day.
  
### Disadvantages :o:

* Graphql query can get very complex. Client may not necessarily know
  how expensive the queries can be for server to go and gather the
  data. This can be overcome by limiting the query depth, recursion,
  etc.
* Caching gets pretty tricky and messy in case of graphql. In REST,
  you can have seperate API url for each resource requested, caching
  can be done at this resource level. However in graphql you can have
  different queries but they can operate over a single API url. This
  means that caching needs to be done at the field level rather, and
  hence it is difficult.


## Conclusion :o:

In general there are many reasons to have graphql in our software
ecosystem. Beauty of it lies in the flexibility and extensiveness it
provides and also fits well with the microservices architecture which
many are moving towards. Already big players like Github, Pinterest,
Intuit, Coursera, Shopify, etc. are using it.  With that being said,
REST APIs still have it is own place and may prove better choice in
certain use cases. Both REST and graphql have some tradeoffs which
need to be understood before being considered.
