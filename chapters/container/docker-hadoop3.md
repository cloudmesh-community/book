# Hadoop 3.0.3

:o: THis section needs to be updated to 3.0.3

This section is based on the hadoop release 3.0.3 which
includes significant enhancements over the previous version of Hadoop
2.x.

This section provides a separated Dockerfile to build hadoop 3.0.1 but
the configurations and examples are same except a few minor changes
which are:

* CentOS 7
* systemctl
* Java SE Development Kit 8

## Building Hadoop 3.0.3 using Docker

Build a docker image by Dockerfile from:

:o: 3.0.3 does not exist yet

```bash
$ mkdir hadoop3.0.3
$ cd hadoop3.0.3
$ wget https://raw.githubusercontent.com/cloudmesh/book/master/examples/docker/hadoop/3.0.3/Dockerfile
$ docker build -t cloudmesh/hadoop:3.0.3 .
```
    
The complete docker image for Hadoop 3.0.1 consumes the storage size of
1.5GB.

```bash
$ docker images
```

```bash
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
cloudmesh/hadoop                3.0.1               ba2c51f94348        20 hours ago        1.5GB
```

## Start a Hadoop Container with Interactive Shell

```bash
$ docker run -it cloudmesh/hadoop:3.0.1 /etc/bootstrap.sh -bash
$ %docker run -it lee212/e222 /etc/bootstrap.sh -bash
```

The details of the new version is available from the official site here:
http://hadoop.apache.org/docs/r3.0.1/index.html

## Examples

The statistics and PageRank examples are identical to the Section
[Hadoop 2.7.5 on Docker]({#s-hadoop-docker-2})



## DUPLICATION

This Dockerfile builds Hadoop Docker container with CentOS base image and
contains examples to run Hadoop such as statistics like WordCount and PageRank.

### Build

```bash
$`docker build -t cloudmesh/hadoop:3.0.1 .`
```

### Run

```bash
`docker run -it cloudmesh/hadoop:3.0.1 /etc/bootstrap.sh -bash`
```

### PageRank Example

Find instruction and source code to run in the following directory:

`/cloudmesh/pagerank`

### Hadoop Configuration Files

The configuration files are shared with Hadoop 2.7.5.

### Virtual Memory Limit

Increase memory limit in the mapred-site.xml, for example:

- mapreduce.map.memory.mba to 4096
- mapreduce.reduce.memory.mb to 8192

### hdfs Safemode leave command

```bash
$ hdfs dfsadmin -safemode leave`
```

