
## Pyenv in a docker container

We provide a simple docker container on docker hub that is based on
ubuntu 18.04 that has pyenv, python 2.7.16 and python 3.7.1
installed. Using this image is as simple as downloading it and running
it.

To run the container and loginto the command prompt please use

```bash
$ docker run --rm -it cloudmesh/pyenv:1.0  /bin/bash 
```

To switch between the python versions use the command 

```bash
container> ENV2
container> ENV3
```

where container indicates that the command is executed 

### Creating the container locally

This section is only needed if you like to recreate the image or
modify the Dockerfile.

The information about how we create the image is provided at in a
repository. You can download the code in the directory and can create
the image from the Docker file while using the Makefile as follows:

``` bash
$ mkdir cloudmesh-community
$ cd cloudmesh-community
$ git clone https://github.com/cloudmesh-community/images.git
$ cd images/pyenv
$ make image
```

This will create an image locally. with


```bash
$ make login
```

you can login to the shell. Typically you will only need the docker
command as descripbed in the prvious section.
