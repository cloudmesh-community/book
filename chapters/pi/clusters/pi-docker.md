# Docker {#sec:pi-docker}

Docker is a tool that allows us to deploy applications inside of
software containers.  A container allows a developer to package the
application along with dependencies associated with it and put all in
a box which is an isolated environment so that the underlying host
operating system is completely abstracted from the application running
inside the box.

It is a method of packaging software, to include not only our code,
but also other components such as a full file system, system tools,
services, and libraries. This can be useful for the Raspberry Pi
because it allows users to run applications without lot of steps, as
long as the application is packaged inside of a Docker image. We
simply install Docker and run the container.

According to the developers of Docker it includes the following
features:

* Portability
* Density
* Scalability
* Security


## Installation 

First we need to make sure the Raspberry Pi is up to date so we can
install a recent version of docker.  The automated script maintained
by the Docker project will create a systemd service file and copy the
relevant Docker binaries into `/usr/bin/`.


```bash
pi$ sudo apt-get update
pi$ curl -sSL https://get.docker.com | sh
```

In order for us to start the docker daemon at the next boot, we add it
as follows:
			
```bash
pi$ sudo systemctl enable docker
```
    
Now if we reboot, the Docker daemon will start. In case you like to
avoid the first reboot, you can use the command:

```bash
pi$ sudo systemctl start docker
```
      
Naturally you do not have to do this after you reboot the next time.

The Docker client can only be used by `root` or members of the
`docker` group.  Thus, let us add the user pi (or your equivalent
user) to the docker group using:

```bash
pi$ sudo usermod -aG docker pi
```
	
After executing the above command, we log out of the terminal restart
it so we are sure the user permissions are available in the shell we
use.

To test docker is installed successfully, we run the `hello-world`
docker image with the command:

```bash
pi$ docker run hello-world
```
	
If Docker is installed properly, we will see a `Hello from Docker!`
message.

## Docker Swarm

Swarm is a native clustering and scheduling tool for Docker. Instead
of just managing containers on a single server, we can manage
containers on a set of servers. The containers will be automatically
scheduled on the pool of servers making them appear as a single
resource. We will set up and use Docker on a number of Raspberry Pi's
install Docker on them and register them into a Docker Swarm.

## Creating a Network of Pi's with docker

In [Network of Pis](#pi-now-main) section we explained how to set up a network
of Pis. Here we assume that we start from such a network. The Pi's have all
different names, and are registered on the network. Each Pi has the public key
installed from the machine where you will login from for setting up the swarm.

Let us assume the names of the hosts are stored in a shell variable called 

	hostnames = (red00 red01 red02 red03 red04)

Naturally, we want to install on these machines docker and register
them to the swarm. A variety of tools exist to simplify this process,
such as

* parallel shell <https://github.com/vallard/psh>
* cloudmesh parallel (TODO: find the link)

For now we use this simple shell program to install docker on each of
the hosts in the hostnames

```bash
hostnames = (red00 red01 red02 red03 red04)
for host in "${hostnames[@]}"
do
      ssh pi@$host curl -sSL https://get.docker.com | sh
done
```

Save this script in a file called `docker-install.sh` and set the executable rights with 

	chmod u+x docker-install.sh
	   
When we execute it with 

	$ docker-install.sh
	
It will sequentially install docker on each host. This is not very
efficient and only works for a small number of hosts.


## Registering the Pi to the Swarm

Next we need to run on one of the nodes the management node for the
swarm to which all others servers register as workers. Although we
could run on this node als a worker, we will just run the manager on
it as we want to avoid overloading it and make sure it operates
smoothly.

We select the first host in our hostlist for it called `red00` Let us
assume the host has the ipaddress `<manager-ip-address>`. We can log
into this computer and execute the command

```bash
$ sudo docker swarm init --advertise-addr <manager-ip-address>:2377
```

This command will print out a token that we can use on the workers to
register with our swarm. The token will look something like:

	SWMTKN-abc...xyz

Let us use the term `<token>` to indicate the token. To register a
worker a two step process is used.

If you ever forget the token, you simply can use the following command
on the manager

	$ docker swarm join-token worker

It will print out the command that you will have to execute on a worker.

```bash
$ sudo docker swarm join --token SWMTKN-abc...manager...xyz <manager-ip-address>:2377
```

To see the list of nodes, you can use the command

```bash
I $ sudo docker node ls
```


## Docker Cheat Sheet

The following table is copied from the
[docker manual](https://github.com/docker/labs/blob/master/developer-tools/java/chapters/appa-common-commands.adoc)


.<div class="smalltable">
	
| Purpose| Command |
| ---- | ------------ |
| **Image** | |
| Build an image| docker image build --rm=true . |
| Install an image | docker image pull ${IMAGE} |
| List of installed images | docker image ls |
| List of installed images (detailed listing) | docker image ls --no-trunc |
| Remove an image | docker image rm ${IMAGE_ID} |
| Remove unused images | docker image prune |
| Remove all images | docker image rm $(docker image ls -aq) |
| **Containers** | | 
| Run a container | docker container run |
| List of running containers | docker container ls |
| List of all containers | docker container ls -a |
| Stop a container | docker container stop ${CID} |
| Stop all running containers | docker container stop $(docker container ls -q) |
| List all exited containers with status 1 | docker container ls -a --filter "exited=1" |
| Remove a container | docker container rm ${CID} |
| Remove container by a regular expression | docker container ls -a `|` grep gregor `|` awk '{print $1}' `|` xargs docker container rm -f |
| Remove all exited containers | docker container rm -f $(docker container ls -a `|` grep Exit `|` awk '{ print $1 }') |
| Remove all containers | docker container rm $(docker container ls -aq) |
| Find IP address of the container | docker container inspect --format '{{ .NetworkSettings.IPAddress }}' ${CID} |
| Attach to a container | docker container attach ${CID} |
| Open a shell in to a container | docker container exec -it ${CID} bash |
| Get container id for an image by a regular expression | docker container ls | grep gregor | awk '{print $1}' |

</div>

## Exercise

Swarm.1

: Your task is is to identify technologies to execute the Installation 
  in parallel. Suitable technologies include

  * psh
  * ansible
  * puppet
  * python threads
  * cloudmesh

  We like that the class is split up in groups and each group develops this
  solution. Naturally you can test this first with not installing docker, but
  with a simple command such as `uname -a`
  
Swarm.2

: Develop a python cloudmesh command called 

  `cms swarm config hostnames.yaml`
  
  where the yaml file looks something like  

  ```yaml
  manager: <ip00>
  worker:
  - <ip01>
  - <ip02>
  - <ip03>
  ```

  Similarly create other convenient functions such as 
  
  * `cms swarm kill`, which kills the swarm
  * `cms swarm ls`, which gives details about the swarm
