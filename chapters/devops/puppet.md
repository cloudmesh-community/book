# Puppet :smiley:

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
management tool has two approaches for managing infrastructure;
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


First, we download tarball for given operating system and architecture. 

For Ubuntu download -ubuntu-<version and arch>.tar.gz


Second, we import Puppet public key 

```bash
$ wget -O - https://downloads.puppetlabs.com/puppet-gpg-signing-key.pub
  | gpg --import
```

Third, we print fingerprint of used key

```bash
$ gpg --fingerprint 0x7F438280EF8D349F
```

Fourth, we verify release signature of installed package

```bash
$ gpg --verify puppet-enterprise-VERSION-PLATFORM.tar.gz.asc
```


### Text mode monolithic installation


This is called as monolithic installation as all components of 
Puppet Enterprise such as Puppet master, PuppetDB and Console are 
installed on single node. This installation type is easy to install.
Troubleshooting errors and upgrading infrastructure using this type
is simple. This installation type can easily support infrastructure
of up to 20,000 managed nodes. Compiled master nodes can be added as
network grows. This is recommended installation type for small to 
mid size organizations[hid-sp18-523-mono].


`pe.conf` configuration file needs to be specified in order to install
Puppet Enterprise in text mode. This file contains parameters and
values for installing , upgrading and configuring Puppet.

Some important parameters that can be specified in 
`pe.conf` file are

```bash
console_admin_password
puppet_enterprise::console_host
puppet_enterprise::puppetdb_host
puppet_enterprise::puppetdb_database_name
puppet_enterprise::puppetdb_database_user
```

First, we need to unpack installation tarball.
Store location of path in `$TARBALL` variable. This  variable will be
used in our installation.

```bash
export TARBALL=path of tarball file
```

Second, we extract tarball

```bash
$ tar -xf $TARBALL
```

Third, we define variable for storing path of configuration file 

```bash
export PECONFPATH=path of pe.conf file
```

Fourth, we specify console admin password in `pe.conf` file
and use default certificate

Fifth, we run installer from installer directory

```bash
sudo ./puppet-enterprise-installer -c PECONFPATH
```


Lastly, we run puppet twice after installation is complete

```bash
puppet agent `-t` 
```


### Text mode split installation

Compared to monolithic installation split installation type
can manage large infrastucture that requires more than 20,000
nodes.  In this type of installation different components of 
Puppet Enterprise ( master, PuppetDB and Console ) are installed
on different nodes. This installation type is recommended for
organizations with large infrastructure needs[hid-sp18-523-split]. 


In this type of installation, we need to install componenets in 
specific order. First master then puppet db followed by console.

#### Install Puppet master

First, we unpack installation tarball

```bash
$ tar -xf <TARBALL_FILENAME>
```

Second, we run installer from installed directory. 
we run it with  `-c` flag pointed to 
`pe.conf` if parameters have already been populated.


```bash
$ sudo ./puppet-enterprise-installer -c PECONFPATH
```

if parameters values are not already defined in `peconf`
file, we run command without `-c` flag

```bash
$ sudo ./puppet-enterprise-installer
```

Third, we select text-mode when prompted. `pe.conf` file will be opened

Fourth, we change master node related configuration parameters such as
host name

Installation will begin after file is saved and closed.

When installation is completed, transfer installer and pe.conf file 
located at `PECONFPATH` to next server if we need to set up
infrastructure with multiple puppet masters.

#### Install PuppetDB

PuppetDB stores details of relations, nodes and resources
of whole infrastructure.

we need to install PuppetDB after successful installation of
master.

First, we unpack installation tarball

```bash
$ tar -xf <TARBALL_FILENAME>
```

Second, we run installer from installation directory

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

Third, we select text-mode when prompted. `pe.conf` file will be opened


Fourth, we edit value of `puppet_enterprise::puppet_master_host` 
parameter to puppet master host name and change other database
related configuration parameter values

Installation will begin after file is saved and closed.

Transfer installer and `pe.conf` file to next puppet db server 
in case if infrastructure with multiple PuppetDB server needs to be set up.


#### Install the console

Console is installed after installing master and PuppetDB.

First, we unpack installation tarball

```bash
$ tar -xf <TARBALL_FILENAME>
```

Second, we run installer from installation directory

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

Third, we select text-mode when prompted. `pe.conf` file will be opened

Fourth, we edit value of `puppet_enterprise::puppet_master_host` 
parameter to puppet master host name

Installation will begin after file is saved and closed.

#### Run Puppet on infrastructure nodes

To complete split installation, run Puppet on all infrastructure 
nodes in same order as they were installed.

* Run Puppet on master node.
* Run Puppet on PuppetDB node.
* Run Puppet on master node a second time.
* Run Puppet on console node.

## Configuring Puppet

`puppet.conf` is main puppet configuration file. Most configuration settings 
of Puppet Enterprise componenets such as Master, Agent and security certificates 
are all specified in this file.

Config section of Agent Node

[main]

```bash
certname = <http://testing.hid520-hid523.com/>
server = puppetserver
environment = testing
runinterval = 4h
```

Config section of Master Node

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

Comment lines, Settings lines and Settings variables are main
components of puppet configuration file. Comments in config files 
are specified by prefixing hash character.Setting line consists 
name of setting followed by equal sign, value of setting are specified 
in this section. Setting variable value generally consists of one word 
but multiple can be specified in rare cases[hid-sp18-523-config].

## Setting up Puppet master

Puppet server software is installed on puppet master node which then
pushes configuration to clients nodes(puppet agents).

Pull software package from repository.

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

Install puppetserver package on master node

```bash
$ sudo yum -y install puppetserver
```

By default 2GM memory is allocated, but it can be configured based on
available memory as well as number of puppet agent nodes.  

Open configuration file to change configured value

```bash
$ sudo vi /etc/sysconfig/puppetserver
```

For example set value of variable to increase memory to 3GB
by adding 3g after -Xmx to `JAVA_ARGS`. 

```bash
JAVA_ARGS="-Xms3g -Xmx3g"
```

Start puppet server 

```bash
$ sudo systemctl start puppetserver
```

Start puppet server after master server is started.

```bash
$ sudo systemctl enable puppetserver
```

## Installing puppet agent


Puppet agent is installed on all nodes that needs to be part of 
managed network. Puppet master can not reach and manage any node 
that does  not have puppet agent installed.  
Puppet agent can be installed and run on any Linux, Unix or 
windows based platforms[hid-sp18-523-agent].


First, we need to connect to puppet repository

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

Second, we need to install Puppet agent

```bash
$ sudo yum -y install puppet-agent
```

Third, we need to enable agent

```bash
$ sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true
```
 
Once puppet agent is installed and runs for first time, it
generates a SSL certificate and sends it to the master for
signing. Puppet master communicates and manages client nodes after 
certificate is signed.

Each puppet client node that needs to be managed with puppet
is required to follow this process[hid-sp18-523-agent].

First, we want to view all requests on master


```bash $ sudo /opt/puppetlabs/bin/puppet cert list --all ```

cryptographic hash value of agent node will be displayed

```bash

+ "host1.hid523.example.com" (SHA256) F5:DC:68:24:63:E6:F1:9E:C5:
FE:F5:1A:90:93:DF:19:F2:28:8B:D7:BD:D2:6A:83:07:BA:FE:24:11:24:54:6A

"host2.hid523.example.com" (SHA256) F5:DC:68:24:63:E6:F1:9E:C5:
FE:F5:1A:90:93:DF:19:F2:28:8B:D7:BD:D2:6A:83:07:BA:FE:24:11:24:54:6A

```

output staring with + are signed request where as lines that 
does not begin with + sign are unsigned request.


Second, we we need to sign unsigned request


```bash
$ sudo /opt/puppetlabs/bin/puppet cert sign host2.hid523.example.com
```

Puppet master is now ready to communicate and manage client nodes


Lastly, we can remove specific agent node from puppet infrastructure
for debugging or investigation.

```bash
$ sudo /opt/puppetlabs/bin/puppet cert clean hostname
```


# Managing puppet environment through tool

r10k is pupper environment management tool that is used for managing 
configurations related to different environments such as testing, staging 
and production. Configuration information is stored in central repository. 
r10k tool creates an environment on puppet master and then uses modules 
stored in repo to install and update the environment[@hid-sp18-523-r10k]. 

Install r10k tool 

```bash
$ urlgrabber -o /etc/yum.repos.d/timhughes-r10k-epel-6.repo 
[https://copr.fedoraproject.org/coprs/timhughes/yum]
(https://copr.fedoraproject.org/coprs/timhughes/yum)
-y install rubygem-r10k
```

Configure environment in /etc/puppet/puppet.conf for r10k

```bash
[main]
environmentpath = $confdir/environments
```

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

Puppet manifest for Puppet module needs to be compiled in order to
test and validate if environment is working correctly.  

Get YAML manifest for puppet environment

```bash
$ curl --cert /etc/puppet/ssl/certs/puppet.corp.guest.pem \
--key /etc/puppet/ssl/private_keys/puppet.corp.guest.pem \
--cacert /etc/puppet/ssl/ca/ca_crt.pem \-H 'Accept: yaml' \
```



## Reference

:o: add bibtex

* <https://puppet.com/docs/pe/2017.3/installing_pe.html#concept-3157> 
* <https://puppet.com/docs/pe/2017.3/installing_pe.html> --install
* <https://puppet.com/docs/puppet/5.3/config_file_main.html> --config
* <https://fullstack-puppet-docs.readthedocs.io/en/latest/puppet_master.html> r10k
* <https://www.digitalocean.com/community/tutorials/how-to-install-puppet-to-manage-your-server-infrastructure#install-puppet-agent> -- puppet agent
* <https://puppet.com/docs/pe/2017.1/install_text_mode_mono.html> -- mono
* <https://puppet.com/docs/pe/2017.1/install_text_mode_split.html> -- split
* Images - are taken form from <https://www.edureka.co/blog/videos/puppet-tutorial/> devops class
