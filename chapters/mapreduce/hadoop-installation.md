# Installation of Hadoop :o: {#s-hadoop-installation}

In this section we use Hadoop 3.0.1 and we install Hadoop locally in
Ubuntu 18.04. We also describe the installation of the Yarn resource
manager. We assume that you have ssh, and rsync installed and use emacs
as editor.

Prerequisites
------------

    sudo apt-get install ssh
    sudo apt-get install rsync
    sudo apt-get install emacs

User and User Group Creation
----------------------------

For security reasons we will install hadoop in a particular user and
user group. We will use the following

    sudo addgroup hadoop_group
    sudo adduser --ingroup hadoop_group hduser
    sudo adduser hduser sudo

These steps will provide sudo privileges to the created hduser user and
add the user to the group `hadoop_group`.

Configuring SSH
---------------

Here we configure SSH key for the local user to install hadoop with a
ssh-key. This is different from the ssh-key you used for Github,
FutureSystems, etc. Follow this section to configure it for Hadoop
installation.

The ssh content is included here because, we are making a ssh key for
this specific user. Next, we have to configure ssh to be used by the
hadoop user.

    su - hduser

    ssh-keygen -t rsa

Follow the instructions as provided in the commandline. When you see the
following console input, press ENTER. Here only we will create password
less keys. IN general this is not a good idea, but for this case we
make an exception.

    Enter file in which to save the key (/home/hduser/.ssh/id_rsa):

Next you will be asked to enter a password for ssh configuration,

    Enter passphrase (empty for no passphrase):

Here enter the same password

    Enter same passphrase again:

Finally you will see something like this after these steps are finished.

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/hduser/.ssh/id_rsa):
    Created directory '/home/hduser/.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/hduser/.ssh/id_rsa.
    Your public key has been saved in /home/hduser/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:0UBCPd6oYp7MEzCpOhMhNiJyQo6PaPCDuOT48xUDDc0 hduser@computer
    The key's randomart image is:
    +---[RSA 2048]----+
    |    .+ooo        |
    | .   oE.oo       |
    |+  .. ...+.      |
    |X+=  .  o..      |
    |XX.o  o.S        |
    |Bo+ + .o         |
    |*o * +.          |
    |*.. *.           |
    | +.o..           |
    +----[SHA256]-----+

You have successfully configured ssh.

Installation of Java
--------------------

If you are already logged into su, you can skip the next command:

    su - hduser

Now execute the following commands to download and install java

    mkdir -p ~/cloudmesh/bin
    cd ~/cloudmesh/bin
    wget -c --header "Cookie: \
        oraclelicense=accept-securebackup-cookie" \
        "http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.tar.gz"
    tar xvzf jdk-8u161-linux-x64.tar.gz

:o: why not put a github dir in cloudmesh, with some bin script that
installes hadoop and jave ... and than keep that up to date. for
example

```bash
$ cm-hadoop install
```

:o it would figure out the os and to the righ things

Installation of Hadoop
----------------------

First we will take a look on how to install Hadoop 3.0.1 on Ubuntu
16.04. We may need a prior folder structure to do the installation
properly.

    cd ~/cloudmesh/bin/
    wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-3.0.1/hadoop-3.0.1.tar.gz
    tar -xzvf hadoop-3.0.1.tar.gz

Hadoop Environment Variables
----------------------------

In Ubuntu the environmental variables are setup in a file called bashrc
at it can be accessed the following way

    emacs ~/.bashrc

    export JAVA_HOME=~/cloudmesh/bin/jdk1.8.0_161
    export HADOOP_HOME=~/cloudmesh/bin/hadoop-3.0.1
    export YARN_HOME=$HADOOP_HOME
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
    export PATH=$HADOOP_HOME/bin:$JAVA_HOME/bin:$PATH

In Emacs to save the file `Ctrl-X-S` and `Ctrl-X-C` to exit. After
editing you must update the variables in the system.

    source ~/.bashrc
    java -version

If you have installed things properly there will be no errors. It will
show the version as follows,

    java version "1.8.0_161"
    Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
    Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)

And verifying the hadoop installation,

    hadoop

If you have successfully installed this, there must be a message shown
as below.

    Usage: hadoop [--config confdir] COMMAND
           where COMMAND is one of:
      fs                   run a generic filesystem user client
      version              print the version
      jar <jar>            run a jar file
      checknative [-a|-h]  check native hadoop and compression libraries availability
      distcp <srcurl> <desturl> copy file or directories recursively
      archive -archiveName NAME -p <parent path> <src>* <dest> create a hadoop archive
      classpath            prints the class path needed to get the
      credential           interact with credential providers
                           Hadoop jar and the required libraries
      daemonlog            get/set the log level for each daemon
      trace                view and modify Hadoop tracing settings
     or
      CLASSNAME            run the class named CLASSNAME

    Most commands print help when invoked w/o parameters.
