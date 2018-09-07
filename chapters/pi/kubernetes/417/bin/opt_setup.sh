#!/bin/sh
hostname=$1
ip=$2 # should be of format: 192.168.1.100
sudo apt-get update
sudo apt-get install git
mkdir /~/cloudmesh
echo installing git
git clone https://github.com/cloudmesh-community/hid-sp18-417.git
cd *417/tutorial/dhcp
echo running initial dhcp setup
