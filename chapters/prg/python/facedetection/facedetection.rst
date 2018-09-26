
NIST Pedestrian and Face Detection
==================================

Pedestrian and Face Detection uses OpenCV to identify people standing in
a picture or a video and NIST use case in this document is built with
Apache Spark and Mesos clusters on multiple compute nodes.

The example in this tutorial deploys software packages on OpenStack
using Ansible with its roles.

+--------------+-----------------------+
| Original     | Pedestrian Detected   |
+==============+=======================+
| |alt baby|   | |alt baby-detected|   |
+--------------+-----------------------+

.. |alt baby| image:: https://raw.githubusercontent.com/cloudmesh/classes/master/docs/source/notebooks/files/image03.png
.. |alt baby-detected| image:: https://raw.githubusercontent.com/cloudmesh/classes/master/docs/source/notebooks/files/image05.png

+----------------+-------------------------------------+
| Original       | Pedestrian and Face/eyes Detected   |
+================+=====================================+
| |alt person|   | |alt person-detected|               |
+----------------+-------------------------------------+

.. |alt person| image:: https://raw.githubusercontent.com/cloudmesh/classes/master/docs/source/notebooks/files/image06.png
.. |alt person-detected| image:: https://raw.githubusercontent.com/cloudmesh/classes/master/docs/source/notebooks/files/image04.png

Introduction
------------

Human (pedestrian) detection and face detection have been studied during
the last several years and models for them have improved along with
Histograms of Oriented Gradients (HOG) for Human Detection [1]. OpenCV
is a Computer Vision library including the SVM classifier and the HOG
object detector for pedestrian detection and INRIA Person Dataset [2] is
one of popular samples for both training and testing purposes. In this
document, we deploy Apache Spark on Mesos clusters to train and apply
detection models from OpenCV using Python API.

INRIA Person Dataset
~~~~~~~~~~~~~~~~~~~~

This dataset contains positive and negative images for training and test
purposes with annotation files for upright persons in each image. 288
positive test images, 453 negative test images, 614 positive training
images and 1218 negative training images are included along with
normalized 64x128 pixel formats. 970MB dataset is available to download
[3].

HOG with SVM model
~~~~~~~~~~~~~~~~~~

Histogram of Oriented Gradient (HOG) and Support Vector Machine (SVM)
are used as object detectors and classifiers and built-in python
libraries from OpenCV provide these models for human detection.

Ansible Automation Tool
~~~~~~~~~~~~~~~~~~~~~~~

Ansible is a python tool to install/configure/manage software on
multiple machines with JSON files where system descriptions are defined.
There are reasons why we use Ansible:

-  Expandable: Leverages Python (default) but modules can be written in
   any language
-  Agentless: no setup required on managed node
-  Security: Allows deployment from user space; uses ssh for
   authentication
-  Flexibility: only requires ssh access to privileged user
-  Transparency: YAML Based script files express the steps of installing
   and configuring software
-  Modularity: Single Ansible Role (should) contain all required
   commands and variables to deploy software package independently
-  Sharing and portability: roles are available from source (github,
   bitbucket, gitlab, etc) or the Ansible Galaxy portal

We use Ansible roles to install software packages for Humand and Face
Detection which requires to run OpenCV Python libraries on Apache Mesos
with a cluster configuration. Dataset is also downloaded from the web
using an ansible role.

Deployment by Ansible
---------------------

Ansible is to deploy applications and build clusters for
batch-processing large datasets towards target machines e.g. VM
instances on OpenStack and we use ansible roles with *include* directive
to organize layers of big data software stacks (BDSS). Ansible provides
abstractions by Playbook Roles and reusability by Include statements. We
define X application in X Ansible Role, for example, and use include
statements to combine with other applications e.g. Y or Z. The layers
exist in sub directories (see below) to add modularity to your Ansible
deployment. For example, there are five roles used in this example that
are Apache Mesos in a scheduler layer, Apache Spark in a processing
layer, a OpenCV library in an application layer, INRIA Person Dataset in
a dataset layer and a python script for human and face detection in an
analytics layer. If you have an additional software package to add, you
can simply add a new role in a main ansible playbook with *include*
directive. With this, your Ansible playbook maintains simple but
flexible to add more roles without having a large single file which is
getting difficult to read when it deploys more applications on multiple
layers. The main Ansible playbook runs Ansible roles in order which look
like:

::

    ---
    include: sched/00-mesos.yml
    include: proc/01-spark.yml
    include: apps/02-opencv.yml
    include: data/03-inria-dataset.yml
    Include: anlys/04-human-face-detection.yml

Directory names e.g. sched, proc, data, or anlys indicate BDSS layers
like: - sched: scheduler layer - proc: data processing layer - apps:
application layer - data: dataset layer - anlys: analytics layer and two
digits in the filename indicate an order of roles to be run.

Cloudmesh for Provisioning
--------------------------

It is assumed that virtual machines are created by cloudmesh, the cloud
management software. For example on OpenStack,

``cm cluster create -N=6``

command starts a set of virtual machine instances. The number of
machines and groups for clusters e.g. namenodes and datanodes are
defined in the Ansible inventory file, a list of target machines with
groups, which will be generated once machines are ready to use by
cloudmesh. Ansible roles install software and dataset on virtual
clusters after that stage.

Roles Explained for Installation
--------------------------------

Mesos role is installed first as a scheduler layer for masters and
slaves where mesos-master runs on the masters group and mesos-slave runs
on the slaves group. Apache Zookeeper is included in the mesos role
therefore mesos slaves find an elected mesos leader for the
coordination. Spark, as a data processing layer, provides two options
for distributed job processing, batch job processing via a cluster mode
and real-time processing via a client mode. The Mesos dispatcher runs on
a masters group to accept a batch job submission and Spark interactive
shell, which is the client mode, provides real-time processing on any
node in the cluster. Either way, Spark is installed later to detect a
master (leader) host for a job submission. Other roles for OpenCV, INRIA
Person Dataset and Human and Face Detection Python applications are
followed by.

The following software are expected in the stacks according to the
`github <https://github.com/futuresystems/pedestrian-and-face-detection>`__:

-  mesos cluster (master, worker)
-  spark (with dispatcher for mesos cluster mode)
-  openCV
-  zookeeper
-  INRIA Person Dataset
-  Detection Analytics in Python

-  [1] Dalal, Navneet, and Bill Triggs. "Histograms of oriented
   gradients for human detection." 2005 IEEE Computer Society Conference
   on Computer Vision and Pattern Recognition (CVPR'05). Vol. 1. IEEE,
   2005. [pdf]
-  [2] http://pascal.inrialpes.fr/data/human/
-  [3] ftp://ftp.inrialpes.fr/pub/lear/douze/data/INRIAPerson.tar
-  [4] https://docs.python.org/2/library/configparser.html

Server groups for Masters/Slaves by Ansible inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We may separate compute nodes in two groups: masters and workers
therefore Mesos masters and zookeeper quorums manage job requests and
leaders and workers run actual tasks. Ansible needs group definitions in
their inventory therefore software installation associated with a proper
part can be completed.

Example of Ansible Inventory file (inventory.txt)

::

    [masters]
    10.0.5.67
    10.0.5.68
    10.0.5.69
    [slaves]
    10.0.5.70
    10.0.5.71
    10.0.5.72

Instructions for Deployment
---------------------------

The following commands complete NIST Pedestrian and Face Detection
deployment on OpenStack.

Cloning Pedestrian Detection Repository from Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Roles are included as submodules which require ``--recursive`` option to
checkout them all.

.. code:: ipython2

    !git clone --recursive https://github.com/futuresystems/pedestrian-and-face-detection.git


.. parsed-literal::

    Cloning into 'pedestrian-and-face-detection'...
    remote: Counting objects: 81, done.[K
    remote: Total 81 (delta 0), reused 0 (delta 0), pack-reused 81[K
    Unpacking objects: 100% (81/81), done.
    Checking connectivity... done.
    Submodule 'roles/ansible-role-analytics' (https://github.com/futuresystems/ansible-role-analytics.git) registered for path 'roles/ansible-role-analytics'
    Submodule 'roles/ansible-role-dataset' (https://github.com/futuresystems/ansible-role-dataset.git) registered for path 'roles/ansible-role-dataset'
    Submodule 'roles/ansible-role-mesos-by-mesosphere' (https://github.com/lee212/ansible-role-mesos-by-mesosphere.git) registered for path 'roles/ansible-role-mesos-by-mesosphere'
    Submodule 'roles/ansible-role-opencv' (https://github.com/futuresystems/ansible-role-opencv) registered for path 'roles/ansible-role-opencv'
    Submodule 'roles/ansible-role-spark-for-mesos' (https://github.com/lee212/ansible-role-spark-for-mesos.git) registered for path 'roles/ansible-role-spark-for-mesos'
    Cloning into 'roles/ansible-role-analytics'...
    remote: Counting objects: 29, done.[K
    remote: Total 29 (delta 0), reused 0 (delta 0), pack-reused 29[K
    Unpacking objects: 100% (29/29), done.
    Checking connectivity... done.
    Submodule path 'roles/ansible-role-analytics': checked out '6fa1318af5b8d49e833b9042818c7ad4e52cbdc9'
    Cloning into 'roles/ansible-role-dataset'...
    remote: Counting objects: 21, done.[K
    remote: Total 21 (delta 0), reused 0 (delta 0), pack-reused 21[K
    Unpacking objects: 100% (21/21), done.
    Checking connectivity... done.
    Submodule path 'roles/ansible-role-dataset': checked out 'e6517790f8d30f7d75125a01772e8e57a547bb1f'
    Cloning into 'roles/ansible-role-mesos-by-mesosphere'...
    remote: Counting objects: 75, done.[K
    remote: Total 75 (delta 0), reused 0 (delta 0), pack-reused 75[K
    Unpacking objects: 100% (75/75), done.
    Checking connectivity... done.
    Submodule path 'roles/ansible-role-mesos-by-mesosphere': checked out '402ed32ca03b5dc6610136bc00c0d30ed5d2215b'
    Cloning into 'roles/ansible-role-opencv'...
    remote: Counting objects: 36, done.[K
    remote: Total 36 (delta 0), reused 0 (delta 0), pack-reused 36[K
    Unpacking objects: 100% (36/36), done.
    Checking connectivity... done.
    Submodule path 'roles/ansible-role-opencv': checked out '6b73c23334d74c2fcd40055ec6a8ae05d39fd65f'
    Cloning into 'roles/ansible-role-spark-for-mesos'...
    remote: Counting objects: 40, done.[K
    remote: Total 40 (delta 0), reused 0 (delta 0), pack-reused 40[K
    Unpacking objects: 100% (40/40), done.
    Checking connectivity... done.
    Submodule path 'roles/ansible-role-spark-for-mesos': checked out '048d083a5fe7c4ed85d811e57a9301bc0a4a433f'


Change the following variable with actual ip addresses:

.. code:: ipython2

    sample_inventory="""[masters]
    10.0.5.67
    10.0.5.68
    10.0.5.69
    [slaves]
    10.0.5.70
    10.0.5.71
    10.0.5.72"""

Create a ``inventory.txt`` file with the variable in your local
directory.

.. code:: ipython2

    !printf "$sample_inventory" > inventory.txt
    !cat inventory.txt


.. parsed-literal::

    [masters]
    10.0.5.67
    10.0.5.68
    10.0.5.69
    [slaves]
    10.0.5.70
    10.0.5.71
    10.0.5.72

Add ``ansible.cfg`` file with options for ssh host key checking and
login name.

.. code:: ipython2

    ansible_config="""[defaults]
    host_key_checking=false
    remote_user=ubuntu"""
    !printf "$ansible_config" > ansible.cfg
    !cat ansible.cfg


.. parsed-literal::

    [defaults]
    host_key_checking=false
    remote_user=ubuntu

Check accessibility by ansible ping like:

.. code:: ipython2

    !ansible -m ping -i inventory.txt all


.. parsed-literal::

    [0;32m10.0.5.70 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m
    [0;32m10.0.5.71 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m
    [0;32m10.0.5.68 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m
    [0;32m10.0.5.69 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m
    [0;32m10.0.5.67 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m
    [0;32m10.0.5.72 | SUCCESS => {
        "changed": false, 
        "ping": "pong"
    }[0m


Make sure that you have a correct ssh key in your account otherwise you
may encounter 'FAILURE' in the ping test above.

Ansible Playbook
~~~~~~~~~~~~~~~~

We use a main ansible playbook to deploy software packages for NIST
Pedestrian and Face detection which includes: - mesos - spark -
zookeeper - opencv - INRIA Person dataset - Python script for the
detection

.. code:: ipython2

    !cd pedestrian-and-face-detection/ && ansible-playbook -i ../inventory.txt site.yml


.. parsed-literal::

    
    PLAY [mesos base] **************************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : include_vars] *************************
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add apt-key] **************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Remove mesosphere repo] ***************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install mesos] ************************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install zookeeperd if missing (on trusty)] ***
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : remove myid] **************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update from ansibleshipyad] ******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : create dataDir if not exist] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update in dataDir] ***************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-slave override] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-master override] ****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable zk] ***************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Downloading and enable the EPEL repository definitions.] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install mesosphere] *******************
    [0;36mskipping: [10.0.5.67] => (item=[]) [0m
    [0;36mskipping: [10.0.5.68] => (item=[]) [0m
    [0;36mskipping: [10.0.5.69] => (item=[]) [0m
    [0;36mskipping: [10.0.5.70] => (item=[]) [0m
    [0;36mskipping: [10.0.5.71] => (item=[]) [0m
    [0;36mskipping: [10.0.5.72] => (item=[]) [0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install zk] ***************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid var] *****************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add lines in zoo.cfg.template to zoo.cfg] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    PLAY [mesos masters] ***********************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : include_vars] *************************
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add apt-key] **************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Remove mesosphere repo] ***************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install mesos] ************************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install zookeeperd if missing (on trusty)] ***
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : remove myid] **************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update from ansibleshipyad] ******
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : create dataDir if not exist] **********
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update in dataDir] ***************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-slave override] *****************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-master override] ****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable zk] ***************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Downloading and enable the EPEL repository definitions.] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install mesosphere] *******************
    [0;36mskipping: [10.0.5.67] => (item=[]) [0m
    [0;36mskipping: [10.0.5.68] => (item=[]) [0m
    [0;36mskipping: [10.0.5.69] => (item=[]) [0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install zk] ***************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid var] *****************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add lines in zoo.cfg.template to zoo.cfg] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    
    RUNNING HANDLER [ansible-role-mesos-by-mesosphere : Restart zookeeper] *********
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.67][0m
    
    PLAY [mesos slaves] ************************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : include_vars] *************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add apt-key] **************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Remove mesosphere repo] ***************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install mesos] ************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : install zookeeperd if missing (on trusty)] ***
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : remove myid] **************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update from ansibleshipyad] ******
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : create dataDir if not exist] **********
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid update in dataDir] ***************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;33mchanged: [10.0.5.72][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-slave override] *****************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : mesos-master override] ****************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.71][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable zk] ***************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add mesosphere repo] ******************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Downloading and enable the EPEL repository definitions.] ***
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install mesosphere] *******************
    [0;36mskipping: [10.0.5.70] => (item=[]) [0m
    [0;36mskipping: [10.0.5.71] => (item=[]) [0m
    [0;36mskipping: [10.0.5.72] => (item=[]) [0m
    
    TASK [ansible-role-mesos-by-mesosphere : Install zk] ***************************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update /etc/hosts] ********************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : myid var] *****************************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set zoo.cfg.template] *****************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Add lines in zoo.cfg.template to zoo.cfg] ***
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : zookeeper systemd] ********************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : Define zk masters in mesos] ***********
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : /etc/mesos/zk] ************************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : set quorum: a number greater than # of masters divided by 2] ***
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : update quorum on masters] *************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-slave on masters] **********
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-slave on masters] *******
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-master] *****************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : stop mesos-master on slaves] **********
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : disable mesos-master on masters] ******
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-mesos-by-mesosphere : restart mesos-slave] ******************
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    PLAY [spark for mesos] *********************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-spark-for-mesos : unarchive spark directly (new in ansible 2.0)] ***
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-spark-for-mesos : symlink to spark home] ********************
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-spark-for-mesos : spark configuration (spark-env.sh)] *******
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    PLAY [opencv] ******************************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.69][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : compiler package] **********************************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : required packages] *********************************
    [0;33mchanged: [10.0.5.71] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    [0;33mchanged: [10.0.5.69] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    [0;33mchanged: [10.0.5.70] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    [0;33mchanged: [10.0.5.68] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    [0;33mchanged: [10.0.5.67] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    [0;33mchanged: [10.0.5.72] => (item=[u'cmake', u'git', u'libgtk2.0-dev', u'pkg-config', u'libavcodec-dev', u'libavformat-dev', u'libswscale-dev'])[0m
    
    TASK [ansible-role-opencv : optional packages] *********************************
    [0;33mchanged: [10.0.5.68] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    [0;33mchanged: [10.0.5.69] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    [0;33mchanged: [10.0.5.70] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    [0;33mchanged: [10.0.5.67] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    [0;33mchanged: [10.0.5.71] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    [0;33mchanged: [10.0.5.72] => (item=[u'python-dev', u'python-numpy', u'libtbb2', u'libtbb-dev', u'libjpeg-dev', u'libpng-dev', u'libtiff-dev', u'libjasper-dev', u'libdc1394-22-dev'])[0m
    
    TASK [ansible-role-opencv : Create a working directory] ************************
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : git clone opencv (dev)] ****************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.68][0m
    
    TASK [ansible-role-opencv : download opencv (stable)] **************************
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : git clone opencv_contrib (dev)] ********************
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.68][0m
    
    TASK [ansible-role-opencv : git clone opencv_contrib (stable)] *****************
    [0;36mskipping: [10.0.5.67][0m
    [0;36mskipping: [10.0.5.68][0m
    [0;36mskipping: [10.0.5.69][0m
    [0;36mskipping: [10.0.5.70][0m
    [0;36mskipping: [10.0.5.71][0m
    [0;36mskipping: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : remove build if exists] ****************************
    [0;32mok: [10.0.5.68][0m
    [0;32mok: [10.0.5.67][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    [0;32mok: [10.0.5.69][0m
    
    TASK [ansible-role-opencv : Create build directory] ****************************
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : Make the opencv build artifacts] *******************
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : Compile opencv] ************************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-opencv : Install opencv] ************************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.69][0m
    [0;33mchanged: [10.0.5.68][0m
    [0;33mchanged: [10.0.5.67][0m
    [0;33mchanged: [10.0.5.72][0m
    
    PLAY [INRIA Person Dataset (for Human Detection)] ******************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-dataset : Default dataset directory] ************************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-dataset : INRIA Person Dataset] *****************************
    [0;33mchanged: [10.0.5.72][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.70][0m
    
    PLAY [Human and Face Detection] ************************************************
    
    TASK [setup] *******************************************************************
    [0;32mok: [10.0.5.71][0m
    [0;32mok: [10.0.5.70][0m
    [0;32mok: [10.0.5.72][0m
    
    TASK [ansible-role-analytics : Base directory for analytics] *******************
    [0;33mchanged: [10.0.5.70][0m
    [0;33mchanged: [10.0.5.71][0m
    [0;33mchanged: [10.0.5.72][0m
    
    TASK [ansible-role-analytics : Python for Human and Face Detection by OpenCV] **
    [0;36mskipping: [10.0.5.70] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection_by_spark.py) [0m
    [0;36mskipping: [10.0.5.70] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection.py) [0m
    [0;36mskipping: [10.0.5.71] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection_by_spark.py) [0m
    [0;36mskipping: [10.0.5.71] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection.py) [0m
    [0;36mskipping: [10.0.5.70] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_and_face_detection.py) [0m
    [0;36mskipping: [10.0.5.72] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection_by_spark.py) [0m
    [0;36mskipping: [10.0.5.72] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_detection.py) [0m
    [0;36mskipping: [10.0.5.71] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_and_face_detection.py) [0m
    [0;36mskipping: [10.0.5.72] => (item=/home/ubuntu/pedestrian-and-face-detection/roles/ansible-role-analytics/files/pedestrian_and_face_detection.py) [0m
    
    TASK [ansible-role-analytics : Download XML classifiers of Face and Eye Detection by OpenCV] ***
    [0;36mskipping: [10.0.5.70] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml) [0m
    [0;36mskipping: [10.0.5.70] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml) [0m
    [0;36mskipping: [10.0.5.71] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml) [0m
    [0;36mskipping: [10.0.5.71] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml) [0m
    [0;36mskipping: [10.0.5.72] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml) [0m
    [0;36mskipping: [10.0.5.72] => (item=https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml) [0m
    
    PLAY RECAP *********************************************************************
    [0;33m10.0.5.67[0m                  : [0;32mok=49  [0m [0;33mchanged=15  [0m unreachable=0    failed=0   
    [0;33m10.0.5.68[0m                  : [0;32mok=49  [0m [0;33mchanged=15  [0m unreachable=0    failed=0   
    [0;33m10.0.5.69[0m                  : [0;32mok=49  [0m [0;33mchanged=15  [0m unreachable=0    failed=0   
    [0;33m10.0.5.70[0m                  : [0;32mok=47  [0m [0;33mchanged=14  [0m unreachable=0    failed=0   
    [0;33m10.0.5.71[0m                  : [0;32mok=47  [0m [0;33mchanged=14  [0m unreachable=0    failed=0   
    [0;33m10.0.5.72[0m                  : [0;32mok=47  [0m [0;33mchanged=14  [0m unreachable=0    failed=0   
    


The installation may take 30 minutes or an hour to complete.

OpenCV in Python
----------------

Before we run our code for this project, let's try OpenCV first to see
how it works.

Import cv2
~~~~~~~~~~

Let's import opencv python module and we will use images from the online
database image-net.org to test OpenCV image recognition.

.. code:: ipython2

    import cv2

Let's download a mailbox image with a red color to see if opencv
identifies the shape with a color. The example file in this tutorial is:

.. code:: ipython2

    !curl http://farm4.static.flickr.com/3061/2739199963_ee78af76ef.jpg > mailbox.jpg


.. parsed-literal::

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  167k  100  167k    0     0   686k      0 --:--:-- --:--:-- --:--:--  684k


.. code:: ipython2

    %matplotlib inline

.. code:: ipython2

    from IPython.display import Image
    mailbox_image = "mailbox.jpg"
    Image(filename=mailbox_image)




.. image:: facedetection_files/facedetection_46_0.jpeg



You can try other images. Check out the image-net.org for mailbox
images: http://image-net.org/synset?wnid=n03710193

Image Detection
~~~~~~~~~~~~~~~

Just for a test, let's try to detect a red color shaped mailbox using
opencv python functions.

There are key functions that we use: \* cvtColor: to convert a color
space of an image \* inRange: to detect a mailbox based on the range of
red color pixel values \* np.array: to define the range of red color
using a Numpy library for better calculation \* findContours: to find a
outline of the object \* bitwise\_and: to black-out the area of contours
found

.. code:: ipython2

    import numpy as np
    import matplotlib.pyplot as plt
    
    # imread for loading an image
    img = cv2.imread(mailbox_image)
    # cvtColor for color conversion
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # define range of red color in hsv
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    
    # threshold the hsv image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    
    # find a red color mailbox from the image
    im2, contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # bitwise_and to remove other areas in the image except the detected object
    res = cv2.bitwise_and(img, img, mask = mask)
    
    # turn off - x, y axis bar
    plt.axis("off")
    # text for the masked image
    cv2.putText(res, "masked image", (20,300), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    # display
    plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    plt.show()



.. image:: facedetection_files/facedetection_49_0.png


The red color mailbox is left alone in the image which we wanted to find
in this example by opencv functions. You can try other images with
different colors to detect the different shape of objects using
findContours and inRange from opencv.

For more information, see the useful links below.

-  contours features:
   http://docs.opencv.org/3.1.0/dd/d49/tutorial\_py\_contour\_features.html
-  contours:
   http://docs.opencv.org/3.1.0/d4/d73/tutorial\_py\_contours\_begin.html
-  red color in hsv:
   http://stackoverflow.com/questions/30331944/finding-red-color-using-python-opencv
-  inrange:
   http://docs.opencv.org/master/da/d97/tutorial\_threshold\_inRange.html
-  inrange:
   http://docs.opencv.org/3.0-beta/doc/py\_tutorials/py\_imgproc/py\_colorspaces/py\_colorspaces.html
-  numpy:
   http://docs.opencv.org/3.0-beta/doc/py\_tutorials/py\_core/py\_basic\_ops/py\_basic\_ops.html

Human and Face Detection in OpenCV
----------------------------------

INRIA Person Dataset
~~~~~~~~~~~~~~~~~~~~

We use INRIA Person dataset to detect upright people and faces in images
in this example. Let's download it first.

.. code:: ipython2

    !curl ftp://ftp.inrialpes.fr/pub/lear/douze/data/INRIAPerson.tar > INRIAPerson.tar


.. parsed-literal::

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  969M  100  969M    0     0  8480k      0  0:01:57  0:01:57 --:--:-- 12.4M


.. code:: ipython2

    !tar xvf INRIAPerson.tar > logfile && tail logfile


.. parsed-literal::

    INRIAPerson/train_64x128_H96/pos/person_and_bike_191b.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_207a.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_207b.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_208a.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_208b.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_209a.png
    INRIAPerson/train_64x128_H96/pos/person_and_bike_209b.png
    INRIAPerson/train_64x128_H96/pos.lst
    INRIAPerson/train_64x128_H96/neg
    INRIAPerson/train_64x128_H96/neg.lst


Face Detection using Haar Cascades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section is prepared based on the opencv-python tutorial:
http://docs.opencv.org/3.1.0/d7/d8b/tutorial\_py\_face\_detection.html#gsc.tab=0

There is a pre-trained classifier for face detection, download it from
here:

.. code:: ipython2

    !curl https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml > haarcascade_frontalface_default.xml


.. parsed-literal::

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  908k  100  908k    0     0  2225k      0 --:--:-- --:--:-- --:--:-- 2259k


This classifier XML file will be used to detect faces in images. If you
like to create a new classifier, find out more information about
training from here:
http://docs.opencv.org/3.1.0/dc/d88/tutorial\_traincascade.html

Face Detection Python Code Snippet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, we detect faces from the first five images using the classifier.

.. code:: ipython2

    # import the necessary packages
    from __future__ import print_function
    import numpy as np
    import cv2
    from os import listdir
    from os.path import isfile, join
    import matplotlib.pyplot as plt
    
    mypath = "INRIAPerson/Test/pos/"
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    
    cnt = 0
    for filename in onlyfiles:
        image = cv2.imread(filename)
        image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image_grayscale, 1.3, 5)
        if len(faces) == 0:
            continue
    
        cnt_faces = 1
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(image, "face" + str(cnt_faces), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
            plt.figure()
            plt.axis("off")
            plt.imshow(cv2.cvtColor(image[y:y+h, x:x+w], cv2.COLOR_BGR2RGB))
            cnt_faces += 1
        plt.figure()
        plt.axis("off")
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))        
        cnt = cnt + 1
        if cnt == 5:
            break



.. image:: facedetection_files/facedetection_59_0.png



.. image:: facedetection_files/facedetection_59_1.png



.. image:: facedetection_files/facedetection_59_2.png



.. image:: facedetection_files/facedetection_59_3.png



.. image:: facedetection_files/facedetection_59_4.png



.. image:: facedetection_files/facedetection_59_5.png



.. image:: facedetection_files/facedetection_59_6.png



.. image:: facedetection_files/facedetection_59_7.png



.. image:: facedetection_files/facedetection_59_8.png



.. image:: facedetection_files/facedetection_59_9.png



.. image:: facedetection_files/facedetection_59_10.png


Pedestrian Detection using HOG Descriptor
-----------------------------------------

We will use Histogram of Oriented Gradients (HOG) to detect a upright
person from images.

Python Code Snippet
~~~~~~~~~~~~~~~~~~~

.. code:: ipython2

    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    cnt = 0
    for filename in onlyfiles:
        img = cv2.imread(filename)
        orig = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
        # detect people in the image
        (rects, weights) = hog.detectMultiScale(img, winStride=(8, 8),
        padding=(16, 16), scale=1.05)
    
        # draw the final bounding boxes
        for (x, y, w, h) in rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
        plt.figure()
        plt.axis("off")
        plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))
        plt.figure()
        plt.axis("off")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        cnt = cnt + 1
        if cnt == 5:
            break



.. image:: facedetection_files/facedetection_62_0.png



.. image:: facedetection_files/facedetection_62_1.png



.. image:: facedetection_files/facedetection_62_2.png



.. image:: facedetection_files/facedetection_62_3.png



.. image:: facedetection_files/facedetection_62_4.png



.. image:: facedetection_files/facedetection_62_5.png



.. image:: facedetection_files/facedetection_62_6.png



.. image:: facedetection_files/facedetection_62_7.png



.. image:: facedetection_files/facedetection_62_8.png



.. image:: facedetection_files/facedetection_62_9.png


Processing by Apache Spark
--------------------------

INRIA Person dataset provides 100+ images and Spark can be used for
image processing in parallel. We load 288 images from "Test/pos"
directory.

Spark provides a special object 'sc' to connect between a spark cluster
and functions in python code. Therefore, we can run python functions in
parallel to detet objects in this example.

-  *map* function is used to process pedestrian and face detection per
   image from the parallelize() function of 'sc' spark context.
-  *collect* fonction merges results in an array.

.. code:: ipython2

    def apply_batch(imagePath):
            import cv2
            import numpy as np
            # initialize the HOG descriptor/person detector
            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            image = cv2.imread(imagePath)
            # detect people in the image
            (rects, weights) = hog.detectMultiScale(image, winStride=(8, 8),
                padding=(16, 16), scale=1.05)
            # draw the final bounding boxes
            for (x, y, w, h) in rects:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return image

Parallelize in Spark Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The list of image files is given to parallelize.

.. code:: ipython2

    pd = sc.parallelize(onlyfiles)

Map Function (apply\_batch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 'apply\_batch' function that we created above is given to map
function to process in a spark cluster.

.. code:: ipython2

    pdc = pd.map(apply_batch)

Collect Function
~~~~~~~~~~~~~~~~

The result of each map process is merged to an array.

.. code:: ipython2

    result = pdc.collect()

Results for 100+ images by Spark Cluster
----------------------------------------

.. code:: ipython2

    for image in result:
        plt.figure()
        plt.axis("off")
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
