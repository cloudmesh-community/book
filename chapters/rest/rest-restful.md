# Flask RESTful Services

Flask is a micro services framework allowing to write web services in
python quickly. One of its extensions is Flask-RESTful. It adds for
building REST APIs based on a class definition making it relatively
simple. Through this interface we can than integrate with your existing
Object Relational Models and libraries. As Flask-RESTful leverages the
main features from Flask an extensive set of documentation is available
allowing you to get started quickly and thoroughly. The Web page
contains extensive documentation:

* <https://flask-restful.readthedocs.io/en/latest/>

We will provide a simple example that showcases some *hard coded* data
to be served as a rest service. It will be easy to replace this for
example with functions and methods that obtain such information
dynamically from the operating system.

This example has not been tested. We like that the class defines a
beautiful example to contribute to this section and explains what
happens in this example.

```
    from flask import Flask
    from flask_restful import reqparse, abort
    from flask_restful import Api, Resource
    
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
```
        
