# Python Libcloud

With all the cloud providers and cloud services that are currently 
available, it becomes hard to manage and maintain services that work 
with several services. Therefore it is good to have a unified service 
that allows developers to access many of the cloud services through a 
single abstraction. Apache Libcloud is a python library that was 
developed for this purpose. Apache Libcloud provides a unified API for 
many of the popular cloud providers and services.
 
 
Apache Libcloud currently supports many providers, the complete list
of providers that are supported can be found at
[Supported Providers](https://libcloud.readthedocs.io/en/latest/supported_providers.html)
 
However, it is good to keep in mind that the Libcloud API might not
support some of the advanced features that are provided by some cloud 
services or some of the most recent features that are yet to be 
integrated into Libcloud

## Service categories

Libcloud provides many services and defines several categories to
distinguish between the main types of services. The list of categories
is as bellow, More details about this list can be found at
[Categories](https://libcloud.readthedocs.io/en/latest/index.html) The
list is extracted from the LibCloud documentation
[LibCloud Docs](https://libcloud.readthedocs.io/en/latest/index.html)

* Cloud Servers and Block Storage - services such as Amazon EC2 and 
  Rackspace CloudServers
* Cloud Object Storage and CDN - services such as Amazon S3 and 
  Rackspace CloudFiles
* Load Balancers as a Service - services such as Amazon Elastic 
  Load Balancer and GoGrid LoadBalancers
* DNS as a Service - services such as Amazon Route 53 and Zerigo
* Container Services - container virtualization like Docker and Rkt as
  well as container based services
* Backup as a Service - services such as Amazon EBS and OpenStack Freezer

each category has a set of terms that represent various constructs and
services. For example the following list is the list of terms used in
for Compute related services, this list is extracted from the
[Compute docs](https://libcloud.readthedocs.io/en/latest/compute/index.html)

#### Compute

* Node - represents a cloud or virtual server.
* NodeSize - represents node hardware configuration. Usually this is
  amount of the available RAM, bandwidth, CPU speed and disk size. 
  Most of the drivers also expose an hourly price (in dollars) for 
  the Node of this size.
* NodeImage - represents an operating system image.
* NodeLocation - represents a physical location where a server can be.
* NodeState - represents a node state. Standard states are: running, 
rebooting, terminated, pending, stopped, suspended, paused, erro, unknown.

#### Key Pair Management

* KeyPair - represents an SSH key pair object.

#### Block Storage

* StorageVolume - represents a block storage volume
* VolumeSnapshot - represents a point in time snapshot of a StorageVolume

You can find more complete information on Libcloud in the official
documentations, this article will only provide a brief summary in most
part:
[Apache Libcloud Documentaions](https://libcloud.readthedocs.io/en/latest/index.html)

## Installation

Libcloud can be installed via pip. Execute the following command in order
to install Libcloud

```console
pip install apache-libcloud
```

## Quick Example

The following basic example shows you how the Python Libcloud library
can be used to access information in a cloud provider

```code
from pprint import pprint

import libcloud

cls = libcloud.get_driver(
    libcloud.DriverType.COMPUTE,
    libcloud.DriverType.COMPUTE.OPENSTACK)

driver = cls('username', 'api key')

pprint(driver.list_sizes())
pprint(driver.list_nodes())
```

## Working with cloud services

In the following section we will look into how Libcloud can be used to
perform various functions in specific cloud providers. One of the main
aspects that change between different cloud providers is how
authentication is done. Because of the unified API most of the other
features are executed in the same manner.

### Authenticating with cloud providers

Depending on the cloud provider, how Libcloud is granted access to
your cloud account may differ, next we will look at some such examples

There are two main steps that are common to all providers

1. Using the get_driver() method to obtain a reference to the cloud
   provider driver
2. Instantiating the driver with the credentials to access the cloud

After you obtain the connection, it can be used to invoke various services



#### Amazon AWS

Authentication is performed for AWS as follows

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)
```

#### Azure

Authentication is performed for Azure as follows

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Azure related variables

AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
conn = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)
``` 

#### OpenStack

Authentication is performed for OpenStack as follows

```Python
from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider

OpenstackDriver = get_driver(Provider.OPENSTACK)

#OpenStack related variables

OPENSTACK__AUTH_USERNAME = 'your_user_name'
OPENSTACK_AUTH_PASSWORD = 'your_auth_password'

conn = OpenStack(OPENSTACK__AUTH_USERNAME, OPENSTACK_AUTH_PASSWORD',
                   ex_force_auth_url='http://192.168.1.101:5000',
                   ex_force_auth_version='2.0_password')
```


### Invoking services
 
In this section we will look into how we can use the connection
created as instructed above to perform various services such as
creating nodes, listing nodes, starting nodes and stopping nodes.

Appropriate authentication code as described in the previous section
is assumed. This will give us an variable named conn which we will use
for invoking Services. It is in the next sections not explicitly
listed.  It is indicated by our ... at the beginning

#### Creating Nodes

In this section we will look at the code that can be used to create a
node in the provider a node which represents a virtual server

```Python
...
# retrieve available images and sizes
images = conn.list_images()

sizes = conn.list_sizes()

# create node with first image and first size
node = conn.create_node(name='yourservername', image=images[0], size=sizes[0])
```

#### Listing Nodes

In this section we will look at the code that can be used to list the
nodes that have been created in the provider

```Python
...
nodes = conn.list_nodes()
print nodes
```

#### Starting Nodes

After the node (Virtual server) has been created the following code can
be used to start the node

```Python
...
nodes = conn.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
conn.ex_start(node=node)
```

#### Stoping Nodes

When needed the following command can be used to stop a node that has 
been started

```Python
...
nodes = conn.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
conn.ex_stop(node=node)
```

## Cloudmesh Community Program to Manage Clouds

As you have noticed since the authentication can change from cloud
services to cloud service it would be much easier to use a simple
python script to automatically handle the differences in the code.

We have provided such a python script which you can leverage to manage
different cloud providers. You can find the python script and the
corresponding .yaml file in the cloudmesh-community github repository.

* Python Script - <https://github.com/cloudmesh-community/cm/blob/master/cm.py>
* Yaml File - <https://github.com/cloudmesh-community/cm/blob/master/cloudmesh.yaml>

When using the script and yaml file please keep in mind the
following steps to make sure you do not share your private keys and
passwords on your publicly accessible Github account.

1. Create a folder in your computer that is not within a git clone
   that you have made. For example maybe you can use a new directory
   on your desktop

2. Copy the cm.py and `cloudmesh.yaml` files into this folder. Just to
   make sure you are not working with the files under the git repo you
   should delete the cloudmesh.yaml file in that is in your local git
   repo.

3. change the needed fields in the yaml file and use the python script
   to access the cloud services using libcloud.

To illustrate how simple the program is and that it significantly
improves your management of credentials we provide the follwoing
code:

```
from cm import cloudmesh

cm = cloudmesh()
cm.config()
driver = cm.get_driver("aws")
print("driver=", driver)
```

To switch to a different cloud, you just have to create it in the yaml
file and use that name.

It will be your task to add more providers to it.

We intent to host the code sometime soon on pypi so you can issue the
command

```
pip install cm-community
```

and this library will be installed for you.


## Amazon Simple Storage Service S3 via libcloud :hand:

Next we explain how to use Amazon Web Services (AWS) S3 via
libcloud. Apache libcloud is a python library that provides
abstraction layer and hides the complexities of directly integrating
with AWS API's, for that matter it allows you to do so for different
cloud providers. In the sections below more detailed steps are shown
to install and use libcloud for AWS S3.

	
### Access key

To be able to access AWS S3 from libcloud we need the access key to be
specified in the call.  Access key can be setup on AWS console by
navigating to `My Security credentials->Encryption Keys->Access Keys`.


### Create a new bucket on AWS S3

In S3 you first need to create a bucket which is nothing but a
container where you store your data in the form of files. This is
where you can also define access controls.

- Click on S3 link on the AWS console under storage section, this will
  bring you to the create bucket window.
- Click on "Create Bucket" button, this opens up a wizard.
- Answer all mandatory questions on each page.
- Important point here is to note the "Bucket Name" and the "Region"
  you are creating this bucket in, as this information will be used
  while calling the API.

### List Containers

List Containers function list all the containers of buckets available
for the user in that particular region.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver


	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')
 
	d = driver.list_containers();

	print d;


### List container objects

List container objects function shows the list of all objects in that
container. Please note the output could be large depending on the
files present in the bucket.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver
	
	# Note I have used S3_US_EAST2 as this is the
    # "region" where my S3 bucket is located.

	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')
	
	container = driver.get_container(container_name='<bucket name>')
	
	d = driver.list_container_objects(container);
	
	print d;

### Upload a file

Upload a file helps in uploading a local file to S3 bucket.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver

	FILE_PATH = '/<file path>/<filename>'

    # Note I have used S3_US_EAST2 as this is
    # the "region" where my S3 bucket is located.

	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')

	container = driver.get_container(container_name='<bucket name>')

    extra = {'meta_data': {
        'owner': '<owner name>',
        'created': '2018-03-24'}}

	with open(FILE_PATH, 'rb') as iterator:
    obj = driver.upload_object_via_stream(
        iterator=iterator,
        container=container,
        object_name='backup.tar.gz',
        extra=extra)


### References

* https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html
* Documentation about libcloud can be found at <https://libcloud.readthedocs.org>

    * storage driver <http://libcloud.readthedocs.io/en/latest/_modules/libcloud/storage/drivers/s3.html>
    * Examples: <https://libcloud.readthedocs.io/en/latest/storage/examples.html>
    * API docs<http://libcloud.apache.org/apidocs/0.6.1/libcloud.storage.base.StorageDriver.html>


