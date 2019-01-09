# Virtual Machine Management with QEMU {#sec:qemu-kvm}

In this section we provide a short example on how to use QUEMU.  We
will be starting with the instalation, then create a virtual hard
disk, install ubuntu on the disk and start the virtual machine. Next
we will demonstrate how we can emulate a Raspery Pi with QEMU.
Lastly, we sho how to use virsh.

## Install QEMU

To install QEMU+KVM on Ubuntu/Linux Mint please use

    $ sudo apt install qemu qemu-kvm libvirt-bin

On OSX QEMU can be installed with Homebrew

    $ brew install qemu

## Create a Virtual Hard Disk with QEMU

To create an image file with the size of 10GB and `qcow2` format
(default format for QEMU images), run:

    $ qemu-img create -f qcow2 testing-image.img 10G

Note that a new file called `testing-image.img` is now created at your
home folder (or the place where you run the terminal). Note also that
the size of this file is not 10 Gigabytes, it is around 150KB only; QEMU
will not use any space unless needed by the virtual operating system, but
it will set the maximum allowed space for that image to 10 Gigabytes
only.

## Install Ubuntu on the Virtual Hard Disk

Now that we have created our image file, if we have an ISO file for a
Linux distribution or any other operating system and we want to test it
using QEMU and use the new image file we created as a hard drive, we can
run:

    qemu-system-x86_64 \
        -m 1024 \
        -boot d \
        -enable-kvm \
        -smp 3 \
        -net nic -net user \
        -hda testing-image.img \
        -cdrom ubuntu-16.04.iso

Explain the previous command part by part:

`-m 1024`:

> Here we chose the RAM amount that we want to provide for QEMU when
> running the ISO file. We chose 1024MB here. You can change it if you
> like according to your needs.

`-boot -d`:

> The boot option allows us to specify the boot order, which device
> should be booted first? -d means that the CD-ROM will be the first,
> then QEMU will boot normally to the hard drive image. We have used the
> `-cdrom` option as you can see at the end of the command. You can use
> `-c` if you want to boot the hard drive image first.

`-enable-kvm`:

> This is a very important option. It allows us to use the KVM
> technology to emulate the architecture we want. Without it, QEMU will
> use software rendering which is very slow. That is why we must use
> this option, just make sure that the virtualization options are
> enabled from your computer BIOS.

`-smp 3`:

> If we want to use more than 1 core for the emulated operating system,
> we can use this option. We chose to use 3 cores to run the virtual
> image which will make it faster. You should change this number
> according to your computer's CPU.

`-net nic -net user`:

> By using these options, we will enable an Ethernet Internet connection
> to be available in the running virtual machine by default.

`-hda testing-image.img`:

> Here we specified the path for the hard drive which will be used. In
> our case, it was the testing-image.img file which we created before.

`-cdrom ubuntu-16.04.iso`:

> Finally we told QEMU that we want to boot our ISO file
> `ubuntu-16.04.iso`.

Start Ubuntu with QEMU
----------------------

Now, if you want to just boot from the image file without the ISO file
(for example if you have finished installing and now you always want to
boot the installed system), you can just remove the `-cdrom` option:

    $ qemu-system-x86_64 -m 1024 -boot d -enable-kvm -smp 3 -net nic -net user -hda testing-image.img

*Please note QEMU `qemu-system-x86_64` emulates a 64-bit architecture.*

Emulate Raspberry Pi with QEMU
------------------------------

First you have to download a pre-built kernel

    $ wget https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/master/kernel-qemu-4.4.34-jessie

Next, you have to download the Raspbian image. Download a `.img` file
from Raspbian website:

* <https://www.raspberrypi.org/downloads/raspbian/>

To start the emulator type in the following command to have QEMU
emulate an ARM architecture:


```bash
$ qemu-system-arm -kernel ./kernel-qemu-4.4.34-jessie \
    -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" \
    -hda raspbian-stretch-lite.img \
    -cpu arm1176 -m 256 -machine versatilepb \
    -no-reboot -serial stdio
```

Pleaee not that

* `kernel-qemu-4.4.34-jessie` is the pre-built kernel file.
* `raspbian-stretch-lite.img` is the Raspbian image file.



Resources
---------

General

* Official website for `libvirt` is here: <https://libvirt.org/>
* Home page of KVM is here: <https://www.linux-kvm.org/page/Main_Page>
* QEMU home page: <https://www.qemu.org/>
* QEMU User Documentation: <https://qemu.weilnetz.de/doc/qemu-doc.html>
* Wikipedia page for QEMU: <https://en.wikipedia.org/wiki/QEMU>

Comparison

* <http://opensourceforu.com/2012/05/virtualisation-faceoff-qemu-virtualbox-vmware-player-parallels-workstation/>
* <https://stackoverflow.com/questions/43704856/what-is-the-difference-qemu-vs-virtualbox>
