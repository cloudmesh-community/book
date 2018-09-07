Virtual Machine Management with KVM and QEMU
============================================

Virtualization Technologies
---------------------------

### Overview of Machine Virtualization

There are various technologies handling machine virtualization for
resource sharing and CPU architecture emulating. In this tutorial,
`libvirt`, KVM and QEMU are covered. `libvirt` is a system library for
virtualization, which provides low-level abstraction. KVM is a
kernal-based virtualization solution, and QEMU is a suite of emulators.
Cloud providers, such as AWS, Azure, and Google, use these technologies
for compute instance virtualization. OpenStack and Kubernetes also adopt
these technologies.

### Libvirt

`libvirt` is a library that provides a common API for managing popular
virtualization solutions, among them KVM and Xen. The library provides a
normalized management API for these virtualization solutions, allowing a
stable, cross-hypervisor interface for higher-level management tools.
The library also provides APIs for management of virtual networks and
storage on the VM Host Server. The configuration of each VM Guest is
stored in an XML file. The official website for `libvirt` is here:
https://libvirt.org/

### KVM

KVM (for Kernel-based Virtual Machine) is a full virtualization solution
for Linux on x86 hardware containing virtualization extensions (Intel VT
or AMD-V). It consists of a loadable kernel module, kvm.ko, that
provides the core virtualization infrastructure and a processor specific
module, kvm-intel.ko or kvm-amd.ko. The home page of KVM is here:
https://www.linux-kvm.org/page/Main_Page

KVM stands for Kernel Virtual Machine, and it is a module of the Linux
kernel which allows a program to access and make use of the
virtualization capabilities of modern processors, by exposing the
`/dev/kvm` interface.

Using KVM, one can run multiple virtual machines running unmodified
Linux or Windows images. Each virtual machine has private virtualized
hardware: a network card, disk, graphics adapter, etc.

KVM is open source software. The kernel component of KVM is included in
mainline Linux, as of 2.6.20.

### QEMU

QEMU is a virtualization technology emulator that allows you to run
operating systems and Linux distributions easily on your current system
without the need to install them or burn their ISO files.

When used as a machine emulator, QEMU can run OSes and programs made for
one machine (e.g. an ARM board) on a different machine (e.g. your own
PC). By using dynamic translation, it achieves very good performance.

When used as a virtualizer, QEMU achieves near native performance by
executing the guest code directly on the host CPU. QEMU supports
virtualization when executing under the Xen hypervisor or using the KVM
kernel module in Linux. When using KVM, QEMU can virtualize x86, server
and embedded PowerPC, 64-bit POWER, S390, 32-bit and 64-bit ARM, and
MIPS guests.

Once QEMU has been installed, it should be ready to run a guest OS from
a disk image. This image is a file that represents the data on a hard
disk. From the perspective of the guest OS, it actually is a hard disk,
and it can create its own filesystem on the virtual disk.

You can download a few guest OS images from the [QEMU
website](https://wiki.qemu.org/Testing/System_Images). System_Images,
including a simple 8 MB image of a Linux distro (which is meant
primarily for testing; note that it lacks the e1000 driver and therefore
cannot do networking out-of-the-box). To run it, download and unzip the
image in a folder and run the QEMU command.

### Difference between QEMU and VirtualBox

Both have some features which the other does not have, so this might
ease the decision. QEMU+KVM is better integrated in Linux, has a smaller
footprint and should therefore be faster. (Please also note QEMU can run
without KVM in a plain mode. For example, android development emulators
run in this mode.)

VirtualBox is a virtualization software limited to x86 and amd64
architecture. QEMU supports a wide range of hardware and can make use of
the KVM when running a target architecture which is the same as the host
architecture.

Install QEMU
------------

### To install QEMU on Ubuntu/Linux Mint:

To install QEMU+KVM on Ubuntu/Linux Mint please use

    sudo apt install qemu qemu-kvm libvirt-bin

### To install QEMU on MaxOS:

On OSX QEMU can be installed with Homebrew

    brew install qemu

Create a Virtual Hard Disk with QEMU
------------------------------------

To create an image file with the size of 10GB and `qcow2` format
(default format for QEMU images), run:

    qemu-img create -f qcow2 testing-image.img 10G

Note that a new file called `testing-image.img` is now created at your
home folder (or the place where you run the terminal). Note also that
the size of this file is not 10 Gigabytes, it is around 150KB only; QEMU
will not use any space unless needed by the virtual operating system, but
it will set the maximum allowed space for that image to 10 Gigabytes
only.

Install Ubuntu on the Virtual Hard Disk
---------------------------------------

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

    qemu-system-x86_64 -m 1024 -boot d -enable-kvm -smp 3 -net nic -net user -hda testing-image.img

*Please note QEMU `qemu-system-x86_64` emulates a 64-bit architecture.*

Emulate Raspberry Pi with QEMU
------------------------------

### Download a pre-built kernel

    wget https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/master/kernel-qemu-4.4.34-jessie

### Download the Raspbian image

Download a `.img` file from Raspbian website:
https://www.raspberrypi.org/downloads/raspbian/

### Start the emulator

    qemu-system-arm -kernel ./kernel-qemu-4.4.34-jessie -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" -hda raspbian-stretch-lite.img -cpu arm1176 -m 256 -machine versatilepb -no-reboot -serial stdio

-   `kernel-qemu-4.4.34-jessie` is the pre-built kernel file.

-   `raspbian-stretch-lite.img` is the Raspbian image file.

*Please note QEMU `qemu-system-arm` emulates an ARM architecture.*

Manage VM guests with virsh
---------------------------

`virsh` is a command line interface tool for managing guests and the
hypervisor.

To initiate a hypervisor session with virsh :

    virsh connect <name>

Where is the machine name of the hypervisor. If you want to initiate a
read-only connection, append the above command with -readonly.

To display the guest list and their current states with virsh:

    virsh list [ --inactive  |  --all]

The --inactive option lists inactive domains (domains thxsat have been
defined but are not currently active). The --all domain lists all
domains, whether active or not.

Resources
---------

General

-   Official website for `libvirt` is here: https://libvirt.org/

-   Home page of KVM is here: https://www.linux-kvm.org/page/Main_Page

-   QEMU home page: https://www.qemu.org/

-   QEMU User Documentation: https://qemu.weilnetz.de/doc/qemu-doc.html

-   Wikipedia page for QEMU: https://en.wikipedia.org/wiki/QEMU

Comparison

-   <http://opensourceforu.com/2012/05/virtualisation-faceoff-qemu-virtualbox-vmware-player-parallels-workstation/>

-   <https://stackoverflow.com/questions/43704856/what-is-the-difference-qemu-vs-virtualbox>
