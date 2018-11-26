# Pi Software Collection :o: :hand: fa18-516-03

Please improve the sections.

## Web Programming

### Coder

Targeted at the very beginner to Web programming, we will not use this
here.

* <https://googlecreativelab.github.io/coder/>

provide a section

## Computing

### Python on the Raspberry Pi :o: :hand: fa18-516-03

Python packages are typically installed using the `pip` tool. `pip` will
automatically detect if you are running a compatible OS and platform and will
download a [Python wheel](https://pythonwheels.com/) for a given package which
is a pre-compiled binary package that is compatible with your system. Since the
Pi is running an ARM processor (not Intel or AMD compatible) most of the wheels
hosted on PyPi (the standard Python package directory server) are not
compatible. However, there are Pi-compatible wheels hosted on
https://pythonwheels.com/. The pip package in the latest version of Raspbian is
updated to look in piwheels as an additional package index. If you have an older
version of Raspbian installed you can get the update by running
`sudo apt upgrade` to update your system. There is a
[piwheels FAQ](https://www.piwheels.hostedpi.com/faq.html) that you may consult
if you have any questions or issues.

### Numpy

Refer to other section in book and describe what is different

provide a setcion

### Scipy

Refer to other section in book and describe what is different

provide a setcion

### Image Processing

Refer to other section in book and describe what is different

provide a setcion

## System

### DHCP Server

* <http://www.noveldevices.co.uk/rp-dhcp-server>

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

### Enable SSH

Not tested

    sudo mv /boot/boot_enable_ssh.rc /boot/boot.rc
    sudo reboot

* <http://www.noveldevices.co.uk/rp-ssh>

:warning: Not sure if this is needed:

" You may find that you can connect to your Pi with SSH but the session
hangs after a successful logon. This is usually caused because of a
network QoS mismatch that affects certain switches and routers but you
can correct this by editing the two files

    /etc/ssh/ssh_config
    /etc/ssh/sshd_config

and adding

    IPQoS 0x00

to each file as the last record.  " THis is quoted and needs the citation

Develop a a python script to do that

### USB stick

    cat /var/log/messages

find sda\*

Make sure to find the right name.

    sudo fdisk /dev/<device-name>
    sudo mkfs -t vfat /dev/<device-name>
    mkdir ~/<mount-point>
    sudo mount /dev/<device-name> ~/<mount-point>

#### DHCP server on 00

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

### grafana

could be helpful to monitor cluster/clusters

* <https://github.com/grafana/grafana>

* <https://github.com/weaveworks/grafanalib>

there are many more, just search. we have not tested them example with
yaml

* <https://github.com/jakubplichta/grafana-dashboard-builder>

light scheme

in /etc/grafana/grafana.ini uncomment line and set

    default_theme = light 
