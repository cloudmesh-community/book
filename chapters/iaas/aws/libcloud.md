## Summary

Libcloud provides a unified Python API to interact with multiple cloud providers. It was easy to list VMs from Azure as well as AWS with few lines of Python code and couple hours of focused effort.


## Driver Settings

Essentially, there are three steps :

1. Using the get_driver() method to obtain a reference to the cloud provider driver
2. Instantiating the driver with the credentials to access the cloud
3. Using the list_nodes() method to list the VMs



```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
```

## Create a Computing Node

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)

# retrieve available images and sizes
images = conn.list_images()

sizes = conn.list_sizes()

# create node with first image and first size
node = conn.create_node(name='yourservername', image=images[0], size=sizes[0])
```


## List Nodes

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
driver = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)

nodes = driver.list_nodes()
print nodes
```

## Start Nodes

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
driver = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)
nodes = driver.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
driver.ex_start(node=node)
```

## Stop Nodes

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

EC2_ACCESS_ID = 'your access id'
EC2_SECRET_KEY = 'your secret key'

EC2Driver = get_driver(Provider.EC2)
driver = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)
nodes = driver.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
driver.ex_stop(node=node)
```
