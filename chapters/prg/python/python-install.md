# Python Installation {#sec:python-install}

---

![](images/learning.png) **Learning Objectives**

* Learn how to install Python.
* Find additional information about Python.
* Make sure your Computer supports Python.

---

In this section, we explain how to install python 3.10 on a computer.
Likely much of the code will work with earlier versions, but we do
the development in Python on the newest version of Python available at
<https://www.python.org/downloads> .

## Hardware

In general, using Python does not require any special hardware. We have installed Python
not only on PC's and Laptops but also on Raspberry PI's and Lego
Mindstorms.

However, there are some things to consider when developing code. If you use many programs on
your desktop and run them all at the same time, you discover  that in
a up-to-date operating systems you will quickly run out of
memory. This is not really a Python issue, but caused by other programs you may run on your computer
This is especially true if you use Web browsers and editors such as PyCharm, which we highly recommend.
Furthermore, as you likely have lots of disk
access, make sure to use a fast HDD we recommend using SSDs or NVMe storage.

A typical modern developer PC or Laptop has *16GB RAM* and an *SSD*. You
can certainly do Python on a $35-$75 Raspberry PI, but you probably will not
be able to run PyCharm. There are many alternative editors with less
memory footprint available. 

## Python 3.10

Here we discuss how to install Python 3.10 or newer on your operating system. It
is typically advantageous to use a newer version of Python, so you can leverage
the latest features. Please be aware that many operating systems come with
older versions that may or may not work for you. You always can start with the
version that is installed and if you run into issues update later.

### Python 3.10 on macOS

First,  you want tio install a number of useful tools on your macOS. 
This includes git, make, and a c compiler. All this can be installed with Xcode which is
available from

* <https://apps.apple.com/us/app/xcode/id497799835>

Once you have installed it, you need to install macOS XCode command-line
tools:

```bash
$ xcode-select --install
```

The easiest installation of Python is to use the installation from
<https://www.python.org/downloads>. Please, visit the page and follow the
instructions to install the python `.pkg` file. After this install, you have
python3 available from the command line.

### Python 3.10 on macOS via Homebrew

Homebrew provides you with an alternative installation. However we noticed that 
Homebrew may not provide you with the newest version, so we recommend
using the install from python.org if you can.

To use this install method, you need to install Homebrew first. Start
the process by installing first `homebrew`. Install `homebrew` using
the instruction documented on their [web page](https://brew.sh/#install):

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Now you can install Python using:

```bash
$ brew install python@3.10
```


## Python 3.10 on Ubuntu 20.04

The default version of Python on Ubuntu 20.04 may note yet be
3.01.2. Thus we recommend to check it with

```bash
$ python3 --version
$ python3.10 --version
```

If one ov the versions returns 3.10.5 you are all set. However if not
we recommend you update your python version as you can benefit from
newer version while either installing them through python.org or
adding them as follows:


```bash
$ sudo apt-get update -y
$ sudo apt-get upgrade -y
$ sudo apt install software-properties-common -y
$ sudo add-apt-repository ppa:deadsnakes/ppa -y
$ sudo apt-get install python3.10 python3-dev -y
```

Now you can verify the version with 

```bash
$ python3.10 --version
```

which should be `3.10.5` or newer.

Now we will create a new virtual environment:

```bash
$ python3.10 -m venv ~/ENV3
```
Now you must edit the `~/.bashrc` file and add the following line at the end:

```bash
alias ENV3="source ~/ENV3/bin/activate"
ENV3
```

Now activate the virtual environment using:

```bash
$ source ~/.bashrc
```

## Python 3.10.5 on Ubuntu 20.04 from Source

We can also install python from source. We have seen perfomance
improvements in some systems when we compilled it from source compared
to conda and other prebuild python versions. The compilation includes
a parameter CORES that indicates how many parallel cores are use. By
default we use all of them, however to reduce load you can for example
use just half of them. YOu can find out the number of cores with

```bash
nproc
```

Here the full instalation script

```bash
$ PYTHON_VESRION="3.10.5"
$ CORES=`nproc`
$ sudo apt-get update -y
$ sudo apt-get upgrade -y
$ sudo apt install -y build-essential zlib1g-dev libncurses5-dev
$ sudo apt install -y libgdbm-dev libnss3-dev libssl-dev libreadline-dev
$ sudo apt install -y libffi-dev libsqlite3-dev wget libbz2-dev
$ cd /tmp
$ wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
$ tar -xf Python-$PYTHON_VERSION.tgz
$ cd Python-$PYTHON_VERSION
$ ./configure --enable-optimizations
$ make -j $CORES
$ sudo make altinstall
$ python3.10 --version
$ sudo apt install python3-pip
$ python3.10 -m venv ~/ENV3
$ pip install pip -U
$ which python
$ which pip
```

The which commands should have the directory anme ENV3 in it.

## Python 3.10.5 on Windows 10

Python 3.10.5 can be installed on Windows 10 using:
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


However, if you have installed conda for some reason, you need to read up on
how to install 3.10.5 Python in conda or identify how to run conda and
python.org at the same time. We often see others are giving the wrong
installation instructions. Please also be aware that when you uninstall conda
it is not sufficient to just delete it. You will have to make sure that you unset
the system variables automatically set at install time. This includes.
modifications on Linux and or Mac in `.zprofile`, `.bashrc` and `.bash_profile`. In
windows, PATH and other environment variables may have been modified.


### Python in the Linux Subsystem

An alternative is to use Python from within the Linux Subsystem. It
has some limitations, and you will need to explore how to access the
file system in the subsystem to have a smooth integration between your
Windows host so you can, for example, use PyCharm. 


To activate the Linux Subsystem, please follow the instructions at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10>

A suitable distribution would be

* <https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab>

However, as it may use an older version of Python, you may want to update
it as previously discussed

## Using venv

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

You can add at the end of your `.bashrc` (ubuntu) or `.bash_profile` or
.zprofile` (macOS) file the line


If you like to activate it when you start a new terminal, please add
this line to your `.bashrc` or `.bash_profile` or `.zprofile` file.

```bash
$ source ~/ENV3/bin/activate
```

### How to Automatically Start Git Bash in venv on Windows

On Windows the Git Bash can be set to automatically use this venv by issuing these commands:

```bash
$ cd ~
$ vi .bashrc
```

Press the `i` key and then type

```vim
source ~/ENV3/Scripts/activate
```

After typing this command press `Enter` and then press the `Esc` key

```vim
:wq
```

After typing this command press `Enter`. Now every time a new instance
of Git Bash is launched, it will automatically be within a virtual
environment. The first time Git Bash is restarted after configuring
this, it will show an error, but this is normal.

### Confirm Python is installed

Now you are ready to install Cloudmesh.

Check if you have the right version of Python installed with

```bash
$ python --version
```

To make sure you have an up to date version of pip issue the command

```bash
$ pip install pip -U
```

## Install Python 3.10 via Anaconda or Miniconda

We are not recommending ether to use conda or anaconda. If you do so,
it is your responsibility to update the information in this section in
regards to it.


Anaconda is a popular and large distribution of the python ecosystem
frequently used by Data Scientists.  Unlike the other python
installers, anaconda installs additional tools beyond what is normally
considered part of python - such as the conda package management
system and an opinionated set of preinstalled packages.  Some
practitioners consider these additional package installs as bloat as
it increases the installation footprint of python to include several
third-party packages, which a user may not need.

Miniconda, in contrast installs only what is required to execute the
conda packaging system, allowing users to build their own anaconda
distribution from scratch without the additional libraries.

As of writing, only the conda-forge channel for anaconda supports
python versions greater than 3.10.  While you can change channels
during install to install the latest versions of python, it is
generally not recommended as anaconda does not guarantee that all of
its libraries will work properly with the community version of python.

Installing anaconda is straightforward, and all it requires is for
users to go through their guided procedures based on what OS you are
using.  You can find the latest instructions for

* [Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)
* [MacOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)
* [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)

in the conda instalation quide

---

![](images/warning.png) **conda init**

When installing Anaconda, it is important to not add it to the path or by running
`conda init`.  Doing either of these two steps will modify your command prompts and
system configuration to register the `(base)` environment of anaconda by default,
which will adversely interact with other versions of python installed outside of
anaconda.  This can result in unexpected command execution or runtime errors.

Instead, later in the instructions will configure your system to only expose the
conda command and not add any additional commands and keeping your path clear of
any unintentional binaries.

---

### Configuring `conda` to be on the path

There are many ways to place the `conda` command onto your path.  To
prevent polluting the command line path, we choose to only expose the
`conda` command and none of the environment's underlying binaries.
This can be done by doing the following for each OS.

#### Windows

Run the following at the command line.
```batch
setx PATH <path_to_conda_install>\condabin;%PATH%
```

If you are using git-bash or equivalent, follow the Linux/MacOS
instructions.

#### Linux / MacOS

Add the following line to your .bashrc, .bash_profile, or .zprofile

```bash
source <path_to_conda_install>/etc/profile.d/conda.sh
```

### Installing Python via `conda`

Once you have installed conda, you can  install Python 3.10 in a virtual environment
with conda please use 

```bash
$ conda create -n ENV3 -c conda-forge python=3.10.5 pip
```

Optionally, you can omit the python version to get the latest
community version as well.

It is very important that you run the latest version of pip along with
python.  Failure to do so may result in errors when installing
packages designed to use newer versions of pip.

#### Activating, Inspecting, and Deactivating Conda

Once the above steps have been completed, you must activate your
environment for the newly installed version of python and pip are made
available.  You will need to run this command each time you open a new
command window, or you can make it active by default by appending the
line to your bash configuration located at `~/.bashrc`,
`~/.bash_profile`, or your Zsh profile located at `~/.zprofile`.

To activate our `ENV3` environment, run

```bash
conda activate ENV3
```

This will augment your current command prompt to use this python environment
and all of it's dependencies.  Your command prompt will also change to indicate
that you are running within this environment by prepending `(ENV3)` to your
prompt.

Note that doing this will also expose any anaconda managed programs to your
command line (such as openssl and sqlite3).  You can see details on your
environment by running the command `conda info`.  This shows you many important
troubleshooting details about your environment, including its name, the path
where the environment has been configured, and key paths to conda's configuration.

Additionally, you can inspect the current packages installed in the environment
by running the command `conda list`, which will show both conda packages and python
packages, their version and build, and the channel (or source) they were installed
(main, conda-forge, and pypi are the most commonly seen).

When you are done using this conda environment and the software packages it has
installed, you can deactivate the environment by running

```bash
conda deactivate
```

and your shell will remove the conda environment from your current shell's path.

### Version Test

Regardless of which version you install, you must do a version test to make sure you have the correct
python and pip versions:

```bash
$ python --version
$ pip --version
```

If you installed everything correctly, you should see the below versions or newer for each tool:

```
Python 3.10.5
pip 21.3.1
```

If you see an older version of pip, you can update it with

```
pip install -U pip
```

Or with conda,

```
conda update -c conda-forge pip
```

