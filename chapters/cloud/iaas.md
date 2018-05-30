How to Run VMs (IaaS)
=====================

-   17 Video lectures (2 hours 7 minutes 9 seconds)

Course Expectations
-------------------

Examples and definitions are given for SaaS, PaaS, and IaaS.
Computational models must be designed with the problems and effective
resources in mind. A demonstration of cloud use for Bioinformatics on
the FutureGrid educational testbed shows how clouds offer advantages of
provisioning and virtual cluster support. Overhead and performance
issues are touched upon through charts showing the use of three
different virtual clusters.

-   Video: [Youtube](https://www.youtube.com/watch?v=j3sUW376pw8) (7:45)

-   Slide:
    [PDF](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Student Work 1
--------------

The work of previous B649 students is presented, covering a variety of
topics and software: HBase, DryadLINQ, virtualization, commercial cloud
storage, and IU's Twister iterative MapReduce.

-   Video: [Youtube](https://www.youtube.com/watch?v=DYG6_bUGsqY) (8:48)

-   Slide: [PDF (Page
    7-11)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Student Work 2
--------------

This lecture offers further examples of prior student projects in areas
like cloud storage, infrastructure and platforms, as well as high level
languages like Apache Pig. Other topics cover MapReduce in Single
Program Multiple Data mode, genetic algorithms in MapReduce, Hadoop
supporting recommender systems, K-means clustering, etc. Following this
the benefits/vulnerabilities of clouds and some of their most well-known
programs are showcased in other research assignments.

-   Video: [Youtube](https://www.youtube.com/watch?v=DqaQ0kemmaw)
    (10:03)

-   Slide: [PDF (Page
    12-27)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Growth of Virtual Machines
--------------------------

Importance of virtualization is explored, including cross-platform
applications. Virtualization has seen rapid growth in recent years in
terms of use and services offered. Virtual machines differ from
traditional computers in that software virtualization layer (hypervisor)
runs on hardware, allowing guest OS to run on top of host OS. VMs can
run independent of hardware specifications. Four different types of VM
architecture, defined by the layer which the virtual machine monitor
(VMM) runs on. VM is identical to physical machines and can be saved and
stored, as well as migrated across hardware.

-   Video: [Youtube](https://www.youtube.com/watch?v=5oKoAPCXLws)
    (10:16)

-   Slide: [PDF (Page
    28-40)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Implementation Levels
---------------------

Virtualization can be implemented on five levels: application, library,
OS, hardware, and instruction. Their benefits are compared in terms of
performance, flexibility, complexity, and isolation. A layout is
provided for the Linux virtualization layer, OpenVZ (OS level), which
creates virtual private servers. CUDA is a high performance computing
library, not designed for VMs; vCUDA is a virtual layer that allows
interaction between CUDA and VMs, creating a virtual CUDA library.

-   Video: [Youtube](https://www.youtube.com/watch?v=Le-kv-eAhvg) (7:57)

-   Slide: [PDF (Page
    41-46)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Tools and Mechanisms
--------------------

A list of major hypervisors is given. Type 1 hypervisor resides on the
bare metal computer, while Type 2 runs over the host OS. XEN is an open
source hardware level hypervisor: consists of hypervisor, kernel, and
application. Domain0 in XEN is a VM that manages other VMs. Two types of
hardware virtualization: full virtualization and host-based
virtualization. Para-virtualization does not need to modify the guest OS
like full virtualization and works through hypercalls. An example is the
ESX server from VMware.

-   Video: [Youtube](https://www.youtube.com/watch?v=VYz5rp5HDVE) (7:32)

-   Slide: [PDF (Page
    47-57)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

CPU, Memory & I/O Devices
-------------------------

A hybrid approach to virtualization involves offloading some tasks to
the hardware to reduce overhead. This can be combined with
para-virtualization for even greater effects. In a guest OS, the VMM
provides shadow page tables to transfer virtual memory to machine
memory. An example is shown in the Intel Extended Page Table. A
virtualization layer for an I/O device is possible, allowing it to act
like a physical device and manage host and guest addresses, shown in a
detailed VMware example.

-   Video: [Youtube](https://www.youtube.com/watch?v=I_J4eUUavSY) (6:41)

-   Slide: [PDF (Page
    58-65)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Clusters and Resource Mgmt.
---------------------------

Characteristics of VM clusters are listed, including the ability to run
multiple VMs on the same node and size alteration. Physical clusters are
linked through nodes, while virtual clusters can be linked through
physical or virtual nodes and can be replicated in virtual servers.
Prepackaged OS can be installed in a virtual cluster. Should a VM fail
for any reason, its image can be migrated to a new host so work is not
lost. An example of this is demonstrated with XEN.

-   Video: [Youtube](https://www.youtube.com/watch?v=Mn9pgGtFy4g) (5:07)

-   Slide: [PDF (Page
    66-73)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Data Center Automation
----------------------

Whole data centers can be virtualized, enabling for the construction of
private clouds. Some tools for Infrastructure as a Service clouds are
Nimbus, Eucalyptus, OpenNebula, and vSphere. Eucalyptus is shown in
greater detail. Trust issues in cloud security are answered in virtual
machines. Suggested reading material is provided at the end.

-   Video: [Youtube](https://www.youtube.com/watch?v=mvXBRvTwAVg) (3:30)

-   Slide: [PDF (Page
    74-81)](https://drive.google.com/open?id=0B88HKpainTSfQU1uQmxZWHdWQ1k)

Clouds in the Workplace
-----------------------

Clouds run as servers for data storage and sharing on the Internet in an
on-demand capacity. Cloud services are scalable depending on the
client's needs, allowing for a seemingly limitless source of computing
power that can expand or shrink to meet financial demands. Some examples
of cloud services are LinkedIn, Amazon S3, and Google App Engine.
Different variations of clouds like IaaS and PaaS are offered by both
open source and commercial providers. Cloud systems are composed of
separate elements like Eucalyptus, Xen and VMware.

-   Video: [Youtube](https://www.youtube.com/watch?v=Endt6mWUfEo) (7:13)

Checklists & Challenges
-----------------------

The capabilities of several IaaS cloud structures like Amazon EC2 or
PaaS like Microsoft Azure are listed. Public and private clouds share
certain features; the main difference is public clouds are owned by
service providers while private clouds are offered by individual
corporations. Certain enabling technologies are required for clouds to
provide quick and scalable computing. These include virtual cluster
provisioning and multi-tenant environments. PaaS demands the capability
to process huge amounts of data as in the case of web searches. Some
challenges faced by cloud computing include vendor lock-in owing to lack
of standard APIs and metrics; for scientists, there is uncertainty about
whether experiments can be reproduced effectively in different cloud
environments. However there are distinct advantages clouds potentially
have to offer: standardized APIs can eliminate lock-in, and encryption
offers data confidentiality.

-   Video: [Youtube](https://www.youtube.com/watch?v=cwtWpZcWuQ0) (9:08)

Data Center Setup
-----------------

Huge data centers enable cloud computing, containing up to a million
servers. Large data centers charge less for their services than small
ones. A diagram illustrates the typical setup of a cloud; rack space on
the bottom, on top of which are load balancers, then excess routers and
border routers. The next figure compares cost effectiveness in a
traditional IT model to a cloud. Other figures display small server
clusters and a typical data center arrangement, including emergency
power supply and cooling system. A chart shows the power consumption
based on CPU, disk, etc. Disks in warehouse servers may be onsite or
attached to outside connections like InfiniBand. Switches can form an
array of racks. The distribution of memory across a local, rack, or
array server in warehouse server setup is listed.

-   Video: [Youtube](https://www.youtube.com/watch?v=zBVtXzqF2ew) (7:49)

Cultivating Clouds
------------------

Power utilization effectiveness (PUE) for a warehouse is determined by
comparing it to IT power usage. Racks can contain 40 servers, shipping
containers can have up to 1,000 servers; a data center could take 2
years to construct. Warehouse scale computing has greater economy of
scale than data centers by reducing network and administrative costs.
Individual users can interact with clouds in the SaaS model, while
organizations use PaaS. Clouds generally use VMs to recover from system
failures. It is predicted that the cloud job market and demand for
clouds will experience great growth in the future. Clouds have become
ubiquitous in all aspects of the private and public sector. In the
future clouds must take into account user privacy, data security and
copyright protection.

-   Video: [Youtube](https://www.youtube.com/watch?v=zxoqRdvXM28) (5:10)

Applying for FutureSystems Account
----------------------------------

-   Video: [Youtube](https://www.youtube.com/watch?v=98ERlWi3k3U) (5:32)

-   Slide: [PDF (Page
    1-9)](https://drive.google.com/open?id=0B88HKpainTSfZENxeUlOcVFUTkU)

FutureSystems India OpenStack
-----------------------------

-   Video: [Youtube](https://www.youtube.com/watch?v=hyKYTpNmJZc)
    (10:28)

-   Slide: [PDF (Page
    10-16)](https://drive.google.com/open?id=0B88HKpainTSfZENxeUlOcVFUTkU)

Starting VMs on FutureSystems
-----------------------------

-   Video: [Youtube](https://www.youtube.com/watch?v=RPnhJs4IcfQ) (6:40)

-   Slide: n/a (video lecture only)

Hadoop WordCount on VMs
-----------------------

-   Video: [Youtube](https://www.youtube.com/watch?v=1TrjmcPHrRU) (7:30)

-   Slide: [PDF (Page
    17-22)](https://drive.google.com/open?id=0B88HKpainTSfZENxeUlOcVFUTkU)
