# Raspberry PI Setup (Small Number of PIs):o:

This section will be a the start for the replacement for all previous setup instructions. 
I think we want ultimately the section "PI Network of Workstations" to also use this 
or be the final section.

Once the content has either been integrated here or it is determined that 
the previous file is no longer needed, we will move the other file into a dir 
deprecated, and remove the file from chapter.yaml.

We will aslo need to manage a second documentation just for CM-burn in 
the cm-burn repo that just focusses on cm-burn as this is also a stand alone prg

The duplicated sections we are aware of include:

If its integrated mark the checkmark. We need to be carful not to lose info

* [ ] <https://github.com/cloudmesh-community/cm-burn/blob/master/README.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/setup.md>
* [x] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/setup-dev.md>
  Now only contains information for a development environment. needs
  to be renamed. Stays in this file for now.
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/pi-passwordreset.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/run-at-boot.md>
* [x] deleted <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/sd-card.md>
  integrated in setup-ultimate
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/clusters/pi-configure-cluster.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/clusters/pi-setup.md>
 
There may even be more such documentation as part of student
projects. No student that does a PI project MUST DESCRIBE HOW THEY SET
UP THE CLUSTER IN THEIR REPORT. THEY ALL MUST IMPROVE OR USE THIS
SECTION.

I also see that portions of other files include or can leverage what we do in cm-burn and thsu we can 
replace that info or morege portions of it such as in and than these sections need to be fixed while using 
our ultimate guide, e.g. make a pointer to it

* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/pi-kubernetes.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/526/readme-kube.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/pi-kubernetes.md>
 

As you see everyone duplicated in part the steps. So what we need is a
single section that describes the cm-burn procedure, but also the
steps needed by hand for those that can not afford the $50 investment
of the mount prg.

Next we propose an outline. Help improving the outline than contribute
here to this single document while not replicating sections but refer
to sections if needed. IF difference between windows osx and linux,
aslo include the differences.

## Image Choice

When it comes to the operating system install, we have multiple
options. One of the options you will find is the installation of what
is called NOOBS. NOOBS is actually not an operating system, but it
installs an operating system. Nobbs has the feature to install an
operating system of choice on the Raspberry. It aslo allows to recover
from a faulty OS. A good introduction that showcases some of the
features of NOOBS is available at:

* <https://www.raspberrypi.org/blog/introducing-noobs/>

It also provides the necessary tools to modify the `config.txt` file
that is used at boot time.

However, as we at this time only intend to use Raspbian as the OS,
there is no need to install NOOBS. If the OS breakes, we simply burn a
new SD card. Hence the features we gain from NOOBS are not as
beneficial to us.

Instead we will directly install Rasbian on our SD card and configure
it appropriately.

* <https://www.raspberrypi.org/downloads/>

## Simulating a Raspberry PI on a Computer

In case you do not have a computer available, you can also install a
Raspberry Pi in a virtual machine.

* <https://downloads.raspberrypi.org/rpd_x86_latest

You can download the image and start it via virtual box. As we work
with newer PIs we recommend that you set up under Linux virtual machine
with 64 bit with Other.

Once completed, you will see that it looks something like

![Virtual Raspberry Pi](images/pi-desktop.png)

## Setting up a Single Raspberry PI

We discuss here the steps to set up a single Raspberry while
installing Raspbian on an SD Card. For this we will use etcher 
for Windows and macOS. Other solutions such as using command line
scripts are also available and are demonstrated for example in the
section about burning SD Cards in Linux.


### Burn an SD Card with cm-burn :o:

A very convenient program to create an SD card for a Raspberry pi is
using the program `cm-burn`. The program is available from

* <https://github.com/cloudmesh-community/cm>

It can be installed with

```console
mkdir -p cloudmesh-community
cd cloudmesh-community
git clone https://github.com/cloudmesh-community/cm.git
cd cm
pip setup.py .
```

You will now have the program `cm-burn` available. Please note that
`cm-burn` is provided without any warranties to work and that if you
damage your system we do not have any liability.

The command is somewhat very special as
it sets up the Raspberry pi directly on the SD Card without the need
for rebooting it. The downside is that you need to have an OS that can
mount the Ext file system. This can be achieved on OSX and Windows
with a program called `extFS`. However it costs about $40. Detailed
information on how to use cm-burn is provided at

* <https://github.com/cloudmesh-community/cm/blob/master/README.md>


For moere advanced options see cm-burn which also works for a single
card but requires a purchased product. 

1. Burning the SD Card is discussed in Section TBD
2. Section [Password]{#s-pi-setup-password} discusses how to change
   the password after you booted the PI. :warning: This must be the
   first thing before you put the PI on the network or otherwise it is
   broken into quickly.
3. ...

To not have to purchase it we describe here the steps needed to do it
be hand. THis is discussed in Sections ... :o: list all the sections
here.

### Install Raspbian on a SD card

For many Raspberry Pi related projects we need to install an Operating
system on an SD card. We use **Raspbian** as the OS as it is widely
supported. Other OS have recently been added to the available list of
operating systems for the PI, but we will at this time not consider
them here.

To install the OS on an SD Card you will need another computer. We
describe next the process if you have either a MAC or an Linux Ubuntu
machine.  If you have other OSes and like to contribute, please add
your suggestions.

The processes described in this section only work for a few SD cards and is not
suitable for burning hundreds of SD cards as we would need for a
cluster consisting out of many PI's.

#### Download Raspbian

No matter which OS you create the SD Cards on, you will need to
download the Raspbian OS.


Next, you need to download the Raspbian image and place it in a
directory. As you may reuse the image multiple times, we recommend to
place it in a location you remember. Let us assume you place it in
`~/Download` directory.
Visit the link

* <https://downloads.raspberrypi.org/raspbian_latest>

and download the image into the folder of your choice (we assume
`~/Download`).

#### Etcher form Windows and macOS, Linux


An easy way to burn a SD Cards on Windows, macOS, and Linux is with a
programm called Etcher. Etcher can be downloaded from

* <https://etcher.io/>

Chose the download suitable for your OS. On Windows you ahve a couple
of options. We recommend that you use the 64 bit Installer version if
your OS supports it. If you have a Windows 32bit OS, it may be time to
upgrade your computer and/or OS. Also on Linux you need to make sure
you distinguish between 32bit and 64bit. 

#### Windows 10

Once you download it, start Etcher and select the
unzipped Raspbian image file. Now select the drive of the SD
card. click Burn and your image will be written to the SD card. You
can monitor the progress an once it is completed the SD card will
automatically unmount. Use it now in your Raspberry Pi.

The process is the same as the one on macOS


#### macOS

Once the image is downloaded you copy it with etcher onto the SD-card.

2. Place an SD Card into a SD card reader we recommend a 32GB card.
3. Attach the card reader to the computer
4. Open Etcher and select the downloaded `.img` or `.zip`
   file which you will likely find in the `~/Download` folder if you
   followed our previous steps
5. Select the SD card to write the image to. Be careful, to chose the
   right location as otherwise you could create unexpected dataloss
6. Hence, review selections carefully and click *Flash!* to begin
  writing data to the SD card.


#### Ubuntu from Etcher

The process is the same as on macOS.

#### Ubuntu from Commandline

In Ubuntu we can use the advanced Linux commands to burn the SD Cards
In the file explorer, right click on the SD card and format the SD
card. This is done as follows:

1. Run

   ```bash
   $ df -h
   ```

   to list all the drives in the computer
2. Insert the SD card and run the command again
3. Now a new entry will be listed which is the SD card
4. The left column of the results from `df -h` command gives the device
   name of your SD card.  It will be listed as something like
   `/dev/mmcblk0p1` or `/dev/sdX1`, where X is a lower case letter
   indicating the device.  The last part (p1 or 1 respectively) is the
   partition number.
5. Write down the name of the SD card (without the partition)
6. Unmount the card so that the card can not be read from or written
   to with the following command: 

   ```bash
   $ unmount dev/mmcblk0p1
   ``` 

   Make sure to use correct name for the card. If your card has
   multiple partitions unmount all partitions
7. Next write the image to the SD card by running the command:


   ```bash
   $ dd bs=4M if=<path to .img> of=/dev/mmcblk0 status=progress conv=fsunc
   ```
  
   Make sure `if=` contains the path to image and `of=` contains the name 
   of the SD card otherwise you may ruin your hard disk

To check, if the image was properly written you can do the following:

8. Create an image again from the SD card by running the following command:

   ```bash
   $ dd bs=4M if=/dev/sdX of=from-sd-card.img
   ```

9. Truncate the image to be the same size as that of the raspbian image

   ```bash
   $ truncate --reference <original raspbian image> from-sd-card.img
   ```
  
10. Run `diff` to see if the two files are same by running the following
    command:

   ```bash
   $ diff -s from-sd-card.img <original raspbian image>
   ```
  
   If everything iss ok, `diff` should say that the two files are same

In most cases the verification step will not be needed.

### Password {#s-pi-setup-password}

Before you bring your Raspberry Pi on the networks, you need to reset
the password. This can be done by starting the terminal and typing in
it the command

    pi$ passwd

The original password is `raspberrypi` and every one knows it. SO if
you put your pi on the network it is easily compromised. Hence, change
your password first.

### Locale

You want to also set your system to use your language settings for the
keyboard. you can do this isn the terminal with 

    pi$ raspi-config 

or

    pi$ sudo dpkg-reconfigure locales

or using the GUI.


### Wireless Network at Home 

The easiest way to get internet access and to continue the setup is
using a wireless network. You can configure it either via the GUI or commandline.

In case you like to edit the information from commandline edit the
file `interfaces` file with

    pi$ sudo nano /etc/network/interfaces

change the following

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-ssid "your-WLAN-SSID"
    wpa-psk "your-WLAN-password"

and replace the values with the once you have. To save the file use 

    Ctrl-o Y Enter Save changes.
    Ctrl-x Quit nano.

### Wireless network at IU

IU runs several different networks. This includes IUSecure, Eduroam,
and ATT Wifi.  The first two would require you to use your IU username
and password to be entered in the configuration. Although technically
possible we find the method :warning: **HIGHLY** insecure and
:warning: **STRONGLY** advice agains doing so. Let us assume you put
your information on a PI and than someone takes the SDCard from
it. They can than look into the card and steal your
password. Obviously this is not advisable. In other cases you may have
configured your software wrong and someone could login remotely and
lift your password remotely. Obviously this is not advisable.

Regardless, we have seen from instructors the advice to use
IUSecure. This is :warning: **WRONG**! Do not listen to them about
this particular issue and advise them to use an alternative setup

One such alternative (which is also not ideal) is to use the free wifi
offered by ATT Wifi. It is a bit complex to setup as you need to go to
the Web browser to the address <http:\\iu.edu> and click on the
connect button. Sometimes that button is not visible so you need to
scroll down to see it.

We also have an internal network that we will not discuss here, but
can be used upon consultation with Dr. von Laszewski.

### Update

We want to update the software and make sure
everything is up to date. This is done with 

    pi$ sudo apt-get update

To develop easily we need a number of programs on our Pi. Additional programs can
be installed with the command

```bash
pi$ apt-get install PACKAGE
```

where `PACKAGE` is the name of the software we like to install.
A good example is emacs which can be installed with

```bash
pi$ apt-get install emacs
```

### Hostname

The hostname is stored in `/etc/hostname`. Edit the file and change it
to a name such as green00, green01, green02, green03, green04, green05.
Be consistent with the names. The 00 host should be the top most host in
the cluster.

edit

    pi$ nano /etc/hostname

after you edited the hostname

    pi$sudo /etc/init.d/hostname.sh start

Ideally we want to find out how to write the hostname after we burn the
SD card on the laptop that does the burning

develop a python script to do that

### Remote access via ssh

To enable ssh on the pi you need to say

    pi$ sudo systemctl enable ssh
    pi$ sudo systemctl start ssh

Naturally you need to do a bit more such as placing your public key in
the authorized_keys file explained later, but for now we will just
activate ssh.

To access the machine using public keys we recommend that you add your
public key to the `~pi/.ssh/authorized_keys` file

## Setting up a Small Cluster by Hand

:o: This explains how to set up a small cluster by hand discussing how to
burn multiple cards. It uses the method of booting the pi and using a
monitor to set up each of them. starting with passwd

The process described above can be replicated fairly easily for a
small number of PIs. Just make sure you have a different hostname for
each Pi. More complex setups are discussed next while for example
using static IP addresses.


### Wireless network addresses by hand

:o:

### Static network addresses by hand

:o:

### Mixed wireless and static network

:o:



System Preparation without Monitor
----------------------------------

:o: there is lots of duplication here to the ultimate setup

### hostname

Find a way on how to name the host as each of the cluster nodes will
need its own unique name. We simple use color01, where color is the
color of the USB cables you have and the number is the ith PI starting
from the top

### SSH

Describe how you enable SSH without a monitor

### key

Describe how you can generate a private key at the right location on the
SD Card. Place your own public key on the SD Card

Write python programs for this.

### password

Describe how you can change the password on the SD Card


## Post configuration

### Network Addresses

Find a way to find all the network addresses from all Pi's attached to
the network switch.

### key

Write a python program that does the following:

1. login with ssh on each PI and call ssh-keygen to generate a
   unique key on each PI.

2. copy this .pub keys to your computer and store them into a file
   called `authorized_keys`

3. copy that file to all Pis

4. you may also have to copy your authorized key file to

### VNC

find out how to set up vnc so you can login into the PI and see its GUI

* <https://www.raspberrypi.org/forums/viewtopic.php?t=74176>

* <https://www.raspberrypi.org/documentation/remote-access/vnc/>

```bash
host$ alias IP=<IPADDRESSOFPI>
host$ sh pi@$IP

pi@IP's password: 
Linux raspberrypi 3.10.25+ #622 PREEMPT Fri Feb 3 20:00:00 GMT 2018 armv6l
pi@raspberrypi ~ $ sudo apt-get tightvncserver   # download the VNC server
pi@raspberrypi ~ $ tightvncserver                # start the VNC server
pi@raspberrypi ~ $ vncserver :0 -geometry 1920x1080 -depth 24  #start a VNC session
```


Now, back on your Mac:
In the Finder, select Go => Connect To Server...
Type `vnc://xxx.xxx.xxx.xxx` (where `xxx.xxx.xxx.xxx` is the IP address that you discovered in step 2.
Click [Connect]. This will launch the Screen Sharing application, and
with a little luck, you should see this image.


## Setting up a Small Cluster with cm-burn

This discusses how to set things up for many PIs with `cm-burn`

### Setting up a large cluster with cm-burn

here we discuss one lareg cluster setup lets say 100 nodes


### DHCP setup

:o:

### PXE Boot

:o:



## Using Advanced setups with Ansible



## Change Password on the SD-Card

It is possible to reset the password for a PI SD Card. This comesin
handy when you did forget it or the team that worked on a Pi has left
the project but valuable information may still be on the PI. To do so,
You need tou unplug the raspberry pi and remove the SD card from the
slot.  Next you need to have the ability to mount the file systems. On
macOS and Windows you can use extFS. Naturally if you have a linux
machine or another PI, you can use an SD Card reader/writer and mount
it directly. You will need root access on the machine where you
execute the password reset.

After you inserted the card, please Locate and edit the `etc/shadow`
file on the SD card. To create a new password use the command 

```bash
$ openssl passwd -1 -salt <unique string>
```

Next, we e must find the line that starts with pi and replace the text
  between the first and second with the output from the above command
  we had executed in the `etc/shadow` file

Now you can Eject the SD card from the computer, and insert it into
the Pi. Boot the raspberry pi and log in to it while using the new
password. This naturally only works if you allow password login. ON
many systems we however disable it and use public key authentication
only. In this case you need to just replace the public key in the
`authorized_keys` file. Using just keys is obviously more convenient.

Naturally mounting the SD Card and looking in the filesystem would also
allow you to look at the network setup. That is certainly not good and
before a PI is returned sensitive information should be cleaned from
the SD Card. 

## Creating Backup :question:

:question: In this section we will explain how to create a backup of
the image from the SD Card in a PI.

## Duplication :question:

Let us assume you have installed a lot of great programs on the SD Card.
In a cluster, we need to duplicate this card for each PI in the cluster.
Is there a way for us to duplicate the software


## Exercises

SD-Card.1

: Improve the Ubuntu SD-card documentation

SD-Card.2

: Could a script be written that does the entire process via a python
  or shell command in Ubuntu.

SD-Card.2

: Could a script be written that does the entire process via a python
  or shell command in macOS?

SD-Card.3

: could a script be written that does the entire process via a python
  or shell command in gitbash for Windows?

SD-Card.4

: In general the Ubuntu documentation is complex, how can it be
  simplified? Maybe through automation?

