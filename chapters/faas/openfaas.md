# OpenFaaS :o: :hand: :fa18-516-23:

OpenFaas is a framework for building serverless functions on docker containers and follows the same workflow as micro services.
Since, OpenFaas uses Docker and Kubernetes technologies, it will give lot of hosting options ranges from a laptop 
to large-scale cloud systems
Any program written in any language can be packaged as a function within in a container which gives a best approach
to convert all the old code to run on cloud-based infrastructure

Few benefits of OpenFaas
1. Easy to Use
2. Deployable to private or public clouds in container
3. Simplicity in architecture and design
4. Open and extensible platform
5. Language agnostic


## OpenFaas Components and Architecture

There are three components which includes API Gateway, Function Watchdog and the instance of Prometheus.
All the functions are running on Docker containers orchestrated by either Docker Swarm or Kubernetes.
The function watchdog is part of the function containers, whereas the API Gateway and Promoethues instance are services.

![faas - OpenFaas - Arch[@alex2017faas]](images/openFaas_architecutre.jpg){#fig:cf-open-faas}

### API Gateway
Routes inbound requests to the functions and collects metrics through Prometheus. It autoscales modifying service replicas counts.
Offers a convenient UI and endpoints for the CLI

### Function Watchdog
It's a tiny HTTP server, encolsed along with the app in the docker image. It receives request from the API Gateway, triggers the app.
It provide args and catch result through STDIN/STDOUT

### OpenFaas CLI
The OpenFaas CLI provides mechanism to deploy the functions in the containders

### Monitoring
OpenFaas makes monitoring simple with the use of Prometheus. The end users can install Grafana Dashboard and connect point to the Promotehus data source. This provides quick access to the dashboard to monitor the OpenFaas functions

![faas - OpenFaas - Grafana@[alex2017faas]](images/grafana.jpeg){#fig:cf-open-faas-grafana}

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

1.  `$ git clone https://github.com/openfaas/faas`

2. `$ cd faas && \
  git checkout master`
3. `$ ./deploy_stack.sh --no-auth`

4. `cd <test function folder>`

5. `docker build -t <test function image>`

6. `faas-cli deploy --image <test function image> --name <test function name>`

### To Run OpenFaas

OpenFaas can be tested via curl, faas-cli, or any HTTP-based client to connect to the API gateway to invoke a function

Once the function is deployed, the functions can be verified in the following url
http://127.0.0.1:8080

![faas-OpenFaas-Portal[@alex2017faas]](images/markdown_portal.png){#fig:cf-open-faas-portal}


