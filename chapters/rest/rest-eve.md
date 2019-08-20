# Rest Services with Eve

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

    $ pip install pip -U

To install Eve, you can say

    $ pip install eve

As Eve also needs a backend database, and as MongoDB is an obvious
choice for this, we will have to first install MongoDB. MongoDB is a
Non-SQL database which helps to store light weight data easily.

## Ubuntu install of MongoDB

On Ubuntu you can install MongoDB as follows

```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
                   --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu \
    xenial/mongodb-org/3.6 multiverse" | \
    sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```
    
## macOS install of MongoDB

On macOS you can use the command

    $ brew update
    $ brew install mongodb

## Windows 10 Installation of MongoDB

A student or student group of this class are invited to discuss on
piazza on how to install mongoDB on Windows 10 and come up with an easy
installation solution. Naturally we have the same 2 different ways on
how to run mongo. In user space or in the system. As we want to make
sure your computer stays secure. the solution must have an easy way on
how to shut down the Mongo services.

An enhancement of this task would be to integrate this function into
cloudmesh cmd5 with a command *mongo* that allows for easily starting
and stopping the service from *cms*.

## Database Location

After downloading Mongo, create the *db* directory. This is where the
Mongo data files will live. You can create the directory in the default
location and assure it has the right permissions. Make sure that the
/data/db directory has the right permissions by running

## Verification

In order to check the MongoDB installation, please run the following
commands in one terminal:

    $ mkdir -p ~/cloudmesh/data/db
    $ mongod --dbpath ~/cloudmesh/data/db

In another terminal we try to connect to mongo and issue a mongo command
to show the databases:

    $ mongo --host 127.0.0.1:27017
    $ show databases

If they execute without errors, you have successfully installed MongoDB.
In order to stop the running database instance run the following
command. simply CTRL-C the running mongod process

## Building a simple REST Service

In this section we will focus on creating a simple rest service. To
organize our work we will create the following directory:

    $ mkdir -p ~/cloudmesh/eve
    $ cd ~/cloudmesh/eve

As Eve needs a configuration and it is read in by default from the file
`settings.py` we place the following content in the file
`~/cloudmesh/eve/settings.py`:

```
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
```
    
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

    $ mongod --dbpath ~/cloudmesh/data/db/

This is done in its own terminal, so we can observe the log messages
easily. Next we start in another window the Eve service with

    $ cd ~/cloudmesh/eve
    $ python run.py

You can find the codes and commands up to this point in the following
document.

## Interacting with the REST service

Yet in another window, we can now interact with the REST service. We can
use the commandline to save the data in the database using the REST api.
The data can be retrieved in XML or in json format. Json is often more
convenient for debugging as it is easier to read than XML.

Naturally, we need first to put some data into the server. Let us assume
we add the user Albert Zweistein.

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

    $ curl http://127.0.0.1:5000/student?firstname=Albert

Naturally, you can formulate other URLs and query attributes that are
passed along after the `?`.

This will now allow you to develop sophisticated REST services. We
encourage you to inspect the documentation provided by Eve to showcase
additional features that you could be using as part of your efforts.

Let us explore how to properly use additional REST API calls. We assume
you have MongoDB up and running. To query the service itself we can use
the URI on the Eve port

    $ curl -i http://127.0.0.1:5000

Your payload should look like the one listed next, if your output is not
formatted like this try adding `?pretty=1`

    $ curl -i http://127.0.0.1:5000?pretty=1

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 150
    Server: Eve/0.7.6 Werkzeug/0.11.15 Python/2.7.16
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

    $ curl -i http://127.0.0.1:5000/people

What does the `_links` section describe?

What does the `_items` section describe?

```
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
```

## Creating REST API Endpoints

Next we wont to enhance our example a bit. First, let us get back to the
eve working directory with

     $ cd ~/cloudmesh/eve

Add the following content to a file called **run2.py**

```
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
```

After creating and saving the file. Run the following command to start
the service

     $ python run2.py

After running the command, you can interact with the service while
entering the following url in the web browser:

    http://127.0.0.1:5000/student/alberts

You can also open up a second terminal and type in it

    $ curl http://127.0.0.1:5000/student/alberts

The following information will be returned:

```
{
  "firstname": "Albert", 
  "lastname": "Zweistain", 
  "university": "Indiana University", 
  "email": "albert@example.com", 
  "username": "albert"
}
```
    
This example illustrates how easy it is to create REST services in
python while combining information from a dict with information
retrieved from the system. The important part is to understand the
decorator **app.route**. The parameter specifies the route of the API
endpoint which will be the address appended to the base path,
`http://127.0.0.1:5000`.  It is important that we return a jsonified
object, which can easily be done with the `jsonify` function provided by
flask.As you can see the name of the decorated function can be anything
you lok. The route specifies how we access it from the service.

## REST API Output Formats and Request Processing

Another way of managing the data is to utilize class definitions and
response types that we explicitly define.

If we want to create an object like Student, we can first define a
python class. Create a file called **student.py**. Please, note the get
method that returns simply the information in the dict for the class. It
is not related to the REST get function.

```
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
```

Next we define a REST service with Eve as shown in the following listing

```
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
```

In contrast to our earlier example, we are not using the jsonify object,
but create explicitly a response that we return to the clients. The
response includes a header that we return the information in json
format, a status of 200, which means the object was returned
successfully, and the actual data.

##  REST API Using a Client Application

![No](images/no.png) This example is not tested. Please provide feedback and improve.

In the Section [Rest Services with Eve](#rest-services-with-eve) we
created our own REST API application using Python Eve. Now once the
service running, a we need to learn how to interact with it through
clients.

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
computer information mentioned previously and send these information to the
user once the user calls an API endpoint like
`http://localhost:5000/performance/ram`, it must return the RAM value of
the given machine. For each information like disk space, RAM, etc you
can use an endpoint per each feature needed. As a tip for this exercise,
use the psutil library in python to retrieve the data, and then get
these information into an string then populate a class called Computer
and try to save the object like wise.


## Towards cmd5 extensions to manage eve and mongo :o:

![No](images/no.png)

> ![Warning](images/warning.png) *Part of this section related to management of the mongo db
> serviceis done by the cm4 command we will be developping as part of
> this class `cms mongo admin` that does all of the things explained
> next and more.*

Naturally it is of advantage to have in cms administration commands to
manage mongo and eve from cmd instead of targets in the Makefile. Hence,
we **propose** that the class develops such an extension. We will create
in the repository the extension called admin and hope that students
through collaborative work and pull requests complete such an admin
command.

The proposed command is located at:

* <https://github.com/cloudmesh/cloudmesh.rest/blob/master/cloudmesh/admin/command/admin.py>

It will be up to the class to implement such a command. Please
coordinate with each other.

The implementation based on what we provided in the Make file seems
straight forward. A great extension is to load the objects definitions
or eve e.g. settings.py not from the class, but from a place in
.cloudmesh. I propose to place the file at:

    ~/.cloudmesh/db/settings.py

the location of this file is used when the Service class is initialized
with None. Prior to starting the service the file needs to be copied
there. This could be achieved with a set command.
