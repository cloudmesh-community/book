# Docker Hadoop Cluster 

This section is based on the hadoop release 3.0.3 which
includes significant enhancements over the previous version of Hadoop
2.x. Changes include the use of the following software:

* CentOS 7
* systemctl
* Java SE Development Kit 8

A Dockerfile to creat the haddop deployment is available at 

*<https://github.com/cloudmesh-community/book/blob/master/examples/docker/hadoop/3.0.3/Dockerfile>

## Building Hadoop using Docker

You can build hadoop from the Dockerfile as follows:

```bash
$ mkdir cloudmesh-community
$ cd cloudmesh-community
$ git clone https://github.com/cloudmesh-community/book.git
$ cd book/examples/docker/hadoop/3.0.3
$ docker build -t cloudmesh/hadoop:3.0.3 .
```
    
The complete docker image for Hadoop consumes 1.5GB.

```bash
$ docker images
```

```bash
REPOSITORY       TAG   IMAGE ID     CREATED    SIZE
cloudmesh/hadoop 3.0.3 ba2c51f94348 1 hour ago 1.52GB
```

## Start a Hadoop Container with Interactive Shell

```bash
$ docker run -it cloudmesh/hadoop:3.0.3 /etc/bootstrap.sh -bash
```

The details of the new version is available from the official site here:

* <http://hadoop.apache.org/docs/r3.0.3/index.html>


## Hadoop Configuration Files 

The configuration files are included in the `conf` folder

## Virtual Memory Limit

IN case you need more memory, you can increase it by cahnging the
parameters in the file `mapred-site.xml`, for example:

- mapreduce.map.memory.mba to 4096
- mapreduce.reduce.memory.mb to 8192

## hdfs Safemode leave command

:o: it is unclear what this is

```bash
$ hdfs dfsadmin -safemode leave`
```


## Examples

The statistics and PageRank examples are included in the examples
directory at

* <https://github.com/cloudmesh-community/book/tree/master/examples/docker/hadoop/3.0.3/examples>

It includes a simple statistics program and a pagerank example.

:o: a more detailed explanation of the examples should be here or we
need tp point to another section in the handbook.
