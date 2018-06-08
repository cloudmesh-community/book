# Intructions for installing kubernetes

## First install doker, disable swap, install kubeadm

All the following steps are made automatically by the 
docker_kubernetes_install.sh script.

### Install docker
In order to install kubernetes you first need to have docker installed. This is 
very strait forward.

### Disable swap memory
Docker has an issue (in my opinion sever) in that it is **not compatible with 
SWAP memory**, therefore it is needed to disable it. This might create some 
issues, if you encounter them you should try to reboot the cluster again, if 
that fails change line 16 in the script from

orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1"

to

orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=memory"

### Installing kubernetes administrator

Finally, to configure kubernetes you'll need kubeadm. Now the Pi needs to be 
rebooted.

### *All of this will be done by the script, don't worry* (maybe worry)

## For the nodes

All of the above needs to be done in each node as well. The script
copy_dk_kub_install_script_to_nodes.sh should copy the needed script to each of 
them and run it. It is set up to work with 4 nodes named rp\<number\> with pi as 
the username (the numbers start at 1 because the head node is rp0). Changing 
the number of nodes is trivial, if all of your nodes have the same username it 
is also trivial.

If your nodes are not configured like that you'll need to change 
this script or copy docker_kubernetes_install.sh to each of the nodes manually.
We plan on making this script independent on the number of nodes.