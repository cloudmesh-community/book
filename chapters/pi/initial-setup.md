# Inotial Setup

## Password

Before you bring your Raspberry Pi on the networks, you need to reset
the password. This can be done by starting the terminal and typing in
it the command

    $ passwd

The original password is `raspberrypi` and every one knows it. SO if
you put your pi on the network it is easily compromised. Hence, change
your password first.

## Locale

You want to also set your system to use your language settings for the
keyboard. you can do this isn the terminal with 

    raspi-config 

or

    sudo dpkg-reconfigure locales

or using the GUI.


## Wireless Network

The easiest way to continue is to have a wireless network you can
connect to. We do not recommend that you use for example your IU
credentials hence we wil not use the network called `IU
secure`. Instead we will be using on campus the ATT wireless network.
If your are not at IU please use your own wireless network at
home. You can configure it via the GUI.

In case you like to edit the information at a later time or at this
time you can also use an editor.  Edit the file `interfcaes` file with

    sudo nano /etc/network/interfaces

change the following

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-ssid "your-WLAN-SSID"
    wpa-psk "your-WLAN-password"

and replace the values with the once you have. To save the file use 

    Ctrl-o Y Enter Save changes.
    Ctrl-x Quit nano.

TODO: what will the file look like for ATT-wifi

Furthermore, if you are at iu and use ATT-wifi, you need to go with
your web browser to `http:\\iu.edu` and click on the connect
button. Sometimes that button is not visible so you need to scroll to it.

## Update

We want to update the software and make sure
everything is up to date. This is done with 

    $ sudo apt-get update

To develop easily we need a number of programs on our Pi. Programs can
be installed with the command

```bash
$ apt-get install <program>
```

where `<program>` is the name of the software we like to install.

## Hostname

The hostname is stored in `/etc/hostname`. Edit the file and change it
to a name such as green00, green01, green02, green03, green04, green05.
Be consistent with the names. The 00 host should be the top most host in
the cluster.

edit

    nano /etc/hostname

after you edited the hostname

    sudo /etc/init.d/hostname.sh start

Ideally we want to find out how to write the hostname after we burn the
SD card on the laptop that does the burning

develop a python script to do that

## Remote access via ssh

To enable ssh on the pi you need to say

    $ sudo systemctl enable ssh
    $ sudo systemctl start ssh

Naturally you need to do a bit more such as placing your public key in
the authorized_keys file explained later, but for now we will just
activate ssh.
    

## Editors

Naturally we need a useful editor. We have made good experience with
emacs as it supports a variety of different formats and is also
available for OSX and Windows.

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

