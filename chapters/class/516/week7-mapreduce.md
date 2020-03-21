# Week 7: MapReduce :o2:

## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/e516/) [@las19e516]:
* [Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]:

Please read the **Hadoop** sections in [Cloud Computing](https://laszewski.github.io/book/cloud/)[@las19cloudcomputing]


Watch these online videos for Hadoop MapReduce:

* [![Video](images/video.png) Map Reduce, Hadoop, and Spark (19:02) Hadoop A](https://youtu.be/HfuP2RJnQ6k?t=73)
* [![Video](images/video.png) Hadoop 13:19 Hadoop  B](https://youtu.be/-N5PpD2sy3Q?t=17)
* [![Video](images/video.png) Hadoop 12:57 Hadoop  C](https://youtu.be/BaRHay32I80?t=18)
* [![Video](images/video.png) Hadoop 15:14 Hadoop  D](https://youtu.be/MYOosbF6-dA?t=20)


**Note: All Map Reduce/Hadoop Lab activities are optional**

## Lab Activity: Hadoop Installation

The following exercises will guide you to install Hadoop on a single
node and then run a MapReduce job in Python. Please figure out the
required command lines. These commands are available in the book
sections: [Cloud Computing, Gregor von Laszewski, Ed.
2019](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]

### Exercises:

* Install prerequisite software
    * Install Java
    * Install SSH
    * Install Maven
* Configure programming environments
    * `JAVA_HOME`
    * `core-site.xml`
    * `hdfs-site.xml`
    * SSh localhost without a passphrase
* Start Hadoop HDFS
    * Format HDFS filesystem
    * Start NameNode and DataNode via command lines
    * Check NameNode status via Web Interface: NameNode - http://localhost:9870/
* Start Hadoop YARN
    * Configure
        * `mapred-site.xml`
        * `yarn-site.xml`
    * Start YARN via command line
    * Check YARN status via Web Interface: ResourceManager - http://localhost:8088/
    
After finishing all these steps, you are good to move forward to MapReduce programming.

## Lab Activity: Python MapReduce

See in the [map Section of the Python book](https://cloudmesh-community.github.io/book/vonLaszewski-python.epub):


The basic syntax of the map function expects a function
object and any number of iterables like a list or dictionary. It executes
the function object for each element in the sequence and returns a list
of the elements modified by the function object. 

```
def multiply(x):
   return x * 2

map(multiply2, [2, 4, 6, 8]

# Output [4, 8, 12, 16]
```


## Lab Activity Map/Reduce on the Cloud

### Python Word Count in MapReduce

```python
#!/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
words = line.split()
for word in words:
    print('%s\t%s' % (word, 1))
```

This code is used as Mapper.

```python
#!/usr/bin/env python

from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
if current_word == word:
    current_count += count
else:
    if current_word:
        print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
    if current_word == word:
        print('%s\t%s' % (current_word, current_count))
```

This code is used as Reducer.

**Please note these code snippets are used to demonstrate the idea of Mapper and Reducer in Python. It leaves some bugs by
 intentions. Please debug the above code or write your own version of MapReduce.**
 
### Run Hadoop MapReduce in Python

```bash
bin/hadoop jar <path_to_hadoop_libs>/hadoop-*streaming*.jar \
-file /<path_to_mapper>/mapper.py \
-mapper /<path_to_mapper>/mapper.py \
-file /<path_to_reducer>/reducer.py  \
-reducer /<path_to_reducer>/reducer.py  \
-input <input_file_path> \
-output <output_file_path>
``` 

## Lab Activity: MapReduce on the cloud

### Hadoop Cluster Setup

Hadoop’s Java configuration is driven by two types of important configuration files:

* Read-only default configuration - core-default.xml, 
  hdfs-default.xml, yarn-default.xml and mapred-default.xml.
* Site-specific configuration - etc/hadoop/core-site.xml, 
  etc/hadoop/hdfs-site.xml, etc/hadoop/yarn-site.xml and 
  etc/hadoop/mapred-site.xml.

Additionally, you can control the Hadoop scripts found in the bin/
directory of the distribution, by setting site-specific values via the
etc/hadoop/hadoop-env.sh and etc/hadoop/yarn-env.sh.

To configure the Hadoop cluster you will need to configure the
environment in which the Hadoop daemons execute as well as the
configuration parameters for the Hadoop daemons.

HDFS daemons are NameNode, SecondaryNameNode, and DataNode. YARN daemons
are ResourceManager, NodeManager, and WebAppProxy. If MapReduce is to be
used, then the MapReduce Job History Server will also be running. For
large installations, these are generally running on separate hosts.

### Configuration

Configure all Hadoop daemons:

* NameNode: HDFS_NAMENODE_OPTS
* DataNode:	HDFS_DATANODE_OPTS
* Secondary NameNode: HDFS_SECONDARYNAMENODE_OPTS
* ResourceManager: YARN_RESOURCEMANAGER_OPTS
* NodeManager: YARN_NODEMANAGER_OPTS
* WebAppProxy: YARN_PROXYSERVER_OPTS
* Map Reduce Job History Server: MAPRED_HISTORYSERVER_OPTS

Configure Namenode to use parallelGC and a 4GB Java Heap, the following
statement should be added in hadoop-env.sh:

```bash
export HDFS_NAMENODE_OPTS="-XX:+UseParallelGC -Xmx4g"
```

### Operating the Hadoop Cluster

To start a Hadoop cluster you will need to start both the HDFS and YARN
cluster. The first time you bring up HDFS, it must be formatted. Format
a new distributed filesystem as hdfs.

* Format NameNode (on a dedicate node in the cluster)
* Start NameNode (on a dedicate node in the cluster)
* Start DataNode (on each node of the cluster)
* Start ResourceManager (on a dedicate node in the cluster)
* Start NodeManager (on each node of the cluster)

### Run Hadoop MapReduce in Python

```bash
$ bin/hadoop jar <path_to_hadoop_libs>/hadoop-*streaming*.jar \
    -file /<path_to_mapper>/mapper.py \
    -mapper /<path_to_mapper>/mapper.py \
    -file /<path_to_reducer>/reducer.py  \
    -reducer /<path_to_reducer>/reducer.py  \
    -input <input_file_path> \
    -output <output_file_path>
``` 
