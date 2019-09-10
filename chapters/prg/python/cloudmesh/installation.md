# Installation {#sec:cloudmesh-cms-install}

The installation of cloudmesh is simple and can technically done via pip
by a user. However you are not a user, you are a developer. Cloudmesh is
distributed in different topical repositories and in order for
developers to easily interact with them we have written a convenient
`cloudmesh-installer` program.

As developer you must also use a python virtual environment to avoid
affection you system wide python installation. This can be achieved while
using Python3 from python.org or via conda. We do recommend that you use
python.org as this is the vanilla python that most developers in the
world use. COnda is often used by users of python if they only want to
use (bleeding-edge but prepackaged) python tools and libraries.

## Prerequisite

We require you to create a python virtual environment and activate it.
How to do this we discuseed in @sec:python-install. Please create the
ENV3 environment. Please activate it.


## Basic Install

Cloudmesh can install for developers a number of `bundles`. A bundel is
a set of git repositories that are needed for a particular install. For
us we are mostly interested in the bundles `cms`, `cloud`, `storage`. We
will introduce you to the the bundels throughout this documentation. 

If you like to find out more about the details of this you can look at
[cloudmesh-installer](https://pypi.org/project/cloudmesh-installer/)
which will be regularly updated.

To make use of the bundle and the easy instalation for developers please
install the cloudmesh-installer via pip, but make sure you do thi sin a
python virtual env as discussed previously. If not you may impact your
system negatively. Please note that we are not responsible for fixing
your computer. You can use naturally a virtual machine if you prefer. It
is also important that we create a uniform development environment. In
our case we create an empty directory called `cm` in whcih we place the
bundle.

```bash
$ mkdir cm
$ cd cm
$ pip install cloudmesh-installer
```

To see the bundle you can use

```bash
$ cloudmesh-installer bundles
```

We will start with the basic cloudmesh functionality atthis time and
only install the shell and some common API's.

```bash
$ cloudmesh-installer git clone cms
$ cloudmesh-installer git install cms -e
```

These commands download and install cloudmesh shell into your
environment. It is important that you use the `-e` flag

To see if it works you can use the command


```bash
$ cms help
```

You will see an output. If this does not work for you, and you can not
figure out the issue, please get in contact with us so we can identify
what went wrong.

For more information, please visit our 
[Installation Instructions for Developers](https://cloudmesh.github.io/cloudmesh-manual/installation/install.html#source-installation-for-developers)  





