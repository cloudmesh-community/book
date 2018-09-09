# Automated Headless Configuration of a Pi Cluster :o:

Our goal is perform the following configuration automatically:

* [Enable ssh](https://www.raspberrypi.org/documentation/remote-access/ssh/) 
permanently (initial ssh access will be enabled when we burn the SD cards)
* Change the password
* Set up one of the Pis as a DHCP server

These actions are all done with two scripts. The first script,
`configure-pi.sh`, runs on the computer used to set up the Pis. The
second, `setup-pi.sh`, enables ssh, changes the password for the pi
user, and configures the master node as a DHCP server.  Determination
of whether the node is the master or a worker is done with the `-m`
flag.

## Prerequisites

* [Assemble a Pi Cluster](assemble-pi-cluster.md)
* [Burn SD cards with names changed and ssh enabled](modify-pi-image.md)
* Install `expect` on computer running `configure-pi.sh`. On a Mac, this is done with 
`brew install expect`. On Unix, use `apt-get install expect` or `yum install expect`.
More information on `expect` can be found [here](https://likegeeks.com/expect-command/).

## Setting up DHCP

TODO: Find out if cluster should be set up with or without internet
enabled. Tutorial for getting Pi on IU Secure
[here](https://cs.iupui.edu/~xiaozhon/course_tutorials/Connecting_to_IU_Secure_RPi_Tutorial.pdf).

TODO: New version of isc-dhcp-server. Find out if INTERFACES in
/etc/default/isc-dhcp-server should be V4, V6 or both.

TODO: Switch is eth8 when internet sharing is off, names show up, and
IP addresses are on different subnet. When internet sharing is on,
names do not show up. How should DHCP and network be setup? What is the
use case? Below is output of `arp -a` with internet sharing.  I turned
it on so that installations via apt-get would work:

```
(2.7.13) BKS-MBP:project-code bsobolik$ arp -a
hello (192.168.1.1) at 58:ef:68:a9:51:4e on en0 ifscope [ethernet]
bertoltksiphone.hsd1.in.comcast.net (192.168.1.126) at e4:9a:79:7f:19:55 on en0 ifscope [ethernet]
? (192.168.1.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
? (192.168.2.7) at b8:27:eb:0:c3:55 on bridge100 ifscope [bridge]
? (192.168.2.8) at b8:27:eb:d1:21:33 on bridge100 ifscope [bridge]
? (192.168.2.255) at ff:ff:ff:ff:ff:ff on bridge100 ifscope [bridge]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
```

When internet sharing is off I get: 

```
(2.7.13) BKS-MBP:~ bsobolik$ arp -a
raspberrypi.local (169.254.177.219) at b8:27:eb:0:c3:55 on en8 [ethernet]
? (169.254.255.255) at (incomplete) on en0 [ethernet]
hello (192.168.1.1) at 58:ef:68:a9:51:4e on en0 ifscope [ethernet]
? (192.168.1.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
```



