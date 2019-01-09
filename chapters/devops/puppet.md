# Puppet :wave:

:o: Tyler: use of a and the needs to be checked as it seems there is
a different opinion on how to use this. changes thet Gregor did were
for example reverted. So it is importnat that this is checked by a
second native English speaker, E.g. Tyler

:o: there is lots of redundancy in here in install, maybe this could
ebe simplified with a script. or two, one for mono, one for split.

:o: explanation of difference between mono and split need to be improved.

:o: inconsistent use of single `#` in file check TOC for this md file

:o: cert section unclear. I recommend attending online hour to discuss
this. Maybe even separate meetin. We need to have TA in the meeting

:o: I suggest that you do improvements backwards. Often by the end
sections are less worked on

## Overview

Configuration management is an important task of IT department in any
organization. It is process of managing infrastructure changes in
structured and systematic way. Manual rolling back of infrastructure
to previous version of software is cumbersome, time consuming and
error prone.  Puppet is configuration management tool that simplifies
complex task of deploying new software, applying software updates and
rollback software packages in large cluster efficiently. Puppet does
this through Infrastructure as Code (IAC). Code is written for
infrastructure on one central location and is pushed to nodes in all
environments (Dev, Test, Production) using puppet tool.  Configuration
management tool has two approaches for managing infrastructure.
Configuration push and pull. In push configuration, infrastructure as
code is pushed from centralized server to nodes whereas in pull
configuration nodes pulls infrastructure as code from central server
as shown in +@fig:InfrastructureAsCode.

![Infrastructure As Code](Images/IAC.jpg){#fig:InfrastructureAsCode}

[hid-sp18-523-puppetimages]

Puppet uses push and pull configuration in centralized manner 
as shown in +@fig:push-pull-configImage.

![push-pull-config Image](Images/push-pull-configuration.jpg){#fig:push-pull-configImage}

[hid-sp18-523-puppetimages]

Another popular infrastructure tool is Ansible. It does not have
master and client nodes. Any node in Ansible can act as executor.  Any
node containing list of inventory and SSH credential can play master
node role to connect with other nodes as opposed to puppet
architecture where server and agent software needs to be setup and
installed.  Configuring Ansible nodes is simple, it just requires
python version 2.5 or greater.  Ansible uses push architecture for
configuration.

## Master slave architecture

Puppet uses master slave architecture as shown in +@fig:master-slaveImage. 
Puppet server is called as master node and client nodes are called as puppet 
agent. Agents poll server at regular interval and pulls updated  configuration 
from master. Puppet Master is highly available. It supports multi master 
architecture. If one master goes down backup  master stands up to serve 
infrastructure. 

#### Workflow

* nodes(puppet agents) sends information(for e.g IP, hardware detail,
  network etc.) to master. Master stores such information in manifest
  file.

* Master node compiles catalog file containing configuration
  information that needs to be implemented on agent nodes.

* Master pushes catalog to puppet agent nodes for implementing  
  configuration.

* Client nodes send back updated report to Master. Master updates its
  inventory.

* All exchange between master and agent is secured through SSL
  encryption (Refer to Puppet Master Slave Connection figure below)

![Master and Slave Architecture [hid-sp18-523-puppetimages]](Images/master-slave.jpg){#fig:master-slaveImage}

+@fig:master-slave1Image, shows flow between master and slave.

![Master Slave Workflow 1 [hid-sp18-523-puppetimages]](Images/master-slave1.jpg){#fig:master-slave1Image}

+@fig:master-slave-connection shows SSL workflow between
 master and slave.

![Master  Slave SSL Workflow [hid-sp18-523-puppetimages]](Images/master-slave-connection.jpg){#fig:master-slave-connection Image}

## Installation

### Download and verify installation package

Puppet can be installed using below steps:

* Download tarball for given operating system and architecture. 

For Ubuntu download -ubuntu-<version and arch>.tar.gz


* Import Puppet public key 

```bash
$ wget -O - https://downloads.puppetlabs.com/puppet-gpg-signing-key.pub
  | gpg --import
```


- Print fingerprint of used key

```bash
$ gpg --fingerprint 0x7F438280EF8D349F
```

- Verify release signature of installed package.

```bash
$ gpg --verify puppet-enterprise-<version>-<platform>.tar.gz.asc
```

:o: do not use greater equal but just capital letters to be constant
with other sections

### Install using text mode (mono configuration)

:o: no brackets in headlines

Mono configuration is used when single node acts
as both master and agent.

`pe.conf` configuration file needs to be specified in order to install
Puppet Enterprise in text mode. This file contains parameters and
values for installing , upgrading and configuring Puppet.

Following are some important parameters that can be specified in 
`pe.conf` file.

:o: this must be done in verbatim mode

* console_admin_password
* puppet_enterprise::console_host
* puppet_enterprise::puppetdb_host
* puppet_enterprise::puppetdb_database_name
* puppet_enterprise::puppetdb_database_user

Next, you need to Unpack the installation tarball.
Let us assume i is stored in a file. We will be storing the location
in a variable `$TRABALL` and use the variable in our installation.

```bash
export TARBALL=put the path to the tarball filename here
```

First we extract the tarball:

```bash
$ tar -xf $TARBALL
```

- Run the installer from the installer directory

```bash
sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

:o: this seems to complex and you should give more direct instructions
on where to place the conf file maybe using mkdir and place the file
there, or do another export and integrate this above

- Run puppet twice : puppet agent `-t` after installation is complete.


### Install using text mode ( split configuration )

:o: unclear what the difference is between split and mono, no
brackets in headline.

split configuration is used when master and agent node needs to be
installed on separate nodes. Components must be installed in specific
order under this method.


#### Install the master

:o: bullet unnecessary, we need full sentences. Fix in all of the paper.

- Unpack installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

:o use `$TRABALL`

<TARBALL_FILENAME> is the path where .tar file for respective
operating system is downloaded.

* Run the installer from installed directory. Installation steps vary
depending on path. To use pe.conf file that have been previously
populated, run the installer with the `-c` flag pointed at the
`pe.conf` file.

:o:

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```


To have the installer open a copy of pe.conf for editing, run the
installer without the `-c` flag.

```bash
$ sudo ./puppet-enterprise-installer
```

:o: unclear:

* Select text-mode when prompted. `pe.conf` file will be opened

* Change the master node related configuration parameters

* Installation will begin after the file is saved and closed.

* When installation is completed, transfer the installer and pe.conf file 
  located at /etc/puppetlabs/enterprise/conf.d/ to the next server in case
  if infrastructure with multiple server needs to be set up.

#### Install PuppetDB

PuppetDB, stores the details on the relations, nodes, resources
for the whole architecture.

:o: what architecture

This information can be accessed 
any tool or workflow.

In a split installation, after installing the master, its ready to 
install PuppetDB.

* Unpack the installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

:o:

<TARBALL_FILENAME> is the path where .tar file for 
respective operating system is downloaded.
:o:

* From the installer directory, run the installer:

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

* Select text-mode when prompted. `pe.conf` file will be opened

* Change the database node related configuration parameters

* Installation will begin after file is saved and closed.

* Transfer the installer and the `pe.conf` 
  file located at /etc/puppetlabs/enterprise/conf.d/ to the next puppet db 
  server in case if infrastructure with multiple db server needs to be set up.


#### Install the console

In split installation, after installing master and PuppetDB, are ready
to install from console.

- Unpack the installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

- From the installer directory, run the installer:

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

* Select text-mode when prompted. `pe.conf` file will be opened

* Change the console node related configuration parameters

* Installation will begin after the file is saved and closed.

#### Run Puppet on infrastructure nodes

To complete a split installation, run Puppet on all infrastructure 
nodes in the order that they were installed.

* Run Puppet on the master node.
* Run Puppet on the PuppetDB node.
* Run Puppet on the master node a second time.
* Run Puppet on the console node.

## Configuring Puppet

### Puppet.conf

This is the main puppet configuration file. Most settings such as
Master, Agent, certificates are all specified in this file.

### Agent config section

Below :o: is the example

[main]

```bash
certname = <http://testing.hid520-hid523.com/>
server = puppetserver
environment = testing
runinterval = 4h
```

:o: gregor commented till here. will do other later

### Puppet master config file

Below :o: is the example

[main]

```bash
certname =  <http://testing.hid520-hid523.com/>
server = puppetmaster
environment = testing
runinterval = 4h
strict_variables = true
```

[master]

```bash
dns_alt_names = puppetserver,puppet, <http://puppet.test.com/>
reports = pupated
storeconfigs_backend = puppetdb
storeconfigs = true
environment_timeout = unlimited
```

### Key components of config file

Comment lines, Settings lines and Settings variables are main
components of puppet

Comments in config files are specified by prefixing hash character

Setting line consists name of the setting followed by equal sign,
value of the setting would be specified in this section. Setting
variable value generally consists of one word but multiple can be
specified in rare cases.

## Setting up Puppet master

Puppet server software is installed on puppet master node which then
pushes the configuration to clients nodes(puppet agents).

Pull software package from the repository.

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

Install puppetserver package.

Following command is used to install server on master node

```bash
$ sudo yum -y install puppetserver
```

By default 2GM memory is allocated, but it can be configured based on
available memory as well as number of puppet agent nodes.  Use
following command to edit the server configuration

```bash
$ sudo vi /etc/sysconfig/puppetserver
```

Set value of variable to increase memory to 3GB
while specifying the options to the `JAVA_ARGS`:

```bash
JAVA_ARGS="-Xms3g -Xmx3g"
```

Start the puppet server 

```bash
$ sudo systemctl start puppetserver
```

Start the puppet server after the master server is started.

```bash
$ sudo systemctl enable puppetserver
```

## Installing puppet agent

:o: an agent is an agent not just software

Puppet agent is :o: software that needs to be installed on all the nodes 
that needs to be part of network and managed. Puppet master can not 
reach and manage any node that does  not have puppet agent installed.  
Puppet agent software can be installed and run on any Linux, Unix or 
windows based machines.

### Steps to install Puppet agent software

:o: unnecessary use of bullets and no full centences. This is not just
valid here but throughout the paper. Fix in entire paper, use things
this as

Next we describe how to do ....

First, we need to ...

Second, we need to

Third, we need to ...

and so on ...

* Connect to puppet repository.

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

* Install Puppet agent.

```bash
$ sudo yum -y install puppet-agent
```

* Enable agent.

```bash
$ sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true
```
 
Once the puppet agent is installed and runs for the first time, it
generates a SSL certificate and sends it to the master for
signing. The master communicates and manages client nodes after the
certificate is signed.

Each puppet client node in the infrastructure managed with puppet
needs to follow this process.

## Configuring SSL

SSL certificate approval by puppet master is required  for all nodes in order 
for master to communicate and manage client nodes. 

### Find out and list all unsigned  certificate requests.

```bash
$ sudo /opt/puppetlabs/bin/puppet cert list
```

### View requests

Sample request that is displayed after agent is set up successfully

:o: notes must be done in markdown, see notation.md

( Note - Used Certificate name is for illustration purpose only )

:o: unclear

* <http://test.hid520-hid523.com/> (SHA259)

:o: verbatim

15:90:C2:FB:ED:69:A4:F7:B1:87:0B:BF:F7:ll:B5:1C:33:F7:76:67:F3:F6:45:AE:07:4B:F

6:E3:ss:04:11:8d

:o: unclear

Identification of signed/un-signed certificate is done by looking at the 
+ sign in the beginning. Absence of + sign indicate that certificate is not signed.

### Sign request

On the puppet master in order to sign the new certificate 
request that is sent by puppet agent(client node) for approval(signing)

:o: unclear why `<>`. 

Note - <http://test.hid520-hid523.com/> (SHA259) certificate name is used for 
illustration and example only

```bash
$ sudo /opt/puppetlabs/bin/puppet cert sign  
[test.hid520-hid523.com](http://test.hid520-hid523.com/)
```

output - :o: no - here fix throughout the paper. use full sentence,
see next section for an example

Notice: Signed certificate request for <http://test.hid520-hid523.com/>

Notice: Removing file Puppet::SSL::CertificateRequest 
<http://test.hid520-hid523.com/> 
at '/etc/puppetlabs/puppet/ssl/ca/requests/test.hid520-hid523.com.pem'

Puppet master can now communicate and manage the client node

```bash
$ sudo /opt/puppetlabs/bin/puppet cert sign --all
```

### Removing and adding Puppet agent


Sometimes there is a need to remove the puppet agent node from puppet 
infrastructure for debugging. This is done with the following command:

```bash
$ sudo /opt/puppetlabs/bin/puppet cert clean hostname
```

### Viewing all signed requests

To list all signed certificates you can use the command

```bash $ sudo /opt/puppetlabs/bin/puppet cert list --all ```

This will lead to an output similar to, where the + sign in the
beginning indicates signed certificate:

+ "puppet"(SHA256)

:o: please fix the next using verbatim

```
5A:71:E6:06:D8:0F:44:4D:70:F0:BE:51:72:15:97:68:D9:67:16:41:B0:38:9A:F2:B2:6C:BB:33:7E:0F:D4:53 (alt names: "DNS:puppet", 
"DNS:[test.hid520-hid523.puppetproject.com]
(http://test.hid520-hid523.puppetproject.com/)")

+ "[test.hid520-hid523.com](http://test.hid520-hid523.com/)"(SHA259)

F5:DC:68:24:63:E6:F1:9E:C5:FE:F5:1A:90:93:DF:19:F2:28:8B:D7:BD:D2:6A:83:07:BA:FE:24:11:24:54:6A

+ "  [test.hid520-hid523.com](http://test.hid520-hid523.com/)"(SHA259)

CB:CB:CA:48:E0:DF:06:6A:7D:75:E6:CB:22:BE:35:5A:9A:B3
```

# Managing puppet environment through tool

The Puppet environment mangement tool known as r10k is used for managing 
configurations related to different environments such as testing, staging 
and production. The different configuration related information is stored in 
a central repository. The r10k tool creates an environment on the puppet master and 
then uses modules stored in the repo to install and update the
environment. 

Let us first Install the r10k tool with 

```bash
$ urlgrabber -o /etc/yum.repos.d/timhughes-r10k-epel-6.repo 
[https://copr.fedoraproject.org/coprs/timhughes/yum]
(https://copr.fedoraproject.org/coprs/timhughes/yum)
-y install rubygem-r10k
```

### Configure environment in /etc/puppet/puppet.conf for r10k

:o: to long of a heading, no sentence

:o: not verbatim

[main]
environmentpath = $confdir/environments

### Create configuration file for r10k config

```bash 
$ cat <<EOF >/etc/r10k.yaml
:cachedir: '/var/cache/r10k'
:sources:
:opstree:
remote: '/var/lib/git/fullstackpuppet-
environment.git'
basedir: '/etc/puppet/environments'
EOF
```

### Installing Puppet manifest and module

```bash
r10k deploy environment -pv
```

Creating cron job is recommended as environment needs to be updated
frequently.

```bash
$ cat << EOF > /etc/cron.d/r10k.conf SHELL=/bin/bash 
PATH=/sbin:/bin:/usr/sbin:/usr/bin H/15 
* * * * root r10k deploy environment -p EOF
```

### Testing installation

Puppet manifest for Puppet module needs to be complied in order to
test and validate if the environment is working correctly.  Run the
following command and inspect the YAML output.

```bash
$ curl --cert /etc/puppet/ssl/certs/puppet.corp.guest.pem \
--key /etc/puppet/ssl/private_keys/puppet.corp.guest.pem \
--cacert /etc/puppet/ssl/ca/ca_crt.pem \-H 'Accept: yaml' \
```

## Reference

:o: add bibtex

* <https://puppet.com/docs/pe/2017.3/installing_pe.html#concept-3157> 
* <https://puppet.com/docs/pe/2017.3/installing_pe.html>
* <https://puppet.com/docs/puppet/5.3/config_file_main.html>
* Images - are taken form from <https://www.edureka.co/blog/videos/puppet-tutorial/> devops class
