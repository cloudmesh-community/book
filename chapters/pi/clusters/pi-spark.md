# Raspberry PI Spark Cluster :o: :raised_hand: hid: fa18-516-24


We provide step-by-step instructions on installing a Spark cluster on
a cluster of Raspberry Pi's.

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real kubernetes install.
- [ ] so before you can work on the section you need to make sure the NOW section is up to date.
- [ ] The section contains some issues
- [ ] A per node setup is used instead of a scripted setup
- [ ] Some text in the later part is unclear


## Prerequisites :o:

:warning: This prerequisit is the same as for any other NOW
cluster. Thus this section needs to be moved to the NOW cluster setup
and than we refere just to this section from here.

We assume that you have on all the Raspberry Pi nodes the following
software and configuration files installed:

**SSH**:

: Configure passwordless SSH key based authentication:
  All the public keys of the nodes must be added to all the nodes'
  authorized keys files. See our SSH information in section on how to
  do this.

**Java**:


: To install Java on the PI please use the following commands

  ```bash 
  pi$ sudo add-apt-repository ppa:webupd8team/java
  pi$ sudo apt-get update
  pi$ sudo apt-get install oracle-java8-installer
  pi$ echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~\.bashrc
  pi$ source ~/.bashrc 
  ``` 

**Scala**:

: To install Scala you can use the following commands

  ```bash 
  pi$ sudo apt-get install scala
  ```

**Hostnames**:

: :warning: this can b automatically done and needs to be documented
  in the Pi NOW section. THe way we do this is set up key authentication
  foirts and than use scp or better cloudmesh to copy it. We need to describe that provess
  in more detail in the NOW section.

  IN our example we assume we use 3 hosts. The hosts will be added to
  the file `/etc/hosts`. Please use IP numbers for your network
  configuration. For us this is 

   ```bash 
	192.168.10.2		pi-master
	192.168.10.3		pi-slave0
	192.168.10.4	 	pi-slave1
   ```

## Download 

Download the most recent version of Spark from the Apache website (we use here
version 2.3.2).

---

:warning: *if a newer version is available, your task will be to use the
newer version and create a new updated set of instructions. At this
time the newest version is 2.3.2. Please double check.*

---

* [[Apache Spark Latest Download](http://spark.apache.org/downloads.html)] 

After the download is completed run the command

```bash 
pi$ wget https://www.apache.org/dyn/closer.lua/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz 
```

## Installation

Create the folder for storing spark install files

```bash 
pi$ sudo mkdir -p /opt/spark-2.3.0
```

Unzip the tar fle into destination folder

```
pi$ bash tar -xzf spark-2.3.2-bin-hadoop2.7.tgz -C /opt/spark-2.3.0 --strip-components=1
```

Update the `PATH` variable

```bash 
pi$ echo "export SPARK_HOME=/opt/spark-2.3.2" >> ~\.bashrc
pi$ echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~\.bashrc
pi# echo "export PATH=$PATH:$SPARK_HOME/sbin" >> ~\.bashrc
pi$ source ~/.bashrc 
```

Copy the template from `spark-env.sh.template` to `spark-env.sh`

```bash 
pi$ cp $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh 
```

Edit `spark-env.sh` file to change the configurations and add the
following configurations in to the `spark-env.sh` file:

```
#!/usr/bin/env bash
SPARK_WORKER_MEMORY = 512m
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export SPARK_WORKER_CORES=1
```

Now edit slaves file on master node

```bash 
cp $SPARK_HOME/conf/slaves.template $SPARK_HOME/conf/slaves
vi $SPARK_HOME/conf/slaves
``` 

And add the following content. (Change this according to the number of slaves you configure).

```
pi-slave0
pi-slave1
```

Note: The above mentioned slaves are of the same names of the
hostnames specified in the /etc/hosts file in the prerequisites
section.

## Run Spark	

Now that you've followed the installation steps completely you can
start the Spark cluster.  Since the SSH server configurations have
been done, you only need to run the following command on the master
and it will automatically start the Spark workers on the slaves we've
mentioned in the ```/etc/hosts``` file and setup the whole cluster.

Run this on the master:

```bash 
$SPARK_HOME/sbin/start-all.sh 
```

You can now view the Spark cluster information in the Spark Master UI:  

```http://master_IP:8080```

You can run the following command on the master to stop the cluster. 
```bash 
$SPARK_HOME/sbin/stop-all.sh 
```

:o: :warning: see also the file `pi-spark-orig.md` as it still contains
useful information such as the output when running pi spark

## Towards a cm4 command for pi-spar instalation

We suggest that a command be developed as part of cm4 taht installs
sparck on a number of machines. THis needs t be done in phases as not
to duplicated work

* Phase 1: add keys: here you add keys to the hosts in the network
  using python hostlists as already demonstrated in cm4

  `cm4 deploy keys --hosts HOSTNAMES [--key FILEANME]` uses the publick key 

* Phase 2: deploy spark: This deployes spark on the different hosts

  `cm4 deploy spark --hosts HOSTNAMES` 

* Phase 3: test spark: This runs a simple test to see if things work

  `cm4 test spark --hosts HOSTNAMES` 

For the implementation either ansible could be used, or simply a queue
in python executing the various commands or shell scripts.

## Refernces

See another effort documented at:

* Edge Computing and Big Data Processing using Raspberry Pi
Naveen Kaul
<http://cyberaide.org/papers/vonLaszewski-cloud-vol-9.pdf#page=104&zoom=100,0,96>
* Benchmarking Hadoop and Spark on Mutiple Platforms
<http://cyberaide.org/papers/vonLaszewski-cloud-vol-9.pdf#page=27&zoom=100,0,96>

* We have an extensive section on how to use SSH keys. However others
also pointed to this
[article](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)
It describes also how to disable the password for root.
