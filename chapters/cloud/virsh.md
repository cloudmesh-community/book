# Manage VM guests with virsh

`virsh` is a command line interface tool for managing guests and the
hypervisor.

To initiate a hypervisor session with virsh :

    virsh connect <name>

Where is the machine name of the hypervisor. If you want to initiate a
read-only connection, append the previous command with -readonly.

To display the guest list and their current states with virsh:

    virsh list [ --inactive  |  --all]

The --inactive option lists inactive domains (domains thxsat have been
defined but are not currently active). The --all domain lists all
domains, whether active or not.

A manual page can be found on line at

* <https://linux.die.net/man/1/virsh>

A practical example of using virsh is provided at

* [Redhat Customer Portal: CHAPTER 26. MANAGING GUESTS WITH VIRSH](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/virtualization/chap-virtualization-managing_guests_with_virsh)