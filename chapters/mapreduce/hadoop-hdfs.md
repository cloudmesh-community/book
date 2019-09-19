# Hadoop Distributed File System (Hadoop HDFS)

## Introduction

The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware (@www-hadoop-hdfs-design). It has many similarities with existing distributed file systems. HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware. HDFS provides high throughput access to application data and is suitable for applications that have large data sets. HDFS relaxes a few POSIX requirements to enable streaming access to file system data. The project URL is https://hadoop.apache.org/hdfs/.

## Features

* Detect Hardware Failure
Hardware failure is the norm rather than the exception. An HDFS instance may consist of hundreds or thousands of server machines, each storing part of the file system’s data. Detection of faults and quick, automatic recovery from them is a core architectural goal of HDFS.

* Support Streaming Data Access
Applications that run on HDFS need streaming access to their data sets. They are not general purpose applications that typically run on general purpose file systems. HDFS is designed more for batch processing rather than interactive use by users.

* Support Large Data Sets
Applications that run on HDFS have large data sets. A typical file in HDFS is gigabytes to terabytes in size. Thus, HDFS is tuned to support large files. It should provide high aggregate data bandwidth and scale to hundreds of nodes in a single cluster. It should support tens of millions of files in a single instance.

## HDFS Components

![Hadoop HDFS [@www-hadoop-hdfs-design]](images/hdfsarchitecture.gif){#fig:hadoop_hdfs_arch}

### NameNode and DataNodes

HDFS has a master/slave architecture. An HDFS cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients (see @fig:hadoop_hdfs_arch). In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on. HDFS exposes a file system namespace and allows user data to be stored in files. 

Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes. The NameNode executes file system namespace operations like opening, closing, and renaming files and directories. It also determines the mapping of blocks to DataNodes. The DataNodes are responsible for serving read and write requests from the file system’s clients. The DataNodes also perform block creation, deletion, and replication upon instruction from the NameNode.

The NameNode and DataNode are pieces of software designed to run on commodity machines. A typical deployment has a dedicated machine that runs only the NameNode software. Each of the other machines in the cluster runs one instance of the DataNode software. The architecture does not preclude running multiple DataNodes on the same machine but in a real deployment that is rarely the case.

The existence of a single NameNode in a cluster greatly simplifies the architecture of the system. The NameNode is the arbitrator and repository for all HDFS metadata.


## Usage

### Java Client API

HDFS can be accessed from applications in many different ways. Natively, HDFS provides a Java API for applications to use. A C language wrapper for this Java API is also available. In addition, an HTTP browser can also be used to browse the files of an HDFS instance. Work is in progress to expose HDFS through the WebDAV protocol.

Here is an example of Java code to read and write files on HDFS:

```java
// ====== Init HDFS File System Object
Configuration conf = new Configuration();
// Set FileSystem URI
conf.set("fs.defaultFS", hdfsuri);
// Because of Maven
conf.set("fs.hdfs.impl", org.apache.hadoop.hdfs.DistributedFileSystem.class.getName());
conf.set("fs.file.impl", org.apache.hadoop.fs.LocalFileSystem.class.getName());
// Set HADOOP user
System.setProperty("HADOOP_USER_NAME", "hdfs");
System.setProperty("hadoop.home.dir", "/");
//Get the filesystem - HDFS
FileSystem fs = FileSystem.get(URI.create(hdfsuri), conf);
```

```java
//==== Read file
logger.info("Read file from hdfs");
//Create a path
Path hdfsreadpath = new Path(newFolderPath + "/" + fileName);
//Init input stream
FSDataInputStream inputStream = fs.open(hdfsreadpath);
//Classical input stream usage
String out= IOUtils.toString(inputStream, "UTF-8");
logger.info(out);
inputStream.close();
fs.close();
```

```java
//==== Write file
logger.info("Begin Write file into hdfs");
//Create a path
Path hdfswritepath = new Path(newFolderPath + "/" + fileName);
//Init output stream
FSDataOutputStream outputStream=fs.create(hdfswritepath);
//Cassical output stream usage
outputStream.writeBytes(fileContent);
outputStream.close();
logger.info("End Write file into hdfs");
```

### FS Shell

HDFS allows user data to be organized in the form of files and directories. It provides a commandline interface called FS shell that lets a user interact with the data in HDFS. The syntax of this command set is similar to other shells (e.g. bash, csh) that users are already familiar with. Here are some sample action/command pairs:

```bash
bin/hadoop dfs -mkdir /foodir

bin/hadoop dfs -rmr /foodir

bin/hadoop dfs -cat /foodir/myfile.txt
```

## References

* HDFS Java API: https://hadoop.apache.org/core/docs/current/api/
* HDFS source code: https://hadoop.apache.org/hdfs/version_control.html