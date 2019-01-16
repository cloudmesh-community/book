# Amazon Web Services {#sec:aws}

## AWS Products

Amazon Web Services offers a large number of products that are
centered around their cloud services. These services have grown
considerably over the years from the core offering related to virtual
machine (EC2) and datastorage (S3). An overview of them is provided by
Amazon in the following document:

* <https://d0.awsstatic.com/whitepapers/aws-overview.pdf>

We list the product in screenshots from their Product Web page panel
in Figure below: +@fig:aws-products1, +@fig:aws-products.

![AWS Products](images/aws-products-1.png){#fig:aws-products1}
![AWS Products](images/aws-products-2.png){#fig:aws-products}



Service offerings are grouped by categories:

* Compute
* Storage
* Database
* Migration
* Networking and Content Delivery
* Developer Tools
* Management Tools
* Media Services
* Machine Learning
* Analytics
* Security and Identity Compliance
* Mobile Services
* AR and VR
* Application Integration
* Customer Engagement
* Business Productivity
* Desktop and App Streaming
* Internet of Things
* Game Development
* Software
* Aws Core Management

Within each category you have several products. When choosing products
form AWS it is best to start with the overview paper and identify
products that can be of benefit to you. For our purpose we focus on
the traditional Compute and Storage offerings. We list the products
that are available In Sep. 2018 next.

###  Virtual Machine Infrastructure as a Services

Amazon offers a large number of services relatesd to virtual machine
management


* [Amazon EC2](https://aws.amazon.com/ec2/?nc2=h_mo)
* [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/?nc2=h_mo)

### Container Infrastructure as a Service

Amazon offers the following container based services

* [Amazon Elastic Container Service](https://aws.amazon.com/ecs/?nc2=h_mo)
* [Amazon Elastic Container Service for Kubernetes](https://aws.amazon.com/eks/?nc2=h_mo)
* [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/?nc2=h_mo)

### Serverless Compute using AWS Lambda

 In addition to these services a number of additional compute services
Serverless computing or FaaS is a new cloud computing paradigm that
has are offered which you can find in the Appendix. This includes
gained popularity recently.  Serverless Computing with AWS Lambda.
Serverless computing or Function as a Service (FaaS) is a new cloud
computing paradigm that has gained popularity recently. AWS Lambda was
one of the first serverless computing services that was made available
to the public, Serverless computing allows users to run small
functions in the cloud without having to worry about resource
requirements. More information regarding AWS Lambda can be found in
the following document

* <https://aws.amazon.com/lambda/>

### Serverless Compute using AWS Lambda

Serverless computing or FaaS is a new cloud computing paradigm that has
gained popularity recently.




### Storage

AWS provides many storage services that users can leverage for developing
applications and solutions. The list below showcases AWS storage
services. Amazon offers the following storage services

* [Amazon Simple Storage Service
(S3)](https://aws.amazon.com/s3/?nc2=h_mo)
* [Amazon Elastic Block Store (EBS)](https://aws.amazon.com/ebs/?nc2=h_mo)
* [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/?nc2=h_mo)
* [Amazon Glacier](https://aws.amazon.com/glacier/?nc2=h_mo)
* [AWS Storage Gateway](https://aws.amazon.com/storagegateway/?nc2=h_mo)
* [AWS Snowball](https://aws.amazon.com/snowball/?nc2=h_mo)
* [AWS Snowball Edge](https://aws.amazon.com/snowball-edge/?nc2=h_mo)
* [AWS Snowmobile](https://aws.amazon.com/snowmobile/?nc2=h_mo)
* [AWS
Marketplace](https://aws.amazon.com/marketplace/b/2649337011/ref=mkt_ste_l2_S3CDN?page=1&category=2649337011&nc2=h_mo)

### Databases


AWS also provides many data base solutions. AWS has both SQL based
databases and NoSQL based databases. The list below shows the database
services that AWS offers. And other database related services

* [Amazon Aurora](https://aws.amazon.com/rds/aurora/?nc2=h_mo)
* [Amazon RDS](https://aws.amazon.com/rds/?nc2=h_mo)
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?nc2=h_mo)
* [Amazon ElastiCache](https://aws.amazon.com/elasticache/?nc2=h_mo)
* [Amazon Redshift](https://aws.amazon.com/redshift/?nc2=h_l3_db)
* [Amazon Neptune](https://aws.amazon.com/neptune/?nc2=h_mo)
* [AWS Database Migration Service](https://aws.amazon.com/dms/?nc2=h_mo)
* [AWS
Marketplace](https://aws.amazon.com/marketplace/search/results/ref=mkt_ste_l2_database_category?page=1&category=2649364011&nc2=h_mo)




## Locations
As the following figure shows: +@fig:aws-locations.

![AWS-Locations](images/aws-locations.png){#fig:aws-locations}




## Creating an account

In order to create a AWS account you will need the following

* A valid email address
* A credit/debit card
* A valid phone number

First you need to visit the AWS
[signup page](https://aws.amazon.com/free/) and click "Create Free
Account". You will then be asked to provide some basic details
including your email address as shown in the image below: +@fig:aws-signup.

![AWS Signup](images/aws_signup_page.png){#fig:aws-signup}

Next you will be asked to provide further details such as your name,
address and phone number. After the additional details have been
provided. AWS will ask for credit/debit card details as shown below: +@fig:payment-information.
They require this information to verify your identity and make sure
they have a method to charge you if needed. However no charges will be
applied to your credit/debit card unless you use the AWS services and
exceed the free tier limits, which will be discussed in the next
section.

![Payment Information](images/creditcard_details.png){#fig:payment-information}

After the credit/debit card has been verified AWS will use your phone
number to verify your identity. Once you are logged into your account
you will be able to sign into the console, from the link on the top
right corner in your account. Once you are in the AWS console the
services tab in the left top corner will allow you to access all the
services that are available to you through AWS as shown in the image
below: +@fig:aws-console.

![AWS Console](images/aws_console.png){#fig:aws-console}

## AWS Command Line Interface

### Introduction

Amazon's CLI allows for programatic interaction with AWS product through the command line. CLI provide many pre-built functions that allow for interaction with Amazon's Elastic Compute Cloud (EC2) instances and S3 storage.

### Prerequisites
* [Linux](https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md)
* [Python](https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-install.md)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [AWS Account](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account)
* [AWS Key Pair](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#setting-up-key-pair)

#### Install CLI
Run the follwoing code to install CLI.

```bash
pip install awscli
```

#### Configure CLI
Using the following code to configure AWS using. You will need to specify four parameters:

1. AWS Access Key ID
2. AWS Secret Access Key
3. Default region name (this is the default region that will be used when you create EC2 instances)
4. Default output format (the default format is json)

```bash
aws configure
```

## AWS Admin Access

### Introduction
In order to access various AWS functionality remotely (through command-line) you must enable administrative access.

### Prerequisites

* [Set up AWS account](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account)

* [Install and configure AWS CLI](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#aws-command-line-interface)

* [Linux environment](https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md)

* [AWS Key Pair](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#setting-up-key-pair)

### Setting up admin access using AWS CLI

#### Create an admin security group

```bash
aws iam create-group --group-name Admins
```

#### Assign a security policy to the created group granting full admin access

```bash
aws iam attach-group-policy --group-name Admins --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

## Understanding the free tier

AWS provides a set of services free of charge. These free services are
to allow new users test and experiment with various AWS services
without worrying about any cost. Free services are provided as a
product that is free until a certain amount of usage, that is if you
exceed those limits you will be charged for the additional usage.
However the free quotas are typically more than sufficient for testing
and learning purposes. For example under the free tier you are able to
use 750 hours of EC2 resources per month for the first 12 months after
account creation. However it is important to make note of important
details that are included in the limits. For example for the 750 hours
of free EC2 usage, you can only use "EC2 Micro" instances, using any
other instance type for your EC2 machine will not fall under the free
tier agreement and you will be charged for them, see picture below: +@fig:free-tier. To view all the AWS
free tier details visit [AWS Free Tier](https://aws.amazon.com/free/)

![Free tier](images/freetier.png){#fig:free-tier}

Basically there are two categories in the free tier,

* 12 months free
* Always free

12 months free offer are only good for the first 12 months after you
create your AWS account. The always free offer are valid even after
the first 12 months.

## Important Notes

:warning: When using AWS services make sure you understand how and when you will
be charged for. For example if you are using an EC2 to run some
application, usage of the instance will be calculated from the time
you started the instance to the time you stop or terminate the
instance. So even if you do not use the application itself, if you are
have the instance in an active mode that will be added to the usage
hours and you will be billed if you exceed the 750 hour limit. In EC2
even if you stop the instance you might be charged for data that is
stored in the instance so terminating it would be the most safest
option if you do not have any important data stored in the instance.
You can look up other such tricky scenarios at
[Avoiding Unexpected Charges](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/checklistforunwantedcharges.html)
to make sure you will not get an unexpected bill


## Introduction to the AWS console

As we discussed previously we can access all the service and product
offerings that are provided by AWS from the AWS console. In the
following section we will look into how we can start and stop a
virtual machine using AWS EC2 service. Please keep in mind that this
will reduce time from your free tier limit of 750 hours/month, So be
careful when starting EC2 instances and make sure to terminate them
after you are done.

### Starting a VM

To go to the EC2 services you can click on the services link on the
top left corner in the console and then click on EC2 which is listed
under "Compute". Then you will see a blue button labeled "Launch
instance". Click on the button and the console will take you to the
page shown below: +@fig:launch-instance. Notice that the check box for "Free tier only" is
clicked to make sure the instance type we choose is eligible for the
free tier hours. The instance type you select defines the properties
of the virtual machine you are staring such as RAM, Storage,
processing power. However since we are using instance that are free
tier eligible we will only be able to use "EC2 Micro instances". You
can also select a OS that you want to be started as the virtual
machine. We will select "Ubuntu Server 16.04 LTS" as our Operating
system. press the blue select button to do so.

![Launch Instance](images/launch_instance.png){#fig:launch-instance}

Once you select the OS type you will be asked to select the instance
type. You can notice that only the "t2.micro" is marked as free tier
eligible as shown in the image below: +@fig:instance-type. Now that you have selected all
the basic details press the "Review and Launch" button located in the
button right corner. This will give you a summary of your current
selections.

![Instance Type](images/instance_type.png){#fig:instance-type}

#### Setting up key pair

Before we can launch the VM we need to perform one more step. We need
to setup a SSH key pair for the new VM. Creating this will allow us to
access our VM through SSH. Once you click on the launch button, you
will get the following dialog box: +@fig:key-pair. If you already have a worked with
SSH keys and if you already have a key pair you can use it, otherwise
you can create a new key pair as we will do. To create a new key pair
select the "Create a new key pair" in the first drop down box and
enter a name of your choosing as the name. Next you need to download
and save the private key, Keep the private key in a safe place and do
not delete it since you will need it when you are accessing the VM
(This tutorial will not cover accessing the VM through SSH but you
need to keep the private key so you can use the same key value pair
later). Once you have downloaded the private key, the "Launch
Instance" button will activate. Press this button to start the VM.

![Key Pair](images/keypair.png){#fig:key-pair}

After starting the instance go back to the EC2 dashboard ( Services ->
EC2). Now the dashboard will show the number of running instance as
shown in the image below: +@fig:running-instance1. If you do not see is initially, refresh the
page after a little while, starting the VM may take a little time so
the dashboard will not be updated until the VM starts.

![Running Instance1](images/running_instance.png){#fig:running-instance1}

Now to get a more detailed view click on the "Running Instances" link.
This will give you the following view: +@fig:running-instance2. Is shows the current instance
that you are running

![Running Instance2](images/running_instance2.png){#fig:running-instance2}

### Stopping a VM

In AWS EC2 you can either stop a VM or terminate it. If you terminate
it you will loose all the data that was stored in the VM as well,
simply stopping will save the data for future use if you restart the
instance again. In order to stop the VM you can select the VM machines
you want to stop from the GUI and go to "Actions -> Instance status"
and click on stop: +@fig:instance-stop. This will stop your VM machine.

![Instance Stop](images/instance_stop.png){#fig:instance-stop}

After a little while the dashboard will show the instance as stopped as the following: +@fig:stopped-instance.
If you want to go further and terminate the instance you can again go
to "Actions -> Instance status" and select terminate, which will
terminate the VM.

![Stopped Instance](images/stopped_instance.png){#fig:stopped-instance}

## Access from the Command Line

AWS also provides an command line interface that can be used to manage
all the AWS services through simple commands. below are two example
commands.

	aws s3 <Command> [<Arg> ...]
	aws ec2 <Command> [<Arg> ...]

You can find more information regarding the AWS CLI in the following
documents.

* AWS Command Line: <https://aws.amazon.com/cli/>
* AWS Command Line reference:
  <https://docs.aws.amazon.com/cli/latest/reference/>
* EC2:
  <https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html>
* S3: <https://docs.aws.amazon.com/cli/latest/reference/s3/index.html>

Amazon Web Services (AWS) is a cloud platform that provides a large
number os services for individuals and enterprises. You can get an
overview of the AWS offering at
[Amazon Web Services Overview](aws.md). This section will guide
through the processes of creating an AWS account and explain the free
tier details so that you can leverage the tools and products available
in AWS for your work and research.


## Access from Python


## Boto

Boto is a Python software development kit specifically targeting
Amazon Web Services (AWS). It allows access to services such as S3 and
EC2. It is using object oriented programming paradigms ta access the
lower level services. The advantage is that it is written just for
Amazon and thus we assume it will be developed with high quality due
to its specialization. However this is also its limitation as in
contrast to libcloud it does not support other cloud providers. Hence
it bares the risk of vendor lockin. Boto is maintained in github.

Documentation about boto can be found at

* <https://boto3.readthedocs.io/en/latest/>
* <https://github.com/boto/boto3>


## libcloud

"Libcloud is a Python library for interacting with many of the popular
cloud service providers using a unified API. It was created to make it
easy for developers to build products that work between any of the
services that it supports." A more detailed description on Libcloud and
how you can use it to connect with AWS is provided in the Section
[Python libcloud](#python-libcloud).

For more information about the features and supported providers, please
refer to the [documentation](https://libcloud.readthedocs.org/en/latest/)
