# Raspberry Pi Kubernetes Cluster (A) :o:

## Hardware

Each cluster consists of:

* 1 head node ([setup](head)) (recommend following the instructions here first)
* 4 compute nodes

## General Configuration

First you need to flash Raspbian Stretch on the SD cards

1. Download Raspbian image <https://www.raspberrypi.org/downloads/>.
2. Download Etcher <https://etcher.io/>.
3. Using Etcher, flash Raspbian onto SD card.

Next you need to configure the keyboard layout

The default keyboard layout may need to be changed to US.

Menu -> Preferences -> Mouse and Keyboard Settings -> Keyboard tab -> Variant ->
 English (US)

Most importantly you need to change the password

    passwd
    
Enter new password via prompts.

### Change hostnames

Change hostname of each raspberry pi (in descending order).

1. rp0
2. rp1
3. rp2
4. rp3
5. rp4

This can be done on the command line using:

    sudo raspi-config
    
Or on the desktop by going to Menu -> Preferences -> Raspbery Pi Configuration

Or by modifying **/etc/hostname**

### Configure Head Node

Install Dependencies:

    apt-get update
    apt-get install -qy dnsmasq clusterssh iptables-persistent

#### Create Static IP

Copy old config (-n flag prevents overwrite):

    \cp -n /etc/dhcpcd.conf /etc/dhcpcd.conf.old
    
To update DHCP configuration, add the following to **/etc/dhcpd.conf**:
 
    interface wlan0
    metric 200

    interface eth0
    metric 300
    static ip_address=192.168.50.1/24
    static routers=192.168.50.1
    static domain_name_servers=192.168.50.1

#### Configure DHCP Server:

Copy old config (-n flag prevents overwrite):

    \cp -n /etc/dnsmasq.conf /etc/dnsmasq.conf.old
    
To update DNS configuration, add the following to **/etc/dhcpd.conf**
    
    interface=eth0
    interface=wlan0

    dhcp-range=eth0, 192.168.50.1, 192.168.50.250, 24h
    
#### NAT Forwarding

To Setup NAT Forwarding, uncomment the following line in **/etc/sysctl.conf**:

    net.ipv4.ip_forward=1
    
#### IP Tables

Create IP Tables:

    sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    sudo iptables -A FORWARD -i $INTERNAL -o wlan0 -j ACCEPT
    sudo iptables -A FORWARD -i $EXTERNAL -o eth0 -j ACCEPT

Make rules permanent:

    iptables-save > /etc/iptables/rules.v4

### SSH Configuration

**Note: Gregor says this is not best practice**

Generate SSH keys:

    ssh-keygen -t rsa
    
Copy key to each compute node:

    ssh-copy-id <hostname>
    
For hostnames rp1-4 (final node names will be: rp0, rp1, rp2, rp3, rp4).

### Configure Cluster SSH

To update Cluster SSH configuration, add the following to **/etc/clusters**:

    rpcluster rp1 rp2 rp3 rp4

Now you can run commands to all clusters by:

    cssh rpcluster

## Installing kubernetes

First install doker, disable swap, install kubeadm

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

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1"
```

to

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=memory"
```

### Installing kubernetes administrator

Finally, to configure kubernetes you'll need kubeadm. Now the Pi needs to be 
rebooted.

---

:warning: **All of this will be done by the script, don't worry** (maybe worry)

---


### Configure the nodes

All of the above needs to be done in each node as-well. The script

* [kubernetes/copy_dk_kub_install_script_to_nodes.sh](kubernetes/copy_dk_kub_install_script_to_nodes.sh)

should copy the needed script to each of them and run it. It is set up
to work with 4 nodes named `rp<number>` with pi as the username (the
numbers start at 1 because the head node is rp0). Changing the number
of nodes is trivial, if all of your nodes have the same username it is
also trivial.


If your nodes are not configured like that you'll need to change this
script or copy `docker_kubernetes_install.sh` to each of the nodes
manually.  We plan on making this script independent on the number of
nodes.


## Files

* [kubernetes/adm_kub_config.yaml](kubernetes/adm_kub_config.yaml)
* [kubernetes/config_kub.sh](kubernetes/config_kub.sh)
* [kubernetes/copy_dk_kub_install_script_to_nodes.sh](kubernetes/copy_dk_kub_install_script_to_nodes.sh)
* [kubernetes/docker_kubernites_install.sh](kubernetes/docker_kubernites_install.sh)
* [kubernetes/issues_todo.md](kubernetes/issues_todo.md)
* [kubernetes/kube_install_and_config_readme.md](kubernetes/kube_install_and_config_readme.md)
* [kubernetes/useful_links.txt](kubernetes/usefull_links.txt)

