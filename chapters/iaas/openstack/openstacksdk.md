# OpenStackSDK {#sec:openstacksdk}



## Introduction

OpenStackSDK is a new API to interface with openstack from python Older
libraries provide an API for each component, such as nova, keystone and
others. OpenStackSDK attempts to unify the APIs into a single API.

The user documentation is provided at 

* <https://docs.openstack.org/openstacksdk/latest/user>

## Instalation

Openstacksdk can easily installed with pip as follows

```bash
$ pip install openstacksdk
```

## Data Model

Openstacksdk provides a data model that is documented at 

* <https://docs.openstack.org/openstacksdk/latest/user/model.html>

In this data model you will find data structures for abstractions relatting to 

* [Location](https://docs.openstack.org/openstacksdk/latest/user/model.html#location)
* Resources

  * [Flavor](https://docs.openstack.org/openstacksdk/latest/user/model.html#flavor)
  * [Flavor Access](https://docs.openstack.org/openstacksdk/latest/user/model.html#flavor-access)
  * [Image](https://docs.openstack.org/openstacksdk/latest/user/model.html#image)
  * [KeyPair](https://docs.openstack.org/openstacksdk/latest/user/model.html#keypair)
  * [SecurityGroup](https://docs.openstack.org/openstacksdk/latest/user/model.html#security-group)
  * [SecurityGroupRule](https://docs.openstack.org/openstacksdk/latest/user/model.html#security-group-rule)
  * [Server](https://docs.openstack.org/openstacksdk/latest/user/model.html#server)  
  * [ComputeLimits](https://docs.openstack.org/openstacksdk/latest/user/model.html#computelimits)
  * [ComputeUsage](https://docs.openstack.org/openstacksdk/latest/user/model.html#computeusage)
  * [ServerUsage](https://docs.openstack.org/openstacksdk/latest/user/model.html#serverusage)
  * [FloatingIP](https://docs.openstack.org/openstacksdk/latest/user/model.html#floating-ip)
  * [Volume](https://docs.openstack.org/openstacksdk/latest/user/model.html#volume)
  * [VolumeType](https://docs.openstack.org/openstacksdk/latest/user/model.html#volumetype)
  * [VolumeTypeAccess](https://docs.openstack.org/openstacksdk/latest/user/model.html#volumetypeaccess)
  * [ClusterTemplate](https://docs.openstack.org/openstacksdk/latest/user/model.html#clustertemplate)
  * [MagnumService](https://docs.openstack.org/openstacksdk/latest/user/model.html#magnumservice)
  * [Stack](https://docs.openstack.org/openstacksdk/latest/user/model.html#stack)
  * [Project](https://docs.openstack.org/openstacksdk/latest/user/model.html#project)
  * [Role](https://docs.openstack.org/openstacksdk/latest/user/model.html#role)
 
Please note that access to these API could be restricted based on the
role you have n ths OpenStack cloud.
  
## Conection

The first activity you need to conduct is to connect to the cloud. We
provide here an example for chameleon cloud while assuming you are using
the cloudmesh.yaml file. Please note that you have to change the project
id and name according to your account on chameleon cloud. For the
classes the Gregor von Laszewski teaches, we have provided that
information for you, so you only have to make sure to provide the
username and password.


```python
from openstack import connection
from pprint import pprint
import yaml
from cloudmesh.configuration.Config import Config

cred = """
# This is a clouds.yaml file, which can be used by OpenStack tools as a source
# of configuration on how to connect to a cloud. If this is your only cloud,
# just put this file in ~/.config/openstack/clouds.yaml and tools like
# python-openstackclient will just work with no further config. (You will need
# to add your password to the auth section)
# If you have more than one cloud account, add the cloud entry to the clouds
# section of your existing file and you can refer to them by name with
# OS_CLOUD=openstack or --os-cloud=openstack
clouds:
  openstack:
    auth:
      auth_url: https://kvm.tacc.chameleoncloud.org:5000/v3
      username: TBD
      project_id: 36198064bc7e4b33b02d5ee59ff75017
      project_name: "cloudmesh"
      user_domain_name: "Default"
      password: 'TBD'
    region_name: "KVM@TACC"
    interface: "public"
    identity_api_version: 3
"""

config = Config()
data = config['cloudmesh.cloud.chameleon.credentials']
cloud = connection.Connection(**data)


print (cloud)

servers = cloud.list_servers()

pprint (servers[0]['hostname'])
```

As we see establishing a connection while using our yaml file is
extreemly easy. The advantage of using the cloudmesh.yaml file is that
it allows us to easily manage credentials for orther clouds also so we
can switch between them and are independent from openstack in general
(see chapters about AWS, Azure, and others in the cloudmesh manual.)

Simple example demonstrations on how to use the API are provided at 

* <https://docs.openstack.org/openstacksdk/latest/user/guides/compute.html>


The program just lists the name of the first server if ther is such as
server. 


:o2: Next we will showcase you how to start a server from the API.
The detailed API for managing compute servers is provided at 

* <https://docs.openstack.org/openstacksdk/latest/user/proxies/compute.html>
