# Cluster Setup

In this isection we discuss how we setup the cluster. To explore that we
can conduct the setup without monitor, we are collecting in this section
a variety of tasks in regrads to it and documenting solutions for them.
Students in the residential or in the online classes that participate in
cluster building can contribute to this section.

A number of students have been assigned for particular tasks. and will
be adde dhere by the TA's. It is expected that you conduct your task
ASAP.

## Links

A number of usefule links may help for this task. However be aware that
we want to develop a *script* for most of the tasks eliminating input by
hand. The information here deals to identifying the information needed
to do so.

* <https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0>

*
<https://installvirtual.com/enable-ssh-in-raspberry-pi-without-monitor/>

According to

*
<https://www.raspberrypi.org/documentation/configuration/raspi-config.md>

rasp-config writes a file /boot/config.txt. Maybe it is a good idea to
inspect this file manipulate it and see if there are field we simply
coudl write and overwrite it on the SDcard. See also

* <https://elinux.org/R-Pi_configuration_file>

## SDCards

The cluster will have an SDCard in each of the PIs. To enable them to
boot an opreating system has to be put on the card. We recommend that
you use Etcher for doing so which is available for Linux, Windows, and
OSX. Etcher can be found at

If there are better tools or methods please document.

For your OS, discuss how to install Etcher. Then dicuss how to burn the
OS on the SD card.

### Linux

Describe this for Linux.

### OSX

Describe this for OSX.

### Windows 10

Describe this for Windows 10.

### Creating Backup

In this task you will be documenting how to create a backup of the image
on the SDCard.

### Duplication

Let us assume you have installed a lot of great programs on the SDCard.
In a cluster, we need to duplicate this card for each PI in the cluster.
Is there a way fo us to duplicate the software

### Mount the SD Card on the Host System

Describe on how to mount the SDCard on the host system so you can
manipulate the files on the SDCard

### Linux

Describe this for Linux.

### OSX

Describe this for OSX.

### Windows 10

Describe this for Windows 10.

System Preparation without Monitor
----------------------------------

### hostname

Find a way on how to name the host as each of the cluster nodes will
need its own unique name. We simple use color01, where color is the
color of the USB cables you have and the number is the ith PI starting
from the top

### SSH

Describe how you enable SSH without a monitor

### key

Describe how you can generate a private key at the right location on the
SDCard. Place your own public key on the SDCard

Write python programs for this.

### password

Describe how you can change the password on the SDCard


## Post confoguration

### Netwwork Addresses

Find a way to find all the network addresses from all PIs attached to
the network switch.

### key

Write a python program that does the follwoing:

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
    alias IP=<IPADDRESSOFPI>

    sh pi@$IP
    pi@IP's password: 
    Linux raspberrypi 3.10.25+ #622 PREEMPT Fri Feb 3 20:00:00 GMT 2018 armv6l
    pi@raspberrypi ~ $ sudo apt-get tightvncserver   # download the VNC server
    pi@raspberrypi ~ $ tightvncserver                # start the VNC server
    pi@raspberrypi ~ $ vncserver :0 -geometry 1920x1080 -depth 24  #start a VNC session
```


Now, back on your Mac:
In the Finder, select Go => Connect To Server...
Type vnc://xxx.xxx.xxx.xxx (where xxx.xxx.xxx.xxx is the IP address that you discovered in step 2.
Click [Connect]. This will launch the Screen Sharing application, and
with a little luck, you should see this image.

Addon Hardware
--------------

recently ordered add on hardware

power switches

*
<https://www.amazon.com/dp/B01DE57SD4/ref=psdc_6396124011_t2_B075WZJL6N>

SDCard Writers

*
<https://www.amazon.com/Collection-MicroSD-MicroSDHC-MicroSDXC-Kingston/dp/B01IF7TPMS/ref=sr_1_15?s=electronics&ie=UTF8&qid=1518271583&sr=1-15&keywords=Micro+SD+Card+writer>

