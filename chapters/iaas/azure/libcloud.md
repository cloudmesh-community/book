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

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
driver = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)
```

## Create a Computing Node

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'
AZURE_CLOUD_SERVICE_NAME = 'MyCloudService'

AZDriver = get_driver(Provider.AZURE)
conn = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)

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

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
driver = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)

nodes = driver.list_nodes()
print nodes
```

## Start Nodes

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
driver = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)
nodes = driver.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
driver.ex_start(node=node)
```

## Stop Nodes

```Python
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Azure related variables
AZURE_SUBSCRIPTION_ID = 'xxxxxxxx–xxxx-xxxx-xxxx-xxxxxxxxxxxx'
AZURE_MANAGEMENT_CERT_PATH = 'C:/Demo/azure_cert.pem'

AZDriver = get_driver(Provider.AZURE)
driver = AZDriver(subscription_id=AZURE_SUBSCRIPTION_ID, key_file=AZURE_MANAGEMENT_CERT_PATH)
nodes = driver.list_nodes()
node = [n for n in nodes if 'yourservername' in n.name][0]
driver.ex_stop(node=node)
```
