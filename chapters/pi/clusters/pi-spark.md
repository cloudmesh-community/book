# Raspberry PI Spark Cluster :o: :raised_hand: hid: 24

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real kubernetes install.
- [ ] so before you can work on the section you need to make sure the NOW section is up to date.
- [ ] The section contains some issues
- [ ] A per node setup is used instead of a scripted setup
- [ ] Some text in the later part is unclear


## Download 

Download the most recent version from the Apache website (we use here
version 2.3.0).

---

:warning: *if a newer version is available, your task will be to use the
newer version and create a new updated set of instructions. At this
time the newest version is 2.3.0. Please double check.*

---

* [[Apache Spark](https://www.apache.org/dyn/closer.lua/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz)] 

Run the command

```bash 
wget http://apache.claz.org/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz 
```

## Installation

Create the folder for storing spark install files

```bash 
$ sudo mkdir -p /opt/spark-2.3.0
$ sudo chown -R hduser:hadoop /opt/spark-2.3.0 
```

Unzip the tar fle into destination folder

```bash tar -xzf spark-2.3.0-bin-hadoop2.7.tgz -C /opt/spark-2.3.0 --strip-components=1 ```

Update the `PATH` variable

```bash 
$ echo "export SPARK_HOME=/opt/spark-2.3.0" >> ~\.bashrc
$ echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~\.bashrc
$ echo "export PATH=$PATH:$SPARK_HOME/sbin" >> ~\.bashrc
$ source ~/.bashrc 
```

Copy the template from `spark-env.sh.template` to `spark-env.sh`

```bash 
$ cp $SPARK_HOME/spark-env.sh.template $SPARK_HOME/spark-env.sh 
```

Edit spark-env.sh file to change configurations


```bash 
$ nano $SPARK_HOME/spark-env.sh 
```

Edit slaves file on master node

```bash 
$ cd $SPARK_HOME/conf
$ cp slaves.template slaves
$ nano slaves
``` 

Update the configurations

```
SPARK_MASTER_HOST = 169.254.24.132
SPARK_WORKER_MEMORY = 512m
```

---

:warning: *it is possible to write a script doing this*

---


Add the hostnames to the file

* pimaster (hostname of master node)
* pislave01 (hostname of worker slave 01)
* pislave02 (hostname of worker slave 02)

---

:warning: *it is possible to write a script doing this*

---

## Test Setup	

Run `spark-shell` from the command line. You will have succeed if you
see something like this

```bash 
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.3.0
      /_/
         
Using Scala version 2.11.8 (Java HotSpot(TM) Client VM, Java 1.8.0_65)
```

Repeat above steps on all worker/slave nodes

:warning: it is unclear which steps these are

Alternative to running above steps for each worker node, you can run
the the following command on each worked node to create spark directory

```bash 
$ sudo mkdir -p /opt/spark-2.3.0`
$ sudo chown -R hduser:hadoop /opt/spark-2.3.0
```

Run next you can copy the configuration as follows:

``` bash
$ rsync -avxP /opt/spark-2.3.0 hduser@pislave:/opt
```

Run the previous command only after creating the /opt/spark-2.3.0 on
all worker nodes

```bash 
$ sudo mkdir -p /opt/spark-2.3.0
$ sudo chown -R hduser:hadoop /opt/spark-2.3.0
```

:warning: this seems duplicated

Next you need to set the spark home and add it to your path on all
worker nodes

```bash 
$ echo "export SPARK_HOME=/opt/spark-2.3.0"
$ echo "export PATH=$PATH:$SPARK_HOME/bin"
$ source ~/.bashrc
```

Finally you need to start the spark server and workers by running the
master command on the master and the salve command on the slaves

Run this on the master:

```bash 
$SPARK_HOME/sbin/start_master.sh 
```
Run this on the slave:

```bash 
$SPARK_HOME/sbin/start_slaves.sh 
```

To test it out use the following URL:

```http://master_host_name:8080```
