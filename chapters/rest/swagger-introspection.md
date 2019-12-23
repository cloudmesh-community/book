# OpenAPI 3.0 REST Service via Introspection {#sec:openapi-introspection}

The simplest way to create an OpenAPI service is to use the conexion
service and read in the specification from its YAML file. It then
introspects and dynamically creates methods that are used for
the implementation of the server.

The full example for this is available in

* <https://github.com/cloudmesh-community/book/tree/master/examples/rest/cpu>

An extensive documentation is available at

* <https://media.readthedocs.org/pdf/connexion/latest/connexion.pdf>

This example returns the cpu information of a computer to dynamically
demonstrate how simple it is to generate in python a REST service from an
OpenAPI specification.

Our requirements.txt file includes

```
flask
connexion[swagger-ui]
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

This will run our REST service under the assumption we have a
`cpu.yaml` and a `cpu.py` files as our YAML file calls out methods
from `cpu.py`

The YAML file looks as follows.

```yaml
openapi: 3.0.2
info:
  title: cpuinfo
  description: A simple service to get cpuinfo as an example of using OpenAPI 3.0
  license:
    name: Apache 2.0
  version: 0.0.1

servers:
  - url: http://localhost:8080/cloudmesh

paths:
  /cpu:
    get:
      summary: Returns cpu information of the hosting server
      operationId: cpu.get_processor_name
      responses:
        '200':
          description: cpu info
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/cpu"

components:
  schemas:
    cpu:
      type: "object"
      required:
        - "model"
      properties:
        model:
          type: "string"
 ```

Here we implement a get method and associate is with the URL
/cpu. The operationid, defines the method that we call which, as we
used the local directory, is included in the file `cpu.py`. This is
controlled by the prefix in the operation id.

A straightforward function to return the CPU information is defined in
`cpu.py` which we list next

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

We have implemented this function to return a *jsonified* information
from the dict pinfo.

To simplify working with this example, we also provide a makefile for
OSX that allows us to call the server and the call to the server in
two different terminals

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

## Verification {#sec:swagger-verify}

It is essential to be able to verify if a YAML file is correct. To identify
this, the easiest method is to use the swagger editor. There is an online version
available at:

* <https://editor.swagger.io/>

Go to the Web site, remove the current petstore example, and paste your YAML file in it.
Debug messages are helping you to correct things.

A terminal-based command may also be helpful but is a bit difficult to read.

```bash
$ connexion run cpu.yaml --stub --debug
```

## Swagger-UI 

Swagger comes with a convenient UI to invoke REST API calls using the Web browser rather than relying on the curl commands. 

Once the request and response definitions are correctly specified, you can start 
the server by, 

```bash
$ python server.py
``` 

Then the UI would also be spawned under the service URL *http://\[service url\]/ui/*

Example: <http://localhost:8080/cloudmesh/ui/>


## Mock service

In some cases, it may be useful to develop the API without having yet developed
methods that you call with the OperationI. In this case, it is useful to run a
mock service. You can invoke such a service with

```bash
$ connexion run cpu.yaml --mock=all -v
```

## Exercise

OpenAPI.Conexion.1:

> Modify the makefile, so it also works on ubuntu, but do not disable
> the ability to run it correctly on OSX. Tip use if's in makefiles
> base on the OS. You can look at the makefiles that create this book
> as an example. Find alternatives to starting a terminal in Linux.

OpenAPI.Conexion.2:

> Modify the makefile, so it also works on Windows 10, but do not
> disable the ability to run it correctly on OSX. Tip use ifs in
> makefiles. You can look at the makefiles that create this book as
> example. Find alternatives to start a PowerShell or cmd.exe in
> windows. Maybe you need to use GitBash.

OpenAPI.Conexion.3:

> Implement a swagger specification of an issue related to the NIST
> BDRA. Implement it. Please remember this could prepare you for a
> project good topics include:

> * virtual compute service interfacing with AWS, Azure, Google or OpenStack
> * virtual directory service interfacing with google drive, box,
>   GitHub, iCloud, FTP, scp, and others

> As there are so many possibilities to contribute, come up in class with
> one specification and then implement it for different providers. The
> difficulty here is that it is not done for one IaaS, but for all of
> them and all can be integrated.

> This exercise is typically growing to be part of your class project.

OpenAPI.Conexion.4:

> Develop instructions on how to integrate the OpenAPI service framework in a
> WSGI based Web service. Chose a service you like so that the service could
> run in production.

OpenAPI.Conexion.5:

> Develop instructions on how to integrate the OpenAPI service framework in
> Tornado so the service could run in production.


