# Ansible

## Introduction to Ansible

Ansible is an open-source IT automation DevOps engine allowing you to manage
and configure many compute resources in a scalable, consistent and
reliable way.

Ansible to automates the following tasks:

* **Provisioning:** It sets up the servers that you will use as part
  of your infrastructure.

* **Configuration management:** You can change the configuration of an
application, OS, or device. You can implement security policies and
other configuration tasks.

* **Service management:** You can start and stop services, install
updates

* **Application deployment:** You can conduct application deployments
in an automated fashion that integrate with your DevOps strategies.


### Prerequisite

We assume you 

-   can install Ubuntu 18.04 virtual machine on VirtualBox

-   can install software packages via 'apt-get' tool in Ubuntu
    virtual host

-   already reserved a virtual cluster (with at least 1 virtual
    machine in it) on some cloud. OR you can use VMs installed in
    VirtualBox instead.

-   have SSH credentials and can login to your virtual machines.


### Setting up a playbook

Let us develop a sample from scratch, based on the paradigms that
ansible supports. We are going to use Ansible to install Apache server on
our virtual machines.

First, we install ansible on our machine and make sure we have an up
to date OS:

    $ sudo apt-get update
    $ sudo apt-get install ansible

Next, we prepare a working environment for your Ansible example

    $ mkdir ansible-apache
    $ cd ansible-apache

To use ansible we will need a local configuration. When you execute
Ansible within this folder, this local configuration file is always
going to overwrite a system level Ansible configuration.  It is in
general beneficial to keep custom configurations locally unless you
absolutely believe it should be applied system wide. Create a file
`inventory.cfg` in this folder, add the following:

    [defaults]
    hostfile = hosts.txt

This local configuration file tells that the target machines' names
are given in a file named `hosts.txt`. Next we will specify hosts in
the file.

You should have ssh login accesses to all VMs listed in this file as
part of our prerequisites. Now create and edit file `hosts.txt` with
the following content:

    [apache]
    <server_ip> ansible_ssh_user=<server_username>

The name `apache` in the brackets defines a server group name. We will
use this name to refer to all server items in this group. As we intend
to install and run apache on the server, the name choice seems quite
appropriate. Fill in the IP addresses of the virtual machines you
launched in your VirtualBox and fire up these VMs in you VirtualBox.

To deploy the service, we need to create a playbook. A playbook tells
Ansible what to do. it uses YAML Markup syntax. Create and edit a file
with a proper name e.g. `apache.yml` as follow:

    ---
    - hosts: apache #comment: apache is the group name we just defined
      become: yes #comment: this operation needs privilege access
      tasks:
        - name: install apache2 # text description
          apt: name=apache2 update_cache=yes state=latest

This block defines the target VMs and operations(tasks) need to apply.
We are using the `apt` attribute to indicate all software packages that
need to be installed. Dependent on the distribution of the operating
system it will find the correct module installer without your
knowledge. Thus an ansible playbook could also work for multiple
different OSes. 

Ansible relies on various kinds of modules to fulfil tasks on the remote
servers. These modules are developed for particular tasks and take in
related arguments. For instance, when we use `apt` module, we 
need to tell which package we intend to install. That is why we provide
a value for the `name=` argument. The first `-name` attribute is just
a comment that will be printed when this task is executed. 

### Run the playbook

In the same folder, execute

    ansible-playbook apache.yml --ask-sudo-pass

After a successful run, open a browser and fill in your server IP. you
should see an 'It works!' Apache2 Ubuntu default page. Make sure the
security policy on your cloud opens port 80 to let the HTTP traffic go
through.

Ansible playbook can have more complex and fancy structure and syntaxes.
Go explore! This example is based on:

* <https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04>

We are going to offer an advanced Ansible in next chapter.

## Ansible Roles

Next we install the R package onto our cloud VMs.  R is a useful
statistic programing language commonly used in many scientific and
statistics computing projects, maybe also the one you chose for this
class.  With this example we illustrate the concept of Ansible Roles,
install source code through Github, and make use of variables. These
are key features you will find useful in your project deployments.

We are going to use a top-down fashion in this example. We first start
from a playbook that is already good to go. You can execute this
playbook (do not do it yet, always read the entire section first) to
get R installed in your remote hosts. We then further complicate this
concise playbook by introducing functionalities to do the same tasks
but in different ways. Although these different ways are not necessary
they help you grasp the power of Ansible and ease your life when they
are needed in your real projects.

Let us now create the following playbook with the name `example.yml`:

    ---
    - hosts: R_hosts
      become: yes
      tasks:
        - name: install the R package
          apt: name=r-base update_cache=yes state=latest

The hosts are defined in a file `hosts.txt`, which we configured in
a file that we now call `ansible.cfg`:

    [R_hosts]
    <cloud_server_ip> ansible_ssh_user=<cloud_server_username>

Certainly, this should get the installation job done. But we are going
to extend it via new features called role next

Role is an important concept used often in large Ansible projects.
You divide a series of tasks into different groups. Each group
corresponds to certain role within the project. 

For example, if your project is to deploy a web site, you may need to
install the back end database, the web server that responses HTTP
requests and the web application itself. They are three different roles
and should carry out their own installation and configuration tasks.

Even though we only need to install the R package in this example, we
can still do it by defining a role 'r'. Let us modify our `example.yml` to be:

    ---
    - hosts: R_hosts

      roles:
        - r

Now we create a directory structure in your top project directory as follows

    $ mkdir -p roles/r/tasks
    $ touch roles/r/tasks/main.yml

Next, we edit the  `main.yml` file and include the following content:

    ---
    - name: install the R package
      apt: name=r-base update_cache=yes state=latest
      become: yes

You probably already get the point. We take the 'tasks' section out of
the earlier `example.yml` and re-organize them into roles. Each role
specified in `example.yml` should have its own directory under roles/ and
the tasks need be done by this role is listed in a file 'tasks/main.yml'
as above.

## Using Variables

We demonstrate this feature by installing source code from Github.
Although R can be installed through the OS package manager (apt-get
etc.), the software used in your projects may not. Many research
projects are available by Git instead. Here we are going to show you how
to install packages from their Git repositories. Instead of directly
executing the module 'apt', we pretend Ubuntu does not provide this
package and you have to find it on Git. The source code of R can be
found at <https://github.com/wch/r-source.git>. We are going to clone it
to a remote VM's hard drive, build the package and install the binary
there.

To do so, we need a few new Ansible modules. You may remember from the
last example that Ansible modules assist us to do different tasks
based on the arguments we pass to it. It will come to no surprise that
Ansible has a module 'git' to take care of git-related works, and a
'command' module to run shell commands.  Let us modify
`roles/r/tasks/main.yml` to be:

    ---
    - name: get R package source
      git:
        repo: https://github.com/wch/r-source.git
        dest: /tmp/R

    - name: build and install R
      become: yes
      command: chdir=/tmp/R "{{ item }}"
      with_items:
        - ./configure
        - make
        - make install

The role `r` will now carry out two tasks. One to clone the R source
code into `/tmp/R`, the other uses a series of shell commands to build and
install the packages.

Note that the commands executed by the second task may not be
available on a fresh VM image. But the point of this example is to
show an alternative way to install packages, so we conveniently assume
the conditions are all met.

To achieve this we are using variables in a separate file.

We typed several string constants in our Ansible scripts so far. In
general, it is a good practice to give these values names and use them
by referring to their names. This way, you complex Ansible project can
be less error prone. Create a file in the same directory, and name it
`vars.yml`:

    ---
    repository: https://github.com/wch/r-source.git
    tmp: /tmp/R

Accordingly, we will update our `example.yml`:

    ---
    - hosts: R_hosts
      vars_files:
        - vars.yml
      roles:
        - r

As shown, we specify a `vars_files` telling the script that the file
`vars.yml` is going to supply variable values, whose keys are denoted by
Double curly brackets like in `roles/r/tasks/main.yml`:

    ---
    - name: get R package source
      git:
        repo: "{{ repository }}"
        dest: "{{ tmp }}"

    - name: build and install R
      become: yes
      command: chdir="{{ tmp }}" "{{ item }}"
      with_items:
        - ./configure
        - make
        - make install


Now, just edit the `hosts.txt` file with your target VMs' IP addresses and
execute the playbook.

You should be able to extend the Ansible playbook for your
needs. Configuration tools like Ansible are important components to
master the cloud environment. 

## Ansible Galaxy

Ansible Galaxy is a marketplace, where developers can share Ansible
Roles to complete their system administration tasks. Roles exchanged
in Ansible Galaxy community need to follow common conventions so that
all participants know what to expect. We will illustrate details in
this chapter.

It is good to follow the Ansible Galaxy standard during your development
assignment as much as possible, however, you will submit your
assignments to this class's repository not the global Galaxy community.

### Ansible Galaxy helloworld

Let us start with a simplest case: We will build an Ansible Galaxy
project. This project will install the Emacs software package on your
localhost as the target host. It is a "helloworld" project only meant to
get us familiar with Ansible Galaxy project structures.

First you need to create a directory.  Setup your submission directory
after you clone and rebased with
<https://github.com/cloudmesh/sp17-i524>:

    $ git rebase upstream/master
    $ ./setup galaxy <your HID>

It will create a folder named after your HID inside directory galaxy/.
Your Galaxy related assignments will be completed and submitted there.
Go ahead and create files `README.md`, `playbook.yml`, `inventory` and a
subdirectory `roles/` then. playbook.yml is your project playbook. It
should perform the Emacs installation task by executing the
corresponding role you will develop in the folder 'roles/'. The only
difference is that we will construct the role with the help of
ansible-galaxy this time.

Now, let ansible-galaxy initialize the directory structure for you:

    $ cd roles
    $ ansible-galaxy init <to-be-created-role-name>

The naming convention is to concatenate your name and the role name by a
dot. Here is how it looks like:

![image](/images/ansible-galaxy-init-structure.png)

Let us fill in information to our project. There are several `main.yml`
files in different folders, and we will illustrate their usages.

defaults and vars:

> These folders should hold variables key-value pairs for your
> playbook scripts. We will leave them empty in this example.

files:

> This folder is for files need to be copied to the target
> hosts. Data files or configuration files can be specified if
> needed. We will leave it empty too.

templates:

> Similar missions to files/, templates is allocated for template
> files. Keep empty for a simple Emacs installation.

handlers:

> This is reserved for services running on target hosts. For example,
> to restart a service under certain circumstance.

tasks:

> This file is the actual script for all tasks. You can use the role you
> built previously for Emacs installation here:
>
>     ---
>     - name: install Emacs on Ubuntu 16.04
>       become: yes
>       package: name=emacs state=present

meta:

> Provide necessary metadata for our Ansible Galaxy project for
> shipping:

        ---
        galaxy_info:
          author: <you name>
          description: emacs installation on Ubuntu 16.04
          license:
            - MIT
          min_ansible_version: 2.0
          platforms:
            - name: Ubuntu
              versions:
                - xenial
          galaxy_tags:
            - development

        dependencies: []

Next let us test it out. You have your Ansible Galaxy role ready
now. To test it as a user, go to your HID directory and edit the other
two files `inventory.txt` and `playbook.yml`, which are already generated
for you in directory `tests` by the script:

    $ ansible-playbook -i ./hosts playbook.yml

After running this playbook, you should have Emacs installed on
localhost.

A Complete Ansible Galaxy Project
---------------------------------

We are going to use ansible-galaxy to setup a sample project. This
sample project will:

-   use a cloud cluster with multiple VMs

-   deploy Apache Spark on this cluster

-   install a particular HPC application

-   prepare raw data for this cluster to process

-   run the experiment and collect results

Ansible: Write a Playbooks for MongoDB
======================================

Ansible Playbooks are automated scripts written in YAML data format.
Instead of using manual commands to setup multiple remote machines, you
can utilize Ansible Playbooks to configure your entire systems. YAML
syntax is easy to read and express the data structure of certain Ansible
functions. You simply write some tasks, for example, installing
software, configuring default settings, and starting the software, in a
Ansible Playbook. With a few examples in this tutorial, you will
understand how it works and how to write your own Playbooks.

There are also several examples of using Ansible [Playbooks](http://docs.ansible.com/playbooks.html) from the official site. It covers

:   from basic usage of Ansible Playbooks to advanced usage such as
    applying patches and updates with different roles and groups.

Tutorial: Writing Ansible Playbook
----------------------------------

In this tutorial, we are going to write a basic playbook of Ansible
software. Keep in mind that `Ansible` is a main program and `playbook`
is a template that you would like to use. You may have several playbooks
in your Ansible.

### First playbook for MongoDB Installation

As a first example, we are going to write a playbook which installs
MongoDB server. It includes the following tasks:

-   Import the public key used by the package management system

-   Create a list file for MongoDB

-   Reload local package database

-   Install the MongoDB packages

-   Start MongoDB

This tutorial is based on the manual installation of MongoDB from the
official site:
<http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/*>

We also assume that we install MongoDB on Ubuntu 15.10.

### Enabling Root SSH Access

Some setups of managed nodes may not allow you to log in as root. As
this may be problematic later, let us create a playbook to resolve this.
Create a `enable-root-access.yaml` file with the following contents:

    ---
    - hosts: ansible-test
      remote_user: ubuntu
      tasks:
        - name: Enable root login
          shell: sudo cp ~/.ssh/authorized_keys /root/.ssh/

Explanation:

-   `hosts` specifies the name of a group of machines in the inventory

-   `remote_user` specifies the username on the managed nodes to log in
    as

-   `tasks` is a list of tasks to accomplish having a `name` (a
    description) and modules to execute. In this case we use the `shell`
    module.

We can run this playbook like so:

    $ ansible-playbook -i inventory.txt -c ssh enable-root-access.yaml

    PLAY [ansible-test] *********************************************************** 

    GATHERING FACTS *************************************************************** 
    ok: [10.23.2.105]
    ok: [10.23.2.104]

    TASK: [Enable root login] ***************************************************** 
    changed: [10.23.2.104]
    changed: [10.23.2.105]

    PLAY RECAP ******************************************************************** 
    10.23.2.104                : ok=2    changed=1    unreachable=0    failed=0   
    10.23.2.105                : ok=2    changed=1    unreachable=0    failed=0

### Hosts and Users

First step is choosing hosts to install MongoDB and a user account to
run commands (tasks). We start with the following lines in the example
filename of `mongodb.yaml`:

    ---
    - hosts: ansible-test
      remote_user: root
      become: yes

In a previous tutorial, we setup two machines with `ansible-test` group
name. This tutorial uses that two machines for MongoDB installation.
Also, we use `root` account to complete Ansible tasks.

Indentation is important in YAML format. Do not ignore spaces start

:   with in each line.

### Tasks

A list of tasks contains commands or configurations to be executed on
remote machines in a sequential order. Each task comes with a `name` and
a `module` to run your command or configuration. You provide a
description of your task in `name` section and choose a `module` for
your task. There are several modules that you can use, for example,
`shell` module simply executes a command without considering a return
value. You may use `apt` or `yum` module which is one of the packaging
modules to install software. You can find an entire list of modules
here: <http://docs.ansible.com/list_of_all_modules.html>

### Module apt_key: add repository keys

We need to import the MongoDB public GPG Key. This is going to be a
first task in our playbook.:

    tasks:
      - name: Import the public key used by the package management system
        apt_key: keyserver=hkp://keyserver.ubuntu.com:80 id=7F0CEB10 state=present

### Module apt_repository: add repositories

Next add the MongoDB repository to apt:

    - name: Add MongoDB repository
      apt_repository: repo='deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' state=present

### Module apt: install packages

We use `apt` module to install `mongodb-org` package. `notify` action is
added to start `mongod` after the completion of this task. Use the
`update_cache=yes` option to reload the local package database.:

    - name: install mongodb
      apt: pkg=mongodb-org state=latest update_cache=yes
      notify:
      - start mongodb

### Module service: manage services

We use `handlers` here to start or restart services. It is similar to
`tasks` but will run only once.:

    handlers:
      - name: start mongodb
        service: name=mongod state=started

### The Full Playbook

Our first playbook looks like this:

    ---
    - hosts: ansible-test
      remote_user: root
      become: yes
      tasks:
      - name: Import the public key used by the package management system
        apt_key: keyserver=hkp://keyserver.ubuntu.com:80 id=7F0CEB10 state=present
      - name: Add MongoDB repository
        apt_repository: repo='deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' state=present
      - name: install mongodb
        apt: pkg=mongodb-org state=latest update_cache=yes
        notify:
        - start mongodb
      handlers:
        - name: start mongodb
          service: name=mongod state=started

### Running a Playbook

We use `ansible-playbook` command to run our playbook:

    $ ansible-playbook -i inventory.txt -c ssh mongodb.yaml

    PLAY [ansible-test] *********************************************************** 

    GATHERING FACTS *************************************************************** 
    ok: [10.23.2.104]
    ok: [10.23.2.105]

    TASK: [Import the public key used by the package management system] *********** 
    changed: [10.23.2.104]
    changed: [10.23.2.105]

    TASK: [Add MongoDB repository] ************************************************ 
    changed: [10.23.2.104]
    changed: [10.23.2.105]

    TASK: [install mongodb] ******************************************************* 
    changed: [10.23.2.104]
    changed: [10.23.2.105]

    NOTIFIED: [start mongodb] ***************************************************** 
    ok: [10.23.2.105]
    ok: [10.23.2.104]

    PLAY RECAP ******************************************************************** 
    10.23.2.104                : ok=5    changed=3    unreachable=0    failed=0   
    10.23.2.105                : ok=5    changed=3    unreachable=0    failed=0

If you rerun the playbook, you should see that nothing changed:

    $ ansible-playbook -i inventory.txt -c ssh mongodb.yaml 

    PLAY [ansible-test] *********************************************************** 

    GATHERING FACTS *************************************************************** 
    ok: [10.23.2.105]
    ok: [10.23.2.104]

    TASK: [Import the public key used by the package management system] *********** 
    ok: [10.23.2.104]
    ok: [10.23.2.105]

    TASK: [Add MongoDB repository] ************************************************ 
    ok: [10.23.2.104]
    ok: [10.23.2.105]

    TASK: [install mongodb] ******************************************************* 
    ok: [10.23.2.105]
    ok: [10.23.2.104]

    PLAY RECAP ******************************************************************** 
    10.23.2.104                : ok=4    changed=0    unreachable=0    failed=0   
    10.23.2.105                : ok=4    changed=0    unreachable=0    failed=0

### Sanity Check: Test MongoDB

Let's try to run 'mongo' to enter mongodb shell.:

    $ ssh ubuntu@$IP
    $ mongo
    MongoDB shell version: 2.6.9
    connecting to: test
    Welcome to the MongoDB shell.
    For interactive help, type "help".
    For more comprehensive documentation, see
            http://docs.mongodb.org/
    Questions? Try the support group
            http://groups.google.com/group/mongodb-user
    > 

### Terms

-   Module: Ansible library to run or manage services, packages, files
    or commands.

-   Handler: A task for notifier.

-   Task: Ansible job to run a command, check files, or update
    configurations.

-   Playbook: a list of tasks for Ansible nodes. YAML format used.

-   YAML: Human readable generic data serialization.

### Reference

The main tutorial from Ansible is here:
<http://docs.ansible.com/playbooks_intro.html>

You can also find an index of the ansible modules here:
<http://docs.ansible.com/modules_by_category.html>

Ansible Assignment
==================

We have shown a couple of examples of using Ansible tools. Before you
apply it in you final project, we will practice it in this assignment.

Requirements
------------

-   use the `galaxy` directory in the class assignment repository

-   set up the project structure similar to Ansible Galaxy example

-   install MongoDB from the package manager (apt in this class)

-   configure your MongoDB installation to start the service
    automatically

-   use default port and let it serve local client connections only
