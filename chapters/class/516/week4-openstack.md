# Week 4: Openstack :warning:

---

:warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning::warning:

This section is not yet complete and is
being updated. We included it so you can see what we will be doing next
so you can work ahead. However, be advised that the content still can
change.

---


# Lecture Material

* A Book for OpenStack will be added
* Material about OpenStack will be made available here

* :warning: The Python book will be updated
* :warning: The cloud book will be updated. 

# Lab: OpenStack

This week we will be learning how to manage virtual machines on
OpenStack. You are requested to explore the GUI interface which is
called horizon so you can. verify your activities easily in case you
have issues with the command line tools. However, our main goal will be
that you use command line tools to interact with Chameleon cloud.

Whatever you do after you are dine with the VMs you need to terminate
them so you do not unnecessarily wast compute time.

## Naming of vms

Your HID is of the form fa16-516-NNN or similar for other classes.
Please note that the number is unique across classes. This identifies
you and if you start a vm in a shred space such as chameleon we can use
it to identify people and notify them easily.

Thus pleas use the following naming scheme

`NNN-firstname-i`

where topic is a topic for the vm such as `webserver` and i is a number
such as `1` as you may start multiple vms.

Please never start more than 3 vms without consultation with Gregor as
we will run out of node hours for the class if we do so.

## Horizon

:warning: Information in how to use it will be added here. This
information is already in our git book repo but has not yet been
released.

## OpenStack Command line Client

:warning: Information in how to use it will be added here. This
information does not yet exist. as we usually use cloudmesh anyways as
it is more convenient. We just want mention it exists and point to the
manual page.

## OpenStack Python API

:warning: Information in how to use it will be added here. This
information does not yet exists, but is used in the OpenStack provider
for cloudmesh.

## Cloudmesh OpenStack interface

In this section (which will be moved) and made an exercise we will be
discussing how to set up cloudmesh to interface with chameleon cloud.

### Installation

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

:warning: If not done yet set up ssh with 

```
$ ssh-keygen
```

### Configuration

:warning: Here we will explain how to configure Chameleon cloud access
with `~/.cloudmesh/cloudmesh.yaml`

:warning: we need to explain how to set up the VM naming schema with 
`~/.cloudmesh/names.yaml`:

```
path: /Users/grey/.cloudmesh/name.yaml
schema: NNN-gregor-{counter}
counter: 1
```

:warning: We need an easy command line program to change the schema. This
could be developed by a student.

:warning: Explain how to configure images and flavor in the
`cloudmesh.yaml` file


### Cloudmesh Mongo 

Explain how to set up Mongo

Explain `cms init` and that it wipes the db and should only be used once

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

:warning: show how to use status

### Start a VM

:warning: Explain that OpenStack could be over-utilized and that a VM may
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

### Working with the VM

Log into the vm with 

```bash
cms ssh
```

:exercise: lets assume you start 3 vms how do you log in in each one of
them. Explain. Explore the manual pages. Use the list command.

### Notes

:warning: explain `cc` user
