# Docker Flask REST Service 

We discuss how to use Docker to deploy a REST service designed using
Python Flask.

# Creating the Image 

```console
$ mkdir -p ~/cloudmesh/containers/docker-flask
$ cd ~/cloudmesh/containers/docker-flask
```

In this directory we will have the following file and directory
structure, where directories are indicated with a `/` at the end

```
~/cloudmesh/containers/docker-flask
    - Dockerfile
    - requirements.txt
    - app/
        - main.py
```

Include the following content in the `requirements.txt` file.

```
Flask==0.11.1
```

To fulfill the requirements, please run the  command

```console
$ pip install -r requirements.txt
```

Next we are going to create the Dockerfile which includes all the
instructions for the deployment of the REST API on docker. This file
includes the following content:

:warning: we do not know if this is a good image as this was
originally contributed by a student. We would prefer if the image is
created from scratch by a dockerfile. Running arbitrary docker images
on your machine could pose a security risk

```
FROM tiangolo/uwsgi-nginx-flask:flask
COPY ./app /app
```
    
The Dockerfile contains the `FROM` command which downloads a parent
image in which we install the rest of our services. The image is
hosted on Dockerhub


So in this case for the ease of the task and to keep it simple with
minimum packages we are going to select an image including nginx, flask
and uWSGI.

1.  Nginx: An open source software for web serving capability.

2.  Flask: REST API package in Python

3.  uWSGI: A server and one of the protocols implemented in WSGI which
    is a protocol used for pure HTTP communications and load balancing.

So this image includes everything we need to work on this tutorial.

COPY: Here it will copy content from app folder created in local machine
to the Docker container.

Now the Dockerfile is completed and we have everything needed to build a
docker image.

Next we create the main.py file inside the app folder with the
following content.

```python
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    data = {"message": "Hey I am using Docker!")
    return flask.jsonify(**data)

@app.route("/cloudmesh/cpu")
def get_cpu():
    data = {"cpu": "icore7")
    return flask.jsonify(**data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=80)
```

To build the container, please use the commands 

```console
$ cd ~/cloudmesh/containers/docker-flask
$ docker build -t sample-flask-rest-app .
```

If it builds successfully, you will get the following response

:warning: this image may not work and may not be secure so do not use
this example!

```console
$ docker build -t sample-flask-rest-app .
Sending build context to Docker daemon  19.15MB
Step 1/2: FROM tiangolo/uwsgi-nginx-flask:python3.7
 ---> ec43f17def9a
Step 2/2: COPY ./app /app
 ---> e8eb1bff86b8
Successfully built e8eb1bff86b8
Successfully tagged sample-flask-rest-app:latest

Note: Changing any content inside the app folder must be
      updated in the container by rebuilding the image.
```
      

## Running the Docker Image

Run the following commands to get the REST API hosted on
<http://127.0.0.1:80>

```console
$ docker run -p 80:80 -t sample-flask-rest-app
```

If it is loaded and if it runs successfully you will see a response
similar to

```console
Checking for script in /app/prestart.sh
Running script /app/prestart.sh
Running inside /app/prestart.sh, you could add migrations to this file, e.g.:

#! /usr/bin/env console

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head

/usr/lib/python2.7/dist-packages/supervisor/options.py:296:
UserWarning: Supervisord is running as root and it is searching
for its configuration file in default locations (including its
current working directory); you probably want to specify a "-c"
argument specifying an absolute path to a configuration file for
improved security.

'Supervisord is running as root and it is searching '
2018-02-19 18:07:46,198 CRIT Supervisor running as root 
           (no user in config file)
2018-02-19 18:07:46,198 WARN Included extra file
           "/etc/supervisor/conf.d/supervisord.conf" during parsing
2018-02-19 18:07:46,204 INFO RPC interface 'supervisor' initialized
2018-02-19 18:07:46,204 CRIT Server 'unix_http_server' 
           running without any
           HTTP authentication checking
2018-02-19 18:07:46,204 INFO supervisord started with pid 7
2018-02-19 18:07:47,207 INFO spawned: 'nginx' with pid 10
2018-02-19 18:07:47,211 INFO spawned: 'uwsgi' with pid 11
[uWSGI] getting INI configuration from /app/uwsgi.ini
[uWSGI] getting INI configuration from /etc/uwsgi/uwsgi.ini
*** Starting uWSGI 2.0.15 (64bit) on [Mon Feb 19 18:07:47 2018] ***
compiled with version: 4.9.2 on 04 February 2018 16:11:35
os: Linux-4.4.0-112-generic #135-Ubuntu SMP 
    Fri Jan 19 11:48:36 UTC 2018
nodename: 7f9706084219
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 8
current working directory: /app
detected binary path: /usr/local/bin/uwsgi
your memory page size is 4096 bytes
detected max file descriptor number: 1048576
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to UNIX address /tmp/uwsgi.sock fd 3
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! 
    (use the --uid flag) *** 
Python version: 2.7.14 (default, Dec 12 2017, 16:55:09)  [GCC 4.9.2]
*** Python threads support is disabled. You can enable it 
    with --enable-threads ***
Python main interpreter initialized at 0x1eed1b0
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 1237056 bytes (1208 KB) for 16 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 
     0x1eed1b0 pid: 11 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 11)
spawned uWSGI worker 1 (pid: 14, cores: 1)
spawned uWSGI worker 2 (pid: 15, cores: 1)
2018-02-19 18:07:48,357 INFO success: nginx entered RUNNING 
  state, process has stayed up for > than 1 seconds (startsecs)
2018-02-19 18:07:48,358 INFO success: uwsgi entered RUNNING 
  state, process has stayed up for > than 1 seconds (startsecs)
```

## Interact with the container

Now you can go in your web browser to the URL

 <http://127.0.0.1:80>

To see the status of the container you can sue the command 

```console
$ docker ps -a
```

Note the CONTAINER ID. To sopt the container with a particular ID, use 

```
$ docker stop dc8cccf22216
```

To delete the docker container image, you must first sop all instances
using it and the remove the image. YOu can see the images with the
command 


```console
$ docker images
```

Then you can locate all containers using that image while looking in
the IMAGE column or using a simple fgrep in case you have many
images. stop the containers using that image and that you can say


```console
$ docker rm 74b9b994c9bd
```

while the number is the container id

Once you killed all containers using that image, you can remove the
image with the `rmi` command.

```console
$ docker rmi 8b3246425402
```
