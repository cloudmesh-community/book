Python Libcloud
---------------

### Install

    pip install apache-libcloud

### Disadvantage

Some advanced cloud features do not work.

### Quick example

    from pprint import pprint

    import libcloud

    cls = libcloud.get_driver(
        libcloud.DriverType.COMPUTE,
        libcloud.DriverType.COMPUTE.OPENSTACK)

    driver = cls('username', 'api key')

    pprint(driver.list_sizes())
    pprint(driver.list_nodes())

### Providers

-   [List of  Providers](https://libcloud.readthedocs.io/en/latest/supported\_providers.html)
-   [Azure](https://libcloud.readthedocs.io/en/latest/compute/drivers/azure.html),
    [Azure](https://libcloud.readthedocs.io/en/latest/compute/drivers/azure_arm.html)
-   [AWS EC2](https://libcloud.readthedocs.io/en/latest/compute/drivers/ec2.html)
-   [Google Compute Engine](https://libcloud.readthedocs.io/en/latest/compute/drivers/gce.html)
-   [OpenStack](https://libcloud.readthedocs.io/en/latest/compute/drivers/openstack.html)
-   [libvirt](https://libvirt.org/)

### Features

-   https://libcloud.readthedocs.io/en/latest/supported\_providers.html

    Provider    list nodes  create node reboot node destroy node    list images list sizes  deploy node
    Azure Virtual machines  yes yes yes yes yes yes yes
    Amazon EC2  yes yes yes yes yes yes yes
    Google Compute Engine   yes yes yes yes yes yes no
    Libvirt yes no  yes yes no  no  no
    OpenStack   yes no  yes yes yes yes no

    add trystack

### Compute

https://libcloud.readthedocs.io/en/latest/compute/index.html\#terminology

Compute

Node - represents a cloud or virtual server. 

NodeSize - represents node
hardware configuration. Usually this is amount of the available RAM,
bandwidth, CPU speed and disk size. Most of the drivers also expose an
hourly price (in dollars) for the Node of this size. 

NodeImage -
represents an operating system image. 

NodeLocation - represents a
physical location where a server can be. 

NodeState - represents a node
state. Standard states are: running, rebooting, terminated, pending,
stopped, suspended, paused, error, unknown.

Security

KeyPair - represents an SSH key pair object.

Block Storage

StorageVolume - represents a block storage volume VolumeSnapshot -
represents a point in time snapshot of a StorageVolume

### Pricing

https://libcloud.readthedocs.io/en/latest/compute/pricing.html

out of date

Currently only way to update pricing is programmatically using
libcloud.pricing.download\_pricing\_file() function. By default this
function retrieves the latest pricing file from our git repository and
saves it to \~/.libcloud.pricing.json

Custom pricing

Exercise: write prising fetcher with beautiful soap

### Deployment

TBD

### keypair

https://libcloud.readthedocs.io/en/latest/compute/key\_pair\_management.html

### Data

#### Providers

-   Google cloud storage
-   Azure Blobs
-   Local Storage
-   OPenstack swift
-   Amazon S3
-   Ceph

#### Object Storage

https://libcloud.readthedocs.io/en/latest/storage/index.html

https://libcloud.readthedocs.io/en/latest/storage/examples.html

### Examples

https://libcloud.readthedocs.io/en/latest/compute/examples.html

### API

https://libcloud.readthedocs.io/en/latest/compute/api.html

\#\#Load balancers

-   Amazon application load balancing
-   Amazon Elastic load balancer
-   google compute load balancer
-   softlayer loadbalancer (? ibm)

### DNS as a Service

We will not discuss

https://libcloud.readthedocs.io/en/latest/dns/index.html

### Container

https://libcloud.readthedocs.io/en/latest/container/index.html

https://libcloud.readthedocs.io/en/latest/container/supported\_providers.html

docker amazon google kubernetes rancher joynet?
