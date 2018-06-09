## Docker Swarm
manager
Swarm is a native clustering and scheduling tool for Docker. Instead of just managing containers on a single server, we can manage containers on a set of servers. The containers will be automatically scheduled on the pool of servers making them apear as a single resource. We will set up and use Docker on a number of Raspberry Pi's install Docker on them and register them into a Docker Swarm.

## Creating a Network of Pi's with docker

In Section ??? we explained how to set up a network of PI's. Here we assume that we start from such a network. The Pi's have all different names, and are registered on the network. Each Pi has the public key installled from the machine where you will login from for setting up the swarm.

Let us assume the names of the hosts are stored in a shell variable called 

	hostnames = (red00 red01 red02 red03 red04)

Natuarlly, we want to install on these machines docker and register them to the swarm. A variety of tools exist to simplify this process, such as 

* parallel shell <https://github.com/vallard/psh>
* cloudmesh parallel (TODO: find the link)

For now we use this simple shell program to install docker on each of the hosts in the hostnames

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
	
It will sequentially install docker on each host. This is not very efficient and only works for a small number of hosts.


## Registering the Pi to the Swarm

Next we need to run on one of the nodes the management node for the swarm to whcih all others servers register as workers. Although we could run on this node als a worker, we will just run the manager on it as we want to avoid overloading it and make sure it operates smoothly.

We select the first host in our hostlist for it called `red00` Let us assume the host has the ipaddress `<manager-ip-address>`. We can log into this computer and execute the command

```bash
$ sudo docker swarm init --advertise-addr <manager-ip-address>:2377
```
This command will print out a token that we can use on the workers to register with our swarm. The tocken will look something like:

	SWMTKN-abc...xyz

Let us use the term <token> to indicate the token. To register a worker a two step process is used. 

If you ever forget the token, you simply can use the following command on the manager

	$ docker swarm join-token worker

It will print out the command that you will have to execute on a worker.

```bash
$ sudo docker swarm join --token SWMTKN-abc...manager...xyz <manager-ip-address>:2377
```

To see the list of nodes, you can use the command

```bash
I $ sudo docker node ls
```


## Exercise

Swarm.1

: Your task is is to identify technologies to execute the instalation 
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
  
  where the yaml file loosk something like  

  ```yaml
  manager: <IP>
  worker:
  - <ip01>
  - <ip02>
  - <ip03>
  ```

  Similarly create other convenient functions such as 
  
  * `cms swarm kill`, which kills the swarm
  * `cms swarm ls`, which gives details about the swarm
