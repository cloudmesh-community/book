## Modifying the Pi Image without a PI

TODO: status: 75

Goals:

* [ ] change the hostname
* [ ] add ssh keys
* [ ] set the network configuration
* [ ] change the default password


## Overview

When creating large clusters it is not convenient to log in by hand in each PI. Typically to avoid this. One configures the PI via PXE boot. However in this setup we do not use PXE boot, but try to burn an individualized OS that contains from the beginning on the individualized hostname, an ssh key (and the public key is shared with all other images that are burned this way, as well as the network configuration. 

## Approach

The goal is to change the hostname on the Stretch Lite images before
we burn the SD cards so that we can use `arp -a` to populate a
database matching hostnames to MAC addresses. We need to modify both
sectors. In the first sector, we want to add an empty file called ssh so that we can ssh into the pi. In the second sector we change the hostname in `/etc/hostname` from `raspberrypi` to a dynamically
generated unique name.

---

:warning: This has only been tested on an Ubuntu VM. Both the .img file
and the mount point need to be on Ubuntu VM drives. The mount will fail
on a Mac shared drive.

---

First create a directory and download the [latest build of Rasbian Lite](https://downloads.raspberrypi.org/raspbian_lite_latest). The last step is to download a script that is located at 

* <https://github.com/cloudmesh-community/hid-sp18-419/blob/master/project-code/pi-config/make-pi-images.py>

Please look at the details of this script as it uses some fairly advanced features.

```
$ mkdir os-images
$ wget -O os-images/pi-img.zip https://downloads.raspberrypi.org/raspbian_lite_latest
$ wget -O os-images/pi-img.zip https://sourceforge.net/projects/dexterindustriesraspbianflavor/files/latest/download
$ unzip -d os-images/master os-images/pi-img.zip
$ cd os-images
$ wget https://github.com/cloudmesh-community/hid-sp18-419/blob/master/project-code/pi-config/make-pi-images.py) 
```

To run the make-pi-images.py script execute the following command

```
$ sudo python make-pi-images.py 2018-03-13-raspbian-stretch-lite.img
```

NOTE: the most current build of Raspbian Lite at the time of writing
is in the previous command.  You will need to replace it with the name of
the current file that came out of the zip archive.

The customized image will be in a subdirectory called
`make-pi-images.pyoutput`. If you run it multiple times, you will need
to remove the `mountpoint` directory and move the
`make-pi-images.pyoutput`.

#### TODO: Automated Cluster SD-Card Script :o:

---

:warning: This is just an idea and has not been implemented

---

First we are creating a configuration file that describes our cluster. It is written in yaml and loos as follows:

```yaml
data:
   images:
       dexter: https://sourceforge.net/projects/dexterindustriesraspbianflavor/files/latest/download
       rasbian: https://downloads.raspberrypi.org/raspbian_lite_latest
   hostname: red
       start: 0001
       end:   0005
       lead:  0000
       range: 0002-0004 
   ssh: enable
   sshkey: ~/.ssh/id_rsa.pub
   passwd:  readline 
```
       
The meaning of the attributes is rather simple. Under images we specify a number of images that we could chose and are downloaded onto the computer that burns the SD-cards if they are not present. The cluster base hostname is defined by the attribute `hostname` and the first worker node to be specified has the postfix defined by start. We define the last number also in the yaml file, while we will look between the start and the end number. The number of leading blanks is defined by the start and end numbers. A special node called `lead` is specified that is the lead node and all worker nodes are accessible by this lead node. Furthermore. the lead node will be used to monitor the cluster. If the start number includes the lead ode the lead node will be configured. The attribute range specifies which SD-cards are configured. Note this could be a subset of the entire cluster defined by start and end.
       
       
### Gregor: Manual page cmd5 may be easier than click.

    modify_sdcard -fetch [rasbian|dexter|https://downloads.raspberrypi.org/raspbian_lite_latest]  - fetched the image
    modify_sdcard -burn IMAGE   - puts the given image on the sd card
    modify_sdcard -ssh [enable|disable] enables or disables ssh 
    modify_sdcard -sshkey [~/.ssh/id_rsa.pub]  puts the default key for login
    modify_sdcard -name NAME puts the given name on the image
    

TODO: Loop to create multiple images, handle exception of existing mount point and output directory

- Change the name of the machine
- [Enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/)
- Change the password
- Set up one of the Pis as a DHCP server

The image we are modifying can be downloaded from [Raspberry Pi](https://downloads.raspberrypi.org/raspbian_lite_latest).

Instructions are based on
[this](http://blog.videgro.net/2015/11/modify-disk-image-raspbian/).
Developed on Ubuntu running on VirtualBox on a Mac. It will be easier,
but less automated, to modify the image using the VM and burn the
image with the MacOS. To burn the SD card from the VM, we will need to
set up the VM to use the SD card device on the Mac. Instruction on how
to do this are
[here](https://superuser.com/questions/373463/how-to-access-an-sd-card-from-a-virtual-machine).

Some information on how to burn an SD image without using Etcher can be found 
[here](https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/). 

