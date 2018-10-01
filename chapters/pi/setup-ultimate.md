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
* [ ] <https://github.com/cloudmesh-community/book/blob/master/chapters/pi/initial-setup.md>
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

## Setting up a Single Raspberry PI

Discuss here the steps to do that including burning the sd card. IT is fine to use etcher, BUt there is one solution discussed that does dd which we aslo like to keep

### Password

Before you bring your Raspberry Pi on the networks, you need to reset
the password. This can be done by starting the terminal and typing in
it the command

    $ passwd

The original password is `raspberrypi` and every one knows it. SO if
you put your pi on the network it is easily compromised. Hence, change
your password first.

### Locale

You want to also set your system to use your language settings for the
keyboard. you can do this isn the terminal with 

    raspi-config 

or

    sudo dpkg-reconfigure locales

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

### Update

We want to update the software and make sure
everything is up to date. This is done with 

    $ sudo apt-get update

To develop easily we need a number of programs on our Pi. Programs can
be installed with the command

```bash
$ apt-get install <program>
```

where `<program>` is the name of the software we like to install.

### Hostname

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

### Remote access via ssh

To enable ssh on the pi you need to say

    $ sudo systemctl enable ssh
    $ sudo systemctl start ssh

Naturally you need to do a bit more such as placing your public key in
the authorized_keys file explained later, but for now we will just
activate ssh.

## Setting up a Small Cluster by Hand

THis explains how to set up a small cluster by hand discussing how to burn multiple cards. It uses the method of booting the pi and using a monitor to set up each of them. starting with passwd

## Setting up Many Pis for a Cluster

THis discusses how to set things up for many PIs with cm burn, we have multiple scenarios

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




 
