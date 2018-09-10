# Python Libcloud
With all the cloud providers and cloud services that are currently 
available, it becomes hard to manage and maintain services that work 
with several services. Therefore it is good to have a unified service 
that allows developers to access many of the cloud services through a 
single abstraction. Apache Libcloud is a python library that was 
developed for this purpose. Apache Libcloud provides a unified API for 
many of the popular cloud providers and services.
 
 
Apache Libcloud currently supports many providers, the complete list of 
providers that are supported can be found at [Supported Providers](https://libcloud.readthedocs.io/en/latest/supported_providers.html)
 
However, it is good to keep in mind that the Libcloud API might not
support some of the advanced features that are provided by some cloud 
services or some of the most recent features that are yet to be 
integrated into Libcloud

## Service categories

Libcloud provides many services and defines several categories to 
distinguish between the main types of services. The list of categories 
is as bellow, More details about this list can be found at [Categories](https://libcloud.readthedocs.io/en/latest/index.html)
The list is extracted from the LibCloud documentation [LibCloud Docs](https://libcloud.readthedocs.io/en/latest/index.html)

* Cloud Servers and Block Storage - services such as Amazon EC2 and 
Rackspace CloudServers
* Cloud Object Storage and CDN - services such as Amazon S3 and 
Rackspace CloudFiles
* Load Balancers as a Service - services such as Amazon Elastic 
Load Balancer and GoGrid LoadBalancers
* DNS as a Service - services such as Amazon Route 53 and Zerigo
* Container Services - container virtualization like Docker and Rkt 
as well as container based services
* Backup as a Service - services such as Amazon EBS and OpenStack Freezer

each category has a set of terms that represent various constructs and
services. For example the following list is the list of terms used in
for Compute related services, this list is extracted from the [Compute docs](https://libcloud.readthedocs.io/en/latest/compute/index.html)

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
part: [Apache Libcloud Documentaions](https://libcloud.readthedocs.io/en/latest/index.html)

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
aspects that change between different cloud providers is how authentication
is done. Because of the unified API most of the other features are
executed in the same manner.

### Authenticating with cloud providers
Depending on the cloud provider, how Libcloud is granted access to your
cloud account may differ, below we will look at some such examples

There are two main steps that are common to all providers

1. Using the get_driver() method to obtain a reference to the cloud 
provider driver
2. Instantiating the driver with the credentials to access the cloud

After you obtain the connection, it can be used to invoke various services



#### Amazon AWS
Below is how authentication is performed for AWS 

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)
```

#### Azure
Below is how authentication is performed for Azure 

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
conn = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)
``` 

### Invoking services
 
In this section we will look into how we can use the connection created
as instructed above to perform various services such as creating nodes,
listing nodes, starting nodes and stopping nodes.

Appropriate authentication code as described in the previous section  is assumed. This will give us an variable named conn which we will use for invoking Services. It is in the next sections not explicitly listed.

#### Creating Nodes

:o: text missing

```Python
# retrieve available images and sizes
images = conn.list_images()

sizes = conn.list_sizes()

# create node with first image and first size
node = conn.create_node(name='yourservername', image=images[0], size=sizes[0])
```

#### Listing Nodes

:o: text missing

```Python
nodes = conn.list_nodes()
print nodes
```

#### Starting Nodes

:o: text missing


```Python
nodes = conn.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
conn.ex_start(node=node)
```

#### Stoping Nodes

:o: text missing

```Python
nodes = conn.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
conn.ex_stop(node=node)
```

