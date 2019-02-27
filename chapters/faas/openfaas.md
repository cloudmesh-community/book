# OpenFaaS :o: :hand: :fa18-516-23:

OpenFaas is a framework for building serverless functions on docker containers and follows the same workflow as micro services.
Since, OpenFaas uses Docker and Kubernetes technologies, it will give lot of hosting options ranging from a laptop 
to large-scale cloud systems
Any program written in any language can be packaged as a function within in a container which gives a best approach
to convert all the old code to run on cloud-based infrastructure

Few benefits of OpenFaas

* Easy to Use
* Deployable to private or public clouds in container
* Simplicity in architecture and design
* Open and extensible platform
* Language agnostic


## OpenFaas Components and Architecture

There are three components which include API Gateway, Function Watchdog and the instance of Prometheus.
All the functions run on Docker containers orchestrated by either Docker Swarm or Kubernetes.
The function watchdog is part of the function containers, whereas the API Gateway and Promoethues instance are services.

![faas - OpenFaas - Arch [@alex2017faas]](images/openFaas_architecutre.jpg){#fig:cf-open-faas}

### API Gateway

Routes inbound requests to the functions and collects metrics through Prometheus. It autoscales modifying service replicas counts.
Offers a convenient UI and endpoints for the CLI

### Function Watchdog

It is a tiny HTTP server, encolsed along with the app in the docker image. It receives request from the API Gateway, triggers the app.
It provide args and catch result through STDIN/STDOUT

### OpenFaas CLI

The OpenFaas CLI provides mechanism to deploy the functions in the containders

### Monitoring

OpenFaas makes monitoring simple with the use of Prometheus. The end users can install Grafana Dashboard and connect point to the Promotehus data source. This provides quick access to the dashboard to monitor the OpenFaas functions

![faas - OpenFaas - Grafana [@alex2017faas]](images/grafana.jpeg){#fig:cf-open-faas-grafana}

## OpenFaas in Action

### Prerequistics

1. Docker
2. Git Bash (for Windows)

### Single Node Cluster

$ docker swarm init

Using a Terminal on Mac or Linux:

`$ curl -sL cli.openfaas.com | sudo sh`

For windows faas-cli.exe need to be downloaded from this link https://github.com/openfaas/faas-cli/releases


### Deploy OpenFaas 

OpenFaas gives the option to use yaml(.yml) file for configuring the functions and the image will be built by OpenFaas automatically.
Alternatively, custom docker image can be built and passed as an argument to the OpenFaas CLI. This gives the flexibility for the developers to extend further which is not in the standard yaml file.

```bash
$ git clone https://github.com/openfaas/faas
$ cd faas
$ git checkout master
$ ./deploy_stack.sh --no-auth
$ cd <test function folder>
$ docker build -t <test function image>
$ faas-cli deploy --image <test function image> --name <test function name
```

### To Run OpenFaas

OpenFaas can be tested via curl, faas-cli, or any HTTP-based client to connect to the API gateway to invoke a function

Once the function is deployed, the functions can be verified in the following url
<http://127.0.0.1:8080>

![faas-OpenFaas-Portal [@alex2017faas]](images/markdown_portal.png){#fig:cf-open-faas-portal}

## OpenFaaS Function with Python

This section illustrates how to create a simple Python function with OpenFaaS. 

Following are the the steps involved in creating and deploying a function with OpenFaaS
* Install OpenFaas
* Install the OpenFaaS CLI
* Build the function
* Deploy the function


Installing OpenFaas:

OpenFaaS installation guide can be viewed here - <https://docs.openfaas.com/deployment/> 


Installing CLI:

For Linux, type the following
```bash
$ curl -sSL https://cli.openfaas.com | sudo sh
```
For Mac, type the following
```bash
$ brew install faas-cli
```

Developing a Python function:

First, scaffold a new Python function using the CLI
```bash
$ faas-cli new --lang python func-python
```

Following 3 files will be created in the current directory
```bash
func-python/handler.py
func-python/requirements.txt
func-python.yml
```

Edit the handler.py
```python
def handle(req):
    print("Python Function: " + req)
```

Functions need to be specified in a YAML file created to indicate what to build and deploy onto the OpenFaas cluster. 
YAML file should be created as follows

```yaml
provider:
  name: faas
  gateway: http://127.0.0.1:8080

functions:
  func-python:
    lang: python
    handler: ./func-python
    image: func-python
```

YAML file description is as follows

* *gateway*- Location to specify a remote gateway, the programming language, and location of the handler within the filesystem.
* *functions* - This block defines the functions in our stack.
* *lang* - Programming language used. 
* *handler* - This is the folder / path fo the handler.py file and any other source code
* *image* - This is the Docker image name. If it is being pushed to the Docker Hub, prefix should include Docker Hub accountn


Build the function:
```bash
$ faas-cli build -f ./func-python.yml
...

Successfully tagged func-python:latest
Image: func-python built.
```

Docker engine builds the function into an image in the docker library and images will appear as follows
```bash
$ docker images | grep func-python
func-python        latest       <image ID>      one minute ago
```

Deploy the function:
```bash
$ faas-cli deploy -f ./func-python.yml
Deploying: func-python.
No existing service to remove
Deployed.
200 OK
URL: http://127.0.0.1:8080/function/func-python
```

Function can be tested either through the OpenFaas portal UI or with curl command
```bash
$ curl 127.0.0.1:8080/function/func-python -d "Test Successfull"
Python Function: Test Successfull
```

faas-cli commands can also be used to list and invoke the functions
```bash
faas-cli list
```

```bash
echo "Test" | faas-cli invoke func-python
```

In case third party dependencies are required, they can be specified in a requirements.txt file along with the function handler and the fucntion can be deployed.
