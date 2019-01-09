# Puppet :wave:

## Overiew

:o: overview needs to be changed as its part of the devops section and we need to avoid repetition. We will do change once it is integrated.

Configuration management is an important task of IT department in any 
organization. It is a process of managing changes in infrastructure 
in a structured and systematic way. Configuring large infrastructure 
has always been a tedious task. Moreover in case of any technical 
glitches when updating software, manual rolling back the infrastructure 
to previous version of the software is time consuming and error prone. 
Puppet is a configuration management tool that makes the complex task 
of deploying new software, updating software updates , rolling back 
software on large cluster easily and in efficient way. Puppet does this 
through Infrastructure as Code (IAC). In this process code is written for 
infrastructure on one central location and is pushed to all the nodes 
in all environments (Dev, Test, Production) using puppet as tool. 
Configuration management tool has two approaches for managing infrastructure 
configuration push and pull. In push configuration, infrastructure as 
code is pushed from centralized server to the nodes where as in pull 
configuration nodes pulls the infrastructure as code from central server 
as shown in +@fig:InfrastructureAsCode. 

![Infrastructure As Code](Images/IAC.jpg){#fig:InfrastructureAsCode}

[hid-sp18-523-puppetimages]

Puppet uses push and pull configuration in centralized manner 
as shown in +@fig:push-pull-configImage. :o: contarst this to ansible.

![push-pull-config Image](Images/push-pull-configuration.jpg){#fig:push-pull-configImage}

[hid-sp18-523-puppetimages]

## Master Slave Architecture

:o: grammar errors in regards to the usage of a and the

Puppet uses a master slave architecture as shown below +@fig:master-slaveImage. 
There is puppet master node and client nodes called as puppet agent. 
Agents poll the server at regular interval and pulls the updated 
configuration from the master. Puppet Master is highly available :o: as 
it supports multi master architecture, in case if one goes down backup 
master stands up to serve the infrastructure. In this architecture :o:

* nodes(puppet agents) sends the information(for e.g IP, hardware detail, 
network etc.) to master. Master stores such information in the manifest.

* :o: Puppet master then compiles the catalog which is the information about 
the configuration that master wants the client resources also known as 
puppet agent to implement.

* :o: Master sends the catalog to puppet agent nodes to implement the 
desired configuration.

* Client nodes sends :o: back the updated report to Master

* :o: Connection between master and slave is SSL encrypted (Refer to 
Puppet Master Slave Connection figure below)

![Master and Slave Architecture](Images/master-slave.jpg){#fig:master-slaveImage}

[hid-sp18-523-puppetimages]

In +@fig:master-slave1Image, we can see :o: flow between master and slave.

![Master Slave Workflow 1](Images/master-slave1.jpg){#fig:master-slave1Image}

[hid-sp18-523-puppetimages]

+@fig:master-slave-connection Image, we can see the SSL workflow for 
master and slave

![Master  Slave SSL Workflow](Images/master-slave-connection.jpg){#fig:master-slave-connection Image}

[hid-sp18-523-puppetimages]

## Installation

To install puppet you need to do the following:

* Download the tarball as per the operating system and architecture. 

For Ubuntu download -ubuntu-<version and arch>.tar.gz

:o: we never use below and above

* Import the Puppet public key using below command

```bash
$ wget -O - [https://downloads.puppetlabs.com/puppet-gpg-signing-key.pub]
(https://downloads.puppetlabs.com/puppet-gpg-signing-key.pub)  | 
gpg --import
```
:o: hyperlink in code illeagal

- Print the fingerprint of the key using below command

```bash
$ gpg --fingerprint 0x7F438280EF8D349F
```

- Verify the release signature of the installation package.

```bash
$ gpg --verify puppet-enterprise-<version>-<platform>.tar.gz.asc
```

### Install using a Configration file (Master/Client installation)

Specify the configuration file `pe.conf` when it has to be installed 
in text mode. This file contains values for the parameters needed for 
installation. :o: unclear

#### Install the Master

- Unpack the installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

* From the installer directory, run the installer. The installation 
steps vary depending on the path. To use a pe.conf file that have 
been previously populated, run the installer with the -c flag 
pointed at the pe.conf file.

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

To have the installer open a copy of pe.conf for editing, 
run the installer without the -c flag.

```bash
$ sudo ./puppet-enterprise-installer
```

* When installation is completed, transfer the installer and pe.conf file 
located at /etc/puppetlabs/enterprise/conf.d/ to the next server for 
installation.

#### Install Puppet DB

PuppetDB, stores the details on the relations, nodes, resources
for the whole architecture. This information can be accessed 
any tool or workflow.

In a split installation, after installing the master, its ready to 
install PuppetDB.

* Unpack the installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

:o: not defined previously use `$TARBALL_FILENAME`

* From the installer directory, run the installer:

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

* When installation completes, transfer the installer and the pe.conf 
file located at/etc/puppetlabs/enterprise/conf.d/ to the next server.

:o: this can be done differently

#### Install using console

:o: what is a split instalation

In a split installation, after installing master and PuppetDB, 
are ready to install from console.

- Unpack the installation tarball:

```bash
$ tar -xf <TARBALL_FILENAME>
```

- From the installer directory, run the installer:

```bash
$ sudo ./puppet-enterprise-installer -c <FULL PATH TO pe.conf>
```

#### Run Puppet on the infrastructure nodes

To complete a split installation, run Puppet on all infrastructure 
nodes in the order that they were installed.

* Unpack the installation tarball:

:o: illegal bullets

** Run Puppet on the master node.  
** Run Puppet on the PuppetDB node.  
** Run Puppet on the master node a second time.  
** Run Puppet on the console node.

## Configuring Puppet

### Puppet.conf

This is the main puppet configuration file. Most settings such as 
Master, Agent, certificates are all specified in this file.

### Agent Config Section

Below is the example

[main]

```bash
certname = <http://testing.hid520-hid523.com/>
server = puppetserver
environment = testing
runinterval = 4h
```

:o: gregor commented till here. will do other later

### Puppet Master Config File

Below is the example

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

### Key Components of Config File

Comments Lines, Settings Lines and Settings Variables are the 
main components of puppet

configuration file. comments in config files are specified by 
prefixing hash character

Setting line consists the name of the setting followed by equal sign , 
value of the setting would be specified in this section. Setting variable 
value generally consists of one word but multiple can be specified in 
rare cases.

## Setting up Puppet Master

Puppet server software is installed on puppet master machine which then 
pushes the configuration to clients nodes(puppet agents).

Following command is used to pull the software package from the repository.

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

Install puppetserver package.

Following command is used to install the server on master node

```bash
$ sudo yum -y install puppetserver
```

By default 2GM memory is allocated, but it can be configured based on 
available memory as well as number of puppet agent nodes.
Use following command to edit the server configuration

```bash
$ sudo vi /etc/sysconfig/puppetserver
```

Set the value of the following variable to increase memory to 3GB
(3g after -Xmx specify that)

```bash
JAVA_ARGS="-Xms3g -Xmx3g"
```

Start the puppet server using following command

```bash
$ sudo systemctl start puppetserver
```

Following command automatically starts the puppet server when master 
server is started.

```bash
$ sudo systemctl enable puppetserver
```

# Installing puppet agent

:o: Puppet agent is a software that needs to be installed on all the nodes 
that needs to be part of network that which has to be manage d and control 
through puppet. :o: Puppet master can not reach and manage any node that does 
not have puppet agent installed. so, it is required for software for managing 
any puppet infrastructure. Puppet agent software can be installed and run on 
any Linux, Unix or windows based machines.

### Steps to install Puppet agent software

* Use :o: following command for puppet repository.

```bash
$ sudo rpm -ivh 
[https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm]
(https://yum.puppetlabs.com/puppetlabs-release-pc1-el7.noarch.rpm)
```

* Use :o: following command to Install the Puppet agent.

```bash
$ sudo yum -y install puppet-agent
```

* Use following command to enable agent.

```bash
$ sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true
```

As explained in :o: workflow section and :o: digram in :o: above section :o: ; When the 
puppet agent is installed and run first time it generates SSL certificate 
and sends it to master for signing, once the certificate is approved 
master can communicate and mage the client node.

Each puppet client node in the puppet infrastructure needs to follow this process

# Configuring SSL

As explained :o: above, SSL certificate approval by puppet master is required 
for all the nodes in the infrastructure in order for master to communicate 
and manage client nodes. Following will describe the SSL signing process-

Use the following command on :o: puppet master to in order to list all unsigned 
certificate requests.

```bash
$ sudo /opt/puppetlabs/bin/puppet cert list
```

### View the requests

If the new agent node is set up, :o: request similar to following will be displayed
(Note - :o: Below certificate name is for illustration purpose only.)

* <http://test.hid520-hid523.com/> (SHA259)

15:90:C2:FB:ED:69:A4:F7:B1:87:0B:BF:F7:ll:B5:1C:33:F7:76:67:F3:F6:45:AE:07:4B:F

6:E3:ss:04:11:8d

Identification of signed/un-signed certificate is done by looking at the 
+ sign in the beginning. Absence of + sign indicate that certificate is not signed.

### Sign a Request

:o: Following command is run on puppet master in order to sign the new certificate 
request that is sent by puppet agent(client node) for approval(signing)

Note - <http://test.hid520-hid523.com/> (SHA259) certificate name is used for 
illustration and example only

```bash
$ sudo /opt/puppetlabs/bin/puppet cert sign  
[test.hid520-hid523.com](http://test.hid520-hid523.com/)
```

:o: Following will be the output.

Notice: Signed certificate request for <http://test.hid520-hid523.com/>

Notice: Removing file Puppet::SSL::CertificateRequest 
<http://test.hid520-hid523.com/> 
at '/etc/puppetlabs/puppet/ssl/ca/requests/test.hid520-hid523.com.pem'

After certificate approval :o: Puppet master can now communicate and 
manage the client node

```bash
$ sudo /opt/puppetlabs/bin/puppet cert sign --all
```

### Removing and adding puppet agent

:o: inconsistent capitalization 

Sometimes there is a need to remove the puppet agent node from puppet 
infrastructure and then add again in order to debug any issue or 
rebuilding it. This can be done using following command

```bash
$ sudo /opt/puppetlabs/bin/puppet cert clean hostname
```

### Viewing All Signed Requests

Use the following command to list all the certificates that are signed
(Note + sign in the beginning indicates signed certificate).

```bash
$ sudo /opt/puppetlabs/bin/puppet cert list --all
```

Following will be its output details .

+ "puppet"(SHA256)

5A:71:E6:06:D8:0F:44:4D:70:F0:BE:51:72:15:97:68:D9:67:16:41:B0:38:9A:F2:B2:6C:B

B:33:7E:0F:D4:53 (alt names: "DNS:puppet", 
"DNS:[test.hid520-hid523.puppetproject.com]
(http://test.hid520-hid523.puppetproject.com/)")

+ "[test.hid520-hid523.com](http://test.hid520-hid523.com/)"(SHA259)

F5:DC:68:24:63:E6:F1:9E:C5:FE:F5:1A:90:93:DF:19:F2:28:8B:D7:BD:D2:6A:83:07:BA:F

E:24:11:24:54:6A

+ "  [test.hid520-hid523.com](http://test.hid520-hid523.com/)"(SHA259)

CB:CB:CA:48:E0:DF:06:6A:7D:75:E6:CB:22:BE:35:5A:9A:B3

# Managing puppet environment through tool

:o: In puppet environment mangement tool known as r10k is used for managing 
configurations related to different environments such as testing, staging 
and production etc. These configuration related information is stored in 
central repository. r10k tool creates environment on puppet master and 
then use modules stored in repo to install and update the environment
Following command is used on any node to install r10k tool

```bash
$ urlgrabber -o /etc/yum.repos.d/timhughes-r10k-epel-6.repo 
[https://copr.fedoraproject.org/coprs/timhughes/yum]
(https://copr.fedoraproject.org/coprs/timhughes/yum)  
-y install rubygem-r10k
```

### Configure environment in /etc/puppet/puppet.conf for r10k

[main]
environmentpath = $confdir/environments

### Create a Configuration File for r10k Config

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

### Installing Puppet Manifest and Module

r10k deploy environment -pv

Since the environment needs to be updated at regular intervals it is 
recommended to create :o: cron job.

```bash
$ cat << EOF > /etc/cron.d/r10k.conf SHELL=/bin/bash 
PATH=/sbin:/bin:/usr/sbin:/usr/bin H/15 
* * * * root r10k deploy environment -p EOF
```

### Testing Installation

Puppet manifest for Puppet module needs to be complied in order to 
test and validate if the environment is working correctly.
Run the following command and inspect the YAML output.

```bash
$ curl --cert /etc/puppet/ssl/certs/puppet.corp.guest.pem \
--key /etc/puppet/ssl/private_keys/puppet.corp.guest.pem \
--cacert /etc/puppet/ssl/ca/ca_crt.pem \-H 'Accept: yaml' \
```

## Reference

:o: add bibtex

* <https://www.google.com/url?q=https://puppet.com/docs/pe/2017.3/installing/installing_pe.html%23concept-3157&sa=D&source=hangouts&ust=1522821857125000&usg=AFQjCNEPcs-uZes-m-fZYqK2WcTfkYRPLQ> 
* Images - are taken form from <https://www.edureka.co/blog/videos/puppet-tutorial/> devops class
