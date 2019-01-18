# OpenAPI REST Service via Introspection {#sec:openapi-introspection}

The simplest way to create an OpenAPI service is to use the conexion service and read in the specification. It will than be introspected and dynamically methods are created that are used for the implementation of the server.

The full example for this is available in

* <https://github.com/cloudmesh-community/nist/tree/master/examples/flask-connexion-swagger>

This example will return dynamically the cpu information of a computer.

Our requirements.txt file includes 

```
flask
connexion
```
as dependencies. The `server.py` file simply contains the following code:

```python
from flask import jsonify
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
```

This will run our REST service under the assumption we have a `cpu.yaml` and a `cpu.py` files as our yaml file calls out methods from `cpu.py`

The yaml file looks as follows

```
swagger: "2.0"
info: 
  version: "0.0.1"
  title: "cpuinfo"
  description: "A simple service to get cpuinfo as an example of using swagger-2.0 specification and codegen"
  termsOfService: "http://swagger.io/terms/"
  contact: 
    name: "Cloudmesh REST Service Example"
  license: 
    name: "Apache"
host: "localhost:8080"
basePath: "/cloudmesh"
schemes: 
  - "http"
consumes: 
  - "application/json"
produces: 
  - "application/json"
paths: 
  /cpu:
    get:
      tags:
        - CPU
      operationId: cpu.get_processor_name
      description: "Returns cpu information of the hosting server"
      produces: 
        - "application/json"
      responses: 
        "200":
          description: "CPU info"
          schema: 
            $ref: "#/definitions/CPU"
definitions:
  CPU:
    type: "object"
    required: 
      - "model"
    properties: 
      model:
      type: "string"
 ```

Here we simply implement a get method and associate is with the URL /cpu. The operationid, defines the method that we call which as we used the local directory is included in the file `cpu.py`. This is controlled by the prefix in the operation id.

A very simple function to return the cpi information is defined in `cpu.py` which we list next

```python
import os, platform, subprocess, re
from flask import jsonify

def get_processor_name():
    if platform.system() == "Windows":
        p = platform.processor()
    elif platform.system() == "Darwin":
        command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
        p = subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).strip().decode()
        for line in all_info.split("\n"):
            if "model name" in line:
                p = re.sub(".*model name.*:", "", line, 1)
    else:
        p = "cannot find cpuinfo"
    pinfo = {"model": p}
    return jsonify(pinfo)
```

We have implemented this function to return a jsonified information from the dict pinfo.

To simplify working with this example, we also provide a makefile for OSX that allows us to call the server and the call to the servoer in two different terminals

```
define terminal
	osascript -e 'tell application "Terminal" to do script "cd $(PWD); $1"'
endef

install:
	pip install -r requirements.txt

demo:
	$(call terminal, python server.py)
	sleep 3
	@echo "==============================================================================="
	@echo "Get the info"
	@echo "==============================================================================="
	curl http://localhost:8080/cloudmesh/cpu
	@echo
	@echo "==============================================================================="
```

When we call

```bash
make demo
```

our demo is run.

## Exercise

OpenAPI.Conexion.1:

> Modify the makefile so it works also on ubuntu, but do not disable the ability to
> run it correctly on OSX. Tip use ifs in makefiles

OpenAPI.Conexion.2:

> Modify the makefile so it works also on Windows 10, but do not disable the
> ability to run it correctly on OSX. Tip use ifs in makefiles

OpenAPI.Conexion.3:

> Implement a swagger specification of an issue related to the NIST
> BDRA. Implement it. Please remember this could prepare you for a
> project good topics include: 

> * virtual compute service interfacing with aws, azure, google or openstack
> * virtual directory service interfacing with google drive, box,
>   github, iCloud, ftp, scp, and others

As there are so many possibilities to contribute, come up in class with
one specification and than implement it for different providers. The
difficulty here is that it is not done for one IaaS, but for all of
them and all can be integrated.

This exercise is typically growing to be part of your class project.



