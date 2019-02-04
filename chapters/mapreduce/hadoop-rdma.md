# Hadoop RDMA :o: :question:

This section was copied with permission from: <https://www.chameleoncloud.org/appliances/17/docs/>

The CentOS 7 SR-IOV RDMA-Hadoop appliance is built based on CC-CentOS7
appliance. In this appliance, it also contains a CentOS 7 Virtual
Machine image, a VM startup script and a Hadoop cluster launch script,
so that users can launch VMs with SR-IOV in order to run RDMA-Hadoop
across these VMs on SR-IOV enabled InfiniBand clusters.

* Image name: CC-CentOS7-RDMA-Hadoop
* Default user account: cc
* Remote access: Key-Based SSH
* Root access: passwordless sudo from the cc account
* Chameleon admin access: enabled on the ccadmin account
* Cloud-init enabled on boot: yes
* Repositories (Yum): EPEL, RDO (OpenStack)
* Installed packages:
* Rebuilt kernel to enable IOMMU
* Mellanox SR-IOV drivers for InfiniBand
* KVM hypervisor
* Standard development tools such as make, gcc, gfortran, etc.
* Config management tools: Puppet, Ansible, Salt
* OpenStack command-line clients
* Included VM image name: chameleon-rdma-hadoop-appliance.qcow2
* Included VM startup script: start-vm.sh
* Included Hadoop cluster launch script: launch-hadoop-cluster.sh
* Default VM root password: nowlab

Please refer to the bare metal user guide for documentation on how to
reserve and provision resources using the appliance of
CC-CentOS7-RDMA-Hadoop.

Launching a Virtual Hadoop Cluster on Bare-metal InfiniBand Nodes with SR-IOV on Chameleon
------------------------------------------------------------------------------------------

We provide a CentOS 7 VM image (chameleon-rdma-hadoop-appliance.qcow2)
and a Hadoop cluster launch script (launch-hadoop-cluster.sh) to
facilitate users to setup Virtual Hadoop Clusters effortlessly.

First, launch bare-metal nodes using the RDMA-Hadoop Appliance and
select one of the nodes as the bootstrap node. This node will serve as
the host for the master node of the Hadoop cluster and will also be used
to setup the entire cluster. Now, ssh to this node. Before you can
launch the cluster, you have to download your OpenStack credentials file
(see how to download your credentials file). Then, create a file
(henceforth referred to as ips-file) with the ip addresses of the
bare-metal nodes you want to launch your Hadoop cluster on (excluding
the bootstrap node), each on a new line. Next, run these commands as
root:

    [root@host]$ cd /home/cc
    [root@host]$ ./launch-hadoop-cluster.sh <num-of-vms-per-node> <num-of-MB-per-VM> <num-of-cores-per-VM> <ips-file> <openstack-credentials-file>

The launch cluster script will launch VMs for you, then install and
configure Hadoop on these VMs. Note that when you launch the cluster for
the first time, a lot of initialization is required. Depending on the
size of your cluster, it may take some time to setup the cluster. After
the cluster setup is complete, the script will print an output telling
you that the cluster is setup and how you can connect to the Hadoop
master node. Note that the minimum required memory for each VM is 8,192
MB. The Hadoop cluster will already be setup for use. For more details
on how to use the RDMA-Hadoop package to run jobs, please refer to its
user guide.

Launching Virtual Machines Manually
-----------------------------------

We provide a CentOS 7 VM image (chameleon-rdma-hadoop-appliance.qcow2)
and a VM startup script (start-vm.sh) to facilitate users to launch VMs
manually. Before you can launch a VM, you have to create a network port.
To do this, source your OpenStack credentials file (see how to download
your credentials file) and run this command:

    [user@host]$ neutron port-create sharednet1

Note the MAC address and IP address are in the output of this command.
You should use this MAC address while launching a VM and the IP address
to ssh to the VM. You also need the PCI device ID of the virtual
function that you want to assign to the VM. This can be obtained by
running \"lspci \| grep Mellanox\" and looking for the device ID (with
format - XX:XX.X) of one of the virtual functions as shown below:

    [cc@host]$ lspci | grep Mellanox
    03:00.0 Network controller: Mellanox Technologies MT27500 Family [ConnectX-3]
    03:00.1 Network controller: Mellanox Technologies MT27500/MT27520 Family [ConnectX-3/ConnectX-3 Pro Virtual Function]
    ...

The PCI device ID of the Virtual Function is 03:00:1 in the previous
example.

Now, you can launch a VM on your instance with SR-IOV using the provided
VM startup script and corresponding arguments as follows with the root
account.

    [root@host]$ ./start-vm.sh <vm-mac> <vm-ifname> <virtual-function-device-id>

Please note that and are the ones you get from the outputs of previous
commands. And is the name of VM virtual NIC interface. For example:

    [root@host]$ ./start-vm.sh fa:16:3e:47:48:00  tap0  03:00:1

You can also edit corresponding fields in VM startup script to change
the number of cores, memory size, etc.

You should now have a VM running on your bare metal instance. If you
want to run more VMs on your instance, you will have to create more
network ports. You will also have to change the name of VM virtual NIC
interface to different ones (like tap1, tap2, etc.) and select different
device IDs of virtual functions.

Extra Initialization when Launching Virtual Machines
----------------------------------------------------

In order to run RDMA-Hadoop across VMs with SR-IOV, and keep the size of
VM image small, extra initialization will be executed when launching VM
automatically, which includes:


* Detect Mellanox SR-IOV drivers, download and install it if
nonexistent \* Detect Java package installed, download and install if
non-existent \* Detect RDMA-Hadoop package installed, download and
install if non-existent

After finishing the extra initialization procedure, you should be able
to run Hadoop jobs with SR-IOV support across VMs. Note that this
initialization will be done automatically. For more details about the
RDMA-Hadoop package, please refer to its user guide.

Important Note for Tearing Down Virtual Machines and Deleting Network Ports
---------------------------------------------------------------------------

Once you are done with your experiments, you should kill all the
launched VMs and delete the created network ports. If you used the
launch-hadoop-cluster.sh script to launch VMs, you can do this by
running the kill-vms.sh script as shown below. This script will kill all
launched VMs and also delete all the created network ports.

    [root@host]$ cd /home/cc                                                                 
    [root@host]$ ./kill-vms.sh <ips-file> <openstack-credentials-file>
    \end{vernatim}

    If you launched VMs using the start-vm.sh script, you should first manually kill all the VMs. Then, delete all the created network ports using this command:

    [user@host]$ neutron port-delete PORT

Please note that it is important to delete unused ports after
experiments.
