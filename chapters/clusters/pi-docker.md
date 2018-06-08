# Docker on a Pi

Docker is a tool that allows us to deploy applications inside of
software containers.  A container allows a developer to package the
application along with dependencies associated with it and put all in
a box which is an isolated environment so that the underlying host
operating system is completely abstracted from the application running
inside the box.

It is a method of packaging software, to include not only our code,
but also other components such as a full file system, system tools,
services, and libraries. This can be useful for the Raspberry Pi
because it allows users to run applications without lot of steps, as
long as the application is packaged inside of a Docker image. We
simply install Docker and run the container.

According to the developers of Docker it includes the following
features:

* Portability
* Density
* Scalability
* Security


## Installation 

First we need to make sure the Raspberry Pi is up to date so we can
install a recent version of docker.  The automated script maintained
by the Docker project will create a systemd service file and copy the relevant Docker binaries into `/usr/bin/`.


```bash
$ sudo apt-get update
$ curl -sSL https://get.docker.com | sh
```

In order for us to start the docker deamon at the next boot, we add it as follows:
			
```bash
$ sudo systemctl enable docker
```
    
Now if we reboot, the Docker deamon will start. In case you like to avoid the firts reboot, you can use the command:

```bash
$ sudo systemctl start docker
```
      
Naturally you do not have to do this after you reboot the next time.

The Docker client can only be used by `root` or members of the `docker` group.  Thus, let us add the user pi (or your equivalent user) to the docker group using:

```bash
$ sudo usermod -aG docker pi
```
	
After executing the above command, we log out of the terminal restart it so we are sure the user permissions are available in the shell we use. 

## Testing

To test docker is installed successfully, we run the `hello-world` docker image with the command:

```bash
$ docker run hello-world
```
	
If Docker is installed properly, we will see a `Hello from Docker!`
message.
