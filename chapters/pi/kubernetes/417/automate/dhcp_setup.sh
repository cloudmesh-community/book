#!/bin/sh

hostname=$1
ip=$2 # should be of format: 192.168.1.100
router=$3 # should be of format: 192.168.1.1
dns=$4 # should be of format: 192.168.1.1

# Change the hostname
touch hostname
sudo cat <<end>> hostname
$hostname
end
sudo cp hostname /etc/hostname

head -n -1 /etc/hosts > temp ; sudo mv temp /etc/hosts
sudo cat <<end11>> /etc/hosts
127.0.0.1     $hostname
end11

# Set the static ip

sudo cat <<EOT >> /etc/dhcpcd.conf
interface eth0
static ip_address=$ip/24
static routers=$router
static domain_name_servers=$dns

interface wlan0
static ip_address=$ip/24
static routers=$router
static domain_name_servers=$dns
EOT
reboot

