# Swagger-bravado, a fork of Swagger-py maintained by Yelp

In this section, we are discussing a Yelp maintained fork of Swagger. Bravado is a python client library for Swagger 2.0 services and it aims to replace Swagger-Codegen.  

We assume that you already understand the concept of REST API service and you have some knowledge on Swagger-Codegen.

## Some important features afforded by Bravado 
- Swagger models as Python types (no need to deal with JSON).
- Dynamically generated client - no code generation needed!
- Swagger Schema is v2.0 compatible.

To understand the features and advantages of Bravado, it is better to start with some practice.

### Installation
You can start easily in a python environment with this command to install the latest version of Bravado:

	$ pip install --upgrade bravado

### First try

After you have installed the bravado packages, here is a simple example for you to make the first try, you could run you code in a python environment:

	from bravado.client import SwaggerClient
	client = SwaggerClient.from_url("http://petstore.swagger.io/v2/swagger.json")
	pet = client.pet.getPetById(petId=42).result()

This piece of code shows an example that how to setup a bravado client and test its property. If you were lucky, and pet Id with 42 was present, you will get back a result. It will be a dynamically created instance of bravado.model.Pet with attributes category, etc. You can even try pet.category.id or pet.tags[0].
A sample response should be:

	Pet(category=Category(id=0L, name=u''), status=u'', name=u'', tags=[Tag(id=0L, name=u'')], photoUrls=[u''], id=2)

### Try to make a POST call
Here we will demonstrate how bravado hides all the JSON handling from the user.

	Pet = client.get_model('Pet')
	Category = client.get_model('Category')
	pet = Pet(id=42, name="tommy", category=Category(id=24))
	client.pet.addPet(body=pet).result()

### Example with Basic Authentication
Here is example code on how to request authentication from client side:


	from bravado.requests_client import RequestsClient
	from bravado.client import SwaggerClient

	http_client = RequestsClient()
	http_client.set_basic_auth(
   		 'api.yourhost.com',
    	'username', 'password'
	)
	client = SwaggerClient.from_url(
   		 'http://petstore.swagger.io/v2/swagger.json',
    	  http_client=http_client,
	)
	pet = client.pet.getPetById(petId=42).result()


### Asynchronous client
Bravado also provides an out of the box asynchronous http client with an optional timeout parameter. Before you could utilize the function as an asynchronous http client, you need to install your library as following command:

	$ pip install bravado[fido]

Then here is an example on how to configure a timeout option:
]
	from bravado.client import SwaggerClient
	from bravado.fido_client import FidoClient

	client = SwaggerClient.from_url(
   		 'http://petstore.swagger.io/v2/swagger.json',
    	FidoClient()
	)

	result = client.pet.getPetById(petId=42).result(timeout=4)


### Simple Returning without any model
If you want to get the result without specifying any models, you could try the following code:

	from bravado.client import SwaggerClient
	from bravado.fido_client import FidoClient

	client = SwaggerClient.from_url(
   		 'http://petstore.swagger.io/v2/swagger.json',
    	config={'use_models': False}
	)

	result = client.pet.getPetById(petId=42).result(timeout=4)

You can get the result as this:

	{
   	 	'category': {
        	'id': 0L,
        	'name': u''
    	},
    	'id': 2,
    	'name': u'',
    	'photoUrls': [u''],
    	'status': u'',
    	'tags': [
        	{'id': 0L, 'name': u''}
    	]
	}

## Configuration
### Configuration on Client Side
You can configure certain behaviours when creating a SwaggerClient. Here is a sample skeleton code for configuration:

	from bravado.client import SwaggerClient, SwaggerFormat

	mysuperformat = SwaggerFormat(...)

	config = {
   		# === bravado config ===

	    #Determines what is returned by the service call.
    	'also_return_response': False,

	    # === bravado-core config ====

   		#  validate incoming responses
    	'validate_responses': True,

	    # validate outgoing requests
   		'validate_requests': True,

    	# validate the swagger spec
    	'validate_swagger_spec': True,

    	# Use models (Python classes) instead of dicts for #/definitions/{models}
    	'use_models': True,

    	# List of user-defined formats
    	'formats': [my_super_duper_format],

	}

	client = SwaggerClient.from_url(..., config=config)

