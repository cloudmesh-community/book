# Spark

---

![](images/learning.png) **Learning Objectives**

* Learn about Apache Spark
* Learn perform data analysis using a Spark cluster and Python.

---

## What is Spark?

The Apache Software Foundation [@www-apachespark] describes Spark as:
>a unified analytics engine for large-scale data processing.


It's main goal is to help alleviate one of the most critical problems that face most data scientists in the era of 'big
data', which is that using lots of data requires one to be able to manage the data lifecycle at scale. With gigabytes,
or even terabytes, of new arriving on a daily basis, the capabilities of a single computer are quickly outstripped or
would taken an incredibly long time to process.

To alleviate this issue, Spark was developed first as a research project and then open-sourced into a standalone project
in 2010 and later adopted by the Apache Software Foundation in 2013. Since then, Spark has become one of the leading
technologies for processing data at scale utilizing commodity hardware. At its core, Spark aims to accomplish three
things [@www-apachesparkhistory]:

1. Allow for the processing and analysis of large quantities of data quickly
in a distributed manner.
2. Provide fault tolerance in the event of a node's failure.
3. Utilize hetergenous, potentially virtual, servers and computers.

By not tying itself to any one piece of hardware or requiring 100% uptime to process data successfully, Spark provides
the user with the flexibility of using as much or as little computing resources that's neccesary to accomplish a task,
allows for off-the-shelf components to be used in developing the cluster to reduce costs, and provides users with a
familiar dataset based approach to interacting with data, but at a much larger scale.

## The Building Pieces of a Spark Cluster

At a high level, all of this is accomplished via a cluster setup that can be broken down into three pieces
[@www-sparkarch]:

1. A **Driver** that tells the cluster what to do.
2. A **Cluster Manager** that processes the request and distributes it to workers.
3. **Workers** that process tasks as they are received.

The fundamental building block of a Spark cluster is the worker. As the name suggests, these workers perform the tasks
requested of the cluster whether it be reading in data, manipulating data, and reporting results back to the user.
Typically, a worker will have one executor per logical core available to the operating system. For example, a processor
with 8 physical cores and 16 logical cores would be considered 1 worker and have 16 executor threads in order to best
utilize the resources available to it. Each worker will connect to a Cluster Manager and inform it of its current status
and will then wait to be assigned work. When work arrives, the worker will execute the instructions given to it and then
report the result (success, failure, etc.) back to the cluster manager before returning to an idle state.

The cluster manager oversees the work being done by workers/executors and tasks requested by users. Its job is to
distribute work (not necessarily the data) to workers, monitor their status, restart tasks that were given to failed
workers, and to return the status of the job to the driver. The cluster manager does not contain copies of the data
itself, but, rather, manages which workers and executors are responsible for which pieces of the data. Apache Spark is
agnostic in terms of what platform the cluster manager is running on and supports the native manager bundled with Spark,
Apache Mesos, or Kubernetes [@www-sparkoverview].

The driver is the final piece of the Spark puzzle. When using a Spark cluster, the driver is typically the user's
computer that is running the program interacting with the cluster. Its job is to issue commands, receive the results,
and return them to the user. The driver is responsible for managing the SparkContext and managing the communication
between the host program and the remote cluster [@www-sparkoverview].

## How Spark Manages Data

Spark stores data in Resilient Distributed Datasets (RDDs). As the name suggests, they are resilient against failure and
distributed in nature. The resilience comes from how Spark manages the data internally and the distributed nature comes
from how the data is split amongst various workers.

### Resiliency

One of the key issues with any cluster is how to manage the failure of a worker node. If the data only exists on the
failed node and there is no other available copy of the data, then the entire job fails, which is not an ideal situation
when calculations may take a long period of time to perform from start to finish. Spark alleviates this via two methods
[www-sparkrdd]:

1. The provenance of each all data is tracked using a Directed Acyclic Graph.
2. Once an RDD is created, it is immutable and any changes made to it result in a new RDD, not a modified one.

The first method utilizes a mathematical construct: a directed acyclic graph (DAG). Breaking it down, the graph is
directed - step A can lead to step B but step B cannot lead back to step A - and acyclic - the steps in the graph do not
contain any loops. When a task is running, Spark keeps track of this DAG and can reconstruct data from a failed node by
simply repeating the steps on the DAG that lead up to the failed point and then continuing on from there. The second
method leads from the first: in order to avoid long recalculation chains, RDDs are immutable and cannot be changed.
Rather, new copies of the RDD are created when actions are performed.

Finally, with the above two methods in mind, it's important to note one tradeoff Spark made when it came to performance
and how it relates to the immutability of RDDs. One of the common complaints about Hadoop and MapReduce was that it
wrote the entire dataset out to disk after each step in the graph, which made things slow but allowed for large datasets
to be active as they mostly existed on disk where space is measured in terabytes. Spark, instead, keeps RDDs resident in
memory, which makes is much quicker. The tradeoff, then, is increased speed at the cost of more expensive storage (RAM
instead of hard disk) [www-sparkrdd].

### Distributed

As mentioned above, RDDs are distributed in nature. When reading data, for example, each worker is given a part of the
file to read and process. Assuming no network congestion, that means a Spark cluster can read data almost linearly
faster than a single computer. The distributed nature of the dataset does come at a cost: merging datasets or any action
that causes the data to need to look up values in other records (e.g. a SQL join) may require a significant number of
observations/records to be shuffled across the network. One of the key optimizations in Spark is reducing actions that
cause unnecessary shuffles or providing hints to Spark to keep observations/records logically organized.

To take a real life example, imagine that a Spark cluster contains customer purchase data that has been distributed
amongst all of the workers such that a customer's data is equally split across the entire cluster. If the cluster is
asked how much the customer has spent, that question can be answered without shuffling any data: each worker will sum
up the amount it has for that customer and report it to the cluster manager. The manager will them sum the sums from the
workers to arrive at the total. However, if we want to know the distinct list of items the customer has ordered, then
shuffling the data is  required as the list may not fit inside of the cluster manager's memory - so the workers have to
tell each of the other workers the distinct list it has and then collapse the list down before returning it to the
cluster manager as a new RDD. It's important to keep track of commands that may cause a shuffle. A more exhaustive
discussion can be found in the documentation [@www-apacheshuffle].

## Installing Spark

The underlying core technology behind Spark is Java. Any system that can run Java can run Spark if the user follows the
correct steps. Linux and Mac OS X have fairly direct install paths while Windows is slightly more involved. No matter
the platform, however, Spark requires three pieces: Java, Scala, and Spark itself. Many guides are available online and
a quick synopsis of each is presented below.

### Ubuntu

An article by Jose Portilla discusses how to install Spark on Ubuntu. [@www-sparkubuntu]  Ubuntu comes pre-installed
with Java and can be checked with `java -version` in a terminal. If it is not installed, which may be the case if you
did a minimal install in a virtual machine, you can install Java easily by running:

```bash
$ sudo apt-get update
$ sudo apt-get install default-jdk
```

Once Java has been successfully installed, Scala can be installed on top of it:

```bash
$ sudo apt-get install scala
```

Scala's install can be verified simply by entering a Scala prompt via `scala`. To quit, use `:q`. Last, Spark can be
installed by downloading the latest version from https://spark.apache.org/downloads.html. It's easiest to use a
pre-built version with Hadoop included. Once the TGZ compressed file is downloaded, extract it with `tar xvf
spark-VERSION-bin-hadoopVERSION.tgz`. After the folder is extracted, you can `cd` into it, navigate into the bin
directory and run Spark via `./spark-shell`. If all has gone well, a Spark prompt should appear.

### Mac OS X

Another tutorial [@www-sparkosx] shows how to install Spark on a platform running OS X, which is best done via homebrew.
To install homebrew, open a terminal and enter:

```bash
$ /usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
```

You may be prompted for your administrator password.  Once homebrew has been installed, the rest of the installation
follows along similarly to the Ubuntu install in the previous section with the only addition being the installation of
xcode-select:

```bash
$ xcode-select –install
$ brew cask install java
$ brew install scala
$ brew install apache-spark
```

Once the installation of xcode-select, java, scala, and apache-spark is done, then you should be able to open a Spark
shell via `spark-shell`.

### Windows

The installation for Windows operating systems is a bit more involved in comparison to Ubuntu and OS X. While the
software is almost the same (Scala isn't required), there are additional path variables that need to be created in order
for all of the pieces to be able to find each other. A helpful article by Michael Galarnyk [@www-sparkwindows] best
describes how to get Spark up-and-running on Windows. As with the two prior systems, installation begins with installing
[Java](https://www.java.com/en/) by downloading it and running the Windows installer. Next, download the latest
pre-built version of [Apache Spark](http://spark.apache.org/downloads.html) and extract the TGZ and TAR files to some
place convenient (e.g. C:\Spark\). Finally, download WinUtils from
[GitHub](https://github.com/steveloughran/winutils/blob/master/hadoop-2.6.0/bin/winutils.exe?raw=true). This utility
program offers pre-built Hadoop binaries that are required for Spark to launch. Place this program into your Spark
folder's \bin\ directory.

Finally, once all of the pieces are installed, environment variables must be set up so that each of the pieces can
find each other and Spark can be launched. To add these variables, open the Windows menu and type 'Environment' and
select 'Edit system environment variables'. In the window that opens, click on 'New...' and add the following variables:

* SPARK_HOME : C:\path\to\spark\spark-2.1.0-bin-hadoop2.7
* HADOOP_HOME : C:\path\to\spark\spark-2.1.0-bin-hadoop2.7
* PYSPARK_DRIVER_PYTHON : ipython
* PYSPARK_DRIVER_PYTHON_OPTS : notebook

Finally, add C:\path\to\spark\spark-2.1.0-bin-hadoop2.7\bin to your path variable. Once the paths are added, open a new
terminal and enter `pyspark`. This should launch a Spark shell.

## Using Spark

When developing Spark programs and analyses, users typically run Spark in one of two modes: standalone mode and cluster
mode. Standalone mode runs an instance of Spark on the local computer, which then acts as the Driver, Master, and Worker
nodes. This is typically useful for testing and development as cluster setup doesn't have to be performed and there are
no costs incurred for using a Amazon or Google cluster, for example. To launch a standalone cluster, simply enter a
Spark shell via `pyspark`. This will open up a normal Python prompt with a Spark header:

```bash
Python 3.7.4 (tags/v3.7.4:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
2019-04-17 14:11:34 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-
java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.1
      /_/

Using Python version 3.7.4 (tags/v3.7.4:9a3ffc0492, Dec 23 2018 23:09:28)
SparkSession available as 'spark'.
>>>
```

This will set up a convenience object representing the Spark cluster:

```bash
>>> type(spark)
<class 'pyspark.sql.session.SparkSession'>
```

From there, the user can begin using Spark commands and issuing requests to the 'cluster' and extracting data. One may
ask themselves why bother going through with setting up Spark just to use it locally. The primary reason is two fold:
it provides a simple environment for development and it still provides advantages over native Python code. The second
benefit is realized with how Spark operates: it creates one worker thread per core. By utilizing Spark, data can be
processed using multi-core systems much faster than Python's native single threaded performance. Likewise, Spark
speedups, such as using multiple threads to read different parts of a file being imported can be extremely beneficial.
For example, whereas Python would take around 60-120 seconds to read in and process a 4GB file, Spark can do it in
30-60 seconds, depending on setup (disk I/O eventually saturates).

Launching a Spark cluster is fairly straightforward once Spark has been successfully installed on each of the cluster's
nodes. The process involves launching one master node and then however many worker nodes will be a part of the cluster.
This makes Spark extremely simple to setup and provides for the ability to quickly expand or shrink the cluster as needs
change. To launch a master node, open a terminal and enter `spark-class org.apache.spark.deploy.master.Master`. If all
goes well, a Spark master node will start up. The important part to note are the lines indicating the IP address and
port the master node is listening on:

```bash
2019-04-17 14:48:50 INFO  Master:2608 - Started daemon with process name: 16392@NB391RDC2
2019-04-17 14:48:55 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-
java classes where applicable
...
2019-04-17 14:48:57 INFO  Utils:54 - Successfully started service 'sparkMaster' on port 7077.
2019-04-17 14:48:57 INFO  Master:54 - Starting Spark master at spark://192.168.56.1:7077
...
2019-04-17 14:48:57 INFO  Utils:54 - Successfully started service 'MasterUI' on port 8080.
...
```

In the above section, our master node launched with a public IP address of 192.168.56.1 and is listening for worker
nodes on port 7077. The note about the 'MasterUI' starting on port 8080 provides a pointer to the web-based Spark UI
that lists which applications are running, which nodes are connected, and what errors (if any) have occurred. It
provides a convenient way to check on the health of the cluster without having to launch a whole new application. In the
above scenario, visiting http:\\192.168.56.1:8080 would bring up the Master UI for the cluster.

Launching a worker node operates similarly to a Master node. Simply execute `spark-class org.apache.spark.deploy.worker.
Worker spark://192.168.56.1:7077` in a terminal window on the worker node. This will spin up a new worker node and have
it connect to the master node. If all goes well, the worker node should display:

```bash
2019-04-17 14:53:50 INFO  Worker:2608 - Started daemon with process name: 132@NB391RDC2
...
2019-04-17 14:53:58 INFO  Worker:54 - Connecting to master 192.168.56.1:7077...
2019-04-17 14:53:58 INFO  ContextHandler:781 - Started o.s.j.s.ServletContextHandler@2ebf3995{/metrics/json,null,AVAILABLE,@Spark}
2019-04-17 14:53:58 INFO  TransportClientFactory:267 - Successfully created connection to /192.168.56.1:7077 after 55 ms (0 ms spent in bootstraps)
2019-04-17 14:54:02 INFO  Worker:54 - Successfully registered with master spark://192.168.56.1:7077
```

The master node should also show that a new worker node has connected and registered:

```bash
2019-04-17 14:54:02 INFO  Master:54 - Registering worker 192.168.56.1:63779 with 4 cores, 14.8 GB RAM
```

With the cluster up-and-running, the user can then have their computer (the driver) connect to it an issue commands to
the cluster to read files, manipulate data, and store results.

```python
conf = SparkConf().setAppName("My First Spark App").setMaster("spark://192.168.56.1:7077").set("spark.driver.host",
"192.168.56.2")
sc   = SparkContext(conf=conf)
```

With the above bit of Python, we're doing 3 things. First, we are creating our application's name, which is what will be
presented in the Master UI if a user looks to see what the cluster is currently processing (helpful for debugging if
things get stuck). Second, we're telling our Spark Context to use a remote Master node. By default, Spark will use the
local computer as both Master and Worker node but here, instead, we're telling it to use the cluster that was set up in
the previous steps. Third, we're telling Spark what IP address hosts the driver. The driver is what is issuing commands
to the cluster and the cluster must know where to find the driver in order to return results from the master and worker
nodes.

With the above steps completed, a complete Spark setup has been implemented and the cluster (or local host) is ready for
use.

### Basic File I/O

Spark supports many different file formats including text, CSV, JSON, and parquet files. The only significant hurdle
when reading in data is that all elements of the cluster must have access to the resource - either placed on a network
storage device that all nodes can access via the same URI or on each node at some common path (e.g. /spark/data/). To
read a file into an RDD, one can use:

````python
#Load text data into an RDD...
my_text_data = sc.textFile('/path/to/the/data.txt')

#Load CSV data into an RDD...
from pyspark.sql import SQLContext
sql = SQLContext(sc)
my_csv_data = sql.read.csv('/path/to/the/data.csv', header=True)


#Load JSON data into an RDD...
import json

my_json_data = sc.textFile('/path/to/the/data.json').map(lambda x: json.loads(x))
````

The preceding code introduces three new concepts that are important to cover. The first is reading in data from a text
file via the `textFile()` method. This function will read in a text file and split it along newline characters. If doing
a textual analysis, it would be necessary to split the lines into words, but you do not need to bother splitting the
text into lines. Further, Spark will split the file automatically amongst worker threads so that each thread reads a
part of the file, greatly reducing the time it takes to load large quantities data - assuming the disk I/O supports the
speeds. The second concept is the introduction of Spark's SQLContext. As the name suggests, Spark supports querying
datasets via SQL commands. This provides a simple way to access data in Spark that is, hopefully, familiar to end users.
To query our CSV data, for example, we can register our CSV dataset as a SQL table and then query it as if it were a SQL
database:

```python
my_csv_data.registerTempTable("data")
results = sql.sql("SELECT SUM(some_field) FROM data")
results.show()
```

The final concept introduced is the idea of mapping functions. The `map()` function takes another function as an
argument - here, it's a lambda expression but a function defined using `def` could also be passed. This functionality is
incredibly powerful as Python functions will be serialized, distributed to the cluster, and then executed there -
meaning that the full power of the cluster can be leveraged without having to worry about parallelizing the code by
hand. User Defined Functions are covered in a later section.

### Resilient Distributed Dataset

Resilient Distributed Datasets (RDDs) are the original way Spark read in data. They represent a collection of data and,
to a new Spark user, may seem difficult to understand. RDDs are accessed using map and reduce functions, which belies
Spark's underlying technology, Hadoop, which made the map-reduce framework popular. The best way to think of RDDs is
as a collection of arrays containing data in a set sequence. For example, most word count toy programs typically follow
the pattern:

```python
lines = sc.textFile('/path/to/the/data.txt')
words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
min_len_words = words.filter(lambda x: len(x[0]) > 3)
counts = min_len_words.reduceByKey(lambda a, b: a + b).sortBy(lambda word: word[1], False)
counts.show()

```

There's quite a bit to unpack here, so the program will be examined line-by-line:

The line `words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))` takes the lines that were
read in during the previous line and calls `flatMap()`. The `flatMap()` function takes data that is wide and makes it
long. For example, the phrase "I like Spark!" would be split into one entry with three elements (I, like, Spark!). The
`flatMap()` call, instead, produces three entries with 1 element. The call to `map()` then changes the three entries
to have two elements: the word and the number 1 occupying index 0 and 1, respectively. The third line calls `filter()`.
As the name suggests, this function removes entries that do not meet a given criteria (our lambda function). Finally,
the call to `reduceByKey()` collapses the entries along the key (element 0). The `a` and `b` arguments being passed into
our lambda expression represent the element at index 1 in the entry (the 1 created earlier). Note that since the program
is counting words, it adds the two numbers together. It is, however, possible to reduce by `max()`, `min()`, etc. So the
program could easily be adjusted to find the maximum line length by removing the split or oldest person named 'John' by
simply adjusting the lambda expression. Then the `sortBy()` function orders the data in ascending sequence and creates
a final RDD named counts.

Two important notes: the first is that the first four lines of code are not run until the `counts.show()` line is
executed. This is due to Spark's lazy evaluation nature - it defers work until it has to return data to the user. This
allows it to optimize calls and avoid unnecessary work. For example, if our first step after reading the data is to
remove all lines containing 'DELETE', that step will be combined into reading the text file - avoiding the overhead
of creating the entry just to discard it. Finally, it's important to note that all of the lambda expressions can be
replaced with user functions, covered later. It is, therefore, possible to impalement much more complex logic that would
otherwise look rather messy if crammed into a single lambda.

### RDDs as a Dataframe

One of the main shortcomings of Spark was how unwieldy RDDs could be as the user is required to keep the data mapped
out in their head rather than accessing things via column names or more direct field names. In particular, as the Data
Science field developed and the Pandas library became more popular, the shortcomings of RDDs in comparison to dataframes
became more apparent. To fix this issue, Apache eliminated a dataframe class that emulates many of the features
available to other data analysis libraries. This change made Spark datasets much easier to handle and less prone to
error as the user was able to focus more on what was contained in the data rather than keeping it organized in their
head.

Extending the previous section, the main advantage of dataframes over RDDs is that they use named columns. Rather than
accessing a field via `x[0]`, the user is able to access is as a friendlier column, e.g. `x['FirstName']`. This allows for
users to think of their data in a more familiar manner - as named columns rather than as indexes into an array. While
dataframes still use RDDs as the underlying technology, the featureset that they expose to the user is more familiar
and easier to comprehend. By-and-large, the Spark commonity has shifted towards dataframes for most analytical tasks
though RDDs may still be used for problems that dataframes are ill-equipped to handle (e.g. multi-dimensional data).

Apache's documentation for DataFrames is available at:
https://spark.apache.org/docs/1.6.1/api/java/org/apache/spark/sql/DataFrame.html which, if one is familiar with Pandas,
should look very familiar to users of Python. To read data into a dataframe, simply use a function that reads in data
and can be used to infer a schema:

```python
from pyspark.sql import SQLContext
sql = SQLContext(sc)

my_csv_data = sql.read.csv('/path/to/the/data.csv', header=True)
my_csv_data.describe("field")

>>> +-------+------------------+
>>> |summary|             field|
>>> +-------+------------------+
>>> |  count|              1000|
>>> |   mean|                 5|
>>> | stddev|                 1|
>>> |    min|                 0|
>>> |    max|                10|
>>> +-------+------------------+
```

While it is beyond the scope of this book to describe every function and feature, one can go into Spark understanding
that all common data manipulation functions and analyses are implemented as simple functions that should be familiar.

### User Defined Functions

User Defined Functions, as the name suggests, are functions that users define and are then distributed to the Spark
cluster to be applied against the data. UDFs provide incredible flexibility when it comes to customizing operations and
allows for unique situations to be handled by simply passing in a function that handles the situation cleanly rather
than cobbling together several functions to try and emulate the user's need. While some examples may be trivial:

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def upper_case(line):
    return line.upper()

dataset_with_upper = dataset_without_upper.withColumn("uppercase", udf(lambda z: upper_case(z), StringType()))
```

However, they can also be more complex and utilize multiple fields:

```python
from pyspark.sql.functions import udf, array
from pyspark.sql.types import StringType

#Assume we have some dataframe with a person's test grades...

def calculate_grade(scores):
    total_score = scores[0] + scores[1] + scores[2]
    grade = total_score / 300

    if grade > 0.60:
        return "Pass"
    else:
        return "Fail"

grade_udf = udf(lambda arr: calculate_grade(arr), StringType())

dataset_with_grade = dataset_without_grade.withColumn("grade", grade_udf(array('Test1', 'Test2', 'Test3'),
IntegerType()))
```

The above UDF will take in 3 grades passed as an array and return the student's grade as a pass/fail string. While both
are toy examples, they should hopefully show how powerful UDFs can be - they provide the flexibility of writing your own
code but the power of being distributed amongst a cluster to be processed against massive amounts of data in a quick,
efficient manner.

### Machine Learning

An important note for this section: Spark's mllib library has been deprecated in favor of the ml library. Older articles
may make reference to mllib and, if possible, should be written to use the newer and better supported ml library.

If one has used scikit-learn and pandas, then Spark's machine learning library should seem very familiar. The primary
difference between passing a Pandas dataframe to scikit-learn for analysis and using Spark's ml library is that the
features for each entry must be vectorized first as a new column. Otherwise, things can be handled very similarly to
scikit-learn:

```python
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import OneHotEncoderEstimator, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier, LogisticRegression

#Let our dataframe have a 'gender', 'hours_studied', and 'score' field.
data = sql.read.csv('/path/to/the/student_data.csv', header=True)
#Our gender field is a string, but to utilizing in linear regression, it needs to be one-hot encoded...

encoder = OneHotEncoderEstimator(inputCols=['gender'], outputCols=['gender_onehot'])
model = encoder.fit(data)
data_onehot = model.transform(data)
data_onehot.remove('gender')

assembler = VectorAssembler(inputCols=['gender_onehot', 'hours_studied'], outputCol='features')
data_vec = assembler.transform(data_onehot)

lr = LinearRegression(featuresCol="features", labelCol="score")
model = lr.fit(data_vec)

print(model.summary.r2)
```

Spark supports a wide variety of machine learning algorithms such as support vector machines, logistic regression, naive
bayes, and k-means clustering. All of these models are able to harness Spark's distributed nature and can handle large
amounts of data quickly and in an efficient manner. As can be seen the preceding bit of code, it only takes a few lines
to start a large number of servers working on a problem. In the next section, we'll make it even easier by abstracting
away a lot of the server maintenance via Cloudmesh-EMR.

## Spark via Cloudmesh

Cloudmesh supports Spark clusters via the EMR command. Full documentation is available at
https://github.com/cloudmesh/cloudmesh-emr. The command handles the full life cycle of a Spark cluster from starting up,
submitting programs to be run, and then shutting down the cluster. This eases the burden of having to acquire equipment,
get Spark installed and running on all of them, and then managing the servers. The ideal scenario is to have a program
that has been tested on a local computer using a small subset of the data and a local copy of Spark and then deploy the
final program against the full dataset on a Spark cluster. The power of Cloudmesh lies in that a lot of the details of
setting up the cluster, monitoring it, and issuing commands are abstracted away into a commandline interface. The main
analysis lifecycle would normally consist of three phases that can be implemented in four simple commands:

```bash
$ cms emr start MyFirstCluster --master=m4.large --node=m3.2xlarge --count=10
$ cms emr upload MyPythonProgram.py MyS3Bucket MyPythonProgram.py
$ cms emr run j-ClusterIDFromStep1 MyS3Bucket MyPythonProgram.py
$ cms emr stop j-ClusterIDFromStep1
```

The first command will start a 10 node cluster with 1 master node and 9 worker nodes. It's important to never use nodes
with only 1 vCore as they will start up the main Spark daemon but then be unable to start any worker threads - leading
to a useless server. The next command uploads the Spark program to an S3 bucket the user has created. For more advanced
needs, please see [cloudmesh-storage](https://github.com/cloudmesh/cloudmesh-storage). The third command then submits
the application to the Spark cluster to be run - it's important to note that, for convenience, Amazon sets up a 's3'
file path and permissions to read and write to buckets on the account. This means the Spark program should, for example,
read data as `sc.textFile('s3://path/to/file/on/s3/data.txt')` and save data to an s3 path. Finally, the stop command
will shutdown the cluster.

Beyond those four critical commands, there are ones to list what clusters are running, describe them, and list active
jobs/tasks on each cluster. In very specific scenarios, it's also possible to copy files directly to the master node
by utilizing the copy function, though that usage scenario is somewhat rare.

### OpenAPI

Finally, cloudmesh-emr can be run as an OpenAPI rest service. The user can launch the service by navigating to the
cloudmesh-emr directory and calling:

```bash
$ cms openapi server start ./emr.yaml
```

This will start a server on the localhost using port 8080 and expose the following commands:

```
http://localhost:8080/api/list_clusters
http://localhost:8080/api/list_instances
http://localhost:8080/api/list_steps
http://localhost:8080/api/describe
http://localhost:8080/api/stop
http://localhost:8080/api/start
http://localhost:8080/api/upload
http://localhost:8080/api/copy
http://localhost:8080/api/run
```

The full methodology of how to utilize them is covered in the [documentation](https://github.com/cloudmesh/cloudmesh-emr/blob/master/README.md).
