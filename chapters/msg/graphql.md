# GraphQL :o:

:o: TODO: use full sentences, there are several ocasions where a
sentence seems incomplete. such as Examples available at I will fix
that pariculare example, but can you fix the other sentences ...

:o: you switch examples, between car and employee, i suggest to make
examples consistent :o: why not use the example computer and you do ip
adresses, and OS, and things like that relating it to cloud.


## Introduction

GraphQL is data query language developed by Facebook. 

GraphQL allows clients to request data they need without thinking
about the API implementation. It makes application devlopment fast and
stable because the application has control over data it needs and
format. The benefit of Graphql is also to reduce network I/O since
only the necessary data is transfered from the server to the client.

Unlike REST APIs which require loading data via multiple URLs, GraphQL
can get all data the application needs in single request. GraphQL APIs
are defined in terms of types and fields. Types help GraphQL to ensure
that client only asks for what is possible and in case of faults
provides clear and helpful errors.

Initially GraphQL was implemented in JavaScript. Today there are
several other implementations in different language available of
GraphQLs. We will explore the *graphql-python* implementation in this
chapter. The gGraphQL official documentation is available at
[@graphql-learn]


## GraphQL type system and schema

:o: TODO: no section without initial paragraph

### Type System

In GraphQL a query is what we request from a graphql server. The
result will be obtained in structure defined bby a type and schema. It
means we will know ahead of time what we arre going to get as result,
nothing less and nothing more. For this to work, the data is often to
be assumed structured data.

Here is how a simple graphQL query would look like

```graphql
{
    person {
        name 
        age
        friends {
            name
        }
    }
}
```

The response is

```json
{
    "person": {
        "name": "John Doe",
        "age": 25,
        "friends": [
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
server, it is firts validated to a schema that defines the types
contained within the graphql service.

Hence, types must be defined as part of each graphql service. THey are
defined with the graphql schema language which is programming language
agnostic. An example of a graphql type is:

```graphql
type Person {
    name: String!
    age: Int
    friends: [Person!]!
}
```

Note that the `!` indicates a field value, that cannot be null and
must have a defined value. `[Person!]!` means that an array is
returned, but that the array cannot be null and also none of the items
in the array can be null.


### Scalar Types

Graphql supports the following scalar types:

* `String`: UTF8 characters
* `Int`: 32 bit signed integer
* `Float`: Double precision floating point value
* `Boolean`: true or false
* `ID`: Represents a unique identifier which can be used as a key to fetch the object

### Enumeration Types

`Enums` also are scalar types which define a certain set of restricted
values. When a graphql schema defines a field of enum type, we expect
that the field's value be of the type enum values only. An example of
an enum type is

```graphql
enum FuelType {
    Petrol
    Diesel
    Hybrid
}
```

### Interfaces

Similar to any programming language, the graphql type system also supports
interfaces. When a type implements an interface, it needs to specify all the
fields that ar defined through the interface.

We illustrate this in the following example, where we define simple
vehicle interface type. The Vehicle interface declares `Id`, `Name`
and `Wheels` fields. This means that a `Motorcycle` and a Car both
implement a Vehicle and must have the fields defined in the
interface. They may or may not have additional fields like we
demonstrat in our example with the field `Make` in case of Motorcycle
and Fuel in case of the `Car`.

```graphql
interface Vehicle {
    Id: ID!
    Name: String!
    Wheels: Int!
}

type Motorcycle implements Vehicle {
    Id: ID!
    Name: String!
    Wheels: Int!
    Make: String!
}

type Car implements Vehicle {
    Id: ID!
    Name: String!
    Wheels: Int!
    Fuel: FuelType
}
```


### Union Types

As the name suggests, union types represent the union of two or more
types. Here is how we can define a union type. As you can see we use
the `|` charater to indicate the union operator.

```graphql
union VehicleType = Motorcycle | Car
```

Now when we write a graphql query to fetch the `VehicleType`
information, we can ask some of the common fields and some of the
specific fields conditionally. In the next example we request
`AllVehicleTypes` with common fields like `Id`, `Name` and fields
specific to either `Motorcycle` or `Car`.

```graphql
{
    AllVehicleTypes {
        Id
        Name
        ... on Motorcyle {
            Make
        }
        ... on Car {
            Fuel
        }
    }
}
```

### Input Types :o:

:o: TODO: an introduction paragraph is missing

## GraphQL Query

An application asks for data from server in form of a GraphQL *query*. A GraphQL
query can have different fields and arguments. We describe how to use
them next.

### Fields

A very simple definition of a query is to ask for speific fields
that belong to an object stored in graphQL.

When asking the query

```graphql
{
    employee {
        name
    }
}
```

we obtain the following response

```json
{
    "data": {
        "employee": {
            "name": "John Doe"
        }
    }
}
```


As we see the response data format exactly looks like the query. This
way a client knows excatly what data it has to consume. In the previous
example the `name` field returns the data of type `String`. Clients can also
ask for an object representing any match within the graphQL database.

For example the query

```graphql
{
    employer {
        name
        employees {
            name
        }
    }
}
```

returns the response

```json
{
    "data": {
        "employer": {
            "name": "Abc Company",
            "employees": [{
                "name": "John Doe"
            }, {
                "name": "Jon Doe"
            }]
        }
    }
}
```

### Arguments :o:

Unlike REST services where you can pass parameters as part of a
request via query parameters through *GET* or a request body thorough
*POST*, in GraphQL you can provide to every field an argument
restrictiong the data returned to only the information that you
need. This reduces the traffic for returning the information that is
needed without doing the postprocessing on the client.  The
restricting arguments can be of scalar type, enumeration type and
others.

Let use look at an example where through a query we only aske for
emplyees with the age of 29.

:o: TODO: as age discrimination in the US is serious, we want to come
up with a better example. Or describe a scenario where fecthing the 29
year olds makes sense. Maybe we can do department?

```graphql
{
    employees(age: 29) {
        name
        age
    }
}
```

The response will be similar to

```json
{
    "data": {
        "employees": [{
            "name": "John Doe",
            "age": 29
        }, {
            "name": "Jon Doe",
            "age": 29
        }]
    }
}
```

:o: TODO: Gregor came till here

### Fragments :o:

To resuse your fields in query you can create Fragments in
GraphQL. For example

Query

```graphql
{
    employer(id: 10) {
        ...employeeInfo
    }
}
fragment employeeInfo on Employer {
    name
    employees {
        name
    }
}
```

Response

```json
{
    "employer": {
        "name": "Abc Company",
        "employees": [{
            "name": "John Doe"
        }, {
            "name": "Jon Doe"
        }]
    }
}
```

Fragement are generally used to split complex queries into chunks and
reuse of query fields.

### Variables :o:

Variables are used to pass dynamic values to queries. It is not good
practice to interpolate dynamic values from user action on client side
to construct queries. Instead of that GraphQL provides a way to define
a variable and pass value for that variable at runtime using
dictionary.

Query

```graphql
{
    employees(age: $employeeAge) {
        name
        age
    }
}
```

```json
{
    "employeeAge": 29
}
```

Response

```json
{
    "data": {
        "employees": [{
            "name": "John Doe",
            "age": 29
        }, {
            "name": "Jon Doe",
            "age": 29
        }]
    }
}
```

### Directives :o:

Directives are used to change structure of queries at runtime using
variables. Directive can be attached to field or fragment
inclusion. There are two directives which must be supported by any
graphql-server implementation

* `@skip (if: Boolean)` - It skips the field if argument is true
* `@Include (if: Boolean)` - It inclues the field if argument is true

Query

```graphql
{
    employees(age: $employeeAge) {
        name
        age
        personalInfo @Include(if: $showPersonalInfo) {
            address
            contact
        }
    }
}
```

```json
{
    "employeeAge": 29,
    "showPersonalInfo": true
}
```

Response

```json
{
    "data": {
        "employees": [{
            "name": "John Doe",
            "age": 29,
            "personalInfo": {
                "address": "remote",
                "contact": "123456789"
            }
        }]
    }
}
```

### Mutations :o:

Mutations are used to modify server side data. 

Query

```graphql
mutation CreateEmployeeForEmployer($employer: Employer!, $employee: Employee!) {
    createEmployee(employer: $employer, employee: $employee) {
        name
        age
    }
}
```

```json
{
    "employer": "Abc Company",
    "employee": {
        "name": "John Doe",
        "age": 29
    }
}
```

Response

```json
{
    "data": {
        "createEmployee": {
            "name": "John Doe",
            "age": 29
        }
    }
}
```

### Query Validation :o:

Because of use of types in GraphQL query we can know whether query is
valid or not before executing it. It can be achieved using validator
provided by GraphQL implementation. To use validator you need to write
test cases and use validator to validate schema

## Django Django is a very popular full-blown python web framework :o:

which is fast and comes with a lot of boilerplate code. Django is
matured and has a huge community support as against flask which is
very new, still evolving and generally considered for only small
applications. Django has inbuilt support for Object Relational Mapping
which is based on Database Code-First approach. Please refer
[@www-djangoproject] for more Django information.

## GraphQL Implementations :o:

GraphQL is supported in Python, JavaScript, Java, Ruby, C#, Go, PHP,
Erlang, Scala, Go, Groovy, Elixir.

## GraphQL-python (Graphene) Example :o:

### Getting Started :o:

To start with GraphQL server implementation in python we will create
virtual environment for project to keep all the dependencies isolated
from other projects and system. To leave it execute "deactivate"
command in shell. Always remember to activate virtual environment.

* :o: TODO: mkdir -p  example/graphql
* :o: TODO: whould we just do a wget or culr on the git example dir
  and cd into it?
* :o: TODO: you remind me that venv is now part of python 3, so we
  coudl do an alternative install of python 3 with altinstall and
  document hat in the pythin section instead of using pyenv


```bash
mkdir python-graphql-example
cd python-graphql-example
python3 -m venv venv
source venv/bin/activate
```

Now the project has been changed to (venv) so it means we are in
virtual environment. Execute following commands

```bash
pip install graphene==2.0.1 graphene-django==2.0.0 
pip install django==2.0.2 django-filter==1.1.0
pip install django-graphql-jwt==0.1.5
django-admin startproject cloudmeshrepo
cd cloudmeshrepo
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
Repo.objects.create(name="boat",full_name="cloudmesh-community/boat",url="https://github.com/cloudmesh-community/boat",description="S.T.A.R. boat")
Repo.objects.create(name="book",full_name="cloudmesh-community/book",url="https://github.com/cloudmesh-community/book",description="Gregor von Laszewski")
Repo.objects.create(name="cm",full_name="cloudmesh-community/cm",url="https://github.com/cloudmesh-community/cm",description="Cloudmesh v4")
Repo.objects.create(name="cm-burn",full_name="cloudmesh-community/cm-burn",url="https://github.com/cloudmesh-community/cm-burn",description="Burns many SD cards so we can build a Raspberry PI cluster")
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

Now open

* <http://localhost:8000/graphql>

URL in your broweser. You will see GraphiQL. In the left pane add
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

Similar to Query you can add mutation to create your own data. Add a
Create class for new repo object which will inherit from graphene's
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

There a few ways of adding authentication to your graphql server

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

:o: :TODO: could we not put the token in an env variable and use that, or
have a secript that does find the token from the file that you use earlier?

* curl command 

```bash
curl -X POST \
-H "Content-Type: application/json;" \
-H "Authorization: JWT eyJ0eXAiOiJKV1.... (cut to fit in line)" \
-d '{"query": "{ repos { url } }"}' \
http://localhost:8000/graphql/
```

Result obtained from running this command: 

```
{"data":{"repos":[{"url":"https://github.com/cloudmesh-community/boat"},{"url":"https://github.com/cloudmesh-community/book"},{"url":"https://github.com/cloudmesh-community/cm"},{"url":"https://github.com/cloudmesh-community/cm-burn"},{"url":"https://github.com/cloudmesh-community/vineet-test-1"},{"url":"https://github.com/cloudmesh-community/vineet-test"}]}}
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
