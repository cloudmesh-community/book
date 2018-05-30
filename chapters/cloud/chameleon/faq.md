Frequently Asked Questions
==========================

Appliances
----------

### What is an appliance?

An appliance is an application packaged together with the environment
that this application requires. For example, an appliance can consists
of the operating system, libraries and tools used by the application,
configuration features such as environment variable settings, and the
installation of the application itself. Examples of appliances might
include a KVM virtual machine image, a Docker image, or a bare metal
image. Chameleon appliance refers to bare metal images that can be
deployed on the Chameleon testbed. Since an appliance captures the
experimental environment exactly, it is a key element of
reproducibility; publishing an appliance used to obtain experimental
results will go a long way to allowing others to reproduce and build on
your research easily.

To deploy distributed applications on several Chameleon instances,
complex appliances combine an image and a template describing how the
cluster should be configured and contextualized. You can read more about
them in the [Complex Appliances
documentation](https://www.chameleoncloud.org/docs/complex-appliances/).

### What is the Appliance Catalog?

[The Chameleon Appliance
Catalog](https://www.chameleoncloud.org/appliances/) is a repository
that allows users to discover, publish, and share appliances. The
appliance catalog contains useful images of both bare metal and virtual
machine appliances supported by the Chameleon team as well appliances
contributed by users.

### How do I publish an appliance in the Appliance Catalog?

The new Appliance Catalog allows you to easily publish and share your
own appliances so that others can discover them and use them either to
reproduce the research of others or as a basis for their own research.
Before creating your own appliance it is advisable to review other
appliances on the [Chameleon Appliance
Catalog](https://www.chameleoncloud.org/appliances/) in order to get an
idea of the categories you will want to contribute and what others have
done.

Once you are ready to proceed, an appliance can be contributed to
Chameleon in the following steps:

1.  Create the appliance itself. You may want to test it as well as give
    some thought to what support you are willing to provide for the
    appliance (e.g., if your group developed and supports a software
    package, the appliance may be just a new way of packaging the
    software and making it available, in which case your standard
    support channels may be appropriate for the appliance as well).

2.  Upload the appliance to the Chameleon Image Repository (Glance) and
    make the image public. In order to enter the appliance into the
    Catalog you will be asked to provide the Glance ID for the image.
    These IDs are per-cloud, so that there are three options right now:
    bare metal/CHI at University of Chicago, bare metal/CHI at TACC, and
    OpenStack/KVM at TACC. You will need to provide at least one
    appliance, but may want to provide all three.

3.  Go to the [Appliance Catalog Create Appliance web
    form](https://www.chameleoncloud.org/appliances/create/), fill out,
    and submit the form. Be prepared to provide the following
    information: a descriptive name (this sometimes requires some
    thought!), author and support contact, version, and an informative
    description. The description is a very important part of the
    appliance record; others will use it to evaluate if the appliance
    contains tools they need for their research so it makes sense to
    prepare it carefully. To make your description effective you may
    want to think of the following questions: what does the appliance
    contain? what are the specific packages and their versions? what is
    it useful for? where can it be deployed and/or what
    restrictions/limitations does it have? how should users connect to
    it / what accounts are enabled?

If you are adding a complex appliance, skip the image ID fields and
enter your template instead in the dedicated text box.

As always, if you encounter any problems or want to share with us
additional improvements we should do to the process, please don't
hesitate to [submit a ticket](https://www.chameleoncloud.org/help/).

### How can I manage an appliance on Appliance Catalog?

If you are the owner of the appliance, you can edit the appliance data,
such as the description or the support information. Browse to the
appliance that you want to edit and view its Details page. At the top
right of the page is an Edit button. You will be presented with the same
web form as when creating the appliance, pre-filled with the appliances
current information. Make changes as necessary and click Save at the
bottom of the page.

And finally, you can delete appliances you had made available. Browse to
the appliance that you want to delete and click Edit on the Appliance
Details page. At the bottom of the page is a Delete button. You will be
asked to confirm once more that you do want to delete this appliance.
After confirming, the appliance will be removed and no longer listed on
the Appliance Catalog.

### Why are there different image IDs for the same appliance?

The three clouds forming the Chameleon testbed are fully separated, each
having its own Glance image repository. The same appliance image
uploaded to the three clouds will produce three different image IDs.

In addition, it is sometimes needed to customize an appliance image for
each site, resulting in slightly different image files.

### Can I use another operating system on bare-metal?

The recommended appliance for Chameleon is CentOS 7 (supported by
Chameleon staff), or appliances built on top of it.\
These appliances provide Chameleon-specific customizations, such as
login using the cc account, the cc-checks utility to verify hardware
against our resource registry, gathering of metrics, etc.

Since 2016, we also provide and support Ubuntu 14.04 and 16.04
appliances with the same functionality.

Bare Metal Troubleshooting
--------------------------

### Why are my Bare Metal instances failing to launch?

The Chameleon Bare Metal clouds require users to reserve resources
before allowing them to launch instances. Please follow the
[documentation](https://www.chameleoncloud.org/docs/bare-metal/) and
make sure that:

1.  You have created a lease and it has started (the associated
    reservation is shown as **Active**)

2.  You have selected your reservation in the **Launch Instance** panel

If you still cannot start instances, please [open a ticket with our help
desk](https://www.chameleoncloud.org/user/help/).

OpenStack KVM Troubleshooting
-----------------------------

### Why are my OpenStack KVM instances failing to launch?

If you get an error stating that **No valid host was found**, it might
be caused by a lack of resources in the cloud. The Chameleon staff
continuously monitors the utilization of the testbed, but there might be
times when no more resources are available. If the error persists,
please [open a ticket with our help
desk](https://www.chameleoncloud.org/user/help/).

### Why can't I ping or SSH to my instance?

While the possibility that the system is being taking over by nanites
should not be discounted too easily, it is always prudent to first check
for the following issues:

-   Do you have a floating IP associated with your instance? By default,
    instances do not have publicly-accessible IP addresses assigned. See
    the **Managing Virtual Machine Instances** section in the [User
    Guide](https://www.chameleoncloud.org/docs/user-guides/openstack-kvm-user-guide/).

-   Does your security group allow incoming ICMP (e.g. ping) traffic? By
    default, firewall rules do not allow ping to your instances. If you
    wish to enable it, see the **Firewall (Access Security)** section in
    the [User
    Guide](https://www.chameleoncloud.org/docs/user-guides/openstack-kvm-user-guide/).

-   Does your security group allow incoming SSH (TCP port 22) traffic?
    By default, firewall rules do not allow SSH to your instances. If
    you wish to enable it, see the **Firewall (Access Security)**
    section in the [User
    Guide](https://www.chameleoncloud.org/docs/user-guides/openstack-kvm-user-guide/).

If none of these solve your problem, please [open a ticket with our help
desk](https://www.chameleoncloud.org/user/help/), and send us the
results of the above (and any evidence of nanites you find as well).
