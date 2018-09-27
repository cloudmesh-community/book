# Manage VM guests with virsh :o: :?:

`virsh` is a command line interface tool for managing guests and the
hypervisor.

To initiate a hypervisor session with virsh :

    virsh connect <name>

Where is the machine name of the hypervisor. If you want to initiate a
read-only connection, append the above command with -readonly.

To display the guest list and their current states with virsh:

    virsh list [ --inactive  |  --all]

The --inactive option lists inactive domains (domains thxsat have been
defined but are not currently active). The --all domain lists all
domains, whether active or not.
