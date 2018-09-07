
## Preparing the SD card :o:

TODO: We should at this time assume we have an OS.

Download the latest Raspbian Jessie Lite image from

	https://www.raspberrypi.org/downloads/raspbian/
	

Please note that Raspbian Jessie Lite image contains the only the bare
minimum amount of packages.

## Download Etcher :o:

	https://etcher.io/

Now follow the instructions in Etcher to flash Raspbian image on the
SD card.  Before ejecting the SD card do the following.

## Enable SSH on the SD Card :o:

To prevent Raspberry Pis from being hacked the RPi foundation have now
disabled SSH on the default image. So, create a text file in /boot/
called ssh - it can be empty file or you can type anything you want
inside it.

Please note that you have renamed the ssh.txt to ssh i.e. without
extension.

Now insert the SD card, networking and power etc.

## Starting Pi :o: 

Once you boot up the Raspberry Pi, Connect using SSH

		$ ssh pi@raspberrypi.local

The password is raspberry.

For security reasons, please change the default password of the user
pi using the passwd command.

Note: If you want to change the hostname of the Pi, Use an editor and
change the hostname Raspberry Pi in:

		* /etc/hosts
		* /etc/hostname
