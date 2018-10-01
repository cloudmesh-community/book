# Setup of a development environment
    
rename this file to setup-dev.md

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

## Python 3

Raspbian comes by default with Python 2. However, more and more
libraries become available in Python 3 and you can install it with 

```bash
$ sudo apt-get install python3
```

If this does not work you can also compile the newest version as
follows

```bash
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev
$ sudo apt-get install libssl-dev libsqlite3-dev tk-dev libgdbm-dev
$ sudo apt-get install libc6-dev libbz2-dev
cd /usr/src
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
sudo tar xzf Python-3.6.5.tgz
d Python-3.6.5
sudo -s
bash configure
make altinstall
exit
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

