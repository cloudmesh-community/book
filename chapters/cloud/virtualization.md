# Virtualization


---

**:mortar_board: Learning Objectives**

* Gain understanding of the basic the concepts of virtualization
* Understand what a virtual machine is
* Understand what a Hypervisor is

---

Virtualization is one of the important technologies that started the
cloud revolution. It provides the basic underlaying principles for the
development and adoption of clouds. The concept, although old and
already used in the early days of computing, has recently been
exploited to lead to better utilization of servers as part of data
centers, but also the local desktops.

Virtualization enables to execute multiple applications in such a way
that the applications seem to run independently form each other in
their own virtualized context.

Examples of the usefulness of virtualization include testing of
applications and run experiments on a different operating system than
the one on our host computer. To enable this we need virtual machines.

## Virtual Machines

We define a virtual machine as follows:

> A virtual machine (VM) is a software-based emulation of a computer
> system. This can include process virtualization and physical
> computer virtualization such as running an operating
> system. Multiple virtual machines share the resources of the
> computer or system on which they run.

We distinguish the following types of Virtual machines

* **System Virtual Machines** or **Hardware Virtual Machine**, which
  is the virtualization of the operating system providing a complete
  system platform environment emulating the hardware. Here we
  essentially run another operating system on top of the existing OS
  while using a software abstraction between them allowing the
  virtualization.

  Examples of such virtualization include VirtualBox and VMWare.

* **Process Virtual Machines** or **Application Virtual Machine**
  which provides a platform independent programming environment that
  abstracts the details of the underneath hardware or OS from software
  or application runtime.

  Examples of such virtual machines include Java Virtual Machine (JVM)
  and the .NET Framework

Next we will be analyzing the system machine virtualization in more
detail, as they are one of the reasons for the clouds revolution.

## System Virtual Machines 

The use of a system as a virtual machine has its clear advantages for
the cloud. We distinguish two main ways of system virtualizing:

* **Bare-metal Virtualization** in which the virtual machine monitor 
  is installed directly on top of the hardware so that the it
  has direct access to the underlaying hardware. It hosts the
  operating system. The VMM is also called hypervisor. We also use for bare-metal supporting VMM the term *Type 1 hypervisor*.

* **Hosted Virtualization** in which the base operating system is
  installed on the hardware. Here a virtual machine monitor (VMM) is
  installed on top of the host OS allowing the users to run
  other operating systems on the VMM. In addition, the Virtual Machine
  Monitor or *Hypervisor* manages the deploymenst of potentialy
  multiple virtual machines on top of the underlaying Operating system.
  We also use for hosted VMM the term *Type 2 hypervisor*.

In either case the functionality a virtual machine is supported
through configuration files, specifications, and access to the
physical resources either directly or indirectly through the host
OS. A virtual machine provides the same functionality as a physical
computer, but with the advantage that through virtualization the are
portable, can be managed and provide increased security while
shielding the underlaying OS from harmful actions. As a virtual
machine is in principle a program, it consists of several files including
a configuration file, virtual disk files, virtual RAM, and a log
file. virtual machines are configured to run a virtual operating
system that allows applications to run on them. Each virtual machine
has its own copy of the OS making it independent and more secure.

End users and developers will benefit from using virtual machines in
case they need to operate or support on different hardware or porting software on it.

## Hosted Virtualization

As in the hosted virtualization the guest operating system accessed the underlaying hardware through the host OS, it usyally has limited acces to the hrdware as defined by the host OS. This allows the host OS to impose policies that govern the operation of  multiple guest OS concurrently. This includes management and scheduling of processes, memory, I/O operations to assign them appropreatly to the guest OS. Through this mechanism the hypervisor provides an emulation of available hardware to each Virtual Machine run on top of it in timesharing fashion for resource constraint or resource shared activities.

As example, the hypervisor has the ability to present generic I/O devices and it has no access to non-generic I/O devices. Generic I/O devices are network, interface cards,  CD-ROMs. Examples for non-generic I/O devices are PCI data acquisition card, etc. However with appropriate driver support even such devices could be made accessible to the VMs.

Often we also find that hosted virtualization supports  connected USB drives in the VMs which becomes very practical for USB attached devices needed in storage, or even edge computing applications.


Advantages of Hosted Virtualization include

* Multiple Operating systems run on separate virtual machines on a VMM. 
* Different Operating systems run on separate virtual machines on a VMM. 
* Hardware level driver support is controlled by VMM, allowing an isolation of certain security aspects for accessing the hardware.
* Instalation of software can be doen by the owner of the virtual machine and does not have to be conducted by the provider of the hypervisor.

Disadvantages of Hosted Virtualization include 


* Increased resource requirements as the GUest OS is running a full copy of the OS. In iits worst case this will lead to a significant performance reduction while using resources that are in contention.
*  The user of hypervisors must be familiar with operating system management and security to assure it is safe to use.

## Summary

To showcase how these technologies relate to each other wil like you to review +@fig:vm-taxonomy


![Virtualization Taxonomy](images/vm.png){@fig:vm-taxonomy}

We summarize the following *hypervisor* types:

* Type-1 hypervisors supporting native or bare-metal. They run directly on the host's hardware to control the hardware and to manage guest operating systems. 

* Type-2 hypervisors supporting hosted virtualization. They run on a conventional operating system (OS) just as other computer programs do. A guest operating system runs as a process on the host.

## Virtualization Approches

Next we look at different virtualization approaches that relate to resource utilization.

### Fullvirtualization

When looking at virtualization we often identify it with being a full virtualization. The hypervisor provides a full abstraction of the OS exposed to  the guest OS's. In this case, the the guest OS's the virtual machine just run without any special modification on the host OS. It just looks like an independent running computer [@paravsfull-virt]. 

### Paravirtualization

Para -- alongside/partial -- virtualization is developed to improve 
performance by intarcting between the OS and the hypervisor. This is done for  complex and time-consuming tasks that otherwise could not be managed by the VMM manager. Commands sent from the OS to the hypervisor are called *hypercalls* [@paravsfull-virt]. 

## Virtualization Technologies

In this section we cover introduction to underlying virtualization technologies used on some main stream platforms.


### Selected Hardware Virtualization Technologies

### AMD-V and Intel-VT

The hardware virtualization support enabled by AMD-V and Intel VT technologies introduces virtualization in the x86 processor architecture. According to Intel, Intel Hyper-Threading Technology allows a single processor to execute two or more separate threads concurrently. When it is enabled, multi-threaded software applications can execute their threads in parallel, thereby improving their performance.

### I/O MMU virtualization (AMD-Vi and Intel VT-d)

The term IOMMU is an abbreviation for input–output memory management unit. An IOMMU allows through virtual adresses to interface with physical adresses, allowing external  direct-memory-access–capable IO devices to interface with the main memory [@iommu-1]. AMD's I/O Virtualization Technology (AMD-Vi) was originally called *IOMMU*.

To use Intel's *Virtualization Technology for Directed I/O* (VT-d), both the motherboard chipset and system firmware (BIOS or UEFI) need to fully support the IOMMU I/O virtualization functionality for it to be usable [@iommu-2].



### Selected VM Virtualization Software and Tools

A number of noteworthy virtualization software and tools exist which make the development and use of virtualization on the hardware possible. They include

* Libvirt
* KVM
* Xen
* Hyper-V
* QEMU
* VMWare
* VirtualBox

We will be discussing them next.


#### Libvirt

[Libvirt](<https://libvirt.org/api.html>) is an library with an API for managing virtualization solutions such as provided by  KVM and Xen. It provides a common management API for them, allowing uniform, cross-hypervisor interfaces for higher-level management tools. Furthermoe, it  provides APIs for management of virtual networks and storage on the VM Host Server. The configuration of each VM Guest is stored in an XML file [@libvirt]. 

#### Libvirt (G)

#### KVM (F)

#### Xen (F)

#### Hyper-V (F)

#### QEMU (G)

#### VMWare (G)

#### VirtualBox (G)

### Selected Storage Virtualization Software and Tools

TBD
