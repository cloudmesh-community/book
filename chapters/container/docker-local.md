# Running Docker Locally :o:

The official installation documentation for docker can be found by
visiting the following Web page:

* <https://www.docker.com/community-edition>

Here you will find a variety of packages, one of which will hopefully
suitable for your operating system. The supported operating systems
currently include:

* OSX, Windows, Centos, Debian, Fedora, Ubuntu, AWS, Azure

Please chose the one most suitable for you. For your convenience we
provide you with installation instructions for OSX
(Section [Docker on OSX](#s:docker-osx){reference-type="ref"
reference="s:docker-osx"}), Windows 10
(Section [Docker on WIndows](#s:docker-windows){reference-type="ref"
reference="s:docker-windows"}) and Ubuntu
(Section [Docker on ubuntu](#s:docker-ubuntu){reference-type="ref"
reference="s:docker-ubuntu"}).

## Instillation for OSX

The docker community edition for OSX can be found at the following link

* <https://store.docker.com/editions/community/docker-ce-desktop-mac>

We recommend that at this time you get the version *Docker CE for MAC
(stable)*

* <https://download.docker.com/mac/stable/Docker.dmg>

Clicking on the link will download a dmg file to your machine, that you
than will need to install by double clicking and allowing access to the
dmg file. Upon installation a `whale` in the top status bar shows that
Docker is running, and you can access it via a terminal.

![Docker integrated in the menu bar on OSX](images/whale-in-menu-bar.png){width="50%"}

## Installation for Ubuntu

In order to install Docker community edition for Ubuntu, you first have
to register the repository from where you can download it. This can be
achieved as follows:

```bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Now that you have configured the repository location, you can install it
after you have updated the operating system. The update and install is
done as follows:

```bash
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo apt-get update
```

## Draft: Installation for Windows 10

The instructions for Windows have not passed our quality control. We
look for TAs and student that test out and improve this section.

:o: TA: Docker on windows. Please improve and finalize the section}
Before we start we create the following directory:

```bash
$ mkdir $HOME/cloudmesh
```

We also assume you have installed gitbash and use the a git bash
terminal window for the next steps.

To install Docker on Windows, please download the following files

* <https://download.docker.com/win/stable/Docker\%20for\%20Windows\%20Installer.exe>
* <https://download.docker.com/win/stable/DockerToolbox.exe>

Move the downloaded files to a directory `$HOME/cloudmesh`

Place the downloaded exe files in the cloudmesh directory we created
earlier. First conduct the Docker installation and then continue with
the Docker Toolbox installation. You can double click the exe files and
run the installation.

When you are doing the installation, check on the selection in the
installation saying to create shortcuts in your desktop. This way you
can start all the programs from a desktop shortcut.

To run docker, you need to start the *Docker Quickstart Terminal*
application and it will load all docker and provide a terminal window in
which you can execute docker commands. Once the terminal is loaded, it
will show something like following:

```bash
$ <username>@<yourpc> ~
```

## Testing the Install

To test if it works execute the following commands in a terminal:

```bash
$ docker version
```

You should see an output similar to

    docker version

    Client:
      Version:      17.03.1-ce
      API version:  1.27
      Go version:   go1.7.5
      Git commit:   c6d412e
      Built:        Tue Mar 28 00:40:02 2017
      OS/Arch:      darwin/amd64

    Server:
      Version:      17.03.1-ce
      API version:  1.27 (minimum version 1.12)
      Go version:   go1.7.5
      Git commit:   c6d412e
      Built:        Fri Mar 24 00:00:50 2017
      OS/Arch:      linux/amd64
      Experimental: true

To see if you can run a container use

```bash
$ docker run hello-world
```

Once executed you should see an output similar to

```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
78445dd45222: Pull complete 
Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a .....
Status: Downloaded newer image for
        hello-world:latest

Hello from Docker!
This message shows that your installation appears
to be working correctly.

To generate this message, Docker took the following
steps:

1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image 
   from the Docker Hub.
3. The Docker daemon created a new container from that 
   image which runs the executable that produces the 
   output you are currently reading.
4. The Docker daemon streamed that output to the Docker 
   client, which sent it to your terminal.

To try something more ambitious, you can run an Ubuntu
container with:

$ docker run -it ubuntu bash

Share images, automate workflows, and more with a
free Docker ID:

https://cloud.docker.com/

For more examples and ideas, visit:
https://docs.docker.com/engine/userguide/
```
