Virtual Box
===========

For development purposes we recommend that you use for this class an
Ubuntu virtual machine that you set up with the help of virtualbox. We
recommend that you use the current version of ubuntu and do not install
or reuse a version that you have set up years ago.

As access to cloud resources requires some basic knowledge of linux and
security we will restrict access to our cloud services to those that
have demonstrated responsible use on their own computers. Naturally as
it is your own computer you must make sure you follow proper security.
We have seen in the past students carelessly working with virtual
machines and introducing security vulnerabilities on our clouds just
because "it was not their computer." Hence, we will allow using of cloud
resources only if you have demonstrated that you responsibly use a linux
virtual machine on your own computer. Only after you have successfully
used ubuntu in a virtual machine you will be allowed to use virtual
machines on clouds.

A *cloud drivers license test* will be conducted. Only after you pass it
we wil let you gain access to the cloud infrastructure. We will announce
this test. Before you have not passed the test, you will not be able to
use the clouds. Furthermore, you do not have to ask us for join requests
to cloud projects before you have not passed the test. Please be
patient. Only students enrolled in the class can get access to the
cloud.

If you however have access to other clouds yourself you are welcome to
use the, However, be reminded that projects need to be reproducible, on
our cloud. This will require you to make sure a TA can replicate it.

Let us now focus on using virtual box.

Installation
-----------

First you will need to install virtualbox. It is easy to install and
details can be found at

* <https://www.virtualbox.org/wiki/Downloads>

After you have installed virtualbox you also need to use an image. For
this class we will be using ubuntu Desktop 16.04 which you can find at:

* <http://www.ubuntu.com/download/desktop>

Please note some hardware you may have may be too old or has too little
resources to be useful. We have heard from students that the following
is a minimal setup for the desktop machine:

-   multi core processor or better allowing to run hypervisors

-   8 GB system memory

-   50 GB of free hard drive space

For virtual machines you may need multiple, while the minimal
configuration may not work for all cases.

As configuration we often use

minimal

:   1 core, 2GB Memory, 5 GB disk

latex

:   2 core, 4GB Memory, 25 GB disk

A video to showcase such an install is available at:

[:clapper: Virtualbox seconds Video](https://youtu.be/NWibDntN2M4)

If you specify your machine too small you will not be able to install
the development environment. Gregor used on his machine 8GB RAM and 25GB
diskspace.

Please let us know the smallest configuration that works.

Guest additions
---------------

The virtual guest additions allow you to easily do the following tasks:

-   Resize the windows of the vm

-   Copy and paste content between the Guest operating system and the
    host operating system windows.

This way you can use many native programs on you host and copy contents
easily into for example a terminal or an editor that you run in the Vm.

A video is located at

[:clapper: Virtualbox 4:46 Video](https://youtu.be/wdCoiNdn2jA)

Please reboot the machine after installation and configuration.

On OSX you can once you have enabled bidirectional copying in the Device
tab with

OSX to Vbox:

:   command c shift CONTRL v

Vbox to OSX:

:   shift CONTRL v shift CONTRL v

On Windows the key combination is naturally different. Please consult
your windows manual. If you let us know TAs will add the information
here.

Exercises
---------

E.Virtualbox.1:

> Install ubuntu desktop on your computer with guest additions.

E.Virtualbox.2:

> Make sure you know how to paste and copy between your host and guest
> operating system.

E.Virtualbox.3:

> Install the programs defined by the development configuration.

E.Virtualbox.4:

> Provide us with the key combination to copy and paste between
> Windows and Vbox.
