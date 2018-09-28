# Packer :hand: :o:

Packer is an open source tool for creating identical machine images 
for multiple platforms from a single source configuration. Packer is 
lightweight, runs on every major operating system, and is highly 
performant, creating machine images for multiple platforms in parallel.

Some key concepts are located at

* <https://www.packer.io/intro/index.html>

Detailed documentation is located at

* <https://www.packer.io/docs/index.html>

Use cases for packer is located at

* <https://www.packer.io/intro/use-cases.html>

## Installation
Installation instructions for all platforms is located at

* <https://www.packer.io/intro/getting-started/install.html>

## Usage

In the previous section, [vagrant](/chapters/cloud/vagrant.md#usage) was used to start up an
Ubuntu 18.04 virtual machine. Once the VM was up and running, vagrant
allowed the user to log in and setup the VM according to the user's
requirements. In that example, the user ran commands to install 
and upgrade software dependencies:

1. upgrade from Python 3.6.5 to Python 3.7
1. installing python3-pip and idle-python
1. alias `python` to `python3`

Let's assume that the VM is now in a desirable state for the purpose
of doing development on your class project and you want to distribute
it to the rest of your team so that you are all using the same 
environment for development. You could simply send your team members
a copy of your Ubuntu 18.04 VirtualBox VM assuming they will be developing
on VMs using VirtualBox. However one team member wants to develop on AWS,
another on Azure, and another on OpenStack. In this case, they will each
need to figure out how to import a VirtualBox VM into the respective cloud
vendor they're utilizing.

@pymonger TODO: fill out example usage
