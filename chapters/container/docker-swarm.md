# Docker Swarm :o:

A swarm is a group of machines that are running Docker and joined into
a cluster. Docker commands are executed on a cluster by a swarm
manager. The machines in a swarm can be physical or virtual. After
joining a swarm, they are referred to as *nodes*.

## Set up your swarm

A swarm is made up of multiple nodes, which can be either physical or
virtual machines. The basic steps are:

1. run `docker swarm init` to enable swarm mode and make your current
   machine a swarm manager,
2. then run `docker swarm join` on other machines to have them join
   the swarm as workers. Choose a tab below to see how this plays out
   in various contexts. We use VMs to quickly create a two-machine
   cluster and turn it into a swarm.

## Create a cluster with VirtualBox

To create virtual machines on your local machine, first create a
couple of VMs using docker-machine, using the VirtualBox driver:

```bash
$ docker-machine create --driver virtualbox myvm1
$ docker-machine create --driver virtualbox myvm2
```

To list the VMs and get their ip addresses.
Use this command to list the machines and get their IP addresses.

```bash
$ docker-machine ls
```

## Initialize the Swarm Manager Node and Add Worker Nodes

The first machine acts as the manager, which executes management
commands and authenticates workers to join the swarm, and the second
is a worker.

### Instruct myvm1 to become a swarm manager:

```bash
$ docker swarm init
```
output should be like this:

```bash
$ docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"
```

Swarm initialized: current node `<node ID>` is now a manager.

To add a worker to this swarm, run the following command:

```bash
$ docker swarm join--token <token> <myvm ip>:<port>
```
  
To add a manager to this swarm, run

```bash
$ docker swarm join-token manager'
```

and follow the instructions.

### To construct myvm2 as a worker node.

Copy this command, and send it to `myvm2` via docker-machine ssh to
have `myvm2` join your new swarm as a worker:

```bash
$ docker-machine ssh myvm2 "docker swarm join --token <token> <ip>:2377"
```

The output should be like this:

```bash
This node joined a swarm as a worker.
```

Run `docker-machine ls` to verify that `myvm1` is now the active
machine, as indicated by the asterisk next to it.

The output should be like this:

```bash
$ docker-machine ls
```

The output will look similar to 

```bash
NAME    ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER        ERRORS
myvm1   *        virtualbox   Running   tcp://192.168.99.100:2376           v17.06.2-ce
myvm2   -        virtualbox   Running   tcp://192.168.99.101:2376           v17.06.2-ce
```

## Deploy the application on the swarm manager

To deploy an application, run the following command to deploy on `myvm1`.

```bash
$ docker stack deploy -c docker-compose.yml getstartedlab
```

To verify the services and associated containers have been
distributed between both `myvm1` and `myvm2`.

```bash
$ docker stack ps getstartedlab
```

The output will look similar to 


ID     |       NAME        |          IMAGE       |            NODE  |  DESIRED STATE |
| --- | --- | --- | --- | --- |
| jq2g... | getstartedlab_web.1 |  john/get-started:part2 | myvm1 | Running |
| 88wg... | getstartedlab_web.2 |  john/get-started:part2 | myvm2 | Running |
| vbb1... | getstartedlab_web.3 |  john/get-started:part2 | myvm2 | Running |
| ghii... | getstartedlab_web.4 |  john/get-started:part2 | myvm1 | Running |
| 0prm... | getstartedlab_web.5 |  john/get-started:part2 | myvm2 | Running |

