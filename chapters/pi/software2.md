### Coder

Targeted at the very beginner to Web programming, we will not use this
here.

* <https://googlecreativelab.github.io/coder/>

provide a mini tutorial

## Computing


### Numpy

Refer to other section in book and describe what is different

provide a mini tutorial

### Scipy

Refer to other section in book and describe what is different

provide a mini tutorial

### Image Processing

Refer to other section in book and describe what is different

provide a mini tutorial

### DHCP Server

* <http://www.noveldevices.co.uk/rp-dhcp-server>

## Gregor's Notes


This section contains some unordered notes by Gregor that you may want
to look at and integrate into proper sections:

### editor

find an editor that is installed and can be used on commandline nano,
vi, other?

### hostname

The hostname is stored in `/etc/hostname`. Edit the file and change it
to a name such as green00, green01, green02, green03, green04, green05.
Be consistent with the names. The 00 host should be the top most host in
the cluster.

edit

    nano /etc/hostname

after you edited the hostname

    sudo /etc/init.d/hostname.sh start

Ideally we want to find out how to write the hostname after we burn the
SD card on the laptop that does the burning

develop a python script to do that

### Gather the mac addresses

Is there a better way?

    /sys/class/net/<interface-name>/address

    cat /sys/class/net/eth0/address
    cat /sys/class/net/wlan0/address
    ifconfig eth0

develop a python script to do that

### Enable sshd

Not tested

    sudo mv /boot/boot_enable_ssh.rc /boot/boot.rc
    sudo reboot

* <http://www.noveldevices.co.uk/rp-ssh>

Not sure if this is needed:

" You may find that you can connect to your Pi with SSH but the session
hangs after a successful logon. This is usually caused because of a
network QoS mismatch that affects certain switches and routers but you
can correct this by editing the two files

    /etc/ssh/ssh_config
    /etc/ssh/sshd_config

and adding

    IPQoS 0x00

to each file as the last record. " develop a a python script to do that

### USB stick

    cat /var/log/messages

find sda\*

Make sure to find the right name.

    sudo fdisk /dev/<device-name>
    sudo mkfs -t vfat /dev/<device-name>
    mkdir ~/<mount-point>
    sudo mount /dev/<device-name> ~/<mount-point>

### DHCP server on 00

    sudo apt-get update
    sudo apt-get install isc-dhcp-server
    sudo nano /etc/network/interfaces

Change it to

    iface eth0 inet static
    address <the-IP-address-of-your-Pi-that-will-be-the-DHCP-server>
    netmask <the-subnet-mask-of-your-LAN>
    gateway <the-IP-address-of-your-LAN-gateway>
    sudo nano /etc/dhcp/dhcpd.conf

uncomment the info so the server can start

    subnet <starting-IP-address-of-your-network> netmask <starting-IP-address-of-your-network> {

         range <first-IP-address-of-your-DHCP-address-range> <last-IP-address-of-your-DHCP-address-range>;

         option routers <the-IP-address-of-your-gateway-or-router>;

         option broadcast-address <the-broadcast-IP-address-for-your-network>;

    }

edit /etc/default/isc-dhcp-server

    DHCPD_CONF=/etc/dhcp/dhcpd.conf
    DHCPD_PID=/var/run/dhcpd.pid
    INTERFACES="eth0"

    sudo service isc-dhcp-server restart

### Temperature

    cat /sys/class/thermal/thermal_zone0/temp

### graphana

could be helpful to monitor cluster/clusters

* <https://github.com/grafana/grafana>

* <https://github.com/weaveworks/grafanalib>

there are many more, just search. we have not tested them example with
yaml

* <https://github.com/jakubplichta/grafana-dashboard-builder>

light scheme

in /etc/grafana/grafana.ini uncomment line and set

    default_theme = light 
