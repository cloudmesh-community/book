# Head Node Setup

Your head node will give you access to your compute nodes.

## Setup

The setup script will install dnsmasq for DNS/DHCP server and Cluster SSH. It will also configure the iptables to allow the compute nodes to access the internet through the head node.

Run setup script:

    sudo sh setup
    
Reboot:

    reboot
    
Run Cluster SSH:

    cssh -l pi rpcluster
    
This opens a new SSH window with username *pi* for each hostname in rpcluster (defined in **/etc/clusters**). Click on the gray box to type commands into each node.
