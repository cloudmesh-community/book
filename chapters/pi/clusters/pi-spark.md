# Raspberry PI Spark Cluster :o: :raised_hand: hid: 24

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real kubernetes install.
- [ ] so before you can work on the section you need to make sure the NOW section is up to date.
- [ ] The section contains some issues
- [ ] A per node setup is used instead of a scripted setup
- [ ] Some text in the later part is unclear

We provide step-by-step instructions on installing a Spark cluster on a cluster of raspberry pis. 

## Prerequisites
On all the raspberry pi nodes, make sure these prerequisites are completed.

1. Configure passwordless SSH key based authentication:  
   All the public keys of the nodes must be added to all the nodes' authorized keys files. 
   You can refer to this [article](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) by DigitalOcean.com for more information on setting up ssh keys. 

2. Install Oracle JDK8 and set the JAVA_HOME.     
   ```bash 
   sudo add-apt-repository ppa:webupd8team/java
   sudo apt-get update
   sudo apt-get install oracle-java8-installer
	echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~\.bashrc
	source ~/.bashrc 
``` 

3. Install Scala.  
   You can install Scala using 
   ```bash 
	sudo apt-get install scala 
   ```

3. Add all the hosts in to the /etc/hosts file.  
   An example /etc/hosts file is shown below. 
   ```bash 
	192.168.10.2		pi-master
	192.168.10.3		pi-slave0
	192.168.10.4	 	pi-slave1
   ```

## Download 

Download the most recent version from the Apache website (we use here
version 2.3.2).

---

:warning: *if a newer version is available, your task will be to use the
newer version and create a new updated set of instructions. At this
time the newest version is 2.3.2. Please double check.*

---

* [[Apache Spark Latest Download](http://spark.apache.org/downloads.html)] 

Run the command

```bash 
wget https://www.apache.org/dyn/closer.lua/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz 
```

## Installation

Create the folder for storing spark install files

```bash 
sudo mkdir -p /opt/spark-2.3.0
```

Unzip the tar fle into destination folder

```bash tar -xzf spark-2.3.2-bin-hadoop2.7.tgz -C /opt/spark-2.3.0 --strip-components=1 ```

Update the `PATH` variable

```bash 
echo "export SPARK_HOME=/opt/spark-2.3.2" >> ~\.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~\.bashrc
echo "export PATH=$PATH:$SPARK_HOME/sbin" >> ~\.bashrc
source ~/.bashrc 
```

Copy the template from `spark-env.sh.template` to `spark-env.sh`

```bash 
cp $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh 
```

Edit spark-env.sh file to change configurations


```bash 
vi $SPARK_HOME/conf/spark-env.sh 
```

Add the following configurations in to the spark-env.sh file.  

```
#!/usr/bin/env bash
SPARK_WORKER_MEMORY = 512m
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export SPARK_WORKER_CORES=1
```

Edit slaves file on master node

```bash 
cp $SPARK_HOME/conf/slaves.template $SPARK_HOME/conf/slaves
vi $SPARK_HOME/conf/slaves
``` 

And add the following content. (Change this according to the number of slaves you configure).

```
pi-slave0
pi-slave1
```

Note: The above mentioned slaves are of the same names of the hostnames specified in the /etc/hosts file in the prerequisites section. 

## Run Spark	

Now that you've followed the installation steps completely you can start the Spark cluster. 
Since the SSH server configurations have been done, you only need to run the following command on the master and it will automatically start the Spark workers on the slaves we've mentioned in the ```/etc/hosts``` file and setup the whole cluster. 

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
