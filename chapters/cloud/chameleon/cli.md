# Cloudmesh OpenStack Command Line Interface {#sec:chameleon-cm-cli}

OpenStack on Chameleon delivers KVM based compute resources to provision
virtual machines. It provides various image types on which we can deploy
tools and software needed for the class and projects. We will you
through the basic steps of getting access to OpenStack Chameleon cloud
under the class allocation. Next, we will introduce you the cloudmesh 
command line tools which you can use in your projects. Naturally using the GUI
for your projects is not sufficient as setting up your environment will
need steps to be executed by hand which is not sufficient. It is a goal
of this class that you create your environment in a reproducible
fashion via scripts. Hence, although the Web interface called OpenStack
Horizon is initially attractive, we should make sure to move on to the
commandline interfaces. Furthermore, it is often difficult to resolve
technical issues as the command line tools generate full debugging
messages in case of issues and copy and past into help windows is much
easier and efficient than copy and past incomplete screenshots.

One important factor for using cloudmesh shell is that it not only works
for chameleon cloud but also for AWS and Azure. We are hoping to add
Google also which is already in our preliminary code.

## Instalation of Cloudmesh Client

We discuss how to install cloudmesh in the [Cloudmesh manual][https://cloudmesh.github.io/cloudmesh-manual/installation/install.html]

We assume that your public key is located at `~/.ssh/id_rsa.pub` 

We assume you have the file `~/.cloudmesh/cloudmesh.yaml` that is
created during the instalation process. Please also make sure that the
file `~/.cloudmesh/names.yaml` Is properly configured for the class.
Typically it will look like

```
path: /Users/grey/.cloudmesh/name.yaml
schema: NNN-accountname-{counter}
counter: 1
```

Where NNN is the last three gigits from your hid that we place in github
and for accountname, please chose your chameleon account name. If you
are not taking any of our classes and you do not have a github directory
that we created for you, please use

```bash
path: /Users/grey/.cloudmesh/name.yaml 
schema: accountname-{counter}
counter: 1
```

instead. Whenever you start a new vm, the counter of the
vm gets increased, guranteeing a unique virtual machine name across all
colaborators and your own virtual machines.

We also assume you have called the command 

```bash
cms init
```

and are running the MongoDB cloudmesh service which you can check with


```bash
$ cms admin mongo status
```

Once you install cloudmesh you need to modify the
`~/.cloudmesh/cloudmesh.yaml` file to add your username and password.
Make sure to properly protect this file as discussed in the manual.

To add the username and password, you can use an editor, or execute on
the commandline with the commands

```bash
$ cms config set chameleon.OS_USERNAME=YOURUSERNAME
$ cms config set chameleon.OS_PASSWORD=YOURPASSWORD
```

They will change the values in the yaml file at

* `cloudmesh.cloud.chameleon.credentials.`


Next test out if you can see some images with 

```bash
cms image list --refresh
```

You will see a table similar to 

```
+--------------------------+--------------+--------------+-------------+--------+-----------+
| Name                     | Size (Bytes) | MinDisk (GB) | MinRam (MB) | Status | Driver    |
+--------------------------+--------------+--------------+-------------+--------+-----------+
| CC-Ubuntu18.04           | 982843392    | 0            | 0           | ACTIVE | openstack |
| CC-Ubuntu16.04           | 844759040    | 0            | 0           | ACTIVE | openstack |
| CC-Ubuntu18.04-20190822  | 982056960    | 0            | 0           | ACTIVE | openstack |
| CC-Ubuntu16.04-20190822  | 844824576    | 0            | 0           | ACTIVE | openstack |
...
```

To see the flavors or sizes, you can use


```bash
cms flavor list flavor --refresh
```

Which will return something like 

```
+----------------+-------+-------+------+
| Name           | VCPUS | RAM   | Disk |
+----------------+-------+-------+------+
| m1.tiny        | 1     | 512   | 1    |
| m1.small       | 1     | 2048  | 20   |
| m1.medium      | 2     | 4096  | 40   |
| m1.large       | 4     | 8192  | 80   |
| m1.xlarge      | 8     | 16384 | 160  |
| storage.medium | 1     | 4096  | 2048 |
| m1.xxlarge     | 8     | 32768 | 160  |
| m1.xxxlarge    | 16    | 32768 | 160  |
+----------------+-------+-------+------+
```

Cloudmesh reads the preset variables in the cloudmesh.yaml file to start
new virtual machines. To see them you can look at the yaml file or use the command


```bash
$ cms config get chameleon.default
```

To start a VM simply use

```bash
cms vm boot
```

You will see something similar to

```
# ----------------------------------------------------------------------
# Create Server
# ----------------------------------------------------------------------

    Name:     benchmark-gregor-vm-684
    User:     cc
    IP:       129.114.33.243
    Image:    CC-Ubuntu14.04
    Size:     m1.small
    Public:   True
    Key:      gregor
    location: None
    timeout:  360
    secgroup: default
    group:    cloudmesh
    groups:   ['cloudmesh']
```


To log into the vm you can use 

```bash
cms ssh
```

To set a different vm, you could use the command line parameters that you can find out with 

```bash
cms vm help
```

but in case you always want to use the same parameters it is much mor
conveneint to use our `config set` command with

```bash
$ cms config set cloud.chameleon.default.size=CC-Ubuntu18.04
$ cms config set cloud.chameleon.default.image=m1.small
$ cms config set cloud.chameleon.default.username=cc
```

On chameleon cloud images with CC are cameleon cloud santioned images.
They include some monitoring extensions and use the username `cc` for
login.



## Floating IP Address

We have configured cloudmesh to automatically assign a floating ip
address so you can use that to log into the vm.

to view it, you can use the command

```bash
$ cms vm list --refresh
```

To delete the vm simply say 

```bash
$ cms vm delete
```

