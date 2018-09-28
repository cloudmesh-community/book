# Packer :hand: :o:

Packer is an open source tool for creating identical machine images
for multiple platforms from a single source configuration. Packer runs
on every major operating system, and creates machine images for
multiple platforms in parallel form configuration specufications.

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

In the Section [vagrant](/chapters/cloud/vagrant.md#usage) we use
vagrant to start up an Ubuntu 18.04 virtual machine. Once the VM was
up and running, vagrant allowed the user to log in and setup the VM
according to the user's requirements. In that example, the user ran
commands to install and upgrade software dependencies:

1. upgrade from Python 3.6.5 to Python 3.7
1. installing python3-pip and idle-python
1. alias `python` to `python3`

Let us assume that the VM is now in a desirable state for the purpose
of doing development on a large number of virtual machines and you
want to distribute it to the rest of your team or community so that
all are using the same environment. You could simply send your team
members a copy of your Ubuntu 18.04 VirtualBox VM assuming they will
be developing on VMs using VirtualBox. However, let us assume one
community member wants to develop on Google Cloud Platform, another on
AWS and another on OpenStack. In this case, they will each need to
figure out how to import a VirtualBox VM into the respective cloud
vendor they're utilizing. Packer can help this situation by codifying
the state of the development environment with a single configuration
file which can then be used to create images in different cloud
environments.

Assuming packer has been installed, let's create a packer JSON file
that will build an Ubuntu 18.04 image and provision it as we did
manually using Vagrant. In this example, we will create the image in
Google Compute Platform.

First download your Google Cloud credentials according to the
documentation at

* <https://www.packer.io/docs/builders/googlecompute.html#running-without-a-compute-engine-service-account>

Save the credential file as `accounts.json`. Also, determine the
project ID you will use in your Google Cloud Platform account. In this
example, we will use `my_project_id` for our project ID.

Next save the following JSON to a file named `e516.json`:

```json
{
  "variables": {
    "google_project_id": null
  },
  "builders": [
    {
      "type":         "googlecompute",
      "account_file": "account.json",
      "project_id":   "{{ user `google_project_id` }}",
      "image_name":   "ubuntu-1804-dev-e516",
      "source_image": "ubuntu-1804-bionic-v20180911",
      "ssh_username": "packer",
      "zone":         "us-central1-a"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "expect_disconnect": true,
      "inline": [
        "sudo apt-get update -y",
        "sudo apt-get install -y python3.7 python3-pip idle-python3.7",
        "echo \"alias python='python3'\" > .bash_aliases"
      ]
    }
  ]
}
```

The packer file format specifies 3 sections, `variables`, `builders`
and `provisioners`. The `variables` section allows you to declare
variables that are to be used in the rest of the document. By
declaring a variable in this section, for example `google_project_id`,
it allows the user to pass in the value of that variable via the
packer command line.

The `builders` section allows you to declare the builders for any
cloud vendor supported by packer. The list of supported vendors can be
found here:

* <https://www.packer.io/docs/builders/index.html>

In our example, we define the builder for Google Cloud Platform which
requires our credential file (account.json), our project ID, base
image name, ssh username and zone.

Finally, the `provisioners` section allows the user to customize the
base image defined in the `builders` section. In our example, we
simply use the `shell` provisioner which allows us to type in shell
commands to provision the image as we want it. Here we install
python3.7, python3-pip and idle-python3.7.  We also write out an
aliases file so that upon login, the user can access python3.7 using
the python alias.

To build the image, we now run packer:

```console
$ packer build -var 'google_project_id=my_project_id' e516.json
```

You will see output that shows the progress of packer as it starts up
and provisions the instance. Upon success, packer will create an image
from the instance and clean up after itself:

```console
$ googlecompute output will be in this color.

==> googlecompute: Checking image does not exist...
==> googlecompute: Creating temporary SSH key for instance...
==> googlecompute: Using image: ubuntu-1804-bionic-v20180911
==> googlecompute: Creating instance...
    googlecompute: Loading zone: us-central1-a
    googlecompute: Loading machine type: n1-standard-1
    googlecompute: Requesting instance creation...
    googlecompute: Waiting for creation operation to complete...
    googlecompute: Instance has been created!
==> googlecompute: Waiting for the instance to become running...
    googlecompute: IP: 104.154.21.240
==> googlecompute: Waiting for SSH to become available...
==> googlecompute: Connected to SSH!
==> googlecompute: Provisioning with shell script: /var/folders/rm/g1h4bhf54x750jzjyryckmnc000lxd/T/packer-shell210916201
    googlecompute: Get:1 http://archive.canonical.com/ubuntu bionic InRelease [10.2 kB]
...
    googlecompute: Setting up idle-python3.7 (3.7.0-1~18.04) ...
    googlecompute: Processing triggers for libc-bin (2.27-3ubuntu1) ...
    googlecompute: Processing triggers for ureadahead (0.100.0-20) ...
    googlecompute: Processing triggers for systemd (237-3ubuntu10.3) ...
==> googlecompute: Deleting instance...
    googlecompute: Instance has been deleted!
==> googlecompute: Creating image...
==> googlecompute: Deleting disk...
    googlecompute: Disk has been deleted!
Build 'googlecompute' finished.

==> Builds finished. The artifacts of successful builds are:
--> googlecompute: A disk image was created: ubuntu-1804-dev-e516
```

You can now click on the list of images in the Google Compute Platform
console to see your new image. The new image is ready to use for
development.

Next, let's add a builder for an AWS AMI. Before we do that, setup
your AWS credentials using the AWS CLI according to the documentation
here:

* <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>

Ensure your `default` profile is saved under `~/.aws/credentials`.

Update the `e516.json` so that the contents is as follows:

```
{
  "variables": {
    "google_project_id": null,
    "image_name":   "ubuntu-1804-dev-e516",
    "ssh_username": "packer"
  },
  "builders": [
    {
      "type":         "googlecompute",
      "account_file": "account.json",
      "ssh_username": "{{ user `ssh_username` }}",
      "project_id":   "{{ user `google_project_id` }}",
      "image_name":   "{{ user `image_name` }}",
      "source_image": "ubuntu-1804-bionic-v20180911",
      "zone":         "us-central1-a"
    },
    {
      "type":         "amazon-ebs",
      "ssh_username": "{{ user `ssh_username` }}",
      "profile":      "default",
      "ami_name":   "{{ user `image_name` }}",
      "source_ami":   "ami-0bbe6b35405ecebdb",
      "instance_type":"t2.micro",
      "region":       "us-west-2"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "expect_disconnect": true,
      "inline": [
        "sudo apt-get update -y",
        "sudo apt-get install -y python3.7 python3-pip idle-python3.7",
        "echo \"alias python='python3'\" > .bash_aliases"
      ]
    }
  ]
}
```

Note that we've added the AWS builder in the `builders` section and that
we've refactored the `ssh_username` and `image_name` to the `variables`
section since those variable hold values that can be reused in both the
Google Compute and AWS builders.

Let's rerun packer:

```
packer build -var 'google_project_id=my_project_id' e516.json
```

You will see output that states the image already exists in your
Google Compute account and so packer smartly skips building that
image. The output also shows the progress of packer as it starts up
and provisions the instance in AWS. Upon success, packer will create
an AMI from the instance and clean up after itself:

```
amazon-ebs output will be in this color.
googlecompute output will be in this color.

==> googlecompute: Checking image does not exist...
==> amazon-ebs: Prevalidating AMI Name: ubuntu-1804-dev-e516
==> googlecompute: Image ubuntu-1804-dev-e516 already exists.
==> googlecompute: Use the force flag to delete it prior to building.
Build 'googlecompute' errored: Image ubuntu-1804-dev-e516 already exists.
Use the force flag to delete it prior to building.
    amazon-ebs: Found Image ID: ami-0bbe6b35405ecebdb
==> amazon-ebs: Creating temporary keypair:
    packer_5bad9d99-f631-1778-1e83-afd19ad0d5cc
==> amazon-ebs: Creating temporary security group for this instance:
    packer_5bad9d9b-38c5-252d-0368-74aa75bfb286
==> amazon-ebs: Authorizing access to port 22 from 0.0.0.0/0
    in the temporary security group...
==> amazon-ebs: Launching a source AWS instance...
==> amazon-ebs: Adding tags to source instance
    amazon-ebs: Adding tag: "Name": "Packer Builder"
    amazon-ebs: Instance ID: i-0d0383f9f84b54051
```

You can now click on the list of images in the AWS EC2 console to see 
your new AMI. The new AMI is ready to use for development.
