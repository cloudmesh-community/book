## Install Raspbian on a SD card

For many Raspberry Pi related projects we need to install an Operating
system on an SD card. We use **Raspbian** as the OS as it is widely
supported. Other OS have recently been added to the available list of
operating systems for the PI, but we will at this time not consider
them here.

To install the OS on an SD Card you will need another computer. We
describe next the process if you have either a MAC or an Linux Ubuntu
machine. If you have other OSes and like to contribute, please add
your suggestions.

The processes described here only work for a few SD cards and are not
suitable for burning hundrets of SD cards as we would need for a
cluster consisting out of many PI's.

### OSX

First, we assume you have Etcher installed on your OSX machine

* You just need to download Etcher and install it. YOU can find the program at
  <https://etcher.io/>

Next, you need to download the image and place it in a directory. We
recommend to keep it in the `~/Download` directory.

1. Download the image from <https://downloads.raspberrypi.org/raspbian_latest>

Once the image is downloaded you copy it with etcher onto the SD-card.

2. Place an SD Card into a SD card reader we recommend a 32GB card.
3. Attach the card reader to the computer
4. Open Etcher and select the downloaded `.img` or `.zip`
   file which you will likely find in the `~/Download` folder if you
   followed our previous steps
5. Select the SD card to write the image to.
6. Review selections and click *Flash!* to begin writing data to the SD
  card.

### Windows 10

First you need to download the rasbian OS from

* <https://downloads.raspberrypi.org/raspbian_latest>

On windows 10 an easy way to create an SD card is to use etcher. You
can download it s form

* <https://etcher.io/>

and chse to download it for Windows. You have a couple of options and
we recommend that you use the 64 bit Installer version if your OS
supports it.  Once you download it, start Etcher and select the
unzipped Raspbian image file. Now select the drive of the SD
card. click Burn and your image will be written to the SD card. You
can monitor the progress an once it is completed the SD card will
automatically unmount. Use it now in your Raspberry Pi.


### Ubuntu

* In the file explorer, right click on the SD card and format the SD card
* Run

  ```bash
  $ df -h
  ```

  to list all the drives in the computer
* Insert the SD card and run the command again
* Now a new entry will be listed which is the SD card
* The left column of the results from `df -h` command gives the device
  name of your SD card.  It will be listed as something like
  `/dev/mmcblk0p1` or `/dev/sdX1`, where X is a lower case letter
  indicating the device.  The last part (p1 or 1 respectively) is the
  partition number.
* Note down the name of the SD card (without the partition)
* Unmount the card so that the card can not be read from or written to
* Run the following command: 

  ```bash
  $ unmount dev/mmcblk0p1
  ``` 

  Make sure to use correct name for the card
* If your card has multiple partitions unmount all partitions
* Next write the image to the SD card.
* Run the following command:

  ```bash
  $ dd bs=4M if=<path to .img> of=/dev/mmcblk0 status=progress conv=fsunc
  ```
  
  Make sure `if=` contains the path to image and `of=` contains the name 
  of the SD card otherwise you may ruin your hard disk

#### Checking that the image was written properly

* Create an image again from the SD card
* Run the following command:

  ```bash
  $ dd bs=4M if=/dev/sdX of=from-sd-card.img
  ```

* Truncate the image to be the same size as that of the raspbian image

  ```bash
  $ truncate --reference <original raspbian image> from-sd-card.img
  ```
  
* Run diff to see if the two files are same
* Run the following command:

  ```bash
  $ diff -s from-sd-card.img <original raspbian image>
  ```
  
* Diff should say that the two files are same

### Exercises

SD-Card.1

: Improve the Ubuntu SD-card documentation

SD-Card.2

: Could a script be written that does the entire process via a python
  or shell command in Ubuntu.

SD-Card.2

: Could a script be written that does the entire process via a python
  or shell command in OSX?

SD-Card.3

: could a script be written that does the entire process via a python
  or shell command in gitbash for Windows?

SD-Card.4

: In general the Ubuntu documentation is complex, how can it be
  simplified? Maybe through automation?

