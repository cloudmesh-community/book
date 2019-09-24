# Week 4: Openstack

## Video


A Video briefly summerizing an introduction to cloudmesh for multi cloud
environments including pointedts to projects related to virtual
directories, compute services, and virtual clusters

* [![Video](images/video.png) Cloudmesh Version 4 (44:01)](https://www.youtube.com/watch?v=VhgGIE2lTpQ)

A video on how to start an login into a virtual machine on Horizon is
presented next:

* [![Video](images/video.png) OpenStack Horizon (10:49)](https://www.youtube.com/watch?v=ofAVUX1gvUg)

A video how to start vms with cloudmesh is available here:

* [![Video](images/video.png) Cloudmesh cms vm boot (15:07)](https://www.youtube.com/watch?v=GgNUXYaB7kQ)

A Video on explaining the internals of cloudmesh is avalable here:

* TBD

In case you have not yet created an ssh key, the following video is
useful. THis can be replicated on any LInux, macOS and Windows 10
mashine, in case of Windows 10 use gitbash

* [![Video](images/video.png) SSH keygen (4:07)](https://www.youtube.com/watch?v=pQb2VV1zNIc)


## Lecture Material

* A Book for [Chameleon Cloud](https://laszewski.github.io/book/chameleon/) is available

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/e516/) [@las19e516]
* [Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
* [Introduction to Python for Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/python/) [@las19python]

## Lab: OpenStack

This week we will be learning how to manage virtual machines on
OpenStack. You are requested to explore the GUI interface which is
called horizon so you can. verify your activities easily in case you
have issues with the command line tools. However, our main goal will be
that you use command line tools to interact with Chameleon cloud.

Whatever you do after you are done with the VMs you need to terminate
them so you do not unnecessarily waste compute time.

## Naming of vms

Your HID is of the form fa16-516-NNN or similar for other classes.
Please note that the number is unique across classes. This identifies
you and if you start a vm in a shared space such as chameleon we can use
it to identify people and notify them easily.

Thus pleas use the following naming scheme

`NNN-firstname-i`

where topic is a topic for the vm such as `webserver` and i is a number
such as `1` as you may start multiple vms.

Please never start more than 3 vms without consultation with Gregor as
we will run out of node hours for the class if we do so.

## Horizon

The information on ho to use it is available in the Chameleon book.

A video of the meeting on Tuesday 17 Sep will be made available


## Cloudmesh OpenStack interface

The information on ho to use it is available in the Chameleon book.

A video of the meeting on Tuesday 17 Sep will be made available

## OpenStack Command line Client

The information on ho to use it is available in the Chameleon book.


### Installation of Cloudmesh Cloud Bundle

:warning: Do these only after you have completed the cloudmesh shell
related assignment from last week.

Compute:

```bash
$ cd cm
$ cloudmesh-installer git clone cloud
$ cloudmesh-installer install cloud -e
```

The next is optional and only for those that chose a cloudmesh storage
related project. The installation of the `storage` bundle includes the
installation of the `compute` bundle. 

```bash
$ cd cm
$ cloudmesh-installer git clone storage
$ cloudmesh-installer install storage -e
```

To see the available commands type

```bash
$ cms help
```

### SSH

Make sure you have a password protected ssh key

```
$ ssh-keygen
```

### Configuration

1. Change the username and password for the chameleon cloud in  `~/.cloudmesh/cloudmesh.yaml`

2. Change the password in the mongodb section
3. Change the information in the profile section

### Cloudmesh Mongo 

Setting up cloudmesh Mongo is discussed in the cloudmesh manual. W
esuggest you do the one discussed in the distribution section for your
system. It is actually build into cloudmesh, but before you do it, we
suggest you backup yor machine.

```bash
$ cms admin mongo install
```

Once you set it up use  `cms init` which wipes the db and should only be
used once

```bash
$ cms init
```

after that always use

```bash
$ cms start
```

```bash
$ cms stop
```

### Start a VM

OpenStack could be over-utilized and that a VM may
not start before a timeout. Gregor observed 70% success rate.

Task: whenever you start a vm, please keep a record if it started or not

do this in a file on your GitHub called chameleon-success.md

```
success: 7
failure: 3
```

make sure the failures are not recorded based on programming errors or
wrong parameters.

Use the commands

:warning: switch on debugging and trace

```bash
cms set cloud=chameleon
cms image list --refresh
cms flavor list --refresh 
cms vm boot
cms image list --refresh
```

:warning: Explain the difference between `--refresh` and not using it.

## Working with the VM

Log into the vm with 

```bash
cms ssh
```

## Exercise 

1. Start a vm with Horizon, login, and terminate it
2. Start a vm with Cloudmesh, login, and terminate it
3. Use robo3T or a similar program to brows in the Cloudmesh MongoDB

