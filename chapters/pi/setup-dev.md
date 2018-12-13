# Setup of a Development Environment


## Editors

Naturally we need a useful editor. We have made good experience with
emacs as it supports a variety of different formats and is also
available for macOS and Windows.

You can install it with

```bash
$ apt-get install <program>
```

Other editors include `emacs`, `vim`, `gedit` and so on. If you are concerned
about space, use `vi` which is pre-installed. If you like to use other
editors use the command we can install them respectively with 

```bash
$ apt-get install emacs
$ apt-get install vim
$ apt-get install gedit
...
```

## Python on the Pi :hand: fa18-516-03

Raspbian Stretch Lite version 2018-11-13 comes by default with Python 2.7.13 and
Python 3.5.3. However, it does not come with `pip` which is the default Python
configuration management tool.

Add instructions to install pip and pip3 which are not installed by default in
the Lite images:

```bash
$ sudo apt-get install -y python-pip python3-pip
$ pip -V
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
$ pip3 -V
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.5)
```

Note that pip for Python 3 can also be run by using the following command

```bash
$ python3 -m pip install ...
```

The installation packages for pip on Raspbian will also properly setup the
<https://www.piwheels.org> package repository which contains pre-compiled binary
wheels for many popular python packages. A *wheel* is a python package that is
already compiled into a binary form for a particular OS and hardware chipset.
Installing a wheel is much faster and less error prone than building a package
from source. These wheels have also been optimized for the ARM chipset that the
Raspberry Pi uses so they will run at the highest speeds possible. For example,
you can install the wheel for numpy and scipy with:

```bash
$ pip3 install numpy scipy
```

If you want to upgrade to the latest python version you can build it from source
as follows

```bash
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev
$ sudo apt-get install libssl-dev libsqlite3-dev tk-dev libgdbm-dev
$ sudo apt-get install libc6-dev libbz2-dev
$ cd /usr/src
$ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
$ sudo tar xzf Python-3.6.5.tgz
$ cd Python-3.6.5
$ sudo -s
$ bash configure
$ make altinstall
```
    
## Python IDLE

Click Menu -> Programming -> Python 3 (IDLE), and you'll get a new
window called 'Python 3.6.5 Shell:'. This Shell works just like Python
on the command line. Enter print("Hello World") to see the message.

## Go

To install go use

```bash
$ wget https://storage.googleapis.com/golang/go1.9.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.9.linux-armv6l.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
```

If you like to have it included every time you start a terminal please
please the line

```export PATH=$PATH:/usr/local/go/bin```

in your ~/.profile file and reboot.

Now you are also able to program go on your Pi.

