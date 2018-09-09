REST
====


Overview of REST
----------------

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

Flask RESTful Services
----------------------

Flask is a micro services framework allowing to write web services in
python quickly. One of its extensions is Flask-RESTful. It adds for
building REST APIs based on a class definition making it relatively
simple. Through tis interface we can than integrate with your existing
Object Relational Models and libraries. As Flask-RESTful leverages the
main features from Flask an extensive set of documentation is available
allowing you to get started quickly and thoroughly. The Web page
contains extensive documentation:

* <https://flask-restful.readthedocs.io/en/latest/>

We will provide a simple example that showcases some *hard coded* data
to be served as a rest service. It will be easy to replace this for
example with functions and methods that obtain such information
dynamically from the operating system.

This example has not been tested., We like that the E222 class defines a
beautiful example to contribute to this section. and explains what
happens in this example.

    from flask import Flask
    from flask_restful import reqparse, abort, Api, Resource

    app = Flask(__name__)
    api = Api(app)

    COMPUTERS = {
        'computer1': {
          'processor': 'iCore7'
        },
        'computer2': {
          'processor': 'iCore5'
        },
        'computer3': {
          'processor': 'iCore3'
        },
    }

    def abort_if_cluster_doesnt_exist(computer_id):
        if computer_id not in COMPUTERS:
            abort(404, message="Computer {} does not exist".format(computer_id))

    parser = reqparse.RequestParser()
    parser.add_argument('processor')

    class Computer(Resource):
        ''' shows a single computer item and lets you delete a computer
            item.'''

        def get(self, computer_id):
            abort_if_computer_doesnt_exist(computer_id)
            return COMPUTERS[computer_id]

        def delete(self, computer_id):
            abort_if_computer_doesnt_exist(computer_id)
            del COMPUTERS[computer_id]
            return '', 204

        def put(self, computer_id):
            args = parser.parse_args()
            processor = {'processor': args['processor']}
            COMPUTERS[computer_id] = processor
            return processor, 201


    # ComputerList
    class ComputerList(Resource):
        ''' shows a list of all computers, and lets you POST to add new computers'''

        def get(self):
            return COMPUTERS

        def post(self):
            args = parser.parse_args()
            computer_id = int(max(COMPUTERS.keys()).lstrip('computer')) + 1
            computer_id = 'computer%i' % computer_id
            COMPUTERS[computer_id] = {'processor': args['processor']}
            return COMPUTERS[computer_id], 201

    ##
    ## Setup the Api resource routing here
    ##
    api.add_resource(ComputerList, '/computers')
    api.add_resource(Computer, '/computers/<computer_id>')


    if __name__ == '__main__':
        app.run(debug=True)

Rest Services with Eve
----------------------

Next, we will focus on how to make a RESTful web service with Python
Eve. Eve makes the creation of a REST implementation in python easy.
More information about Eve can be found at:

* <http://python-eve.org/>

Although we do recommend Ubuntu 17.04, at this time there is a bug that
forces us to use 16.04. Furthermore, we require you to follow the
instructions on how to install pyenv and use it to set up your python
environment. We recommend that you use either python 2.7.14 or 3.6.4. We
do not recommend you to use anaconda as it is not suited for cloud
computing but targets desktop computing. If you use pyenv you also avoid
the issue of interfering with your system wide python install. We do
recommend pyenv regardless if you use a virtual machine or are working
directly on your operating system. After you have set up a proper python
environment, make sure you have the newest version of pip installed with

\smallskip
    {language=bash}
    $ pip install pip -U

To install Eve, you can say

    {language=bash}
    $ pip install eve

As Eve also needs a backend database, and as MongoDB is an obvious
choice for this, we will have to first install MongoDB. MongoDB is a
Non-SQL database which helps to store light weight data easily.

### Ubuntu install of MongoDB

On Ubuntu you can install MongoDB as follows

    {language=bash}
    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
    $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/
    mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org

### OSX install of MongoDB

On OSX you can use the command

    {language=bash}
    brew update.
    brew install mongodb

### Windows 10 Installation of MongoDB

A student or student group of this class are invited to discuss on
piazza on how to install mongoDB on Windows 10 and come up with an easy
installation solution. Naturally we have the same 2 different ways on
how to run mongo. In user space or in the system. As we want to make
sure your computer stays secure. the solution must have an easy way on
how to shut down the Mongo services.

An enhancement of this task would be to integrate this function into
cloudmesh cmd5 with a command *mongo* that allows for easily starting
and stopping the service from *cms*.

### Database Location

After downloading Mongo, create the *db* directory. This is where the
Mongo data files will live. You can create the directory in the default
location and assure it has the right permissions. Make sure that the
/data/db directory has the right permissions by running

### Verification

In order to check the MongoDB installation, please run the following
commands in one terminal:

    {language=bash}
    $ mkdir -p ~/cloudmesh/data/db
    $ mongod --dbpath ~/cloudmesh/data/db

In another terminal we try to connect to mongo and issue a mongo command
to show the databases:

    {language=bash}
    $ mongo --host 127.0.0.1:27017
    $ show databases

If they execute without errors, you have successfully installed MongoDB.
In order to stop the running database instance run the following
command. simply CTRL-C the running mongod process

### Building a simple REST Service

In this section we will focus on creating a simple rest service. To
organize our work we will create the following directory:

    {language=bash}
    $ mkdir -p ~/cloudmesh/eve
    $ cd ~/cloudmesh/eve

As Eve needs a configuration and it is read in by default from the file
`settings.py` we place the following content in the file
`~/cloudmesh/eve/settings.py`:

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'student_db'
    DOMAIN = {
        'student': {
            'schema': {
                'firstname': {
                    'type': 'string'
                },
                'lastname': {
                    'type': 'string'
                },
                'university': {
                    'type': 'string'
                },
                'email': {
                    'type': 'string',
                     'unique': True
                }
                'username': {
                    'type': 'string',
                     'unique': True
                }
            }
        }
    }
    RESOURCE_METHODS = ['GET', 'POST']

The DOMAIN object specifies the format of a `student` object that we are
using as part of our REST service. In addition we can specify
`RESOURCE_METHODS` which methods are activated for the REST service.
This way the developer can restrict the available methods for a REST
service. To pass along the specification for mongoDB, we simply specify
the hostname, the port, as well as the database name.

Now that we have defined the settings for our example service, we need
to start it with a simple python program. We could name that program
anything we like, but often it is called simply `run.py`. This file is
placed in the same directory where you placed the **settings.py**. In
our case it is in the file `~/cloudmesh/eve/run.py` and contains the
following python program:

    from eve import Eve
    app = Eve()

    if __name__ == '__main__':
        app.run()

This is the most minimal application for Eve, that uses the settings.py
file for its configuration. Naturally, if we were to change the
configuration file and for example change the DOMAIN and its schema, we
would naturally have to remove the database previously created and start
the service new. This is especially important as during the development
phase we may frequently change the schema and the database. Thus it is
convenient to develop necessary cleaning actions as part of a Makefile
which we leave as easy exercise for the students.

Next, we need to start the services which can easily be achieved in a
terminal while running the commands:

Previously we started the mongoDB service as follows:

    {language=bash}
    $ mongod --dbpath ~/cloudmesh/data/db/

This is done in its own terminal, so we can observe the log messages
easily. Next we start in another window the Eve service with

    {language=bash}
    $ cd ~/cloudmesh/eve
    $ python run.py

You can find the codes and commands up to this point in the following
document.

### Interacting with the REST service

Yet in another window, we can now interact with the REST service. We can
use the commandline to save the data in the database using the REST api.
The data can be retrieved in XML or in json format. Json is often more
convenient for debugging as it is easier to read than XML.

Naturally, we need first to put some data into the server. Let us assume
we add the user Albert Zweistein.

    {language=bash}
    $ curl -H "Content-Type: application/json" -X POST \
           -d '{"firstname":"Albert","lastname":"Zweistein", \
           "school":"ISE","university":"Indiana University", \
           "email":"albert@iu.edu", "username": "albert"}' \
           http://127.0.0.1:5000/student/

To achieve this, we need to specify the header using **H** tag saying we
need the data to be saved using json format. And **X** tag says the HTTP
protocol and here we use POST method. And the tag **d** specifies the
data and make sure you use json format to enter the data. Finally, the
REST api endpoint to which we must save data. This allows us to save the
data in a table called **student** in MongoDB within a database called
**eve**.

In order to check if the entry was accepted in mongo and included in the
server issue the following command sequence in another terminal:

    $ mongo

Now you can query mongo directly with its shell interface

    > show databases
    > use student_db  
    > show tables # query the table names
    > db.student.find().pretty()  # pretty will show the json in a clear way

Naturally this is not really necessary for A REST service such as eve as
we show you next how to gain access to the data via mongo while using
REST calls. We can simply retrieve the information with the help of a
simple URI:

    {language=bash}
    $ curl http://127.0.0.1:5000/student?firstname=Albert

Naturally, you can formulate other URLs and query attributes that are
passed along after the `?`.

This will now allow you to develop sophisticated REST services. We
encourage you to inspect the documentation provided by Eve to showcase
additional features that you could be using as part of your efforts.

Let us explore how to properly use additional REST API calls. We assume
you have MongoDB up and running. To query the service itself we can use
the URI on the Eve port

    {language=bash}
    $ curl -i http://127.0.0.1:5000

Your payload should look like the one below, if your output is not
formatted like below try adding `?pretty=1`

    {language=bash}
    $ curl -i http://127.0.0.1:5000?pretty=1

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 150
    Server: Eve/0.7.6 Werkzeug/0.11.15 Python/2.7.5
    Date: Wed, 17 Jan 2018 18:34:07 GMT

    {
        "_links": {
            "child": [
                {
                    "href": "student",
                    "title": "student"
                }
            ]
        }

Remember that the API entry points include additional information such
as links and a child, and href.

Set up a python environment that works for your platform. Provide
explicit reasons why anaconda and other prepackaged python versions have
issues for cloud related activities. When may you use anaconda and when
should you not use anaconda. Why would you want to use pyenv?

What is the meaning and purpose of links, child, and href

In this case how many child resources are available through our API?

Develop a REST service with Eve and start and stop it

Define curl calls to store data into the service and retrieve it.

Write a Makefile and in it a target clean that cleans the data base.
Develop additional targets such as start and stop, that start and stop
the mongoDB but also the Eve REST service

Issue the command

    {language=bash}
    $ curl -i http://127.0.0.1:5000/people

What does the `_links` section describe?

What does the `_items` section describe?

    {
        "_items": [],
        "_links": {
            "self": {
                "href": "people",
                "title": "people"
            },
            "parent": {
                "href": "/",
                "title": "home"
            }
        },
        "_meta": {
            "max_results": 25,
            "total": 0,
            "page": 1
        }
    }


### Creating REST API Endpoints

Next we wont to enhance our example a bit. First, let us get back to the
eve working directory with

     $ cd ~/cloudmesh/eve

Add the following content to a file called **run2.py**

    from eve import Eve
    from flask import jsonify
    import os
    import getpass

    app = Eve ()

    @app.route('/student/albert')
    def alberts_information():
        data = {
            'firstname': 'Albert',
            'lastname': 'Zweistsein',
            'university': 'Indiana University',
            'email': 'albert@example.com'
            }
        try:
            data['username'] = getpass.getuser()
        except:
            data['username'] = 'not-found'
        return jsonify(**data)

    if __name__ == '__main__':
        app.run(debug=True, host="127.0.0.1")

After creating and saving the file. Run the following command to start
the service

     $ python run2.py

After running the command, you can interact with the service while
entering the following url in the web browser:

    http://127.0.0.1:5000/student/alberts

You can also open up a second terminal and type in it

    curl http://127.0.0.1:5000/student/alberts

The following information will be returned:

    {
      "firstname": "Albert", 
      "lastname": "Zweistain", 
      "university": "Indiana University", 
      "email": "albert@example.com", 
      "username": "albert"
    }

This example illustrates how easy it is to create REST services in
python while combining information from a dict with information
retrieved from the system. The important part is to understand the
decorator **app.route**. The parameter specifies the route of the API
endpoint which will be the address appended to the base path,
**http://127.0.0.1:5000**. It is important that we return a jsonified
object, which can easily be done with the `jsonify` function provided by
flask.As you can see the name of the decorated function can be anything
you lok. The route specifies how we access it from the service.

### REST API Output Formats and Request Processing

Another way of managing the data is to utilize class definitions and
response types that we explicitly define.

If we want to create an object like Student, we can first define a
python class. Create a file called **student.py**. Please, note the get
method that returns simply the information in the dict for the class. It
is not related to the REST get function.

    class Student(object):
        def __init__(self, firstname, lastname, university, email):
            self.firstname = firstname
            self.lastname = lastname
            self.university = university
            self.email = email
            self.username = 'undefined'

        def get(self): 
           return self.__dict__

        def setUsername(self, name):
           self.username = name
           return name

Next we define a REST service with Eve as shown in the following listing

    from eve import Eve
    from student import Student
    import platform
    import psutil
    import json
    from flask import Response
    import getpass

    app = Eve()


    @app.route('/student/albert', methods=['GET'])
    def processor():
        student = Student("Albert", 
                          "Zweistein", 
                          "Indiana University", 
                          "albert@example.edu")

        response = Response()
        response.headers["Content-Type"] = "application/json; charset=utf-8"

        try:
            student.setUsername(getpass.getuser())
            response.headers["status"] = 200
        except:
            response.headers["status"] = 500

        response.data = json.dumps(student.get())        
        return response

    if __name__ == '__main__':
        app.run(debug=True, host='127.0.0.1')

In contrast to our earlier example, we are not using the jsonify object,
but create explicitly a response that we return to the clients. The
response includes a header that we return the information in json
format, a status of 200, which means the object was returned
successfully, and the actual data.

### WRONG: Consuming REST API Using a Client Application

\TODO{This example is not tested. Please provide feedback and improve}
In the Section [1.3.8](#s:rest-api-endpoints){reference-type="ref"
reference="s:rest-api-endpoints"} we created our own REST API
application using Python Eve. Now once the service running, a we need to
learn how to interact with it through clients.

First go back to the working folder:

     $ cd ~/cloudmesh/eve

Here we create a new python file called **client.py**. The file include
the following content.

    import requests
    import json

    def get_all():
        response = requests.get("http://127.0.0.1:5000/student")
        print(json.dumps(response.json(), indent=4, sort_keys=True))


    def save_record():
        headers = {
            'Content-Type': 'application/json'
        }

        data = '{"firstname":"Gregor",
                 "lastname":"von Laszewski",
                 "university": "Indiana University",
                 "email":"jane@iu.edu",
                 "username": "jane"}'

        response = requests.post('http://localhost:5000/student/',
                                  headers=headers,
                                  data=data)
        print(response.json())


    if __name__ == '__main__':
        save_record()
        get_all()

Run the following command in a new terminal to execute the simple client
by

     $ python client.py

Here when you run this class for the first time, it will run
successfully, but if you tried it for the second time, it will give you
an error. Because we did set the email to be a unique field in the
schema when we designed the settings.py file in the beginning. So if you
want to save another record you must have entries with unique emails. In
order to make this dynamic you can include a input reading by using the
terminal to get the student data first and instead of the static data
you can use the user input data from the terminal to get dynamic data.
But for this exercise we do not expect that or any other form data
functionality.

In order to get the saved data, you can comment the record saving
function and uncomment the get all function. In python commenting is done
by using `#`.

This client is using the **requests** python library to send GET, POST
and other HTTP requests to the server so you can leverage build in
methods to simplify your work.

The `get_all` function provides a way to get the output to the console
with all the data in the student database. The `save_record` function
provides a way to save data in the database. You can create dynamic
functions in order to save dynamic data. However it may take some time
for you to apply as exercise.

Write a RESTful service to determine a useful piece of information off
of your computer i.e. disk space, memory, RAM, etc. In this exercise
what you need to do is use a python library to extract data about
computer information mentioned above and send these information to the
user once the user calls an API endpoint like
http://localhost:5000/performance/ram, it must return the RAM value of
the given machine. For each information like disk space, RAM, etc you
can use an endpoint per each feature needed. As a tip for this exercise,
use the psutil library in python to retrieve the data, and then get
these information into an string then populate a class called Computer
and try to save the object like wise.

### HATEOAS

In the previous section we discussed the basic concepts about RESTful
web service. Next we introduce you to the concept of HATEOAS

HATEOAS stands for Hypermedia as the Engine of Application State and
this is enabled by the default configuration within Eve. It is useful to
review the terminology and attributes used as part of this
configuration. HATEOS explains how REST API endpoints are defined and it
provides a clear description on how the API can be consumed through
these terms:

_links

:   . Links describe the relation of current resource being accessed to
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

:   . The title in the rest endpoint is the name or topic that we are
    trying to address. It describes the nature of the object by a single
    word. For instance student, bank-statement, salary,etc can be a
    title.

parent

:   . The term parent refers to the very initial link or an API
    endpoint in a particular RESTful web service. Generally this is
    denoted with the primary address like http://example.com/api/v1/.

href

:   . The term href refers to the url segment that we use to access the
    a particular REST API endpoint. For instance "student?page=1" will
    return the first page of student list by retrieving a particular
    number of items from a remote database or a remote data source. The
    full url will look like this,
    "http://www.exampleapi.com/student?page=1".

In addition to these fields eve will automatically create the follwoing
information when resources are created as showcased ot

* <http://python-eve.org/features.html>

  Field        Description
  ------------ ----------------------------------------------------------------------
  `_created`   item creation date.
  `_updated`   item last updated on.
  `_etag`      ETag, to be used for concurrency control and conditional requests.
  `_id`        unique item key, also needed to access the individual item endpoint.

Pagenation information can be included in the `_meta` field.

#### Filtering

Clients can submit query strings to the rest service to retrieve
resources based on a filter. This also allows sorting of the results
queried. One nice feature about using mongo as a backend database is
that Eve not only allows python conditional expressions, but also mongo
queries.

A number of examples to conduct such queries include:

    curl -i -g http://eve-demo.herokuapp.com/people?where={%22lastname%22:%20%22Doe%22}

A python expression

    curl -i http://eve-demo.herokuapp.com/people?where=lastname=="Doe"

### Pretty Printing

Pretty printing is typically supported by adding the parameter `?pretty`
or `?pretty=1`

If this does not work you can always use python to beautify a json
output with

    curl -i http://localhost/people?pretty

or

    curl -i http://localhost/people | python -m json.tool

### XML

If for some reason you like to retrieve the information in XML you can
specify this for example through curl with an Accept header

    curl -H "Accept: application/xml" -i http://localhost

### Extensions to Eve

A number of extensions have been developed by the community. This
includes eve-swagger, eve-sqlalchemy, eve-elastic, eve-mongoengine,
eve-neo4j, eve.net, eve-auth-jwt, and flask-sentinel.

Naturally there are many more.

Students have the opportunity to pic one of the community extensions and
provide a section for the handbook.

Pick one of the extension, research it and provide a small section for
the handbook so we add it.

Object Management with Eve and Evegenie
---------------------------------------

<http://python-eve.org/>

Eve makes the creation of a REST implementation in python easy. We will
provide you with an implementation example that showcases that we can
create REST services without writing a single line of code. The code for
this is located at <https://github.com/cloudmesh/rest>

This code will have a master branch but will also have a dev branch in
which we will add gradually more objects. Objects in the dev branch will
include:

-   virtual directories

-   virtual clusters

-   job sequences

-   inventories

You may want to check our active development work in the dev branch.
However for the purpose of this class the master branch will be
sufficient.

### Installation

First we have to install mongodb. The installation will depend on your
operating system. For the use of the rest service it is not important to
integrate mongodb into the system upon reboot, which is focus of many
online documents. However, for us it is better if we can start and stop
the services explicitly for now.

On ubuntu, you need to do the following steps:

\TODO{TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS AS HOMEWORK}
On windows 10, you need to do the following steps:

\TODO{TO BE CONTRIBUTED BY THE STUDENTS OF THE CLASS AS HOMEWORK. If
  you elect Windows 10. You could be using the online documentation
  provided by starting it on Windows, or running it in a docker
  container.}
On OSX you can use home-brew and install it with:

    {language=bash}
    brew update
    brew install mongodb

In future we may want to add ssl authentication in which case you may
need to install it as follows:

    {language=bash}
    brew install mongodb --with-openssl

### Starting the service

We have provided a convenient Makefile that currently only works for
OSX. It will be easy for you to adapt it to Linux. Certainly you can
look at the targets in the makefile and replicate them one by one.
Important targets are deploy and test.

When using the makefile you can start the services with:

    {language=bash}
    make deploy

IT will start two terminals. IN one you will see the mongo service, in
the other you will see the eve service. The eve service will take a file
called sample.settings.py that is base on sample.json for the start of
the eve service. The mongo service is configured in such a way that it
only accepts incoming connections from the local host which will be
sufficient for our case. The mongo data is written into the
`$USER/.cloudmesh` directory, so make sure it exists.

To test the services you can say:

    {language=bash}
    make test

YOu will se a number of json text been written to the screen.

### Creating your own objects

The example demonstrated how easy it is to create a mongodb and an eve
rest service. Now let us use this example to create your own. For this
we have modified a tool called evegenie to install it onto your system.

The original documentation for evegenie is located at:

-   <http://evegenie.readthedocs.io/en/latest/>

However, we have improved evegenie while providing a commandline tool
based on it. The improved code is located at:

-   <https://github.com/cloudmesh/evegenie>

You clone it and install on your system as follows:

    {language=bash}
    cd ~/github
    git clone https://github.com/cloudmesh/evegenie
    cd evegenie
    python setup.py install
    pip install .

This should install in your system evegenie. YOu can verify this by
typing:

    which evegenie

If you see the path evegenie is installed. With evegenie installed its
usage is simple:

    $ evegenie

    Usage:
      evegenie --help
      evegenie FILENAME

It takes a json file as input and writes out a settings file for the use
in eve. Lets assume the file is called sample.json, than the settings
file will be called sample.settings.py. Having the evegenie program
will allow us to generate the settings files easily. You can include
them into your project and leverage the Makefile targets to start the
services in your project. In case you generate new objects, make sure
you rerun evegenie, kill all previous windows in which you run eve and
mongo and restart. In case of changes to objects that you have designed
and run previously, you need to also delete the mongod database.

Towards cmd5 extensions to manage eve and mongo
-----------------------------------------------

Naturally it is of advantage to have in cms administration commands to
manage mongo and eve from cmd instead of targets in the Makefile. Hence,
we **propose** that the class develops such an extension. We will create
in the repository the extension called admin and hope that students
through collaborative work and pull requests complete such an admin
command.

The proposed command is located at:

*
<https://github.com/cloudmesh/rest/blob/master/cloudmesh/ext/command/admin.py>

It will be up to the class to implement such a command. Please
coordinate with each other.

The implementation based on what we provided in the Make file seems
straight forward. A great extension is to load the objects definitions
or eve e.g. settings.py not from the class, but from a place in
.cloudmesh. I propose to place the file at:

    .cloudmesh/db/settings.py

the location of this file is used when the Service class is initialized
with None. Prior to starting the service the file needs to be copied
there. This could be achieved with a set command.

Responses
---------

Django REST Framework
---------------------

Django REST framework is a large toolkit to develop Web APIs. The
developers of the framework provide the following reasons for using it:

> "(1) The Web browsable API is a huge usability win for your developers.
> (2) Authentication policies including packages for OAuth1a and OAuth2.
> (3) Serialization that supports both ORM and non-ORM data sources. (4)
> Customizable all the way down - just use regular function-based views if
> you do not need the more powerful features. (5) Extensive documentation,
> and great community support. (6) Used and trusted by internationally
> recognised companies including Mozilla, Red Hat, Heroku, and
> Eventbrite."
