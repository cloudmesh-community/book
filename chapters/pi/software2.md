# Pi Software Collection

Please improve the sections.

## Web Programming

### Coder

Targeted at the very beginner to Web programming, we will not use this
here.

* <https://googlecreativelab.github.io/coder/>

provide a section

## Computing

### Python on the Raspberry Pi :hand: fa18-516-03

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

provide a section

### Scipy

Refer to other section in book and describe what is different

provide a section

### Image Processing

Refer to other section in book and describe what is different

provide a section

## System

### DHCP Server

* <http://www.noveldevices.co.uk/rp-dhcp-server>

### hostname

Please see the section [Set the hostname](#s-pi-set-hostname) to set the
hostname on the Pi.

### Gather the MAC addresses

The MAC address is the hardware address of an Ethernet network device. The MAC
address is set by the manufacturer and does not change when you join a different
network like an IP address can. You can get the MAC address for the Ethernet
interface `eth0` or the wireless interface `wlan0` on the Pi by using the
`ifconfig` command and looking for the line that begins with `ether`. The
following command will directly output the MAC address for the interface that
you specify. You can run `ifconfig` with no parameters to see a list of all the
interfaces.

```bash
pi$ ifconfig eth0 | awk '/ether/ {print $2}'
b8:27:eb:9c:b8:6e
pi$ ifconfig wlan0 | awk '/ether/ {print $2}'
b8:27:eb:ce:ef:3b
```

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

Could be helpful to monitor cluster/clusters

* <https://github.com/grafana/grafana>

* <https://github.com/weaveworks/grafanalib>

There are many more, just search. We have not tested them example with
yaml

* <https://github.com/jakubplichta/grafana-dashboard-builder>

Light scheme

in /etc/grafana/grafana.ini uncomment line and set

    default_theme = light 
