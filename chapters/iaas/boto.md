# AWS Boto :hand:


Boto is a software development kit (SDK) that provides AWS interface for Python applications. It enables to write applications in Python that make use of Amazon Web Services.


Boto supports different AWS services such as, Elastic Compute Cloud (EC2),
DynamoDB, AWS Config, CloudWatch and Simple Storage Service (S3).

In contrast to libcloud it only focusses to support AWS.

## Boto versions

The current version of Boto is Boto3 and is available from:

* <https://github.com/boto/boto3>

The documentation from amazon is provided here:

* <http://aws.amazon.com/sdk-for-python>

It supports Python versions 2.6.5, 2.7 and 3.3+.



## Boto Installation


To install boto with its latest release, use

```bash
$ pip install boto3
```
    
To install boto from source, use 

```bash
$ git clone https://github.com/boto/boto3.git
$ cd boto3
```

Before you install it we suggest that you either use pyenv or venv.

```bash
$ python setup.py install
```

To install additional modules to use boto.cloudsearch, boto.manage, boto.mashups
and to get all modules required for test suite, than the run command

```bash
$ python setup.py install
```

## Access key

An initial setup is required to be able to access AWS EC2 from BOTO wherein you provide the key and region details. 
You can find the key details from IAM console on AWS.
	
## BOTO configuration

BOTO can be configured in two ways, either by using the aws configure command if you have AWS Command line interface installed or simply by manually creating and editing the `~/.aws/credentials` file to include below parameters.

```python
[default]
aws_access_key_id = <YOUR_ACCESS_KEY>
aws_secret_access_key = <YOUR_SECRET_KEY>
```

Similar to libcloud, BOTO also requires the region where you would create your EC2 instance, the same can be maintained by creating a config file.

```bash
	$ emacs .aws/config
	[default]
	region=<region name> # for example us-east
```

## EC2 interface of Boto


####  Create connection 

To access EC2 instance, first import the required package.

```python
import boto3.ec2
```

Make a connection to from application by specifying AWS region in which the user
account is created, aws access key and secret key. AWS provides access key and
secret key when a new user is created. Access key and secret key helps to
identify the user.

```python
connection = boto3.ec2.connect_to_region('<region name>', aws_access_key_id =
'<access key>', aws_secret_access_key = '<secret key'>)
```

connection object now points to EC2Connection object returned by the function `connect_to_region`.

List EC2 instances
---------------

The code to list the running instances (if you have some) is very simple:

```python
import boto3
	
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
```
	
#### Launch a new instance

To launch a new instance with default properties

```python
connection.run_instances('<ami-id>')
```

Additional parameters can be specified to create instance of specific type and
security group.

```python
connection.run_instances('<ami-id>',key_name='<key>', instance_type='<type>',
security_groups=['<security group list>'])
```

Instance type specifies the storage and type of platform. Secutity groups are
required to provide access rights such as access to SSH into the instance.

#### Check running instances

The `get_all_reservations` function of EC2Connection object will return list of
running instances.

```python
reservations = connection.get_all_reservations()
instances = reservations[0].instances
```


#### Stop instance

Up and running instances can be stopped. Thw `stop_instances` function of connection
object enables multiple instances to be stopped in one command.

```python
connection.stop_instances(instance_ids=['<id1>','<id2>', ...]) 
```

#### Terminate instance

To terminate one or more instances simultaneously, use the `terminate_instances`
function.

```python
connection.terminate_instances(instance_ids=['<id1>','<id2>', ..]) 
```

### Reboot instances

The next example showcases how to reboot an instance, which is copied from  <http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html>

```python
# Code copied form 
# http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html
import boto3
from botocore.exceptions import ClientError
	
ec2 = boto3.client('ec2')
	
try:
    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise
try:
    response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)
```

## Amazon S3 interface of Boto


####  Create connection 

Import required packages

```python
import boto3.s3
from boto3.s3.key import Key
```

Create a connection 

```python
connection = boto.connect_s3('<access-key>','<secret-key>')
```


#### Create new bucket in S3

Amazon S3 stores all its data in Bucket. There is no limitation specified by AWS
about number of data files allowed per bucket.

Bucket name has to be unique name accross all the AWS regions and hence globally
unique.

```python
bucket = conn.create_bucket('<bucket_name>')
```

If bucket name is unique, a new bucket of specified name will get created.
If bucket name is not unique, application will throw error as

```python
boto.exception.S3CreateError: S3Error[409]: Conflict
```

#### Upload data

To upload a file in the S3 bucket, first create a key object from new_key()
function of bucket.

```python
key = bucket.new_key('hello2.txt')
key.set_contents_from_string('Hello World!')
```

This will create hello.txt file with content Hello World! in the text file. This
file can be found inside the bucket in which new key is created.


#### List all buckets

One account can have maximum 100 buckets in which data objects can be stored. 

```python
result = connection.get_all_buckets()
```
    
The `get_all_buckets` function of S3Connection lists all the buckets within account.
It returns ResultSet object which has list of all buckets.
    
 

#### List all objects in a bucket

Data objects stored in a bucket has a metadata associated with it such as
LastModified date and time. This information can also be captured.

```python
# To list files in selected bucket
for key in bucket.list():
    print "{name}".format(name = key.name)
    print "{size}".format(size = key.size)
    print "{modified}".format(modified = key.last_modified)
```

#### Delete object

To delete any data object from bucket, delete_key function of bucket is used. 

```python
k = Key(<bucket-name>, <file-name>)
k.delete()
```

#### Delete bucket

To delete a bucket, provide a bucket name and call the `delete_bucket` function of
S3Connection object.

```python
connection.delete_bucket('<bucket-name>') 
```

## References 

* <https://github.com/boto/boto3>
* <https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation>
* <http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html>

## Excersises


E.boto.cloudmesh.1:

> will will nw create a cloudmesh tool that manages virtual machines on the commandline. For that we copy the code published at 

> * <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html>. 

> Modify this code using docopts and look at samples in 
> 
> * <https://github.com/cloudmesh-community/cm>

> where we use libcloud. The code from Amazon is.  

```python
import sys
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
```
        
E.boto.cloudmesh.2:

> Integrate, start, stop, rebot, and other useful functions

E.boto.cloudmesh.3:

> Discuss the advantages of docopts.
