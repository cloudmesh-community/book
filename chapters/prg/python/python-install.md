# Python Installation {#sec:python-install}

---

![](images/learning.png) **Learning Objectives**

* Learn how to install Python.
* Find additional information about Python.
* Make sure your Computer supports Python.

---

In this section we explain how to install python 3.8 on a computer.
Likely much of the code will work with earlier versions, but we do
the development in Python on the newest version of Python available at
<https://www.python.org/downloads> .

## Hardware

Python does not require any special hardware. We have installed Python
not only on PC's and Laptops but also on Raspberry PI's and Lego
Mindstorms.

However, there are some things to consider. If you use many programs on
your desktop and run them all at the same time, you will find that in
up-to-date operating systems, you will find your self quickly out of
memory. This is especially true if you use editors such as PyCharm
, which we highly recommend. Furthermore, as you likely have lots of disk
access, make sure to use a fast HDD or better an SSD.

A typical modern developer PC or Laptop has *16GB RAM* and an *SSD*. You
can certainly do Python on a $35-$55 Raspberry PI, but you probably will not
be able to run PyCharm. There are many alternative editors with less
Memory footprint available.

## Prerequisites for Ubuntu

:o2: Assignment: which version of Python is installed in which version of ubuntu
by default? Please provide the info for, 18.04, 19.10. Provide instructions on
how to install the newest python version 3.8 released on python.org from the
command line.

Python 3.7 is installed in ubuntu 19.10. Therefore, it already fulfills
the prerequisites. However, we recommend that you update to the newest
version of Python and pip. However, we recommend that you update the
newest version of Python. Please visit:
<https://www.python.org/downloads>

## Prerequisites macOS

### Installation from the Apple App Store

You want a number of useful tools on your macOS. They are not installed
by default but are available via Xcode. First, you need to install XCode
from

* <https://apps.apple.com/us/app/xcode/id497799835>

Next, you need to install macOS XCode command-line tools:

```bash
$ xcode-select --install
```

### Installation from python.org

The easiest installation of Python for Cloudmesh is to use the installation
from <https://www.python.org/downloads>. Please, visit the page and
follow the instructions. After this install, you have
python3 available from the command-line.

### Installation from Homebrew

Homebrew may not provide you with the newest version, so we recommend using the
install from python.org if you can.

An alternative installation is provided from Homebrew. To use this
install method, you need to install Homebrew first. Start the process by
installing Python 3 using `homebrew`. Install `homebrew` using the
instruction in their [web page](https://brew.sh/#install):

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then you should be able to install Python using:

```bash
$ brew install python
```


## Prerequisites Python 3.8 on Ubuntu 18.04

We recommend you update your Ubuntu version to 19.10 and follow the
instructions for that version instead, as it is significantly easier. If
you, however, are not able to do so, the following instructions may be
helpful.

We first need to make sure that the correct version of the Python3 is
installed. The default version of Python on Ubuntu 18.04 is 3.6.
However, this version is insufficient for us and **must** be updated.
You can get the version while doing the following steps:


```bash
$ sudo apt-get update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa -y
$ sudo apt-get install python3.8 python3-dev -y
```

Now you can verify the version with 

```bash
$ python3.8 --version
```

which should be `3.8.1` or newer.

Now we will create a new virtual environment:

```bash
$ python3.8 -m venv --without-pip ~/ENV3
```

The edit the `~/.bashrc` file and add the following line at the end:

```bash
alias ENV3="source ~/ENV3/bin/activate"
ENV3
```

Now activate the virtual environment using:

```bash
$ source ~/.bashrc
```

You can install the pip for the virtual environment with the commands:

```bash
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python get-pip.py
$ rm get-pip.py
```

## Prerequisite Windows 10

Python 3.8 can be installed on Windows 10 using:
<https://www.python.org/downloads>


Let us assume you choose the Web-based installer than you click on the
file in the edge browser (make sure the account you use has
administrative privileges). Follow the instructions that the installer
gives. Important is that you select at one point `[x] Add to Path`.
There will be an empty checkmark about this that you will click on.

Once it is installed chose a terminal and execute

```bash
python --version
```


However, if you have installed conda for some reason, you need to read up
on how to install 3.8 Python in conda or identify how to run conda and
python.org at the same time. We often see others giving the wrong
installation instructions.

An alternative is to use Python from within the Linux Subsystem. But
that has some limitations, and you will need to explore how to access the
file system in the subsystem to have a smooth integration between your
Windows host so you can, for example, use PyCharm. 

### Linux Subsystem Install

To activate the Linux Subsystem, please follow the instructions at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10>

A suitable distribution would be

* <https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab>

However, as it uses an older version of Python, you will have to update
it. We also find on the MongoDB web page that MongoDB is not supported in Linux Subsystem.

## Prerequisite venv

This step is needed if you have not yet already installed a
`venv` for Python to make sure you are not interfering with your system
python. Not using a venv could have catastrophic consequences and the
destruction of your operating system tools if they really on Python. The
use of `venv` is simple. For our purposes we assume that you use the
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
Cloudmesh.

Check if you have the right version of Python installed with

```bash
$ python --version
```

To make sure you have an up to date version of pip issue the command

```bash
$ pip install pip -U
```

## Install Python 3.7 via Anaconda

:o2: We are not recommending ether to use conda or anaconda. If you do so, it is
in your responsibility to update the information in this section in regards to
it. We will check your python installation, and if you use conda and anaconda you
need to work on completing this section.

### Download `conda` installer

Miniconda is recommended here. Download an installer for Windows, macOS,
and Linux from this page: <https://docs.conda.io/en/latest/miniconda.html>

### Install `conda`

Follow instructions to install `conda` for your operating systems:

* Windows. <https://conda.io/projects/conda/en/latest/user-guide/install/windows.html>
* macOS. <https://conda.io/projects/conda/en/latest/user-guide/install/macos.html>
* Linux. <https://conda.io/projects/conda/en/latest/user-guide/install/linux.html>

### Install Python via `conda`

To install Python 3.8.1 in a virtual environment with conda please use 

```bash
$ cd ~
$ conda create -n ENV3 python=3.8.1
$ conda activate ENV3
$ conda install -c anaconda pip
$ conda deactivate ENV3
```

It is very important to make sure you have a newer version of pip installed.
After you installed and created the ENV3 you need to activate it. This
can be done with

```bash
$ conda activate ENV3
```

If you like to activate it when you start a new terminal, please add
this line to your `.bashrc` or `.bash_profile`

If you use zsh please add it to `.zprofile` instead.
