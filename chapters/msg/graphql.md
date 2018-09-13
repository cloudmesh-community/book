# GraphQL :o: {#s-graphql}

To be contributed by

* Mihir
* Vineet

The draft of this section is managed at

* <https://github.com/cloudmesh-community/fa18-516-21/blob/master/chapter/graphql.md>

## Example

We provide an example of using GraphQL as a 
mechanism for creating and developing web APIs.

Graphql has a few software requirements.  Howevre, the installation of all of the tools 
or software libraries will not be covered here.  It will be the 
reader's responsibility to install some of the software packages like python. 

### Required Software

The following software is required:

+ python 3.x
+ pyenv
+ pyenv virtualenv 
+ graphene
+ python libraries for mocking mongdb and mongodb objects
+ flask
+ pip
+ git
+ text editor such as emacs


### Assumptions

+ User knows how to work at the command line.
+ User has installed python 3+
+ User has installed and configured pyenv
+ User has installed and knows how to use a text editor like emacs, or vscode.
+ Working on a Unix/Linux/OSX based operating system.
+ User has a .bashrc (using bash shell)

### Steps/Procedures

1. Install python 3.x - Assumed to have been completely by the user.
2. Install pyenv - Assumed to have been completely by the user.
3. Create virtualenv. We recommend that you use pyenv

The preferred method for developing python based projects is to use a
separate environment for each python project.  There are several ways
to accomplish this.  The first is by creating a docker image and
container for the project but we do not it covered here.
The second method is by installing and using pyenv's virtualenv
plugin, this assumes the user has already installed and configured
pyenv.

### Using Virtualenv

First, access the command line. Next, install pyenv-virtualenv while
following the instructions provided at

* <https://github.com/pyenv/pyenv-virtualenv>

Or better, use our handbook and follow the instructions provided
there. At the command prompt type:

	git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
	echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
	exec "$SHELL"
	pyenv virtualenv graphqltut

We now have a python virtualenv that is specifically for this project.

### Installing Graphql

Before we start we create a a project folder and cd into it

	mkdir ~/cloudmesh/graphql

We need to install some of the libraries it depends on. At the command prompt type 

	pyenv activate graphqltut 
	
This makes sure we are using the local python development virtualenv
and not the global python environment. Now Type

	pip freeze 

which should *not* display a list of libraries since our virtualenv was just created.
We do this step to make sure you do not overwrite or modify your
default python environment. Now install flask and graphene:

	pip install flask
	pip install graphene
	pip install flask-graphql

We now have the minimum environment to build a Python GraphQL server and client.
One last step though.  It is a good idea to keep track of Python dependencies as we install them.  To do that, at the command line type: 

	pip freeze > requirements.text

This command saves the list of libraries we have installed plus the depdencies of the libraries we installed.  If for some reason you need to re-create 
the python virtualenv or someone else does then once the virtualenv is created the python libraries are easily re-installed my issued the command:

	pip install -r requirements.txt

### Build a graphql Application

Create and open a file named app.py.  This will be a very simple application server that runs the demo application.  

Now import the dependencies that we installed using pip.

	# File: app.py
	from flask import Flask
	from graphene import ObjectType, String, Schema
	from flask_graphql import GraphQLView

	class Query(ObjectType):
		status = String(description='Check graphql service status')
		def resolve_hello(self, args, context, info):
			return 'OK'

	view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query))

	app = Flask(__name__)
	app.add_url_rule('/graphql', view_func=view_func)

	@app.route('/')
	def index():
		return 'Hello!'

	if __name__ == '__main__':
		app.run(debug=True)

	Ref: #1

If you copy and paste the code in app.py then you will have to make sure that the file has proper python indenting, otherwise app.py will not run.

Let's test to make sure the server application will run.  Access the command prompt in the project folder and type ```python app.py```.

The flask application should display information to the console that an application server has been started on a local IP address and the server is listening on the default port, 5000.

Open a web browser and connect to http://127.0.0.1:5000.  The browser should render a web page that displays the message "Hello!".

We have already enabled the GraphQL endpoint by have the line in app.py that starts with "view_func".  Let's confirm that the GraphQL query-builder user interface is working by browsing opening the url http://127.0.0.1:5000/graphql in a browser window.

The resulting user interface (UI) lets a user develop and test QraphQL queries against the server created in app.py. The GraphQL UI has to panes.  The left pane is used to create a query and the right pane displays the query output.  A query can be executed by 
clicking the right-arrow (Run) button near the top of the UI.

Let's build and run our first query.
1. Click in the left pane
2. Type "{" and press the Enter key
3. Press the Control/Command key and the space bar at the same time.  This activates the UI's autocomplete feature.  The autocomplete feature knows about the query schema and can make it easier for the user to develop a query.
4. The autocomplete will display the word "status".  Highlight the status word and press the Enter key.  The query should look similar to the follwoing:

	{
  		status
	}

5. Click the Run button.  The query will run and display output that looks similar to the following:

	{
		"data": {
			"status": "OK"
		}
	}

The prior examples show basic setup and use of GraphQL.  We can add fake data and mock a MongoDB instance to demonstrate a more robust example of using GraphQL.

1. Access the terminal/command line in the project's root folder.
2. Type "pip install mongoengine mongomock graphene-mongo" and press the Enter key.
3. Type "pip freeze > requirements.txt" to keep the requirements.txt file update to date.
4. Using your editor open app.py.
5. Add the following code near the top of the app.py file as the last module import.

	from mongoengine import *
	from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
	import graphene
	from graphene.relay import Node

6. To create mock mongodb server, add the next line after the mongoengine import.
	
	connection = connect('mongoenginetest', host='mongomock://localhost')

7. We need a document object so add the following after the connect line.

	class TestObject(Document):
    	param = StringField()

7. We need some fake data, so add the next lines after the one we just created.

	for i in range(1, 5):
		to = TestObject(param=str(i))
		to.save()

8. We now need to let GraphQL know that we have this document or model.  Paste the following code after the for-loop for creating data, but before the Query class definition.

	class TestObjectMongoengineOjbectType(MongoengineOjbectType):
		class Meta:
			model = TestObject
			interfaces = (Node,)

9. In order to tell GraphQL to enable a query to the new object, In the Query class in app.py add:

	all_test_objects = MongoengineConnectionField(TestObjectMongoengineOjbectType)

10. The server app, app.py might need to be restarted, if so, restart the app by running "python app.py" at the terminal.

11. We want to create a new query in the GraphQL query UI to see the new model and data.  In the left-pane of the UI enter the following query definition and after entered click the run-button.

	{
		allTestObjects {
			edges {
			node {
				id
				param
			}
			}
		}
	}

12. The right-pane should produce output similar to the following.
	{
	"data": {
		"allTestObjects": {
		"edges": [
			{
			"node": {
				"id": "VGVzdE9iamVjdE1vbmdvZW5naW5lT2piZWN0VHlwZTo1YWI2YTIzNGJhNTY5YjMyY2EzZTUwYjE=",
				"param": "1"
			}
			},
			{
			"node": {
				"id": "VGVzdE9iamVjdE1vbmdvZW5naW5lT2piZWN0VHlwZTo1YWI2YTIzNGJhNTY5YjMyY2EzZTUwYjI=",
				"param": "2"
			}
			},
			{
			"node": {
				"id": "VGVzdE9iamVjdE1vbmdvZW5naW5lT2piZWN0VHlwZTo1YWI2YTIzNGJhNTY5YjMyY2EzZTUwYjM=",
				"param": "3"
			}
			},
			{
			"node": {
				"id": "VGVzdE9iamVjdE1vbmdvZW5naW5lT2piZWN0VHlwZTo1YWI2YTIzNGJhNTY5YjMyY2EzZTUwYjQ=",
				"param": "4"
			}
			},
			{
			"node": {
				"id": "VGVzdE9iamVjdE1vbmdvZW5naW5lT2piZWN0VHlwZTo1YWI2YTIzNGJhNTY5YjMyY2EzZTUwYjU=",
				"param": "5"
			}
			}
		]
		}
	}
	}

We do not address creating GraphQL queries that create, update, or delete objects.  However, we now have a running GraphQL server or web API that is useful as an example for reading data.

Here is the final app.py file.

	# File: app.py
	from flask import Flask
	from graphene import ObjectType, String, Schema
	from flask_graphql import GraphQLView
	from mongoengine import *
	from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
	import graphene
	from graphene.relay import Node

	# See reference: 3
	connection = connect('mongoenginetest', host='mongomock://localhost')

	# See reference: 3
	class TestObject(Document):
		param = StringField()

	# Fake some data, See ref: 3
	for i in range(1, 6):
		to = TestObject(param=str(i))
		to.save()

	# MongoengineOjbectType - needed by Graphene
	class TestObjectMongoengineOjbectType(MongoengineObjectType):
		class Meta:
			model = TestObject
			interfaces = (Node,)

	class Query(ObjectType):
		""" See: reference 1
		"""
	
		status = String(description='Check graphql service status')
		all_test_objects = MongoengineConnectionField(TestObjectMongoengineOjbectType)

		def resolve_status(self, args):
			return 'OK'

    # See reference 1
	view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query), graphiql=True)

    # See reference 1
	app = Flask(__name__)
	app.add_url_rule('/graphql', view_func=view_func)

	@app.route('/')
	def index():
		return 'Hello!'

	if __name__ == '__main__':
		app.run(debug=True)

## References

1. Graphql Site - https://bcb.github.io/graphql/flask
2. Mongoengine - https://github.com/MongoEngine/mongoengine
3. Mongomock & Mongoengine Example Usage - https://github.com/MongoEngine/mongoengine/issues/1045
4. Graphene-Mongo - https://github.com/graphql-python/graphene-mongo/tree/master/examples/flask_mongoengine
