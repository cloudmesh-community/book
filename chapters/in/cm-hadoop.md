Hadoop Virtual Cluster Installation
===================================

Cloudmesh Cluster Installation
------------------------------

Before you start this lesson, you MUST finish cm_install.

This lesson is created and test under the newest version of Cloudmesh
client. Update yours if not.

To manage virtual cluster on cloud, the command is `cm cluster`. Try
`cm cluster help` to see what other commands are and what options they
supported.

### Create Cluster

To create a virtual cluster on cloud, we must define an active cluster
specification with `cm cluster define` command. For example, we define a
cluster with 3 nodes:

    $ cm cluster define --count 3

All options will use the default setting if not specified during cluster

:   define. Try `cm cluster help` command to see what options
    `cm cluster define` has and means, here is part of the usage
    information: :
```
$ cm cluster help

usage: cluster create [-n NAME] [-c COUNT] [-C
CLOUD] [-u NAME] [-i IMAGE] [-f FLAVOR] [-k KEY] [-s NAME]
[-AI]

Options:
-A --no-activate Donot activate this cluster
-I --no-floating-ip Donot assign floating IPs
-n NAME --name=NAME Name of the cluster
-c COUNT --count=COUNT Number of nodes in the cluster 
-C NAME --cloud=NAME Name of the cloud 
-u NAME --username=NAME Name of the image login user 
-i NAME --image=NAME Name of the image 
-f NAME --flavor=NAME Name of the flavor 
-k NAME --key=NAME Name of the key 
-s NAME --secgroup=NAME NAME of the security group 
-o PATH --path=PATH Output to this path ...
```

Floating IP is a valuable and limited resource on cloud.

`cm cluster define` will assign floating IP to every node within the
    cluster by default. Cluster creation will fail if the floating IPs
    run out on cloud. When you run into error like this, use option `-I`
    or `--no-floating-ip` to avoid assigning floating IPs during cluster
    creation:
```
$ cm cluster define --count 3 --no-floating-ip
```

> Then manually assign floating IP to one of the nodes. Use this node as
> a logging node or head node to log in to all the other nodes.

We can have multiple specifications defined at the same time. Every time
a new cluster specification is defined, the counter of the default
cluster name will increment. Hence, the default cluster name will be
`cluster-001`, `cluster-002`, `cluster-003` and so on. Use
`cm cluster avail` to check all the available cluster specifications:

    $ cm cluster avail
      cluster-001
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : True
        cloud                         : chameleon
    > cluster-002
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : False
        cloud                         : chameleon

With `cm cluster use [NAME]`, we are able to switch between different
specifications with given cluster name:

    $ cm cluster use cluster-001
    $ cm cluster avail
    > cluster-001
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : True
        cloud                         : chameleon
      cluster-002
        count                         : 3
        image                         : CC-Ubuntu14.04
        key                           : xl41
        flavor                        : m1.small
        secgroup                      : default
        assignFloatingIP              : False
        cloud                         : chameleon

This will activate specification `cluster-001` which assigns floating IP
during creation rather than the latest one `cluster-002`.

With our cluster specification ready, we create the cluster with command
`cm cluster allocate`. This will create a virtual cluster on the cloud
with the activated specification:

    $ cm cluster allocate

Each specification can have one active cluster, which means
`cm cluster   allocate` does nothing if there is a successfully active
cluster.

### Check Created Cluster

With command `cm cluster list`, we can see the cluster with the default
name `cluster-001` we just created:

    $ cm cluster list
    cluster-001

Using `cm cluster nodes [NAME]`, we can also see the nodes of the
cluster along with their assigned floating IPs of the cluster:

    $ cm cluster nodes cluster-001
    xl41-001 129.114.33.147
    xl41-002 129.114.33.148
    xl41-003 129.114.33.149

If option `--no-floating-ip` is included during definition, you will see
nodes without floating IP:

    $ cm cluster nodes cluster-002
    xl41-004 None
    xl41-005 None
    xl41-006 None

To log in one of them, use command `cm vm assign IP [NAME]` to assign a
floating IP to one of them:

    $ cm vm ip assign xl41-006
    $ cm cluster nodes cluster-002
    xl41-004 None
    xl41-005 None
    xl41-006 129.114.33.150

Then you can log in this node as a head node of your cluster by
`cm vm ssh [NAME]`:

    $ cm vm ssh xl41-006
    cc@xl41-006 $

### Delete Cluster

Using `cm cluster delete [NAME]`, we are able to delete the cluster we
created:

    $ cm cluster delete cluster-001

Option `--all` can delete all the clusters created, so be careful:

:   :

\$ cm cluster delete --all

Then we need to undefine our cluster specification with command
`cm cluster undefine [NAME]`:

    $ cm cluster undefine cluster-001

Option `--all` can delete all the cluster specifications:

    $ cm cluster undefine --all

Hadoop Cluster Installation
---------------------------

This section is built upon the previous one. Please finish the previous
one before start this one.

### Create Hadoop Cluster

To create a Hadoop cluster, we need to first define a cluster with
`cm cluster define` command:

    $ cm cluster define --count 3

To deploy a Hadoop cluster, we only support image `CC-Ubuntu14.04`

:   on Chameleon. DO NOT use `CC-Ubuntu16.04` or any other images. You
    will need to specify it if it's not the default image:

\$ cm cluster define --count 3 --image CC-Ubuntu14.04

Then we define the Hadoop cluster upon the cluster we defined using
`cm hadoop define` command:

    $ cm hadoop define

Same as `cm cluster define`, you can define multiple specifications for
the Hadoop cluster and check them with `cm hadoop avail`:

    $ cm hadoop avail
    > stack-001
      local_path                    : /Users/tony/.cloudmesh/stacks/stack-001
      addons                        : []

We can use `cm hadoop use [NAME]` to activate the specification with the
given name:

    $ cm hadoop use stack-001

May not be available for current version of Cloudmesh Client.

Before deploy, we need to use `cm hadoop sync` to checkout / synchronize
the Big Data Stack from Github.com:

    $ cm hadoop sync

To avoid errors, make sure you are able to connect to Github.com using SSH:

:   <https://help.github.com/articles/connecting-to-github-with-ssh/>.

Finally, we are ready to deploy our Hadoop cluster:

    $ cm hadoop deploy

This process could take up to 10 minutes based on your network.

To check Hadoop is working or not. Use `cm vm ssh` to log into the
`Namenode` of the Hadoop cluster. It's usually the first node of the
cluster:

    $ cm vm ssh node-001
    cc@hostname$

Switch to user `hadoop` and check HDFS is set up or not:

    cc@hostname$ sudo su - hadoop
    hadoop@hostname$ hdfs dfs -ls /
    Found 1 items
    drwxrwx---   - hadoop hadoop,hadoopadmin          0 2017-02-15 17:26 /tmp

Now the Hadoop cluster is properly installed and configured.

### Delete Hadoop Cluster

To delete the Hadoop cluster we created, use command
`cm cluster delete [NAME]` to delete the cluster with given name:

    $ cm cluster delete cluster-001

Then undefine the Hadoop specification and the cluster specification:

    $ cm hadoop undefine stack-001
    $ cm cluster undefine cluster-001

May not be available for current version of Cloudmesh Client.

Advanced Topics with Hadoop
---------------------------

### Hadoop Virtual Cluster with Spark and/or Pig

To install Spark and/or Pig with Hadoop cluster, we first use command
`cm hadoop define` but with `ADDON` to define the cluster specification.

For example, we create a 3-node Spark cluster with Pig. To do that, all
we need is to specify `spark` as an `ADDON` during Hadoop definition:

    $ cm cluster define --count 3
    $ cm hadoop define spark pig

Using `cm hadoop addons`, we are able to check the current supported
addon:

    $ cm hadoop addons

With `cm hadoop avail`, we can see the detail of the specification for
the Hadoop cluster:

    $ cm hadoop avail
    > stack-001
      local_path                    : /Users/tony/.cloudmesh/stacks/stack-001
      addons                        : [u'spark', u'pig']

Then we use `cm hadoop sync` and `cm hadoop deploy` to deploy our Spark
cluster:

    $ cm hadoop sync
    $ cm hadoop deploy

This process will take 15 minutes or longer.

Before we proceed to the next step, there is one more thing we need to,
which is to make sure we are able to ssh from every node to others
without password. To achieve that, we need to execute
`cm cluster cross_ssh`:

    $ cm cluster cross_ssh

### Word Count Example on Spark

Now with the cluster ready, let's run a simple Spark job, Word Count, on
one of William Shakespear's work. Use `cm vm ssh` to log into the
`Namenode` of the Spark cluster. It should be the first node of the
cluster:

    $ cm vm ssh node-001
    cc@hostname$

Switch to user `hadoop` and check HDFS is set up or not:

    cc@hostname$ sudo su - hadoop
    hadoop@hostname$

Download the input file from the Internet:

    wget --no-check-certificate -O inputfile.txt \
    https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

You can also use any other text file you preferred. Create a new
directory `wordcount` within HDFS to store the input and output:

    $ hdfs dfs -mkdir /wordcount

Store the input text file into the directory:

    $ hdfs dfs -put inputfile.txt /wordcount/inputfile.txt

Save the following code as `wordcount.py` on the local file system on
Namenode:

    import sys

    from pyspark import SparkContext, SparkConf

    if __name__ == "__main__":

      # tak two arguments, input and output
      if len(sys.argv) != 3:
        print("Usage: wordcount <input> <output>")
        exit(-1)

      # create Spark context with Spark configuration
      conf = SparkConf().setAppName("Spark Count")
      sc = SparkContext(conf=conf)

      # read in text file
      text_file = sc.textFile(sys.argv[1])

      # split each line into words
      # count the occurrence of each word
      # sort the output based on word
      counts = text_file.flatMap(lambda line: line.split(" ")) \
               .map(lambda word: (word, 1)) \
               .reduceByKey(lambda a, b: a + b) \
               .sortByKey()

      # save the result in the output text file
      counts.saveAsTextFile(sys.argv[2])

Next submit the job to Yarn and run in distribute:

    $ spark-submit --master yarn --deploy-mode client --executor-memory 1g \
    --name wordcount --conf "spark.app.id=wordcount" wordcount.py \
    hdfs://192.168.0.236:8020/wordcount/inputfile.txt \
    hdfs://192.168.0.236:8020/wordcount/output

Finally, take a look at the result in the output directory:

    $ hdfs dfs -ls /wordcount/outputfile/
    Found 3 items
    -rw-r--r--   1 hadoop hadoop,hadoopadmin          0 2017-03-07 21:28 /wordcount/output/_SUCCESS
    -rw-r--r--   1 hadoop hadoop,hadoopadmin     483182 2017-03-07 21:28 /wordcount/output/part-00000
    -rw-r--r--   1 hadoop hadoop,hadoopadmin     639649 2017-03-07 21:28 /wordcount/output/part-00001
    $ hdfs dfs -cat /wordcount/output/part-00000 | less
    (u'', 517065)
    (u'"', 241)
    (u'"\'Tis', 1)
    (u'"A', 4)
    (u'"AS-IS".', 1)
    (u'"Air,"', 1)
    (u'"Alas,', 1)
    (u'"Amen"', 2)
    (u'"Amen"?', 1)
    (u'"Amen,"', 1)
    ...
