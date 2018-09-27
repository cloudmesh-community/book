# Multinode Hadoop Cluster Deployment with Docker Swarm :o:

<!--- 

Disclaimer: If you reached this file via github, it is ok to make a pull request 
for this file to correct it. However, viewing this file is only done properly 
in the ePub. Thus we recommend that you go to 

https://github.com/cloudmesh-community/book/blob/master/README.md

and download the appropriate ePub
--->

:o: TODO the text is incomplete and may duplicate another section?

## Docker Hadoop 3.0.1

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
