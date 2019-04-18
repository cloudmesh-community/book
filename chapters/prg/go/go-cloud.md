# Go Cloud {#sec:go-cloud}

## Golang Openstack Client

* <https://github.com/openstack/golang-client>

* [Authentication](https://github.com/openstack/golang-client/blob/master/examples/authentication/authentication.go)
* [Images](https://github.com/openstack/golang-client/blob/master/examples/image/image.go)
* [ObjectStore](https://github.com/openstack/golang-client/blob/master/examples/objectstorage/objectstorage.go)
* This file reads in some configurations form a json file, however we
  want to develop one for our `~/.cloudmesh/cloudmesh.yaml` file. For
  the json example see:
  [json setup](https://github.com/openstack/golang-client/blob/master/examples/setup/setup.go)
* [Volume](https://github.com/openstack/golang-client/blob/master/examples/volume/volume.go)


Portable Cloud Programming with Go Cloud:

* <https://blog.golang.org/go-cloud>


## OpenStack from Go

There are multiple API interfaces that allow direct access to
elementary functionality to controll for example virtual machines in
Go. This includes GopgerCloud, and GolangClient. We describe them next.

### GohperCloud

GopherCloud is located at

* <https://github.com/gophercloud/gophercloud>

#### Authentication

To interact with OpenStack, yo will need to first authenticate with
your OpenSatck cloud. You will need to know your username and
password. However the example that we provide here is on intention
wrong to showcase you a better way. The example includes a hard coded
username and password, that actually is supposed to be either read in
via an interactive process or from a `~/.cloudmesh/cloudmesh.yaml`
file as we have used in our python cloudmesh code. We will use the
same format and obtain the information from that file. Your task will
be to write a yaml file reader in go, get the information and modify
the program accordingly while improving this section with a pull
request.

The example copied form goher cloud looks as follows:

```go
import (
  "github.com/gophercloud/gophercloud"
  "github.com/gophercloud/gophercloud/openstack"
  "github.com/gophercloud/gophercloud/openstack/utils"
)

opts := gophercloud.AuthOptions{
  IdentityEndpoint: "https://openstack.example.com:5000/v2.0",
  Username: "{username}",
  Password: "{password}",
}
```

Natirally you can also obtain the values from environment
variables as pointed out by gopher cloud:

```go
import (
  "github.com/gophercloud/gophercloud"
  "github.com/gophercloud/gophercloud/openstack"
  "github.com/gophercloud/gophercloud/openstack/utils"
)

opts, err := openstack.AuthOptionsFromEnv()
provider, err := openstack.AuthenticatedClient(opts)
```

We will at this time not use the second approach.

To start a virtual machine you need to first identify the location of
the client for the region you will use. This can be achieved wit the
command:

```go
client, err := openstack.NewComputeV2(provider, gophercloud.EndpointOpts{
  Region: os.Getenv("OS_REGION_NAME"),
})
```

#### Virtual machines

Now that we know we can authenticate to the cloud,
we can create our first virtual machine, where `flavor_id` and `image_id`
are the approriate flavors and image ids:


```go
import "github.com/gophercloud/gophercloud/openstack/compute/v2/servers"

server, err := servers.Create(client, servers.CreateOpts{
  Name:      "gregor-001",
  FlavorRef: "flavor_id",
  ImageRef:  "image_id",
}).Extract()
```

Additional information can be found in the source code of GoherClient
which you can easily inspect. Some useful documentation is also
provided in <https://github.com/gophercloud/gophercloud/blob/master/doc.go>


#### Resources

Code examples are provided from  <https://github.com/gophercloud/gophercloud/blob/master/doc.go>

As Openstack is providing REST interfaces, gopher cloud leverages this
model. Hence, it provides interfaces to manage REST resources. These
resources are bound to structs so they can easily be manipulated and
interfaced with. To for example get the client with a specific
`{serverId}` and extract its information we can use the following API
call:


```go
server, err := servers.Get(client, "{serverId}").Extract()
```

If we need just a subset of the information, we can get an
intermediate result with just the get method. Than we can obtain
specific information from the result as needed.


```go
result := servers.Get(client, "{serverId}")
  // Attempt to extract the disk configuration from the OS-DCF disk config
  // extension:
  config, err := diskconfig.ExtractGet(result)
```

The previous example is based on a single resource. However, if we
interacts with a list of resources we need to use the `Pager` struct
so we can iterate over each page. A convenient example is provided
next. Here we list all servers while iterating over all pages
returned to us. While calling each page we can invoke special
operations that are applied to each page.

```go
err := servers.List(client, nil).EachPage(func (page pagination.Page) (bool, error) {
  s, err := servers.ExtractServers(page)
  if err != nil {
    return false, err
  }
  // Handle the []servers.Server slice.
  // Return "false" or an error to prematurely stop fetching new pages.
  return true, nil
})
```

However, if we just want to provide a list of all servers, we can
simply use the `AllPages()` method as follows:

```go
allPages, err := servers.List(client, nil).AllPages()
allServers, err := servers.ExtractServers(allPages)
```

Additional methods and resources can be found at

* <https://github.com/gophercloud/gophercloud/blob/master/doc.go>
