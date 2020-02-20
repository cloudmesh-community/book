# Vagrant :o2: {#sec:vagrant} 

---

![](images/learning.png) **Learning Objectives**

* Be able to experiment with virtual machines on your computer before you go on a cloud.
* Simulate a virtual cluster with multiple VMs running on your computer if it is big enough.

---

A convenient tool to interface with Virtual Box is vagrant. Vagrant
allows us to manage virtual machines directly from the command-line. It
also supports other providers and can be used to start virtual machines
and even containers. The latest version of vagrant includes the
ability to automatically fetch a virtual machine image and start it on
your local computer. It assumes that you have virtualbox installed.
Some key concepts and advertisement are located at

* <https://www.vagrantup.com/intro/index.html>:

Detailed documentation for it is located

* <https://www.vagrantup.com/docs/index.html>


A list of *boxes* is available from

* <https://app.vagrantup.com/boxes/search>

One image we will typically use is Ubuntu 18.04. Please note that
older versions may not be suitable for class, and we will not support
any questions about them. This image is located at

* <https://app.vagrantup.com/ubuntu/boxes/bionic64>

## Installation

Vagrant is easy to install. You can go to the download page and
download and install the appropriate version:

* <https://www.vagrantup.com/downloads.html>

### macOS

On MacOS, download the dmg image and click on it. You will find a pkg
in it that you double click. After installation vagrant is installed in

* `/usr/local/bin/vagrant`

Make sure `/usr/local/bin` is in your `PATH`
Start a new  terminal to verify this.

Check it with

```
echo $PATH
```

If it is not in the path put

export PATH=/usr/local/bin:$PATH

in the terminal command or in your `~/.bash_profile`

### Windows :o2:

![Question](images/question.png) students contribute

### Linux :o2:

![Question](images/question.png) students contribute

Vagrant can be installed on linux through multiple ways. Before you install vagrant on Linux, first make sure VirtualBox is installed.

On Ubuntu, you can install using 

* apt install

```bash

sudo apt install vagrant

```

* Manual Zip Download

Download the zip file for linux from <https://www.vagrantup.com/downloads.html> and unzip the zip file.

* Automated Zip Download

Alternatively, you can use the following bash commands to pick the latest zip and unzip it to ~/software folder.

``` bash
export VAGRANT_URL=https://www.vagrantup.com/downloads.html
#Curl and extract the zip file url from the download page
export VAGRANT_FILE_URL=`curl $VAGRANT_URL 2>&1 | grep -o -E 'href="([^"#]+)"' | cut -d'"' -f2 | grep -E 'vagrant_[0-9.]*_linux_amd64.zip'`

wget -O ~/Downloads/vagrant_latest_amd64.zip $VAGRANT_FILE_URL
#Unzip the file into ~/softwares folder.
unzip -d ~/software ~/Downloads/vagrant_latest_amd64.zip
#Add vagrant to path
export PATH=$PATH:~/software
```

## Usage

To download, start and login into install the 18.04 image:

```
host$ vagrant init ubuntu/bionic64
host$ vagrant up
host$ vagrant ssh
```

Once you are logged in you can test the version of python with

```bash
vagrant@ubuntu-bionic:~$ sudo apt-get update
vagrant@ubuntu-bionic:~$ python3 --version
Python 3.6.5
```

To install a newer version of python, and pip you can use

```bash
vagrant@ubuntu-bionic:~$ sudo apt-get install python3.7
vagrant@ubuntu-bionic:~$ sudo apt-get install python3-pip
```

To install the lightweight idle development environment in case you do
not want o use pyCharm, please use

```bash
vagrant@ubuntu-bionic:~$ sudo apt-get install idle-python
```

So that you do not always have to use the number 3, you can also set
an alias with

```bash
alias python=python3
```

When you exit the virtual machine with the

```
exit command
```

It does not terminate the VM. You can use from your host system the
commands such as

```bash
host$ vagrant status
host$ vagrant destroy
host$ vagrant suspend
host$ vagrant resume
```

to manage the vm.
