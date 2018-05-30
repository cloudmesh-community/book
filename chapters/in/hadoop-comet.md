Hadoop SDSC
===========

 

Overview
--------

Users can run Hadoop on Gordon using the myHadoop infrastucture, which
integrates configuration and Hadoop cluster setup within Gordon's normal
job-scheduling environment. The Hadoop File System (HDFS) is built using
the high-performance flash drives (SSDs) mounted on each compute node
via iSER. Internode communication is implemented using the IPoIB
protocol.

Location
--------

The Hadoop distribution on Gordon is located in /opt/hadoop and usage
examples are found in /opt/hadoop/contrib/myHadoop. The examples
include:

\* Simple - a simple setup and usage example \* TestDFS - Depth-first
search (DFS) benchmark \* TeraSort - sorting benchmark

Configuration and Runtime Details
---------------------------------

The example scripts have a large number of parameters, configuration
settings, and environment variables. Several of these are described in
detail below, with user-modified content displayed in bold. Do not alter
the order of content in the scripts because many of the steps depend on
earlier definitions.

- Setting the number of nodes in the Hadoop cluster.

The following lines set the number of nodes (two nodes are used in this
example). Note that the node count must be set consistently in the PBS
and configure lines and that ppn should always be used.

    #PBS -l nodes=2:ppn=1

    $MY_HADOOP_HOME/bin/configure.sh -n 2 -c $HADOOP_CONF_DIR

- Setting primary environment variables:

    export MY_HADOOP_HOME="/opt/hadoop/contrib/myHadoop"
    export HADOOP_HOME="/opt/hadoop"
    export HADOOP_CONF_DIR="/home/$USER/config"

The only variable that is user specific is the HADOOP\_CONF\_DIR. This
is where the configuration files for the Hadoop cluster will be copied.
Make sure this is a location readable by all the nodes in the cluster
(i.e. a global location).

You can also set a wall clock limit, email notification, and account to
charge:

    #PBS -l walltime=1:00:00
    #PBS -M EMAILADDRESS
    #PBS -m abe
    #PBS -A ACCOUNT

- Using the high-performance interconnect

To ensure that the IPoIB (IP over InfiniBand) interface is used for the
network, the following lines should be added to the script:

    sed 's/$/.ibnet0/' $PBS\_NODEFILE > $PBS_O_WORKDIR/hadoophosts.txt
    export PBS_NODEFILEZ=$PBS_O_WORKDIR/hadoophosts.txt

This adds the ibnet0 interface to the node list. The myHadoop
configuration script looks for the list in the file pointed to by
PBS\_NODEFILEZ. Without these lines, Hadoop would use the much slower
1GbE management network.

- Setting up the myHadoop configuration files

The configuration files are set up by the following command. Make sure
(1), (2), and (3) are in the script before this step.

    $MY_HADOOP_HOME/bin/configure.sh -n 2 -c $HADOOP_CONF_DIR

- Using local SSD storage for HDFS

This step must follow (4):

    sed -i 's@HADDTEMP@'$PBS_JOBID'@g' $HADOOP_CONF_DIR/hadoop-env.sh
    $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR namenode -format

At this point all the basic Hadoop configuration steps are complete. The
cluster can now be started and used for Hadoop. For example, to start
the Hadoop cluster:

    $HADOOP_HOME/bin/start-all.sh

Copy a file to a directory created in HDFS from a filesystem:

    $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -mkdir Test
    $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -copyFromLocal ~/.bashrc Test

Once the jobs are complete the Hadoop cluster can be stopped as follows:

    $HADOOP_HOME/bin/stop-all.sh

Keep in mind that the SSD drives are cleaned up once the job is
complete. Hence, any data needed long term must be copied off the HDFS
directories.
