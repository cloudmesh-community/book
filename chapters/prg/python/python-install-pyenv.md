# Multi-Version Python Installation

---

![](images/learning.png) **Learning Objectives**

* Understand why we need to worry about python 3.8 and 2.7
* Use pyenv to support both versions
* Understand the limitations of anaconda/conda for developers

---

We are living in an interesting junction point in the development of
Python. In January 2019, it is encouraged that Python developers switch
from python version 2.7 to python version 3.8.

However there may be the requirement when you still need to develop code
not only in python 3.8 but also in python 2.7. To facilitate this
multi-python version development, the best tool we know about capable of
doing so is *pyenv*. We will explain you in this section how to install
both versions with the help of pyenv.

Python is easy to install and very good instructions for most platforms
can be found on the python.org Web page. We see two different versions:

* Python 2.7.16
* Python 3.8.1

To manage python modules, it is useful to have
[pip](https://pypi.python.org/pypi/pip) package installation tool on
your system.

We assume that you have a computer with python installed. The version of
python however may not be the newest version. Please check with

```bash
$ python --version
```

which version of python you run. If it is not the newest version, we
use  *pyenv* to install a newer version so you do
not effect the default version of python from your system.

## Disabling wrong python installs

While working with students we have seen at times that they take other
classes either at universities or online that teach them how to program
in python. Unfortunately, they seem to often ignore to teach you how to
properly install Python. I just recently had a students that had
installed python 7 different times on his macOS machine, while another
student had 3 different installations, all of which conflicted with each
other as they were not set up properly and the students did not even
realize that they were using Python incorrectly on their computer due to
setup issues and conflicting libraries.

We recommend that you inspect if you have a files such as `~/.bashrc` or
`~/.bashrc_profile` in your home directory and identify if it activates
various versions of python on your computer. If so you could try to
deactivate them while out-commenting the various versions with the \#
character at the beginning of the line, start a new terminal and see if
the terminal shell still works. Than you can follow our instructions
here while using an install on pyenv.

## Managing 2.7 and 3.8 Python Versions without Pyenv

If you need to have more than one python version installed and do not
want or can use pyenv, we recommend you download and install python
2.7.16 and 3.8.1 from python.org
(<https://www.python.org/downloads/>)

YOu can than use either `python2` or `python3` to invoke the python
interpreter.

## Managing Multiple Python Versions with Pyenv

Python has several versions that are used by the community. This
includes Python 2 and Python 3, but all different management of the
python libraries. As each OS may have their own version of python
installed. It is recommended that you **not** modify that version. Instead
you may want to create a localized python installation that you as a
user can modify. To do that we recommend *pyenv*. Pyenv allows users to
switch between multiple versions of Python
(<https://github.com/yyuu/pyenv>). To summarize:

* users to change the global Python version on a per-user basis;
* users to enable support for per-project Python versions;
* easy version changes without complex environment variable
  management;
* to search installed commands across different python versions;
* integrate with tox (<https://tox.readthedocs.io/>).

To install pyenv on your system you can use the command

```
$ curl https://pyenv.run | bash
```

Now you can install different python versions on your system such as
python 2.7 and 3.8 with a few commands:

```bash
$ pyenv install 3.8.1
$ pyenv install 2.7.16
$ pyenv virtualenv 3.8.1 ENV3
$ pyenv virtualenv 2.7.16 ENV2
```

To automatically access them from your shell we integrate them into bash
by editing the bash configuration files. Make sure that on Linux you add
to the `~/.bashrc` file and on macOS to the file `~/.bash_profile` or `.zprofile`.

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

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

alias ENV2="pyenv activate ENV2"
alias ENV3="pyenv activate ENV3"


ENV3
```

We recommend that you do this towards the end of your file. Than look up
our convenience methods to set an ALIAS and install Python 3.8.1 via
pyenv

Next we recommend to update pip

```bash
$ ENV2
$ pip install pip -U
$ ENV3
$ pip install pip -U
```

### Installation pyenv via Homebrew

On macOS you can install pyenv also via Homebrew. Before installing
anything on your computer make sure you have enough space. Use in the
terminal the command:

```bash
$ df -h
```

which gives your an overview of your file system. If you do not have
enough space, please make sure you free up unused files from your drive.

In many occasions it is beneficial to use readline as it provides nice
editing features for the terminal and xz for completion. First, make
sure you have xcode installed:

```bash
$ xcode-select --install
```

On Mojave you will get an error that zlib is not installed. THis is due to that
the header files are not properly installed. To do this you can say

```bash
$ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

Next install homebrew, pyenv, pyenv-virtualenv and pyenv-virtualwrapper.
Additionally install readline and some compression tools:

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew update
$ brew install readline xz
```

To install pyenv with homebrew execute in the terminal:

```bash
brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
```

### Install pyenv on Ubuntu 18.04

The following steps will install pyenv in a new ubuntu 18.04
distribution.

Start up a terminal and execute in the terminal the following commands.
We recommend that you do it one command at a time so you can observe if
the command succeeds:

```bash
$ sudo apt-get update
$ sudo apt-get install git python-pip make build-essential libssl-dev
$ sudo apt-get install zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
$ sudo pip install virtualenvwrapper

$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
$ git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

You can also install pyenv using curl command in following way:

```bash
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

Then install its dependencies:

```bash
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install -y make build-essential libssl-dev
$ sudo apt-get install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
$ sudo apt-get install -y wget curl llvm libncurses5-dev git
```

Now that you have installed pyenv it is not yet activated in your
current terminal. The easiest thing to do is to start a new terminal and
typ in:

```bash
$ which pyenv
```

If you see a response pyenv is installed and you can proceed with the
next steps.

Please remember whenever you modify `.bashrc` or `.bash_profile` or
`.zprofile` you need to start a new terminal.

### Using pyenv

#### Using pyenv to Install Different Python Versions

Pyenv provides a large list of different python versions. To see the
entire list please use the command:

```bash
$ pyenv install -l
```

However, for us we only need to worry about python 2.7.16 and python
3.8.1. You can now install different versions of python into your
local environment with the following commands:

```bash
$ pyenv update
$ pyenv install 2.7.16
$ pyenv install 3.8.1
```

You can set the global python default version with:

```bash
$ pyenv global 3.8.1
```

Type the following to determine which version you activated:

```bash
$ pyenv version
```

Type the following to determine which versions you have available:

```bash
$ pyenv versions
```

Associate a specific environment name with a certain python version, use
the following commands:

```bash
$ pyenv virtualenv 2.7.16 ENV2
$ pyenv virtualenv 3.8.1 ENV3
```

In the example, ENV2 would represent python 2.7.16 while ENV3
would represent python 3.8.1. Often it is easier to type the alias
rather than the explicit version.

#### Switching Environments

After setting up the different environments, switching between them is
now easy. Simply use the following commands:

```bash
(2.7.16) $ pyenv activate ENV2
(ENV2) $ pyenv activate ENV3
(ENV3) $ pyenv activate ENV2
(ENV2) $ pyenv deactivate ENV2
(2.7.16) $
```

To make it even easier, you can add the following lines to your
`.bash_profile` or or `.zprofile` file:

```
alias ENV2="pyenv activate ENV2"
alias ENV3="pyenv activate ENV3"
```

If you start a new terminal, you can switch between the different
versions of python simply by typing:

```bash
$ ENV2
$ ENV3
```

### Updating Python Version List

Pyenv maintains locally a list of available python versions. To see the
list use the command

```bash
$ pyenv update
$ pyenv install -l
```

You will see the updated list.

#### Updating to a new version of Python with pyenv

Naturally python itself evolves and new versions will become available
via pyenv. To facilitate such a new version you need to first install
it into pyenv. Let us assume you had an old version of python installed
onto the ENV3 environment. Than you need to execute the following steps:

```bash
$ pyenv deactivate
$ pyenv uninstall ENV3
$ pyenv install 3.8.1
$ pyenv virtualenv 3.8.1 ENV3
$ ENV3
$ pip install pip -U
```

With the pi install command, we make sure we have the newest version
of pip. In case you get an error, you may have to update xcode as
follows and try again:

```bash
xcode-select --install
```

After you installed it you can activate it by typing `ENV3`. Naturally
this requires that you added it to your bash environment as discussed in
Section [1.1.1.8](#s:set-up-the-shell){reference-type="ref"
reference="s:set-up-the-shell"}. :o2:

## Anaconda and Miniconda and Conda

While in others on the internet or in your classes may have taught you
to use anaconda, We will avoid it as it has several disadvantages for
edevelopers. The reason for this is that it installs many packages that
you are likely not to use. In fact installing anaconda on your VM will
waste space and time and you should look into other installs.

We do not recommend that you use anaconda or miniconda as it may

: interfere with your default python interpreters and setup.

Please note that beginners to python should always use anaconda or
miniconda only after they have installed pyenv and use it. For this class
neither anaconda nor miniconda is required. In fact we do not recommend
it. We keep this section as we know that other classes at IU may use
anaconda. We are not aware if these classes teach you the right way to
install it, with *pyenv*.

### Miniconda

> ![](images/warning.png){height=12pt}
> *This section about miniconda is experimental and has not been
> tested. We are looking for contributors that help completing
> it. If you use anaconda or miniconda we recommend to manage it via
> pyenv.*

To install mini conda you can use the following commands:

```bash
$ mkdir ana
$ cd ana
$ pyenv install miniconda3-latest
$ pyenv local miniconda3-latest
$ pyenv activate miniconda3-latest
$ conda create -n ana anaconda
```

To activate use:

```bash
$ source activate ana
```

To deactivate use:

```bash
$ source deactivate
```

### Anaconda

> ![](images/warning.png){height=12pt} This section about anaconda is experimental and has not
> been tested. We are looking for contributors that help completing
> it.

You can add anaconda to your pyenv with the following commands:

```bash
pyenv install anaconda3-4.3.1
```

To switch more easily we recommend that you use the following in your
`.bash_profile` or `.zprofile` file:

```bash
alias ANA="pyenv activate anaconda3-4.3.1"
```

Once you have done this you can easily switch to anaconda with the
command:

```bash
$ ANA
```

Terminology in anaconda could lead to confusion. Thus we like to point
out that the version number of anaconda is unrelated to the python
version. Furthermore, anaconda uses the term root not for the root user,
but for the originating directory in which the anaconda program is
installed.

In case you like to build your own conda packages at a later time we
recommend that you install the conda-build package:

```bash
$ conda install conda-build
```

When executing:

```bash
$ pyenv versions
```

you will see after the install completed the anaconda versions
installed:

```bash
pyenv versions
system
2.7.16
2.7.16/envs/ENV2
3.8.1
3.8.1/envs/ENV3
ENV2
ENV3
* anaconda3-4.3.1 (set by PYENV_VERSION environment variable)
```

Let us now create virtualenv for anaconda:

```bash
$ pyenv virtualenv anaconda3-4.3.1 ANA
```

To activate it you can now use:

```bash
$ pyenv ANA
```

However, anaconda may modify your `.bashrc` or `.bash_profile` or or `.zprofile`
files and may result in incompatibilities with other python versions. For this
reason we recommend not to use it. If you find ways to get it to work reliably
with other versions, please let us know and we update this tutorial.

## Exercises

E.Python.Install.1:

> Install Python 3.8.1

E.Python.Install.1:

> Write installation instructions for an operating system of your choice
> and add to this documentation.

E.Python.Install.2:

> Replicate the steps to install pyenv, so you can type in ENV2 and ENV3 in your
> terminals to switch between python 2 and 3.

E.Python.Install.3:

> Why do you not want to use generally anaconda for cloud computing?
> When is it ok to use anaconda?

