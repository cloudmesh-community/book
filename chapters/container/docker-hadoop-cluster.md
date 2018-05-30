# Draft:Multinode Hadoop Cluster Deployment with Docker Swarm

## Docker Hadoop 3.0.1

This Dockerfile builds Hadoop Docker container with CentOS base image and
contains examples to run Hadoop such as statistics like WordCount and PageRank.

### Build

`docker build -t cloudmesh/hadoop:3.0.1 .`

### Run

`docker run -it cloudmesh/hadoop:3.0.1 /etc/bootstrap.sh -bash`

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

`hdfs dfsadmin -safemode leave`
