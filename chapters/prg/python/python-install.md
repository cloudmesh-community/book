# Python 3.7.4 Installation {#sec:python-install}

---

![](images/learning.png) **Learning Objectives**

* Learn how to install python.
* Find additional information about Python.
* Make sure your Computer supports Python.

---

In this setion we explain how to install python 3.7.4 on a computer.
Likely much of the code will work with earlier versions, but we do
the development in Python on the newest version of python available at
<https://www.python.org/downloads> .

## Hardware

Python does not require any special hardware. We have installed Python
not only on PC's and Laptops, but also on Raspberry PI's and Lego
Mindstorms.

However, there are some things to consider. If you use many programs on
your desktop and run them all at the same time you will find that in
up-to-date operating systems you will find your self quickly out of
memmory. This is especially true if you use editors such as PyCharm
which we highly recommend. Furthermore, as you likely have lots of disk
access, make sure to use a fast HDD or better an SSD.

A typical modern developer PC or Laptop has *16GB RAM* and an *SSD*. You
can certainly do python on a $35 Rapbperry PI, but you probably will not
be able to run PyCharm. There are many alternative editors with less
Memory footprint avialable.

## Prerequisits Ubuntu 19.04

Python 3.7 is installed in ubuntu 19.04. Therefore, it already fulfills
the prerequisits. However we recommend that you update to the newest
version of python and pip. However we recommend that you update the the
newest version of python. Please visit:
<https://www.python.org/downloads>

## Prerequisits macOS

### Installation from Apple App Store

You want a number of useful tool on your macOS. They are not installed
by default, but are available via Xcode. First you need to install xcode
from

* <https://apps.apple.com/us/app/xcode/id497799835>

Next you need to install macOS xcode command line tools:

```bash
$ xcode-select --install
```

### Installation from python.org

The easiest instalation of Python for cloudmesh is to use the instaltion
from <https://www.python.org/downloads>. Please, visit the page and
follow the instructions. After this install you have
[python3]{.title-ref} avalable from the commandline

### Installation from Hoembrew

An alternative instalation is provided from Homebrew. To use this
install method, you need to install Homebrew first. Start the process by
installing the python 3 using `homebrew`. Install `homebrew` using the
instruction in their [web page](https://brew.sh/#install):

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then you should be able to install Python 3.7.4 using:

```bash
$ brew install python
```

## Prerequisits Ubuntu 18.04

We recommend you update your ubuntu version to 19.04 and follow the
instructions for that version instead, as it is significantly easier. If
you however are not able to do so, the following instructions may be
helpful.

We first need to make sure that the correct version of the Python3 is
installed. The default version of Python on Ubuntu 18.04 is 3.6. You can
get the version with:

```bash
$ python3 --version
```

If the version is not 3.7.4 or newer, you can update it as follows:

```bash
$ sudo apt-get update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get install python3.7 python3-dev python3.7-dev
```

You can then check the installed version using `python3.7 --version`
which should be `3.7.4`.

Now we will create a new virtual environment:

```bash
$ python3.7 -m venv --without-pip ~/ENV3
```

The edit the `~/.bashrc` file and add the following line at the end:

```bash
alias ENV3="source ~/ENV3/bin/activate"
ENV3
```

now activate the virtual environment using:

```bash
$ source ~/.bashrc
```

now you can install the pip for the virtual environment without
conflicting with the native pip:

```bash
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python get-pip.py
$ rm get-pip.py
```

## Prerequisite Windows 10

Python 3.7 can be installed on Windows 10 using:
<https://www.python.org/downloads>

For 3.7.4  can go to the
[download page](https://www.python.org/downloads/release/python-374/) and
download one of the different files for Windows.

Let us assume you choe the Web based installer, than you click on the
file in the edge browser (make sure the account you use has
administrative priviledges). Follow the instructions that the installer
gives. Important is that you select at one point "[x] Add to Path".
There will be an empty checkmark about this that you will click on.

Once it is installed. chose a terminal and execute

```bash
python --version
```


However, if you have installed conda for some reason  you need to read up
on how to install 3.7.4 python in conda or identify how to run conda and
python.org at the same time. We  see often others giving the wrong
installation instructions.

An alternative is to use python from within the Linux Subsystem. But
that has some limitations and you will need to explore how to exxess the
file system in the subssytem to have a smooth integration between your
Windows host so you can for example use PyCharm. 

### Linux Subsystem Install

To activate the Linux Subsystem, please follow the instructions at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10>

A suitable distribution would be

* <https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab>

However as it uses an older version of python you will ahve to update
it.

## Prerequisit venv

This step is highly recommend if you have not yet already installed a
`venv` for python to make sure you are not interfering with your system
python. Not using a venv could have catastrophic consequences and a
destruction of your operating system tools if they realy on Python. The
use of venv is simple. For our purposes we assume that you use the
directory:

```
~/ENV3
```

Follow these steps first:

First cd to your home directory. Then execute

```bash
$ python3 -m venv  ~/ENV3
$ source ~/ENV3/bin/activate
```

You can add at the end of your .bashrc (ubuntu) or .bash\_profile
(macOS) file the line

```bash
$ source ~/ENV3/bin/activate
```

so the environment is always loaded. Now you are ready to install
cloudmesh.

Check if you have the right version of python installed with

```bash
$ python --version
```

To make sure you have an up to date version of pip issue the command

```bash
$ pip install pip -U
```

## Install Python 3.7 via Anaconda

### Download `conda` installer

Miniconda is recommended here. Download an installer for Windows, macOS,
and Linux from this page: <https://docs.conda.io/en/latest/miniconda.html>

### Install `conda`

Follow instructions to install `conda` for your operating systems:

* Windows. <https://conda.io/projects/conda/en/latest/user-guide/install/windows.html>
* macOS. <https://conda.io/projects/conda/en/latest/user-guide/install/macos.html>
* Linux. <https://conda.io/projects/conda/en/latest/user-guide/install/linux.html>

### Install Python 3.7 via `conda`

```bash
$ conda create -n ENV3 python=3.7
```

### Activate and use Python 3.7

```bash
$ conda activate ENV3
```