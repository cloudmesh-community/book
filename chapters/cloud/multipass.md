# Multipass

Multipass is a command line tool to manage Ubuntu virtual machines on a
computer from the command line. With the help of multipass, we can
simulate a cloud that manages virtual machines on your computer.

Naturally, your computer needs to have enough main memory for running
multiple virtual machines. You need administrative privileges
to use multipass (for example, on OSX and Linux being able to run as
`sudo`).

More information about multipass can be found at 

* <https://multipass.run/>

## Install 

Follow the install instructions as documented at

* <https://multipass.run/docs>

### Ubuntu 18.04

On Ubuntu 18.04, `multipass` is provided as a [snap](https://snapcraft.io/) application.
`snap` is part of the core Ubuntu 18.04 system so no additional setup is requied.
To install `multipass` using `snap` via the command line, open up a terminal/command line window and execute this command.

```
sudo snap install multipass --classic
```

## Sudo on OSX

On OSX, you need to be in the sudoer's list. Please consult on the Net to
understand what `sudo` is. We recommend that you create a separate user
with such privileges and use that for trying it out instead of using
your main account. To add this user to `sudo`, conduct the following steps.


First, login as administrator and edit the file 

	/etc/sudoers

In that file find the following line: 

    %admin ALL=(ALL) ALL 

After that line, add your username to the list of sudoers as follows: 

    username ALL=(ALL) ALL
    
    
## Experimenting with Multipass

Now let us experiment with multipass. Launch an instance with 

```bash
$ multipass launch --name ubuntu-lts
```

Execute a command in the instance with 

```bash
$ multipass exec ubuntu-lts -- lsb_release -a
```

List all instances with and specify the output in various formats

```bash
$ multipass list
$ multipass list --format yaml
$ multipass list --format json
$ multipass list --format csv
```

Stop the instance with 

```bash    
$ multipass stop ubuntu-lts
```

Make sure it is stopped

```bash
$ multipass list --format yaml
```

Start the instance

```bash
$ multipass start ubuntu-lts
```

Make sure its started

```bash
$ multipass list --format yaml
```

Stop it again

```bash
$ multipass stop ubuntu-lts
```

Start the primary

```bash
$ multipass start 
```

List the running instances

```bash
$ multipass list --format yaml
```

Delete all instances

```bash
$ multipass delete --all
```

Make sure they are deleted

```bash
$ multipass list --format yaml
```

Purge the instances

```bash
$ multipass purge
```

Make sure they are purged

```bash
$ multipass list --format yaml
```

Find other images

```bash
$ multipass find
```

To switch to a different VM support you can use

OSX: (default is hyperkit)

```bash
sudo multipass set local.driver=hyperkit
sudo multipass set local.driver=virtualbox
```

Windows: (default is hyperv, it must be enabled.)

```bash
multipass set local.driver=hyperv
multipass set local.driver=virtualbox
```

You have to reboot for the feature to take effect in Windows. If you
have Windows 10 Home you must use virtualbox. Please get Windows Pro or
EDU instead.

## Exercises

E.Multipass.1:

> Add installation instruction for your operating system to this
> document.

E.Multipass.2: 

> What is Primary in multipass

E.Multipass.3: 

> What is snapcraft in multipass 

E.Multipass.4:

> How do you write a bibtex entry for <https://multipass.run/>
>
> Add all bibtex entries (e.g. the URLs you see in multipass.md) into
> <https://github.com/cloudmesh-community/book/blob/master/bib/multipass.bib>
>
> Tip: see: <https://github.com/cloudmesh-community/book/blob/master/bib/refs.bib> 
> for examples.
>
> Answer:
>
> Provided by students

E.Multipass.5:

> Provide more extensive examples for find
>
> * <https://multipass.run/docs/find-command>
> * <https://launchpad.net/ubuntu/+series>
> 
> Provide a list of images that are supported on your system.
>
> Solution:
>
> OSX: using hyperkit
>

| Image             | Aliases    | Version   | Description |
| ----------------- | ---------- | --------- | ----------- | 
| snapcraft:core    | core16     | 20200115  | Snapcraft builder for Core 16 |
| snapcraft:core18  |            | 20200115  | Snapcraft builder for Core 18 |
| 16.04             | xenial     | 20200108  | Ubuntu 16.04 LTS |
| 18.04             | bionic,lts | 20200107  | Ubuntu 18.04 LTS |

>
> OSX: using virtualbox
>


| Image             | Aliases    | Version   | Description |
| ----------------- | ---------- | --------- | ----------- | 
| 16.04             | xenial     | 20200108  | Ubuntu 16.04 LTS |
| 18.04             | bionic,lts | 20200107  | Ubuntu 18.04 LTS |

>
> Linux:
>

| Image             | Aliases     | Version   | Description |
| ----------------- | ----------- | --------- | ----------- | 
| snapcraft:core    | core16      | 20200115  | Snapcraft builder for Core 16 |
| snapcraft:core18  |             | 20200115  | Snapcraft builder for Core 18 |
| core              | core16      | 20190806  | Ubuntu Core 16 |
| core18            |             | 20190806  | Ubuntu Core 18 |
| 16.04             | xenial      | 20200108  | Ubuntu 16.04 LTS |
| 18.04             | bionic,lts  | 20200107  | Ubuntu 18.04 LTS |
| 19.04             | disco       | 20200109  | Ubuntu 19.04 |
| 19.10             | eoan        | 20200107  | Ubuntu 19.10 |
| daily:20.04       | devel,focal | 20200113  | Ubuntu 20.04 LTS |

>
> Windows:
>
> * ...

E.Multipass.6:

> Explain cloud-init. Provide an example

E.Multipass.7:

> Install MikroK8s in multipass and provide a users guide

E.Multipass.8:

> Measure the performance of fetching and launching the image with the 
> different hypervisors on your system. Report the results in a table with 
> a timer for each hypervisor and distinguish faetching and launching times. 
> Measure also the time to execute a command in the VM.
>
> The table will have the columns
>
> Image, Hypervisor, Fetch, Launch, Execute 
>
> Make sure to purge the images between tests.
>
> Use a pytest and cloudmesh Benchmark for creating the Benchmarks.
> The pytest can be shared among all students. Discuss on Piazza 
> how to do it. Use a cloudmesh shell variable for the HYPERVISOR type.
>

E.Multipass.9a:

> What is k3s?
>
> Tip: <https://k3s.io/>
> Tip: <https://rancher.com/docs/k3s/latest/en/>


E.Multipass.9b:

> Create a cloudmesh command to start a k3s cluster 
> Leverage the template disucussed at
> <https://medium.com/better-programming/local-k3s-cluster-made-easy-with-multipass-108bf6ce577c>
>
> use 
>
> `cloudmesh sys command generate k3s`
> 
> To generate the command such as
>
> cms k3s [--hypervisor=hyperkit] --names=\"node[0-3]\" deploy
>
> where the first note is assumed to be the master. THis commands deploys 
> on your local computer a 3 node kubernetes cluster.
>
> Extend the 
> commandlist to include
>
> start, stop, purge, delete, ... and so on. Discuss with others in class
> what commands should be implemented.
