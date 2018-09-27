# Apache Hadoop Latest (3.0.1) using Docker :o:

<!--- 

Disclaimer: If you reached this file via github, it is ok to make a pull request 
for this file to correct it. However, viewing this file is only done properly 
in the ePub. Thus we recommend that you go to 

https://github.com/cloudmesh-community/book/blob/master/README.md

and download the appropriate ePub
--->

Apache Hadoop 3.0.1 is the latest release (25 March, 2018) which
includes significant enhancements over the previous version of Hadoop
2.x.

This section provides a separated Dockerfile to build hadoop 3.0.1 but
the configurations and examples are same except a few minor changes
which are:

* CentOS 7
* systemctl
* Java SE Development Kit 8

## Draft: Building Hadoop 3.0.1 using Docker

Build a docker image by Dockerfile from:

```bash
$ mkdir hadoop3.0.1
$ cd hadoop3.0.1
$ wget https://raw.githubusercontent.com/cloudmesh/book/master/examples/docker/hadoop/3.0.1/Dockerfile
$ docker build -t cloudmesh/hadoop:3.0.1 .
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
