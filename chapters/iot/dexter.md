Dexter
======

Creating an SD Card
-------------------

### OSX

First, install Etcher from [etcher.io](https://etcher.io/) which allows
you to flash images onto the SD card. When flashing make sure you only
attach one USB SD card reader/writer or use the build in SD card slot
provided in some Mac's.

The version of etcher we used is

-   [Etcher-1.1.1-darwin-x64.dmg](https://github.com/resin-io/etcher/releases/download/v1.1.1/Etcher-1.1.1-darwin-x64.dmg)

Make sure to check if there is a newer version

### DexterOS

DexterOS:

*
<https://www.dexterindustries.com/dexteros/get-dexteros-operating-system-for-raspberry-pi-robotics/>

* <https://www.dexterindustries.com/download/dexteros>

[:clapper: DexterOS 9:15 Set up SDCard (original Video)](https://www.youtube.com/watch?v=pJZURHLeTs0)

The video is published on the Dexter Web site.

### Dexter Raspbian

Dexter provides a special image that contains the drivers and sample
programs for the GrovePi shield. We had some issues installing it on a
plain Raspbian OS, thus we recommend that you use dexters version if you
use the GrovePi shield. It is available from

-   [Google
    Drive](http://sourceforge.net/projects/dexterindustriesraspbianflavor/)

-   [Sourceforge](http://sourceforge.net/projects/dexterindustriesraspbianflavor/)

Detailed information on how to generate an SD card while using your OS
is provided at

*
<https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/>

### Github

Dexter maintains a github repository that includes their code for the
shield and many other projects at

* <https://github.com/DexterInd>

### Cloning Grove PI

To clone the GrovePI library on other computers you can use the command

    git clone https://github.com/DexterInd/GrovePi.git

### Dexter Sample programs

Dexter maintains all GrovePi related programs at

* <https://github.com/DexterInd/GrovePi>

The python related programs are in a subdirectory at

* <https://github.com/DexterInd/GrovePi/tree/master/Software/Python>

Here you find many programs and for a complete list visit that link.
Dependent on the sensors and actuators you have, inspect some programs.
Some of them may inspire you to purchase some sensors.

We have developed a partial library of GrovePi module classes at

* <https://github.com/cloudmesh/cloudmesh.pi/tree/master/cloudmesh/pi>

