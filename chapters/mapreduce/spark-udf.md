# User Defined Functions in Spark


Apache Spark is a fast and general cluster-computing framework which
perform computational tasks up to 100x faster than Hadoop MapReduce
in memory, or 10x faster on disk for high speed large-scale streaming,
machine learning and SQL workloads tasks. Spark offers support for the
applications development employing over 80 high-level operators using
Java, Scala, Python, and R. Spark powers the combined or standalone
use of a stack of libraries including SQL and DataFrames, MLlib for
machine learning, GraphX, and Spark Streaming. Spark can be utilized
in standalone cluster mode, on EC2, on Hadoop YARN, or on Apache Mesos
and it allows data access in HDFS, Cassandra, HBase, Hive, Tachyon,
and any Hadoop data source.

User-defined functions (UDFs) are the functions created by developers
when the built-in functionalities offered in a programming language,
are not sufficient to do the required work. Similarly, Apache Spark
UDFs also allow developers to enable new functions in higher level
programming languages by extending built-in functionalities.  It also
allows developers to experiment with wide range of options for
integrating UDFs with Spark SQL, MLib and GraphX workflows.

This tutorial explains following:

How to install Spark in Linux, Windows and MacOS.

How to create and utilize user defined functions(UDF) in Spark using Python.

How to run the provided example using a provided docker file and make file.

## Resources

* <https://spark.apache.org/>
* <http://www.scala-lang.org/>
* <https://docs.databricks.com/spark/latest/spark-sql/udf-in-python.html>

## Instructions for Spark installation

###  Linux

First, JDK (Recommended version 8) should be installed to a path where
there is no space.

* <http://www.oracle.com/technetwork/java/javase/downloads/index.html>

Second, setup environment variables for JDK by adding bin folder path
to to user path variable.

	This $ export PATH = $PATH:/usr/local/java8/bin

Next, download and extract Scala pre-built version from

* <http://www.scala-lang.org/download/>

Then, setup environment variables for Scala by adding bin folder path
to the user path variable.

	$ export PATH = $PATH:/usr/local/scala/bin

Next, download and extract Apache Spark pre-built version.

* <https://spark.apache.org/downloads.html>

Then, setup environment variables for spark by adding bin folder path
to the user path variable.

	$ export PATH = $PATH:/usr/local/spark/bin

Finally, for testing the installation, please type the following command.

	spark-shell

##  Windows

First, JDK should be installed to a path where there is no space in
that path. Recommended JAVA version is 8.

<http://www.oracle.com/technetwork/java/javase/downloads/index.html>

Second, setup environment variables for jdk by adding bin folder path
to to user path variable.

	set JAVA_HOME=c:\java8
	set PATH=%JAVA_HOME%\bin;%PATH%

Next, download and extract Apache Spark pre-built version.

<https://spark.apache.org/downloads.html>

Then, setup environment varibale for spark by adding bin folder path
to the user path variable.

	set SPARK_HOME=c:\spark
	set PATH=%SPARK_HOME%\bin;%PATH%

Next, download the winutils.exe binary and Save winutils.exe binary to
a directory (`c:\hadoop\bin`).

<https://github.com/steveloughran/winutils>

Then, change the winutils.exe permission using following command using
CMD with administrator permission.

	$ winutils.exe chmod -R 777 C:\tmp\hive

If your system doesnt have `hive` folder, make sure to create
`C:\tmp\hive` directory.

Next, setup environment variables for hadoop by adding bin folder path to the user path variable.

	set HADOOP_HOME=c:\hadoop\bin
	set PATH=%HADOOP_HOME%\bin;%PATH%

Then, install Python 3.6 with anaconda (This is a bundled python installer for pyspark).

<https://anaconda.org/anaconda/python>

Finally, for testing the installation, please type the following command.

	$ pyspark

##  MacOS

First, JDK should be installed to a path where there is no space in
that path. Recommanded JAVA version is 8.

<http://www.oracle.com/technetwork/java/javase/downloads/index.html>

Second, setup environment variables for jdk by addding bin folder path
to to user path variable.

	$ export JAVA_HOME=$(/usr/libexec/java_home)

Next, Install Apache Spark using Homebrew with following commands.

	$ brew update
	$ brew install scala
	$ brew install apache-spark

Then, setup environment varibale for spark with following commands.

	$ export SPARK_HOME="/usr/local/Cellar/apache-spark/2.1.0/libexec/"
	$ export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
	$ export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH

Next, install Python 3.6 with anaconda (This is a bundled python
installer for pyspark)

<https://anaconda.org/anaconda/python>

Finally, for testing the installation, please type the following command.

	$ pyspark

## Instructions for creating Spark User Defined Functions

### Example: Temperature conversion

In this example we convert temperature data from Celsius to Fahrenheit
with filtering and sorting

#### Description about data set

The file **temperature_data.csv** contains temperature data of
different wheather stations and it has the following structure.

```csv
ITE00100554,18000101,TMAX,-75,,,E,
ITE00100554,18000101,TMIN,-148,,,E,
GM000010962,18000101,PRCP,0,,,E,
EZE00100082,18000101,TMAX,-86,,,E,
GM000010962,18000104,PRCP,0,,,E,
EZE00100082,18000104,TMAX,-55,,,E,
```

We will only consider wheather station ID (column 0), entrytype
(column 2), temperature (column 3: it is in 10*Celsius)

#### How to write a python program with UDF

First, we need to import the relevent libraries to use Spark sql built
in functionalities listed as follows.

	from pyspark.sql import SparkSession
	from pyspark.sql import Row

Then, we need create a user defined fuction which will read the text
input and process the data and return a spark sql Row object. It can
be created as listed as follows.

```python
	def process_data(line):
		fields = line.split(',')
		stationID = fields[0]
		entryType = fields[2]
		temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
		return Row(ID=stationID, t_type=entryType, temp=temperature)
```

Then we need to create a Spark SQL session as listed as follows with
an application name.

	spark = SparkSession.builder.appName("Simple SparkSQL UDF example").getOrCreate()

Next, we read the raw data using spark build-in function textFile() as
shown next.

	lines = spark.sparkContext.textFile("temperature_data.csv")

Then, we convert those read lines to a Resilient Distributed Dataset
(RDD) of Row object using UDF (process_data) which we created as
listed as follows.

	parsedLines = lines.map(process_data)

Alternatively we colud have written the UDF using a python lamda
function to do the same thing as shown next.

```python
parsedLines = lines.map(lambda line: Row(ID=line.split(',')[0],
						t_type=line.split(',')[2],
						temp=float(line.split(',')[3]) * 0.1 * (9.0
						/ 5.0) + 32.0))
```

Now, we can convert our RDD object to a Spark SQL Dataframe as listed
as follows.

	TempDataset = spark.createDataFrame(parsedLines)

Next, we can print and see the first 20 rows of data to validate our
work as shown next.

	TempDataset.show()

#### How to execute a python spark script

You can use **spark-submit** command to run a spark script as shown next.

	spark-submit temperature_converter.py

If everything went well, you should see the following output.

```bash
+-----------+------+-----------------+
|         ID|t_type|             temp|
+-----------+------+-----------------+
|EZE00100082|  TMAX|90.14000000000001|
|ITE00100554|  TMAX|90.14000000000001|
|ITE00100554|  TMAX|            89.42|
|EZE00100082|  TMAX|            88.88|
|ITE00100554|  TMAX|            88.34|
|ITE00100554|  TMAX|87.80000000000001|
|ITE00100554|  TMAX|            87.62|
|ITE00100554|  TMAX|            87.62|
|EZE00100082|  TMAX|            87.26|
|EZE00100082|  TMAX|87.08000000000001|
|EZE00100082|  TMAX|87.08000000000001|
|ITE00100554|  TMAX|            86.72|
|ITE00100554|  TMAX|            86.72|
|ITE00100554|  TMAX|            86.72|
|EZE00100082|  TMAX|            86.72|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|            85.64|
|ITE00100554|  TMAX|            85.64|
+-----------+------+-----------------+
only showing top 20 rows
```

#### Filtering and sorting

Now we are trying to find what is the maximum temperature reported for
a particluar whether station and print the data in ascending order. We
can achieve this by using **where()** and **orderBy()** fundtions as
shown next.

	TempDatasetProcessed = TempDataset.where(TempDataset['t_type'] == 'TMAX'
		).orderBy('temp', ascending=False).cache()


We achieved the filtering using temperature type and it filters out
all the data which is not a TMAX.

Finally, we can print the data to see whether this worked or not using
following statement.

	TempDatasetProcessed.show()

Now, it is the time to run the python script again using following
command.

	spark-submit temperature_converter.py

If everything went well, you should see the following sorted and
filtered output.

```bash
+-----------+------+-----------------+
|         ID|t_type|             temp|
+-----------+------+-----------------+
|EZE00100082|  TMAX|90.14000000000001|
|ITE00100554|  TMAX|90.14000000000001|
|ITE00100554|  TMAX|            89.42|
|EZE00100082|  TMAX|            88.88|
|ITE00100554|  TMAX|            88.34|
|ITE00100554|  TMAX|87.80000000000001|
|ITE00100554|  TMAX|            87.62|
|ITE00100554|  TMAX|            87.62|
|EZE00100082|  TMAX|            87.26|
|EZE00100082|  TMAX|87.08000000000001|
|EZE00100082|  TMAX|87.08000000000001|
|ITE00100554|  TMAX|            86.72|
|ITE00100554|  TMAX|            86.72|
|ITE00100554|  TMAX|            86.72|
|EZE00100082|  TMAX|            86.72|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|             86.0|
|ITE00100554|  TMAX|            85.64|
|ITE00100554|  TMAX|            85.64|
+-----------+------+-----------------+
only showing top 20 rows
```

Complete python script is listed as follows as well as under this
directory (temperature_converter.py).

<https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/temperature_converter.py>

```python
from pyspark.sql import SparkSession
from pyspark.sql import Row

def process_data(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return Row(ID=stationID, t_type=entryType, temp=temperature)

# Create a SparkSQL Session
spark = SparkSession.builder.appName('Simple SparkSQL UDF example'
        ).getOrCreate()

# Get the raw data
lines = spark.sparkContext.textFile('temperature_data.csv')

# Convert it to a RDD of Row objects
parsedLines = lines.map(process_data)

# alternative lamda fundtion

parsedLines = lines.map(lambda line: Row(ID=line.split(',')[0],
                        t_type=line.split(',')[2],
                        temp=float(line.split(',')[3]) * 0.1 * (9.0
                        / 5.0) + 32.0))

# Convert that to a DataFrame
TempDataset = spark.createDataFrame(parsedLines)

# show first 20 rows temperature converted data
# TempDataset.show()

# Some SQL-style magic to sort all movies by popularity in one line!
TempDatasetProcessed = TempDataset.where(TempDataset['t_type'] == 'TMAX'
        ).orderBy('temp', ascending=False).cache()

# show first 20 rows of filtered and sorted data
TempDatasetProcessed.show()
```

## Instructions to install and run the example using docker

Following link is the home directory for the example explained in this tutorial.

<https://github.com/cloudmesh-community/hid-sp18-409/tree/master/tutorial/spark_udfs>

It contains following files

* Python script which contains the example:
  [temperature_converter.py](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/temperature_converter.py
  "temperature_converter.py")
* Temperature data file:
  [temperature_data.csv](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/temperature_data.csv
  "temperature_data.csv")
* Required python dependencies are put here:
  [requirements.txt](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/requirements.txt
  "requirements.txt")
* Docker file which automatically setup the codebase with dependency
  installation:
  [Dockerfile](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/Dockerfile
  "Dockerfile")
* Make file which will excute the example with a single command:
  [Makefile](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/spark_udfs/Makefile
  "Makefile")

To install the example using docker plesse do the following steps.

First, you should install docker in to your computer.

Next, git clone the
[project ](https://github.com/cloudmesh-community/hid-sp18-409/blob/master/tutorial/)
. Alternatively you can also download the docker image from the docker
hub. Then you don't need to do docker build.

```bash
$ docker pull kadupitiya/tutorial
```

Then, change the directory to **spark_udfs** folder.

Next, install the service using following make command

```bash
$ make docker-build
```

Finally, start the service using following make command

```bash
$ make docker-start
```

Now you should see the same output we saw at the end of the example explanation.
