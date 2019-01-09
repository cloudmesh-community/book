# Vagrant {#sec:vagrant}

---

**:mortar_board: Learning Objectives**

* Be able to experiment with virtual machines on your computer before you go on a cloud.
* Simulate a virtual cluster with multiple VMs running on your computer if it is big enough.

---

A convenient tool to interface with Virtual Box is vagrant.Vagrant
allows us to manage virtual machines directly from the commandline. It
support also other providers and can be used to start virtual machines
and even containers. The latest version of vagrant includes the
ability to automatically fetch a virtual machine image and start it on
your local computer. It assumes that you have virtual box installed.
Some key concepts and advertisement are located at

* <https://www.vagrantup.com/intro/index.html>:

Detailed documentation for it is located

* <https://www.vagrantup.com/docs/index.html>


A list of *boxes* is available from 

* <https://app.vagrantup.com/boxes/search>

One image we will typically use is Ubuntu 18.04. Please note that
older version may not be suitable for class and we will not support
any questions about them. This image is located at

* <https://app.vagrantup.com/ubuntu/boxes/bionic64>

## Installation

Vagrant is easy to install. You can go to the download page and
download and install the appropriate version:

* <https://www.vagrantup.com/downloads.html>

### macOS

On MacOS, download the dmg image, and click on it. You will find a pkg
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

### Windows :o: :question: 

:question: students contribute

### Linux :o: :question: 

:question: students contribute

## Usage

To download, start and login into install the 18.04:

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

To install the light weight idle development environment in case you do
not want o use pyCharm, please use 

```bash
vagrant@ubuntu-bionic:~$ sudo apt-get install idle-python
```

So that you do not have to always use the number 3, you can also set
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
