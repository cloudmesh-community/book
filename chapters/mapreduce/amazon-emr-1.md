# Amazon EMR (Elastic Map Reduce) :o:

Amazon EMR provides a managed Hadoop framework that makes big data processing
- Easy
- Fast
- Cost-effective

EMR Supports other distributed framework such as Apache Spark, HBase, Presto, Flink and etc.
Interact with data in AWS data stores such as Amazon S3, DynamoDB and etc.

Components Of EMR:
- Storage
- EC2 instance
- Clusters

## Why EMR?

Easy to Use
- Launch cluster in a min

Pay as you go
- Pay an hourly rate

Flexible
- Easily Add/ Remove capacity

Reliable
- Spend less time for monitoring

Secure
- Manage firewall

## AWS Storage

S3
- Cloud based storage
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
  services (see @fig:aws-console-1, @fig:aws-login), click on S3 under
  Storage, @fig:aws-s3, @fig:aws-s3-bucket, @fig:aws-s3-bucket1. Click
  on Create bucket button and then provide all the details to complete
  bucket creation.
- AWS Console

![AWS Console](images/aws_console.JPG){#fig:aws-console-1}

- AWS Login

![AWS Login](images/aws_login.JPG){#fig:aws-login}

- S3 – Amazon Storage

![Amazon Storage](images/storage_s3.JPG){#fig:aws-s3}

- S3 – Create buckets

![S3 buckets](images/create_bucket.JPG){#fig:aws-s3-bucket}

![S3 buckets1](images/create_bucket_1.JPG){#fig:aws-s3-bucket1}

### Create Key Pairs

- Login to AWS console, go to services, click on EC2 under compute. Select the Key pairs resoure, click on Create Key Pair and provide Key Pair name to complete the Key pairs creation. See @fig:aws-keypair
- Download the. pem file once Key value pair is created. This is needed to access AWS Hadoop environment from client machine. This need to be imported in Putty to access your AWS environemnt. See @fig:aws-keypair1

#### Create Key Value Pair Screen shots

![AMS Key Value Pair](images/key-value-pair.JPG){#fig:aws-keypair}

![AMS Key Value Pair1](images/key-value-pair-1.JPG){#fig:aws-keypair1}


## Create Step Execution – Hadoop Job

Login to AWS console, go to services and then select EMR. Click on Create Cluster. In the cluster configuration provide below details to complete to complete step execution creation.
See: @fig:aws-emr, @fig:aws-create-emr, @fig:emr-step-exe, @fig:step-cluster, @fig:step-cluster1
- Cluster name (Ex: HadoopJobStepExecutionCluster)
- Select Logging check box and provide S3 folder location (Ex: s3://bigdata-raviAndOrlyiuproject/logs/)
- Select launch mode as Step execution
- Select the step type and complete the step configuration
- Complete Software Configuration
- Complete Hardware Configuration
- Complete Security and access
- And then click on create cluster button
- Once job started, if there are no errors output file will be created in the output directory.

#### Screen shots

![AWS EMR](images/aws_emr.JPG){#fig:aws-emr}

![AWS Create EMR](images/create_emr.JPG){#fig:aws-create-emr}

![AWS Config EMR](images/emr-step-execution.JPG){#fig:emr-step-exe}

![AWS Create Cluster](images/step_cluster.JPG){#fig:step-cluster}

![AWS Create Cluster1](images/step_cluster_1.JPG){#fig:step-cluster1}

## Create a Hive Cluster

Login to AWS console, go to services and then select EMR. Click on Create Cluster. In the cluster configuration provide below details to complete.
See, @fig:hive-cluster1, @fig:hive-cluster2, @fig:hive-cluster3
- Cluster name (Ex: MyFirstCluster-Hive)
- Select Logging check box selected and provide S3 folder location
- Select launch mode as Cluster
- Complete software configuration (select hive application)  and click on create cluster
-
### Create a Hive Cluster - Screen shots

![Hive Cluser](images/hive_cluster1.JPG){#fig:hive-cluster1}

![Hive Cluser1](images/hive_cluster2.JPG){#fig:hive-cluster2}

![Hive Cluser2](images/hive_cluster_2.JPG){#fig:hive-cluster3}

## Create a Spark Cluster
Login to AWS console, go to services and then select EMR. Click on Create Cluster. In the cluster configuration provide below details to complete.
See, @fig:spark-cluster1, @fig:spark-cluster2, @fig:spark-cluster3
- Cluster name (Ex:My Cluster - Spark)
- Select Logging check box selected and provide S3 folder location
- Select launch mode as Cluster
- Complete software configuration and click on create cluster
- Select application as Spark

### Create a Spark Cluster - Screenshots

![Spark Cluser](images/spark_cluster1.JPG){#fig:spark-cluster1}

![Spark Cluser](images/spark_cluster2.JPG){#fig:spark-cluster2}

![Spark Cluser](images/spark_cluster3.JPG){#fig:spark-cluster3}
