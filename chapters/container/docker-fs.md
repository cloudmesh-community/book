# Docker and Docker Swarm on FutureSystems

This section is for IU students only that take classes with us.

This section introduces how to run Docker container on FutureSystems.
Currently we have deployed Docker swarm on Echo.

## Getting Access

You will need an account on FutureSystems and be enrolled in an active
project. To verify, try to see if you can log into
india.futuresystems.org. You need to be a member of a valid
FutureSystems project, and had submitted an ssh public key via the
FutureSystems portal.

For 2018 you need to be in the following project:

<https://portal.futuresystems.org/project/537>

If your access to the india host has been verified, try to login to the
docker swarm head node. To conveniently do this let us define some Linux
environment variables to simplify the access and the material presented
here. You can place them even in your `.bashrc` or `.bash_profile` so
the information gets populated whenever you start a new terminal.If you 
directly edit the files make sure to execute the ```source``` command to refresh
 the environment variables for the current session using ```source .bashrc```
or ```source .bash_profile```. Or you can close the current shell and reopen a 
new one. 

```bash
$ export ECHO=149.165.150.76
$ export FS_USER=<put your futersystem here>
```

Now you can use the two variables that were set to login to the Echo serer, 
using the following command

```bash
$ ssh $FS_USER@$ECHO
```

If you have access to india but not the docker swarm system, your
project may not have been authorized to access the docker swarm cluster.
Send a ticket to FutureSystems ticket system to request this.

Once logged in to the docker swarm head node, try to run:

```bash
$ docker run hello-world
```

to verify `docker run` works.

## Creating a service and deploy to the swarm cluster

While `docker run` can start a container and you may even attach to its
console, the recommended way to use a docker swarm cluster is to create
a service and have it run on the swarm cluster. The service will be
scheduled to one or many number of the nodes of the swarm cluster, based
on the configuration. It is also easy to scale up the service when more
swarm nodes are available. Docker swarm really makes it easier for
service/application developers to focus on the functionality development
but not worrying about how and where to bind the service to some
resources/server. The deployment, access, and scaling up/down when
necessary, are all managed transparently. Thus achieving the new
paradigm of *serverless computing*.

As an example, the following command creates a service and deploy it to
the swarm cluster, if the port is in use the port ```9001``` used in the command
can be changed to an available port

:o: Fugang check the command

```bash
$ docker service create --name notebook_test -p 9001:8888 \
    jupyter/datascience-notebook start-notebook.sh
    --NotebookApp.password=NOTEBOOK_PASS_HASH
```
    
The NOTEBOOK_PASS_HASH can be generated in python:

```python
>>> import IPython
>>> IPython.lib.passwd("YOUR_SELECTED_PASSWROD")
'sha1:52679cadb4c9:6762e266af44f86f3d170ca1......'
```

So pass through the string starting with 'sha1:\...\...'.

The command pulls a published image from docker cloud, starts a
container and runs a script to start the service inside the container
with necessary parameters. The option "-p 9001:8888" maps the service
port inside the container (8888) to an external port of the cluster node
(9001) so the service could be accessed from the Internet. In this
example, you can then visit the URL:

```bash
$ open http://$ECHO:9001
```

to access the Jupyter notebook. Using the specified password when you
create the service to login.

Please note the service will be dynamically deployed to a container
instance, which would be allocated to a swarm node based on the
allocation policy. Docker makes this process transparent to the user and
even created mesh routing so you can access the service using the IP
address of the management head node of the swarm cluster, no matter
which actual physical node the service was deployed to.

This also implies that the external port number used has to be free at
the time when the service was created.

Some useful related commands:

```bash
$ docker service ls
```

lists the currently running services.

```bash
$ docker service ps notebook_test
```

lists the detailed info of the container where the service is running.

```bash
$ docker node ps NODE
```

lists all the running containers of a node.

```bash
$ docker node ls
```

lists all the nodes in the swarm cluster.

To stop the service and the container:

```bash
$ docker service rm noteboot_test
```

## Create your own service

You can create your own service and run it. To do so, start from a base
image, e.g., a ubuntu image from the docker cloud. Then you could:

-   Run a container from the image and attach to its console to develop
    the service, and create a new image from the changed instance using
    command 'docker commit'.

-   Create a dockerfile, which has the step by step building process of
    the service, and then build an image from it.

In reality, the first approach is probably useful when you are in the
phase of develop and debug your application/service. Once you have the
step by step instructions developed the latter approach is the
recommended way.

Publish the image to the docker cloud by following this documentation:

* <https://docs.docker.com/docker-cloud/builds/push-images/>

Please make sure no sensitive information is included in the image to be
published. Alternatively you could publish the image internally to the
swarm cluster.

## Publish an image privately within the swarm cluster

Once the image is published and available to the swarm cluster, you
could start a new service from the image similar to the Jupyter Notebook
example.

## Exercises

E.Docker.Futuresystems.1:

> Obtain an account on future systems.

E.Docker.Futuresystems.2:

> Create a REST service with swagger codegen and run it on the echo cloud.
