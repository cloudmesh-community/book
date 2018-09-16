# Go Language :o: {#s-go-language}

:warning: This section is under development. It is contributed by Qianqian

Go is a computer language developed by Google with the goal 
to "build simple, 
reliable, and efficient software". 
The language is open source and the main Web page is


https://golang.org/

* <https://golang.org/>

```
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
    }
```


Portable Cloud Programming with Go Cloud

* <https://blog.golang.org/go-cloud>

## REST services in GO

List here the rest services frameworks

* <https://nordicapis.com/7-frameworks-to-build-a-rest-api-in-go/>
* with mongo <https://hackernoon.com/build-restful-api-in-go-and-mongodb-5e7f2ec4be94>
* <https://tutorialedge.net/golang/consuming-restful-api-with-go/>

### Gorilla

* <https://www.codementor.io/codehakase/building-a-restful-api-with-golang-a6yivzqdo>

## OpenStack from Go

Contributed by Gregor

There are multiple API interfaces that allow direct access to
elementary functionality to controll for example virtual machines in
Go. This includes GopgerCloud, and GolangClient. We describe them next.

### GohperCloud

GopherCloud is located at

* <https://github.com/gophercloud/gophercloud>

#### Authentication

To interact with OpenStack, yo will need to first authenticate with
your OpenSatck cloud. YOu will need to know your username and
password. However the example that we provide here is on intention
wrong to showcase you a better way. The example includes a hard coded
username and password, that actually is supposed to be either read in
via an interactive process or from a `~/.cloudmesh/cloudmesh.yaml`
file as we have used in our python cloudmesh code. We will use the
same format and obtain the information from that file. YOur task will
be to write a yaml file reader in go, get the information and modify
the program accordingly while improving this section with a pull
request.

```
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

An alternative approach is to obtain the values from environment
variables

```
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

```
client, err := openstack.NewComputeV2(provider, gophercloud.EndpointOpts{
  Region: os.Getenv("OS_REGION_NAME"),
})
```

#### Virtual machines

Now that we know we can communicate through the client with the cloud,
we can create our first virtual machine, where flavor_id and image_id
are the approriate flavors and image ids:


```
import "github.com/gophercloud/gophercloud/openstack/compute/v2/servers"

server, err := servers.Create(client, servers.CreateOpts{
  Name:      "gregor-001",
  FlavorRef: "flavor_id",
  ImageRef:  "image_id",
}).Extract()
```

Additional information can be found in the source code of GoherClient
which you can easily inspect. Soem useful documentation is also
provided in


#### Resources :o:

From <https://github.com/gophercloud/gophercloud/blob/master/doc.go>
we quote (we will need to rewrite this section as this is excessive quoting):

"

Resource structs are the domain models that services make use of in order
to work with and represent the state of API resources:

```
  server, err := servers.Get(client, "{serverId}").Extract()
  ```
  
Intermediate Result structs are returned for API operations, which allow
generic access to the HTTP headers, response body, and any errors associated
with the network transaction. To turn a result into a usable resource struct,
you must call the Extract method which is chained to the response, or an
Extract function from an applicable extension:

```
result := servers.Get(client, "{serverId}")
  // Attempt to extract the disk configuration from the OS-DCF disk config
  // extension:
  config, err := diskconfig.ExtractGet(result)
```
  
All requests that enumerate a collection return a Pager struct that is used to
iterate through the results one page at a time. Use the EachPage method on that
Pager to handle each successive Page in a closure, then use the appropriate
extraction method from that request's package to interpret that Page as a slice
of results:

```
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

If you want to obtain the entire collection of pages without doing any
intermediary processing on each page, you can use the AllPages method:

```
allPages, err := servers.List(client, nil).AllPages()
allServers, err := servers.ExtractServers(allPages)
```
    
This top-level package contains utility functions and data types that are used
throughout the provider and service packages. Of particular note for end users
are the AuthOptions and EndpointOpts structs.

"



### Golang Openstack Client

* <https://github.com/openstack/golang-client>

Examples:

*
[Authentication](https://github.com/openstack/golang-client/blob/master/examples/authentication/authentication.go)
*
[Images](https://github.com/openstack/golang-client/blob/master/examples/image/image.go)
*
[ObjectStore](https://github.com/openstack/golang-client/blob/master/examples/objectstorage/objectstorage.go)
* This file reads in some configurations form a json file, however we
  want to develop one for our `~/.cloudmesh/cloudmesh.yaml` file. For
  the json example see:
  [json setup](https://github.com/openstack/golang-client/blob/master/examples/setup/setup.go)
* [Volume](https://github.com/openstack/golang-client/blob/master/examples/volume/volume.go)


