# Docker on a Pi

Docker is a tool that allows you to deploy applications inside of
software containers.  A container allows a developer to package the
application along with dependencies associated with it and put all in
a box which is an isolated environment so that the underlying host
operating system is completely abstracted from the application running
inside the box.

It is a method of packaging software, to include not only your code,
but also other components such as a full file system, system tools,
services, and libraries. This can be useful for the Raspberry Pi
because it allows users to run applications without lot of steps, as
long as the application is packaged inside of a Docker image. You
simply install Docker and run the container.

Key benefits of Docker include

* Portability
* Density
* Scalability
* Security


## Installation 

First we recommend you to update the Pi followed by installing docker
using the automated script. The automated script maintained by the
Docker project will create a systemd service file and copy the
relevant Docker binaries into `/usr/bin/`.


```bash
    $ sudo apt-get update
	$ curl -sSL https://get.docker.com | sh
```

Next we need to configure it by doing the following steps
			
* Set Docker to auto-start

  ```bash
      $ sudo systemctl enable docker
  ```
    
* Reboot the Pi, or start the Docker daemon with:

  ```bash
      $ sudo systemctl start docker
  ```
      
## Enable Docker client

The Docker client can only be used by root or members of the docker
group.  Add pi or your equivalent user to the docker group using :

```bash
	$ sudo usermod -aG docker pi
```
	
After executing the above command, log out and reconnect with ssh.

## Test Docker

To test docker was installed successfully, run the hello-world image.

```bash
	$ docker run hello-world
```
	
If Docker is installed properly, you'll see a `Hello from Docker!`
message.
