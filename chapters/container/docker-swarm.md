# Docker Swarm

A swarm is a group of machines that are running Docker and joined into
a cluster. Docker commands are executed on a cluster by a swarm
manager. The machines in a swarm can be physical or virtual. After
joining a swarm, they are referred to as *nodes*.

## Terminology

In this section if a command is prefixed with `local$` it means the command is
to be executed on your local machine. If it is prefixed with either 
`dsmaster` or `dsworker` that means the command is to be executed from within 
a virtual machine that was created.


## Creating a Docker Swarm Cluster
A swarm is made up of multiple nodes, which can be either physical or
virtual machines. The basic steps are:

1. run `docker swarm init` to enable swarm mode and make your current
   machine a swarm manager,
2. then run `docker swarm join` on other machines to have them join
   the swarm as workers. Choose a tab below to see how this plays out
   in various contexts. We use VMs to quickly create a two-machine
   cluster and turn it into a swarm.

## Create a Swarm Cluster with VirtualBox

In case you do not have access to multiple physical machines, you can
create a virtual cluster on your machine with the help of virtual
box. Instead of using `vagrant` we can use the built in `docker-machine`
command to start several virtual machines. 

If you do not have `virtualbox` installed on your machine install it on your 
machine. Additionally you would require `docker-machine` to be installed on your
local machine. To install `docker-machine` on please follow instructions at 
the docker documentation at [Install Docker Machine](https://docs.docker.com/machine/install-machine/)

To create the virtual machines you can use the command as follows:

```bash
local$ docker-machine create --driver virtualbox dsmaster
local$ docker-machine create --driver virtualbox dsworker
```

To list the VMs and get their ip addresses.
Use this command to list the machines and get their IP addresses.

```bash
local$ docker-machine ls
```

## Initialize the Swarm Manager Node and Add Worker Nodes

The first machine acts as the manager, which executes management
commands and authenticates workers to join the swarm, and the second
is a worker.

To instruct the first vm to become the master, first we need to login to 
the vm that was named `dsmaster`. To login you can use `ssh`, execute the 
following command on your local machine to login to the `dsmaster` vm.

```bash
local$ docker-machine ssh dsmaster 
```

Now since we are inside the `dsmaster` vm we can configure this vm as the docker
swarm manager. Execute the following command within the `dsmaster` vm in 
initialize swarm

```bash
dsmaster$ docker swarm init
```

If you get an error stating something similar to "could not choose an IP address
 to advertise since this system has multiple addresses on different 
interfaces", use the following command instead. To find the IP address 
execute the command `ifconfig` and pick the ip address which is most simmilar
 to `192.x.x.x`.

```bash
dsmaster$ docker swarm init --advertise-addr 192.x.x.x
``` 
The output wil look like this, where `IP-myvm1` is the ip address of the first vm


```bash
dsmaster$ Swarm initialized: current node (p6hmohoeuggtwqj8xz91zbs5t) is now 
a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5c3anju1pwx94054r3vx0v7j4obyuggfu2cmesnx 
    192.168.99.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```

Now that we have the docker swarm manager up we can add worker machines to 
the swarm. The command that is printed in the output shown above can be used 
to join workers to the manager. Please note that you need to use the output 
command that is generated when you run `docker swarm init` since the token 
values will be different. 

Now we need to use a separate shell to login to the worker vm that we created. 
Open up a new shell (or terminal) and use the following command to ssh into 
the `dsworker`

```bash
local$ docker-machine ssh dsworker 
```

Once you are in the `dsworker` execute the following command to join 
`dsworker` to the swam manager.

```bash
dsworker$ docker swarm join --token 
SWMTKN-1-5c3anju1pwx94054r3vx0v7j4obyuggfu2cmesnx 192.168.99.100:2377
```

The generic version of the command would be as follows, you need to fill in 
the correct values to values marked as '<>' to execute the command.
  
```bash
dsworker$ docker swarm join --token <token> <myvm ip>:<port>
```
You will see an output stating that this machine joined the docker swarm.

```bash
This node joined a swarm as a worker.
```

If you want to add another node as a manager to the current swarm you can 
execute the following command and follow the instructions. However this is 
not needed for this exercise.

```bash
newvm$ docker swarm join-token manager'
```

Run `docker-machine ls` to verify that `dsworker` is now the active
machine, as indicated by the asterisk next to it. 

 ```bash
local$ docker-machine ls 
 ```
If the astrix is not present execute the following command

```bash
local$ sudo sh -c 'eval "$(docker-machine env dsworker)"; docker-machine ls'
```

The output will look similar to 

```bash
NAME       ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
dsmaster   -        virtualbox   Running   tcp://192.168.99.100:2376           v18.06.1-ce   
dsworker   *        virtualbox   Running   tcp://192.168.99.102:2376           v18.06.1-ce
```

## Deploy the application on the swarm manager

Now we can try to deploy a test application. First we need to create a docker
configuration file which we will name `docker-compse.yml`. Since we are in 
the vm we need to create the file using the terminal. follow the steps given 
below the create and save the file. First log into the `dsmaster`

```bash
local$ docker-machine ssh dsworker 
```
Then,

```bash
dsmaster$ vi docker-compose.yml
```
This command will open an editor. Press the `Insert` button to enable editing
 and then copy paste the following into the document.
 
```text
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:
```

Then pres the `Ecs` button and enter `:wq` to save and close the editor.

Once we have the file we can deploy the test application using the following 
command. which will be executed in the `dsmaster`

```bash
dsmaster$ docker stack deploy -c docker-compose.yml getstartedlab
```

To verify the services and associated containers have been
distributed between both `dsmaster` and `dsworker`, execute the following 
command.

```bash
dsmaster$ docker stack ps getstartedlab
```

The output will look similar to 

```bash
ID                  NAME                  IMAGE               NODE                DESIRED STATE       CURRENT STATE             ERROR               PORTS
wpqtkv69qbee        getstartedlab_web.1   username/repo:tag   dsworker            Running             Preparing 4 seconds ago                       
whkiecyenuv0        getstartedlab_web.2   username/repo:tag   dsmaster            Running             Preparing 4 seconds ago                       
13obecvxohh1        getstartedlab_web.3   username/repo:tag   dsworker            Running             Preparing 5 seconds ago                       
76srj0nflagi        getstartedlab_web.4   username/repo:tag   dsworker            Running             Preparing 5 seconds ago                       
ymqoonad5c1f        getstartedlab_web.5   username/repo:tag   dsmaster            Running             Preparing 5 seconds ago  
```

