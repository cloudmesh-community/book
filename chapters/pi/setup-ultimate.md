# Raspberry PI Setup

This section will be a the start for the replacement for all previous setup instructions. 
I think we want ultimately the section "PI Network of Workstations" to also use this 
or be the final section.

Once the content has either been integrated here or it is determinde that 
the previous file is no longer needed, we will move the other file into a dir 
deprecated, and remove the file from chapter.yaml.

We will aslo need to manage a second documentation just for CM-burn in 
the cm-burn repo that jsut focusses on cm-burn as this is also a stand alone prg

The duplicated setions we are aware of include:

If its integrated mark the checkmark. We need to be carful not to lose info

* [ ] <https://github.com/cloudmesh-community/cm-burn/blob/master/README.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/setup.md>
* [x] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/initial-setup.md> NOw only contains information for a development environment. needs to be renamed.
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/pi-passwordreset.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/run-at-boot.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/sd-card.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/clusters/pi-configure-cluster.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/clusters/pi-setup.md>
 
There may even be more such documentation as part of student projects. No student that does a PI project MUST DESCRIBE HOW THEY SET UP THE CLUSTER IN THEIR REPORT. THEY ALL MUST IMPROVE OR USE THIS SECTION.

I also see that portions of other files include or can leverage what we do in cm-burn and thsu we can 
replace that info or morege portions of it such as in and than these sections need to be fixed while using 
our ultimate guide, e.g. make a pointer to it

* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/pi-kubernetes.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/526/readme-kube.md>
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/pi-kubernetes.md>
 

As you see everyone duplicated in part the steps. So what we need is a single section that describes 
the cm-burn procedure, but also the steps needed by hand for those that can not afford the $50 
investment of the mount prg. 

Next we propose an outline. Help improving the outline than contribute here to this single document 
while not replicationg sections but refer to sections if needed. IF difference between windows osx and linux, aslo include the differences.

## Image Choice

:o: Differentce between Rasbian and Noobs setup

:o: why we just do Rasbian

## Setting up a Single Raspberry PI

Discuss here the steps to do that including burning the sd card. IT is fine to use etcher, But there is one solution discussed that does dd which we aslo like to keep.

In this section we discuss how to set up a Raspberry pi by hand. It starts with burnin an SD Card

### Burn an SD Card

For moere advanced options see cm-burn which also works for a single card but requires a purchased product. To not have to purcase it we describe here the steps needed to do it be hand.

1. Burning the SD Card is discussed in Section TBD
2. Section [Password]{#s-pi-setup-password} discusses how to change the password after you booted the PI. :warning: This must be the first thing before you put the PI on the network or otherwise it is broken into qucikly.
3. ...

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


### Wireless Network

The easiest way to continue is to have a wireless network you can
connect to. We do not recommend that you use for example your IU
credentials hence we wil not use the network called `IU
secure`. Instead we will be using on campus the ATT wireless network.
If your are not at IU please use your own wireless network at
home. You can configure it via the GUI.

In case you like to edit the information at a later time or at this
time you can also use an editor.  Edit the file `interfcaes` file with

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

#### IU specific setups

IU runs several different networks. THis includes IUSecure, Eduroam, and ATT Wifi. 
The first two would require you to use your IU username and password to be entered 
in the configuration. Although technically possible we find the method **HIGHLY** 
insecure and **STRONGLY** advice agains doing so. Let us assume you put your information 
on a PI and than somone takes the SDCard from it. THey can than look into the card and 
steal your password. Obviously this is not advisable. In other cases you may have 
convigured your software wrong and somone coudl login remotely and lift your password 
remotely. Obviously this is not advisable.

Regardless, we have seen from instructors the advice to use IUSecure. This is 
**WRONG**! Do not listen to them about this particular issue and advise them to use an alternative setup

One such alternative (which is also not ideal) is to use the free wifi offered by ATT Wifi. It is a bit complex to setup as you need to go to the Web browser to the address <http:\\iu.edu> and click on the connect
button. Sometimes that button is not visible so you need to scroll down to see it.

We also have an internal network that we will not discuss here, but can be used upon consultation with Dr. von Laszewski.

### Update

We want to update the software and make sure
everything is up to date. This is done with 

    pi$ sudo apt-get update

To develop easily we need a number of programs on our Pi. Programs can
be installed with the command

```bash
pi$ apt-get install PACKAGE
```

where `PACKAGE` is the name of the software we like to install.

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

## Setting up a Small Cluster by Hand

THis explains how to set up a small cluster by hand discussing how to burn multiple cards. It uses the method of booting the pi and using a monitor to set up each of them. starting with passwd

## Setting up Many Pis for a Cluster

This discusses how to set things up for many PIs with cm burn, we have multiple scenarios

### Setting up a small cluster with cm-burn

here we discuss teh 5 node setup

### Setting up a large cluster with cm-burn

here we discuss one lareg cluster setup lets say 100 nodes

#### Static network addresses

#### DHCP setup

#### PXE Boot

### Setting up a plugable cluster of clusters with cm-burn

Here we discuss a class of students that each ahve 5 node clusters 
that come in a room to place their clusters in a shelf then they plug it into a 
power strip and a network, they replace the sd card of the master with a worker sd card
there is a special master that detects new workers and inventories them with different 
states, so we can get to them if they are registered.


### Using Advanced setups with Ansible




 
