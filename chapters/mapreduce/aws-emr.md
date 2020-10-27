# AWS Elastic Map Reduce (AWS EMR)

---

![](images/learning.png) **Learning Objectives**

* Learn about EMR
* Deploy an EMR cluster using:
  - Amazon's Command Line Interface (CLI)
  - Amazon's Web Interfaces
* Run an example Spark application on an EMR cluster

---

## Introduction

EMR is an Amazon product that allows for the creation of clusters of
Elastic Compute Cloud (EC2) instances [@www-amazon-emr]. EMR allows user to take advantage
of distributed computing capabilities. As the name suggests this product
is designed to allow users to easily scale their cluster to meet their
computing needs.

Amazon EMR facilitates you to analyze and process vast(huge) amounts of
data by distributing the computational work across a cluster of virtual
servers running in the AWS Cloud. The EMR cluster is managed using an
open-source framework called Hadoop. Amazon EMR lets you focus on
crunching or analyzing your data without having to worry about
time-consuming setup, management, and tuning of Hadoop clusters or the
compute capacity they rely on unlike other Hadoop distributors like
Cloudera, Hortonworks etc.,

## Why EMR?

The following are reasons given by Amazon for using EMR:

* Easy to Use: Launch cluster in a 5 to 10 minutes time as many
  cluster of nodes as you need
* Pay as you go: Pay an hourly rate (with AWS latest pricing model,
  customers can choose to pay in minutes)
* Flexible: Easily Add/ Remove capacity(Auto scale out and in anytime)
* Reliable: Spend less time for monitoring and can utilize in-built
  AWS tools which will reduce overhead
* Secure: Manage firewall (VPC both private and subnet)


EMR clusters can be created through relatively simple web interfaces or
can be created through code using CLI. EMR Clusters can be configured
for size and can be provisioned with open-source distributed frameworks
such as SPARK and HBase, Presto, Flink and etc. Interact with data in AWS data stores such as
Amazon S3, DynamoDB and etc.

Components Of EMR:

- Storage
- EC2 instance
- Clusters
- Security
- KMS


## Understanding Clusters and Nodes

The component of Amazon EMR is the cluster. A cluster is a collection
of Amazon Elastic Compute Cloud (Amazon EC2) instances. Each instance
in the cluster is called a node. Each node has a role within the
cluster, referred to as the node type. Amazon EMR also installs
different software components on each node type, giving each node a
role in a distributed application like Apache Hadoop.

The node types in Amazon EMR are as follows:

- Master node: A node that manages the cluster by running software
  components to coordinate the distribution of data and tasks among other
  nodes for processing. The master node tracks the status of tasks and
  monitors the health of the cluster. Every cluster has a master node, and
  it is possible to create a single-node cluster with only the master
  node.

- Core node: A node with software components that run tasks and store
  data in the Hadoop Distributed File System (HDFS) on your
  cluster. Multi-node clusters have at least one core node.

- Task node: A node with software components that only runs tasks and
  does not store data in HDFS. Task nodes are optional.

The following diagram represents a cluster with one master node and
four core nodes.

![Cluster and Nodes [@www-aws-emr]](images/cluster-node-types.png){#fig:aws-emr-cluster-nodes}


## Prerequisites

Official prerequisites are listed here: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs-prerequisites.html

* [AWS Account](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account)
* [AWS Key Pair](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#setting-up-key-pair)
* [Install and Configure AWS CLI](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#aws-command-line-interface)
* [AWS Admin Access](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#aws-admin-access)
* [Linux Environment](https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md)

## Creating EMR Cluster Using CLI

### Create Security Roles

In this example we will use the default EMR security roles. These roles
enable the nodes within the cluster to access each other and to access
other AWS products.

```bash
aws emr create-default-roles
```

### Setting up authentication

In this example we will be using Kerberos for authentication. The
Kerberos configuration would allow you to add additional users to your
EMR cluster.

Create a json file with the following content and save to a local file:
```bash
{
  "AuthenticationConfiguration": {
    "KerberosConfiguration": {
      "Provider": "ClusterDedicatedKdc",
      "ClusterDedicatedKdcConfiguration": {
        "TicketLifetimeInHours": 24
      }
    }
  }
}
```

Create the Kerberos configuration using the previously created json file:

```bash
aws emr create-security-configuration --name "KerberosSecurityConfiguration" --security-configuration file://MyKerberosSecurityConfig.json
```

### Determine the applicable subnet

The EMR cluster will run on a subnet so you need to determine the
appropriate subnet for you availability zone. You will need to enter
your default zone in the code next.

```bash
aws ec2 describe-subnets --filters "Name=availabilityZone,Values=us-east-2b"
```

The applicable information is returned as the `SubnetId` field.

### Create the EMR cluster

In this example we will create a simple cluster with 3 nodes. One master
node and two slave nodes. We will also specify the EC2 instance type
(m4.large).  These parameters are configurable and you can create larger
clusters with more processing power. There are multiple EMR versions
available, this example uses the latest version available at the time of
creation.

There are a variety of applications that can be installed on the EMR
cluster at creation, but in this case we will simply install Spark. The
Kerberos password can be used to add users to your cluster once it is
created. The KeyName is your EC2 key pair that is referenced in the
Prerequisites section.

```bash
aws emr create-cluster --name "Test-Kerberized-Spark-Cluster" \
--release-label emr-5.17.0 \
--instance-type m4.large \
--instance-count 3 \
--use-default-roles \
--ec2-attributes KeyName=your-key,SubnetId=your-subnet-id \
--security-configuration KerberosSecurityConfiguration \
--applications Name=Spark \
--kerberos-attributes Realm=EC2.INTERNAL,KdcAdminPassword=your-password
```

### Check the status of your cluster

The cluster may take several minutes to initialize. To check the status
of your cluster use the cluster-id that was returned in the previous
step.

```bash
aws emr describe-cluster --cluster-id your-cluster-id
```

### Terminate your cluster

To terminate your cluster use the following command (hint: AWS charges
apply while your cluster is up).

```bash
aws emr terminate-clusters --cluster-ids your-cluster-id
```

## Creating EMR Cluster Using AWS Web Console

### Set up authentication

Go to the AWS Console and ensure that the URL references your default
region (see Figure @fig:aws-emr-1 and @fig:aws-emr-2)

[AWS EMR](https://us-east-2.console.aws.amazon.com/elasticmapreduce/home?region=us-east-2#)

Select the `Security configurations` and click `Create`. Give a
meaningful name like: `KerberosSecurityConfiguration`. Then select
`Kerberos` under `Authentication` and click `Create`.



![Set up Kerberos 1 [@www-aws-emr]](images/EMR-Console-1.png){#fig:aws-emr-1}

![Set up Kerberos 2 [@www-aws-emr]](images/EMR-Console-2.png){#fig:aws-emr-2}


### Create the EMR cluster

Go to the AWS Console (ensure that the URL references your default region)

[AWS EMR](https://us-east-2.console.aws.amazon.com/elasticmapreduce/home?region=us-east-2#)

Click `Create cluster` (see Figure @fig:aws-emr-3)


![Set up EMR 1 [@www-aws-emr]](images/EMR-Console-3.png){#fig:aws-emr-3}


* Select your desired EMR version
* Select Spark
* Select your desired instance types
* For this example deselect the `Logging` option
* Select your EC2 key Pair


Next, create a cluster (see Figure @fig:aws-emr-4)

![Set up EMR 2 [@www-aws-emr]](images/EMR-Console-4.png){#fig:aws-emr-4}


* Under `Advanced Options` select `Security` and then YourKerberosSecurityConfiguration
* Click `Create cluster`

(See Figure @fig:aws-emr-5)

![Set up EMR 3 [@www-aws-emr]](images/EMR-Console-5.png){#fig:aws-emr-5}


### View status and terminate EMR cluster

You can view the status of your cluster or termiate the cluster by
naviagting to `>Services>EMR>Clusters` within the AWS Console.

See Figure @fig:aws-emr-6.

![Set up EMR 4 [@www-aws-emr]](images/EMR-Console-6.png){#fig:aws-emr-6}


### Submit Work to a Cluster

When you run a cluster on Amazon EMR, you have several options as to how
you specify the work that needs to be done.

Provide the entire definition of the work to be done in functions that
you specify as steps when you create a cluster. This is typically done
for clusters that process a set amount of data and then terminate when
processing is complete.

Create a long-running cluster and use the Amazon EMR console, the Amazon
EMR API, or the AWS CLI to submit steps, which may contain one or more
jobs.

Create a cluster, connect to the master node and other nodes as required
using SSH, and use the interfaces that the installed applications
provide to perform tasks and submit queries, either scripted or
interactively.

### Processing Data

When you launch your cluster, you choose the frameworks and applications
to install for your data processing needs. To process data in your
Amazon EMR cluster, you can submit jobs or queries directly to installed
applications, or you can run steps in the cluster.

- Submitting Jobs Directly to Applications:

  You can submit jobs and interact directly with the software that is
  installed in your Amazon EMR cluster. To do this, you typically
  connect to the master node over a secure connection and access the
  interfaces and tools that are available for the software that runs
  directly on your cluster. For more information, see Connect to the
  Cluster.

- Running Steps to Process Data

  You can submit one or more ordered steps to an Amazon EMR cluster.
  Each step is a unit of work that contains instructions to manipulate
  data for processing by software installed on the cluster.

The following is an example process using four steps:

1. Submit an input dataset for processing.
2. Process the output of the first step by using a Pig program.
3. Process a second input dataset by using a Hive program.
4. Write an output dataset.

Generally, when you process data in Amazon EMR, the input is data stored as files in your chosen underlying file system, 
such as Amazon S3 or HDFS. This data passes from one step to the next in the processing sequence. The final step writes 
the output data to a specified location, such as an Amazon S3 bucket.

Steps are run in the following sequence:

1. A request is submitted to begin processing steps.
2. The state of all steps is set to PENDING.
3. When the first step in the sequence starts, its state changes to
   RUNNING. The other steps remain in the PENDING state.
4. After the first step completes, its state changes to COMPLETED.
5. The next step in the sequence starts, and its state changes to
   RUNNING. When it completes, its state changes to COMPLETED.
6. This pattern repeats for each step until they all complete and
   processing ends.

The following diagram represents the step sequence and change of state
for the steps as they are processed.

![Cluser and Nodes](images/step-sequence.png)

If a step fails during processing, its state changes to
TERMINATED_WITH_ERRORS. You can determine what happens next for each
step. By default, any remaining steps in the sequence are set to
CANCELLED and do not run. You can also choose to ignore the failure and
allow remaining steps to proceed, or to terminate the cluster
immediately.

The following diagram represents the step sequence and default change of
state when a step fails during processing.

![Cluser and Nodes](images/step-sequence-failed.png)

## AWS Storage

S3
- Cloud based storage
- Using EMRFS can directly connects s3 storage
- Accessible from any where

Instance Store
- Local storage
- Data will be lost on start and stop EC2 instances

EBS
- Network attached storage
- Data preserved on start and stop
- Accessible only through EC2 instances

## Create EMR in AWS

### Create the buckets

- Login to AWS console and create the buckets at
  https://aws.amazon.com/console/. To create the buckets, go to
  services (see @fig:aws-console-page, @fig:aws-login-page), click on S3 under
  Storage, @fig:aws-s3-page, @fig:aws-s3-bucket-page, @fig:aws-s3-create-bucket. Click
  on Create bucket button and then provide all the details to complete
  bucket creation.
- AWS Console

![AWS Console](images/aws_console.JPG){#fig:aws-console-page}


- AWS Login

![AWS Login](images/aws_login.JPG){#fig:aws-login-page}

- S3 – Amazon Storage

![Amazon Storage](images/storage_s3.JPG){#fig:aws-s3-page}

- S3 – Create buckets

![S3 buckets](images/create_bucket.JPG){#fig:aws-s3-bucket-page}

![S3 buckets1](images/create_bucket_1.JPG){#fig:aws-s3-create-bucket}

### Create Key Pairs

- Login to AWS console, go to services, click on EC2 under compute.
  Select the Key pairs resoure, click on Create Key Pair and provide Key
  Pair name to complete the Key pairs creation. See @fig:aws-keypair-page

- Download the. pem file once Key value pair is created. This is needed
  to access AWS Hadoop environment from client machine. This need to be
  imported in Putty to access your AWS environemnt. See @fig:aws-create-keypair

#### Create Key Value Pair Screen shots

![AMS Key Value Pair](images/key-value-pair.JPG){#fig:aws-keypair-page}

![AMS Key Value Pair1](images/key-value-pair-1.JPG){#fig:aws-create-keypair}


## Create Step Execution – Hadoop Job

Login to AWS console, go to services and then select EMR. Click on
Create Cluster. The cluster configuration provides details to complete
to complete step execution creation. See: @fig:aws-emr-page,
@fig:aws-create-emr-page, @fig:emr-step-exe-page, @fig:step-cluster-page,
@fig:step-cluster1-page.

- Cluster name (Example: HadoopJobStepExecutionCluster)
- Select Logging check box and provide S3 folder location
  (Example: s3://bigdata-raviAndOrlyiuproject/logs/)
- Select launch mode as Step execution
- Select the step type and complete the step configuration
- Complete Software Configuration
- Complete Hardware Configuration
- Complete Security and access
- And then click on create cluster button
- Once job started, if there are no errors output file will be created
  in the output directory.

#### Screen shots

![AWS EMR](images/aws_emr.JPG){#fig:aws-emr-page}

![AWS Create EMR](images/create_emr.JPG){#fig:aws-create-emr-page}

![AWS Config EMR](images/emr-step-execution.JPG){#fig:emr-step-exe-page}

![AWS Create Cluster](images/step_cluster.JPG){#fig:step-cluster-page}

![AWS Create Cluster1](images/step_cluster_1.JPG){#fig:step-cluster1-page}

## Create a Hive Cluster

Login to AWS console, go to services and then select EMR. Click on
Create Cluster. The cluster configuration provides details to complete.
See, @fig:hive-cluster1-page, @fig:hive-cluster2-page, @fig:hive-cluster3-page.

- Cluster name (Example: MyFirstCluster-Hive)
- Select Logging check box selected and provide S3 folder location
- Select launch mode as Cluster
- Complete software configuration (select hive application)  and click
  on create cluster

### Create a Hive Cluster - Screen shots

![Hive Cluser](images/hive_cluster1.JPG){#fig:hive-cluster1-page}

![Hive Cluser1](images/hive_cluster2.JPG){#fig:hive-cluster2-page}

![Hive Cluser2](images/hive_cluster_2.JPG){#fig:hive-cluster3-page}

## Create a Spark Cluster

Login to AWS console, go to services and then select EMR. Click on
Create Cluster. The cluster configuration provides details to complete.
See, @fig:spark-cluster1-page, @fig:spark-cluster2-page, @fig:spark-cluster3-page.

- Cluster name (Example: My Cluster - Spark)
- Select Logging check box selected and provide S3 folder location
- Select launch mode as Cluster
- Complete software configuration and click on create cluster
- Select application as Spark

### Create a Spark Cluster - Screenshots

![Spark Cluser](images/spark_cluster1.JPG){#fig:spark-cluster1-page}

![Spark Cluser](images/spark_cluster2.JPG){#fig:spark-cluster2-page}

![Spark Cluser](images/spark_cluster3.JPG){#fig:spark-cluster3-page}

## Run an example Spark job on an EMR cluster

### Spark Job Description

You can submit Spark steps to a cluster as it is being created or to an already
running cluster,

In this example we will execute a simple Python function on a text file using
Spark on EMR. This is a standard word count application that will return the
distinct words in the file along with the count of the number of times the words
are present.

The Python file containing the application will be stored and referenced in a S3
bucket along with the text file being analyzed. The results of the Spark job
will be returned to the same S3 bucket.

### Creating the S3 bucket

```bash
aws s3 mb s3://test-analysis-bucket `--region us-east-2`
```

### Copy files to S3

Create a `WordCount.py` file with the following code.

```python
from pyspark import SparkContext
import sys
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: testjob  ", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="MyTestJob")
    dataTextAll = sc.textFile(sys.argv[1])
    dataRDD = dataTextAll.map(lambda x: x.split(",")).map(lambda y: (str(y[0]), float(y[1]))).reduceByKey(lambda a, b: a + b)
    dataRDD.saveAsTextFile(sys.argv[2])
    sc.stop()
```

You can then sync the folder you stored .py file in to your S3 bucket folder.

```bash
aws s3 sync your-local-folder-path s3://test-analysis-bucket/SparkTutorial
```

Store a text file locally and use the S3 sync function to make it
availaable in your S3 bucket.

```bash
aws s3 sync your-local-folder-path s3://test-analysis-bucket/SparkTutorial/Input
```

### Execute the Spark job on a running cluster

Using your cluster id and the paths within your S3 bucket run the
following command (this assumes you have a cluster up and running).

```bash
aws emr add-steps --cluster-id your-cluster-id \
--steps Type=spark,Name=SparkWordCountApp,\
Args=[--deploy-mode,cluster,--master,yarn,\
--conf,spark.yarn.submit.waitAppCompletion=false,\
--num-executors,2,--executor-cores,2,--executor-memory,1g,\
s3://your-bucket/SparkTutorial/Python/WordCount.py,\
s3://your-bucket/SparkTutorial/Python/Input/input.txt,\
s3://your-bucket/SparkTutorial/Python/Output/]
```
### Execute the Spark job while creating clusters

We can also run the same Spark step during the creation of a cluster
using the following command (assumes you have already done pre-steps to
creating an EMR cluster).

In this case the EMR cluster will spin up, run the Spark job, persist
the results to your S3 bucket, and then auto terminate.

```bash
aws emr create-cluster \
--name "Test-Kerberized-Spark-Cluster" \
--release-label emr-5.17.0 \
--instance-type m4.large \
--instance-count 3 \
--use-default-roles \
--ec2-attributes KeyName=your-key,SubnetId=subnet-d0169eaa \py
--security-configuration KerberosSecurityConfiguration \
--applications Name=Spark \
--kerberos-attributes Realm=EC2.INTERNAL,KdcAdminPassword=your-pw \
--steps Type=spark,Name=SparkWordCountApp,\
Args=[--deploy-mode,cluster,--master,yarn,\
--conf,spark.yarn.submit.waitAppCompletion=false,\
--num-executors,2,--executor-cores,2,--executor-memory,1g,\
s3://your-bucket/SparkTutorial/Python/WordCount.py,\
s3://your-bucket/SparkTutorial/Python/Input/input.txt,\
s3://your-bucket/SparkTutorial/Python/Output/],\
ActionOnFailure=CONTINUE \
--auto-terminate
```
### View the results of the Spark job
You can use the AWS Console to view the results of the Spark Job.

Go to the AWS Console (ensure that the URL references your default region)

[AWS Console](https://us-east-2.console.aws.amazon.com/elasticmapreduce/home?region=us-east-2#)

Navigate to the S3 bucket and folder you specified for the output (see Figure
@fig:aws-emr-7)

![Set up EMR [@www-aws-emr]](images/EMR-Console-7.png){#fig:aws-emr-7}


## Conclusion

AWS EMR is a powerful tool for distributive processing. It is easy to
use from wither the command line utilizing AWS CLI or through the AWS
Console web interface.
