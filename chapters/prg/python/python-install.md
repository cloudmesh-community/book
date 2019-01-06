# Python Installation {#s-python-install}

Python is easy to install and very good instructions for most platforms
can be found on the python.org Web page. We will be using Python 2.7.15
and/or Python 3.7 in our activities.

To manage python modules, it is useful to have
[pip](https://pypi.python.org/pypi/pip) package installation tool on
your system.

We assume that you have a computer with python
installed. The version of python however may not be the newest
version.
Please check with

```bash
$ python --version
```

which version of python you run. If it is not the newest version, we
recommend that you install pyenv to install a newer version so you do
not effect the default version of python from your system.

While in other classes yo may have been taught to use anaconda, this
is not a tool that ought to be used in a cloud class. The reason for
this is that it installs many packages that you are likely not to
use. In fact installing anaconda on your VM will waste space and time
and you should look into other installs.

However, *real* cloud engineers with the most flexibility in python
versions want to install python via pyenv.

Note: whenever possible please use for the newest version of Python 2
or 3. In order not to effect your OS we will use pyenv.

## Managing custom Python installs

Often you have your own computer and you do not like to change its
environment to keep it in pristine condition. Python comes with many
libraries that could for example conflict with libraries that you have
installed. To avoid this it is bets to work in an isolated python we can
use tools such as virtualenv, pyenv or pyenv for 3.7.1. Which you
use depends on you, but we highly recommend pyenv if you can.

### Managing Multiple Python Versions with Pyenv

Python has several versions that are used by the community. This
includes Python 2 and Python 3, but all different management of the
python libraries. As each OS may have their own version of python
installed. It is not recommended that you modify that version. Instead
you may want to create a localized python installation that you as a
user can modify. To do that we recommend *pyenv*. Pyenv allows users to
switch between multiple versions of Python
(<https://github.com/yyuu/pyenv>). To summarize:

-   users to change the global Python version on a per-user basis;
-   users to enable support for per-project Python versions;
-   easy version changes without complex environment variable
    management;
-   to search installed commands across different python versions;
-   integrate with tox (<https://tox.readthedocs.io/>).

#### Installation without pyenv

If you need to have more than one python version installed and do not
want or can use pyenv, we recommend you download and install python
2.7.15 and 3.7.1 from python.org
(<https://www.python.org/downloads/>)

#### Disabling wrong python installs on macOS

While working with students we have seen at times that they take other
classes either at universities or online that teach them how to program
in python. Unfortunately, although they seem to do that they often
ignore to teach you how to properly install python. I just recently had
a students that had installed python 7 times on his macOS machine, while
another student had 3 different installations, all of which conflicted
with each other as they were not set up properly.

We recommend that you inspect if you have a files such as `~/.bashrc` or
`~/.bashrc_profile` in your home directory and identify if it activates
various versions of python on your computer. If so you could try to
deactivate them while out-commenting the various versions with the \#
character at the beginning of the line, start a new terminal and see if
the terminal shell still works. Than you can follow our instructions
here while using an install on pyenv.

#### Install pyenv on macOS from git

This is our recommended way to install pyenv on macOS:

    $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    $ git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    $ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

#### Installation of Homebrew

Before installing anything on your computer make sure you have enough
space. Use in the terminal the command:

    $ df -h

which gives your an overview of your file system. If you do not have
enough space, please make sure you free up unused files from your drive.

In many occasions it is beneficial to use readline as it provides nice
editing features for the terminal and xz for completion. First, make
sure you have xcode installed:

    $ xcode-select --install

On Mojave you will get an error that zlib is not installed. THis is due to that the header files are not properly installed. To do this you can say 

    $ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

Next install homebrew, pyenv, pyenv-virtualenv and pyenv-virtualwrapper.
Additionally install readline and some compression tools:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew update
    brew install readline xz

#### Install pyenv on macOS with Homebrew

This is the recommended way of installing pyenv on macOS High Sierra. This method should also be considered if you get the following error:
"ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?"

We describe here a mechanism of installing pyenv with homebrew. Other
mechanisms can be found on the pyenv documentation page
(<https://github.com/yyuu/pyenv-installer>). You must have homebrew
installed as discussed in the previous section.

To install pyenv with homebrew execute in the terminal:

    brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper

#### Install pyenv on Ubuntu

The following steps will install pyenv in a new ubuntu 18.04
distribution.

Start up a terminal and execute in the terminal the following commands.
We recommend that you do it one command at a time so you can observe if
the command succeeds:

    $ sudo apt-get update
    $ sudo apt-get install git python-pip make build-essential libssl-dev
    $ sudo apt-get install zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
    $ sudo pip install virtualenvwrapper

    $ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    $ git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv   
    $ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

You can also install pyenv using curl command in following way:

    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    
Then install its dependencies:

    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev git

Now that you have installed pyenv it is not yet activated in your
current terminal. The easiest thing to do is to start a new terminal and
typ in:

    which pyenv

If you see a response pyenv is installed and you can proceed with the
next steps.

Please remember whenever you modify `.bashrc` or `.bash_profile` you
need to start a new terminal.

#### Install Different Python Versions

Pyenv provides a large list of different python versions. To see the
entire list please use the command:

    $ pyenv install -l

However, for us we only need to worry about python 2.7.15 and python
3.7.1. You can now install different versions of python into your
local environment with the following commands:

    $ pyenv update
    $ pyenv install 2.7.15
    $ pyenv install 3.7.1

You can set the global python default version with:

    $ pyenv global 3.7.1

Type the following to determine which version you activated:

    $ pyenv version

Type the following to determine which versions you have available:

    $ pyenv versions

Associate a specific environment name with a certain python version, use
the following commands:

    $ pyenv virtualenv 2.7.15 ENV2
    $ pyenv virtualenv 3.7.1 ENV3

In the example, ENV2 would represent python 2.7.15 while ENV3
would represent python 3.7.1. Often it is easier to type the alias
rather than the explicit version.

#### Set up the Shell

To make all work smoothly from your terminal, you can include the
following in your `.bashrc` files:

    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    __pyenv_version_ps1() {
      local ret=$?;
      output=$(pyenv version-name)
      if [[ ! -z $output ]]; then
        echo -n "($output)"
      fi
      return $ret;
    }

    PS1="\$(__pyenv_version_ps1) ${PS1}"

We recommend that you do this towards the end of your file.

#### Switching Environments

After setting up the different environments, switching between them is
now easy. Simply use the following commands:

    (2.7.15) $ pyenv activate ENV2
    (ENV2) $ pyenv activate ENV3
    (ENV3) $ pyenv activate ENV2
    (ENV2) $ pyenv deactivate ENV2
    (2.7.15) $ 

To make it even easier, you can add the following lines to your
`.bash_profile` file:

    alias ENV2="pyenv activate ENV2"
    alias ENV3="pyenv activate ENV3"

If you start a new terminal, you can switch between the different
versions of python simply by typing:

    $ ENV2
    $ ENV3

## Updating Python Version List

Pyenv maintains locally a list of available python versions. To see the
list use the command

    pyenv update
    pyenv install -l

You will see the updated list.

## Updating to a new version of Python with pyenv

Naturally python itself evolves and new versions will become available
via pyenv. To facilitate such a new version you need to first install
it into pyenv. Let us assume you had an old version of python installed
onto the ENV3 environment. Than you need to execute the following steps:

    pyenv deactivate
    pyenv uninstall ENV3
    pyenv install 3.7.1
    pyenv virtualenv 3.7.1 ENV3
    ENV3
    pip install pip -U

With the pi install command, we make sure we have the newest version
of pip. In case you get an error, you may have to update xcode as 
follows and try again:

      xcode-select --install

After you installed it you can activate it by typing `ENV3`. Naturally
this requires that you added it to your bash environment as discussed in
Section [1.1.1.8](#s:set-up-the-shell){reference-type="ref"
reference="s:set-up-the-shell"}.

## Pyenv in a docker container

We provide a simple docker container on docker hub that is based on
ubuntu 18.04 that has pyenv, python 2.7.15 and python 3.7.1
installed. Using this image is as simple as downloading it and running
it.

To run the container and loginto the command prompt please use

```bash
$ docker run --rm -it cloudmesh/pyenv:1.0  /bin/bash 
```

To switch between the python versions use the command 

```bash
container> ENV2
container> ENV3
```

where container indicates that the command is executed 
### Creating the container locally

This section is only needed if you like to recreate the image or
modify the Dockerfile.

The information about how we create the image is provided at in a
repository. You can download the code in the directory and can create
the image from the Docker file while using the Makefile as follows:

``` bash
$ mkdir cloudmesh-community
$ cd cloudmesh-community
$ git clone https://github.com/cloudmesh-community/images.git
$ cd images/pyenv
$ make image
```

This will create an image locally. with


```bash
$ make login
```

you can login to the shell. Typically you will only need the docker
command as descripbed in the prvious section.

## Installation without pyenv

If you need to have more than one python version installed and do not
want or can use pyenv, we recommend you download and install python
2.7.15 and 3.7.1 from python.org (<https://www.python.org/downloads/>)

### Make sure pip is up to date

As you will want to install other packages, make sure pip is up to date:

    pip install pip -U

pyenv virtualenv anaconda3-4.3.1 ANA3 pyenv activate ANA3

## Anaconda and Miniconda

We do not recommend that you use anaconda or miniconda as it may

:   interfere with your default python interpreters and setup.

Please note that beginners to python should always use anaconda or
miniconda only after they have installed pyenv and use it. For this class
neither anaconda nor miniconda is required. In fact we do not recommend
it. We keep this section as we know that other classes at IU may use
anaconda. We are not aware if these classes teach you the right way to
install it, with *pyenv*.

### Miniconda

:warning: This section about miniconda is experimental and has not been 
tested. We are looking for contributors that help completing
it. If you use anaconda or miniconda we recommend to manage it via
pyenv.

To install mini conda you can use the following commands:

    $ mkdir ana
    $ cd ana
    $ pyenv install miniconda3-latest
    $ pyenv local miniconda3-latest
    $ pyenv activate miniconda3-latest
    $ conda create -n ana anaconda

To activate use:

    $ source activate ana

To deactivate use:

    $ source deactivate

To install cloudmesh cmd5 please use:

    $ pip install cloudmesh.cmd5
    $ pip install cloudmesh.sys

### Anaconda

:warning: This section about anaconda is experimental and has not
been tested. We are looking for contributors that help completing
it.

You can add anaconda to your pyenv with the following commands:

    pyenv install anaconda3-4.3.1

To switch more easily we recommend that you use the following in your
`.bash_profile` file:

    alias ANA="pyenv activate anaconda3-4.3.1"

Once you have done this you can easily switch to anaconda with the
command:

    $ ANA

Terminology in anaconda could lead to confusion. Thus we like to point
out that the version number of anaconda is unrelated to the python
version. Furthermore, anaconda uses the term root not for the root user,
but for the originating directory in which the anaconda program is
installed.

In case you like to build your own conda packages at a later time we
recommend that you install the conda-build package:

    $ conda install conda-build

When executing:

    pyenv versions

you will see after the install completed the anaconda versions
installed:

    pyenv versions
    system
    2.7.15
    2.7.15/envs/ENV2
    3.7.1
    3.7.1/envs/ENV3
    ENV2 
    ENV3
    * anaconda3-4.3.1 (set by PYENV_VERSION environment variable)

Let us now create virtualenv for anaconda:

    $ pyenv virtualenv anaconda3-4.3.1 ANA

To activate it you can now use:

    $ pyenv ANA

However, anaconda may modify your `.bashrc` or `.bash_profile` files and
may result in incompatibilities with other python versions. For this
reason we recommend not to use it. If you find ways to get it to work
reliably with other versions, please let us know and we update this
tutorial.

To install cloudmesh cmd5 please use:

    $ pip install cloudmesh.cmd5
    $ pip install cloudmesh.sys

### virtualenv

Documentation about it can be found at:

    * https://virtualenv.pypa.io

The installation is simple once you have pip installed. If it is not
installed you can say:

    $ easy_install pip

After that you can install the virtual env with:

    $ pip install virtualenv

To setup an isolated environment for example in the directory \~/ENV
please use:

    $ virtualenv ~/ENV

To activate it you can use the command:

    $ source ~/ENV/bin/activate

you can put this command in your `.bashrc` or `.bash_profile` files so
you do not forget to activate it. Instructions for this can be found in
our lesson on Linux `bashrc`.

#### Exercises

E.Python.Install.0:

> Write installation instructions for an operating system of your choice
> and add to this documentation.

E.Python.Install.1:

> Replicate the steps to install pyenv, so you can type in ENV2 and ENV3 in your
> terminals to switch between python 2 and 3.

E.Python.Install.3:

> Why do you not want to use generally anaconda for cloud computing?
> When is it ok to use anaconda?

