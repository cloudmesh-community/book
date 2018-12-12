# Network of Pis (NOW) {#pi-now-main}

The purpose of setting up a cluster of Raspberry Pi computers is to be able to
experiment with different server and cluster technologies on a small scale. To
this end we want to be able to use a network configuration that mirrors a large
scale cloud configuration. This section will explain how to setup several
Raspberry Pis in a cluster configuration to run experiments on them.

## Network of Pis Configurations {#pi-now-configs}

There are several possible configurations for a network of Pis. One possibility
is to connect each of the Pis to your local network so that you can
directly connect to each of the Pis in the cluster from your laptop. This
option can be easy to setup but it may have problems scaling up to several
hundred Raspberry Pis. The second option is to use one of the Pi computers as a
master or router and for the other Pis in the cluster to access the Internet
through this master Pi's connection. Note that in most situations each Pi will
need to be able to access the Internet to download packages and interact with
public services. In the second option, however, the worker Pis will be separated
from the main network by the master Pi and it may not be possible to directly
access them, for example, over `ssh` from your laptop.

In the first option we can directly connect each Raspberry Pi to your local
network using either the Ethernet adapter on the Pi or using the Wireless
adapter on the Pi. If using the Ethernet adapter and intermediary router or
switch can also be used to connect the Pis to the local network. The network can
be visualized in +@fig:pi-cluster-network-direct. To setup this kind of cluster
please follow the instructions in
[Direct Network Cluster](#pi-direct-network-cluster).

![Direct Network Cluster](images/pi-cluster-network-direct.png){#fig:pi-cluster-network-direct}

In the second option we will need to configure the master Pi to have two network
interfaces enabled. One of the interfaces will connect to the local network and
have direct internet access and will accessible to the other computers on the
network. The second interface will be attached to the private network that the
worker Pis are connected to and will serve as the DHCP server and router for
that private network. Since the Raspberry Pi comes with an Ethernet adapter and
a wireless network adapter, you can use the built-in Ethernet adapter on all of
the Pis to connect to a switch and form a private network this way. The master
Pi can then connect to your local network using its wireless adapter. Another
possibility is to use a USB Ethernet adapter (purchased from this list of
[Raspberry Pi compatible USB Ethernet adapters](https://elinux.org/RPi_USB_Ethernet_adapters))
on the master Pi so that it can have a stable, wired connection to both
networks. In either case the network setup is illustrated in
+@fig:pi-cluster-network-private. The steps to setup this kind of private
network cluster can be found in
[Private Network Cluster](#pi-private-network-cluster).

![Private Network Cluster](images/pi-cluster-network-private.png){#fig:pi-cluster-network-private}

## Network of Pis Hostnames {#pi-network-hostnames}

When setting up a cluster of Pis it is necessary to assign a hostname to each Pi
in the cluster. These names are important because they must not be repeated
across Pi clusters and they must not conflict with other devices on the same
network. If you are setting up a small network, almost any hostname will be
fine, but for larger networks you should come up with a naming scheme to avoid
conflicts. For a small cluster you may pick a designation such as a color or
name and then assign a number to each Pi. For example, if you have three Pis you
could call them `red01`, `red02`, and `red03`.

For a large cluster we recommend giving each cluster a unique id, for example, a
number from 1 to 100, and then giving each node in the cluster an id that is
based on the cluster that it is assigned to. For example, if each cluster is
named `clusterNN` where `NN` is a zero-padded number from `01` to `99` then we
would have clusters named `cluster01`, `cluster02`, ...,  `cluster11`, etc. The
cluster name will not be assigned to any particular Pi. Each Pi will be given a
name that is based on the cluster it is assigned to. If each of your clusters
are made of 5 Pis then you can number your individual Pis with the following
formula:

```
node number = (cluster number - 1) * 5 + pi number in cluster
```

Our `cluster01` cluster would then have the Pis `node001` to `node005` and
`cluster02` would have the Pis `node006` to `node010`. Our `cluster11` would
have nodes `node051` to `node055`. We assume the lowest numbered node in each
cluster is the master node. If you have more than 999 Pis or clusters with more
than 5 Pis per cluster then you will have to adjust the naming scheme
accordingly.

## Pi Cluster Preparation {#pi-cluster-prep}

To prepare to setup a Pi cluster you will need to choose whether you will be
setting up each Raspberry Pi by hand or by using the tools and scripts that we
have developed to make this task easier and less error prone. The primary tool
that will save time in setting up a Pi cluster is
[cm-burn](https://github.com/cloudmesh-community/cm-burn) which was
introduced in the section [Burn an SD Card with cm-burn](#pi-cm-burn-sd-card).
The installation and setup instructions for cm-burn can be found in the
[cm-burn README.md](https://github.com/cloudmesh-community/cm-burn/blob/master/README.md).
Once you have `cm-burn` successfully installed you can use the instructions here
to setup your cluster. We have also developed some scripts to help setup a Pi
cluster in the
[cloudmesh-community/pi](https://github.com/cloudmesh-community/pi)
project. These scripts can be copied to the Pi after it is running to help
complete various setup tasks easily. Use of these scripts will be covered in the
following sections.

If you choose not to use `cm-burn` or to use our scripts we will provide the
manual setup steps for you to complete. In most cases the manual steps are the
exact same as the operations the scripts perform, so you can also check the
manual steps if you are curious about what the scripts are doing. Before
beginning the manual steps below we assume you are able to burn an image to an
SD card, to login to the Pi, and to complete the locale and hostname setup at a
minimum. If you have not completed these steps, please see the following
sections for details:

* [Install Raspbian on a SD card](#s-install-raspbian)
* [Password](#s-pi-setup-password)
* [Set the hostname](#s-pi-set-hostname)

Any other required steps will be explained in the following sections.

## Direct Network Cluster Setup {#pi-direct-network-cluster}

An overview of this cluster setup is included in the
[Network of Pis Configurations](#pi-now-configs) section. To complete this setup
you will need to select a set of hostnames for the PIs in your cluster. Please
see the [Network of Pis Hostnames](#pi-network-hostnames) section for our
recommendation on setting hostnames. Since each Pi in the cluster will directly
connect to the local network each Pi will have the same network setup. This
makes using this option easier for initial setup and experimentation with a
cluster of Pis. You will need to choose whether the Pis will connect to your
network through a wired Ethernet connection or through a WiFi connection. In
either case you can choose to statically assign and IP address or to let each Pi
get a dynamic IP address using DHCP. Using DHCP may be easier at first but it
can also be a problem if you do not have a monitor connected to the Pi because
you then will not know in advance the IP address that is assigned to each Pi.
Please see the section
[Discover Pi DHCP Network Addresses](#pi-find-dhcp-ip-address)
for details on this procedure.

## Private Network Cluster {#pi-private-network-cluster}

An overview the design of a private Pi cluster is included in the
[Network of Pis Configurations](#pi-now-configs) section. To complete this setup
you will need to select a set of hostnames for the PIs in your cluster. Please
see the [Network of Pis Hostnames](#pi-network-hostnames) section for our
recommendation on setting hostnames.

Network of workstations

Have a number of PIs available on a network to which we can login and execute tasks on.

Elementary to most other cluster deployment activities

Uses ssh key from a server to login to all Pis

## Discover Pi DHCP Network Addresses {#pi-find-dhcp-ip-address}

If you setup your Pis using DHCP on your local network then you may not know the
IP address that has been dynamically assigned to each Pi. If you have physical
access to each Pi and a compatible monitor and keyboard then you can login to
each of them in sequence and then run `ifconfig` to determine which IP address
has been assigned to each of them. If you have access to the DHCP server that
assigns IP address (for example, in your home network) you can also usually
access that device through a webpage to find out which IP address has been
assigned to each device on the network.


## Parallel Shell

TODO

## Cloudmesh Parallel

TODO

## Other Parallel Execution

TODO


* <https://www.rittmanmead.com/blog/2014/12/linux-cluster-sysadmin-parallel-command-execution-with-pdsh/>
* <https://www.linux.com/news/parallel-ssh-execution-and-single-shell-control-them-all>
* <https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/>
* <https://github.com/vallard/psh>
* <https://github.com/karrick/psh/blob/master/psh>
