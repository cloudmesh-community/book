# Dockerized REST Service

We discuss how to use Docker to deploy a REST service designed using
Python Flask.

## Prerequisites

In order to follow our discussion you will need a system on which you
can run docker. THis could either be OSX, Linux, or Windows.

Python 2.7.x can be used to do this tutorial

### Ubuntu and OSX

Please use our instructions on installing pyenv.

### Windows

We start with download Python:

[Download Python
MSI](https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi)

After installing python add an environmental variable by pressing
Windows Key + Pause and Select Advanced system settings. Then add an
environment variable for system variables for the variable PATH which is
already there. And in that add the new variable

    C:\Python27

As older python versions do not come or come with an outdated version of
pip, we install it as follows:

[Download Pip Installer Script](https://bootstrap.pypa.io/get-pip.py)

Now copy this file to

    C:\Users\<your_username>\cloudmesh\bin

If you do not have this path please create it, because we will be using
this place to store all the tools we need. Within the bin folder run the
following commands using command line tool or cmd.exe in windows.

``` {.bash language="bash"}
$ python get-pip.py
```

Now add this environmental variable to PATH in System variables the same
way we did earlier by putting the following value

    C:\Python27\lib\site-packages
    C:\Python27\Scripts

After adding the variables make sure you use a new cmd.exe.

Now continue by installing a Virtualenv installation

``` {.bash language="bash"}
$ pip install virtualenv 
```

Turn on Hyper-V (Windows Features Turn On and In the list selectHyper V)

Turn on Containers (Windows Features Turn On and In the list select
Hyper V)

Install emacs via chocolatey

## Activate Virtual Environment

### Ubuntu and OSX

``` {.bash language="bash"}
$ mkdir -p ~/cloudmesh/containers/docker-flask
$ cd ~/cloudmesh/containers/docker-flask
$ virtualenv venv
$ source venv/bin/activate
```

### Windows

Using cmd.exe Please replace with your username.

``` {.bash language="bash"}
$ mkdir -p C:\Users\<your_username>\cloudmesh\containers\docker-flask
$ cd C:\Users\<your_username>\cloudmesh\containers\docker-flask
$ virtualenv venv
$ venv/Script/activate
```

Now you are inside the created virtual environment. The terminal will
look something like

``` {.bash language="bash"}
(venv) neo$
```

## File Structure

The File structure takes the following look.

    docker-flask/[FOLDER]:[BASE PATH : ~/cloudmesh/containers/docker-flask]
        --|Dockerfile [FILE]
        --|requirements.txt [FILE]
        --|app/ [FOLDER]
            --|--|main.py [FILE]
            --|venv [FOLDER]

### Step 1

Create requirements.txt file

#### Ubuntu and OSX

``` {.bash language="bash"}
$ emacs requirements.txt
```

#### Windows

Install an editor such as emacs on Windows. YOu can use chocolatey for
that, or use pycharm. Do not use notepad++

``` {.bash language="bash"}
emacs requirements.txt
```

Include the following content in the requirements.txt file.

    Flask==0.11.1

Now run the following command

``` {.bash language="bash"}
$ pip install -r requirements.txt
```

### Step 2

Then we are going to create thr Dockerfile which includes all the
instructions for the deployment of the REST API on docker.

#### Ubuntu and OSX

``` {.bash language="bash"}
$ emacs Dockerfile
```

#### Windows

``` {.bash language="bash"}
emacs Dockerfile
```

Include the following content in the Dockerfile

    FROM tiangolo/uwsgi-nginx-flask:flask
    COPY ./app /app

Here we have created a minimal Dockerfile.

FROM: command tells the image that has to be pulled from the Docker hub.
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

### Step 3

Then we need to creat the main.py file inside the app folder.

#### Ubuntu and OSX

``` {.bash language="bash"}
emacs app/main.py
```

#### Windows

``` {.bash language="bash"}
emacs app/main.py
```

Then add the following content.

``` {language="python"}
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey I am using Docker!"

@app.route("/api/cpu")
def get_cpu():
# ADD CODE TO GET CPU INFO
# USE psutil LIBRARY
    return "SHOW YOUR CPU INFO"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=80)
```

After adding the content save and exit emacs.

## Build Docker Image

### Ubuntu and OSX

Now run the following commands.

``` {.bash language="bash"}
$ cd ~/cloudmesh/containers/docker-flask
$ docker build -t sample-flask-rest-app .
```

### Windows

Run Powershell as administrator and replace with your username.

``` {.bash language="bash"}
cd C:\Users\<your_username>\cloudmesh\containers\docker-flask
docker build -t sample-flask-rest-app .
```

If it builds successfully, you will get the following response

``` {.bash language="bash"}
$ docker build -t sample-flask-rest-app .
Sending build context to Docker daemon  19.15MB
Step 1/2: FROM tiangolo/uwsgi-nginx-flask:python2.7
 ---> ec43f17def9a
Step 2/2: COPY ./app /app
 ---> e8eb1bff86b8
Successfully built e8eb1bff86b8
Successfully tagged sample-flask-rest-app:latest

Note: Changing any content inside the app folder must be
      updated in the container by rebuilding the image.
```

## Run Docker Image

Run the following commands to get the REST API hosted on
<http://127.0.0.1:80>

### Ubuntu and OSX

``` {.bash language="bash"}
$ docker run -p 80:80 -t sample-flask-rest-app
```

### Windows

In Windows powershell Run as administrator (use the previous powershell
window)

``` {.bash language="bash"}
$ docker run -p 80:80 -t sample-flask-rest-app
```

Here you may have to grant permission for using this port number. So
please allow that to run.

It will take sometime to load the server once.

``` {.bash language="bash"}
$ docker run -p 80:80 -t sample-flask-rest-app
```

If it is loaded and if it runs successfully you will see a response
similar to

``` {.bash language="bash"}
Checking for script in /app/prestart.sh
Running script /app/prestart.sh
Running inside /app/prestart.sh, you could add migrations to this file, e.g.:

#! /usr/bin/env bash

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

Go to this URL: <http://127.0.0.1:80>

#### Additional INFO

``` {basicstyle="\tiny\ttfamily"}
$ docker ps -a
CONTAINER ID IMAGE                     COMMAND                  CREATED             STATUS        PORTS       NAMES
                                                                                           0.0.0.0:80->80/tcp   
dc8cccf22216 35ffca69dcc3            "/entrypoint.sh /sta..." 4m ago Up 4m                      443/tcp   romantic_sammet
e7a45c81b237 sample-flask            "/entrypoint.sh /usr..." 2d ago    Exited (0) 2d ago                 silly_kare
a4b6419016af sample-flask            "/entrypoint.sh /usr..." 2d ago    Exited (0) 2d ago                 musing_lamport
6eb7102a514e prakhar1989/static-site "./wrapper.sh"           5d ago    Exited (0) 5d ago                 competent_borg
f7c6a4710ad2 prakhar1989/static-site "./wrapper.sh"           5d ago    Exited (0) 5d ago                 static-site
361c8812ba90 busybox                 "echo 'hello from bu..." 5d ago    Exited (0) 5d ago                 blissful_wing
350ec9a2609f busybox                 "sh"                     5d ago    Exited (0) 5d ago                 nifty_mahavira
893cb11019f9 hello-world             "/hello"                 5d ago    Exited (0) 5d ago                 competent_spence
1f90a411c746 hello-world             "/hello"                 11d ago   Exited (0) 11d ago                reverent_raman

$ docker stop dc8cccf22216
dc8cccf22216

$ docker ps -a
CONTAINER ID IMAGE                     COMMAND                  CREATED             STATUS      PORTS  NAMES
dc8cccf22216 35ffca69dcc3            "/entrypoint.sh /sta..."   4m ago     Exited (137) 5s ago         romantic_sammet
e7a45c81b237 sample-flask            "/entrypoint.sh /usr..."   2d ago     Exited (0) 2d ago           silly_kare
a4b6419016af sample-flask            "/entrypoint.sh /usr..."   2d ago     Exited (0) 2d ago           musing_lamport
6eb7102a514e prakhar1989/static-site "./wrapper.sh"             5d ago     Exited (0) 5d ago           ompetent_borg
f7c6a4710ad2 prakhar1989/static-site "./wrapper.sh"             5d ago     Exited (0) 5d ago           tatic-site
361c8812ba90 busybox                 "echo 'hello from bu..."   5d ago     Exited (0) 5d ago           blissful_wing
350ec9a2609f busybox                 "sh"                       5d ago     Exited (0) 5d ago           ifty_mahavira
893cb11019f9 hello-world             "/hello"                   5d ago     Exited (0) 5d ago           competent_spence
1f90a411c746 hello-world             "/hello"                  11d ago     Exited (0) 11d ago          everent_raman
```

#### Deleting Docker Container first and then remove Docker Image

``` {basicstyle="\tiny\ttfamily"}
$ docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED      SIZE
sample-flask-rest-app        latest              8b3246425402        8m ago       697MB
<none>                       <none>              35ffca69dcc3        10m ago      697MB
sample-flask                 latest              b763c65ae11b        2d ago       709MB
my-awesome-nginx             v3                  56cb2d15e863        3d ago       16.8MB
tiangolo/uwsgi-nginx-flask   flask               3ab637f17463        2 weeks ago   709MB
tiangolo/uwsgi-nginx-flask   python2.7           ec43f17def9a        2 weeks ago   697MB
ubuntu                       16.04               0458a4468cbc        3 weeks ago   112MB
ubuntu                       latest              0458a4468cbc        3 weeks ago   112MB
busybox                      latest              5b0d59026729        3 weeks ago  1.15MB
nginx                        alpine              bb00c21b4edf        5 weeks ago  16.8MB
hello-world                  latest              f2a91732366c        3 months ago 1.85kB
prakhar1989/static-site      latest              f01030e1dcf3        2 years ago   134MB
```

``` {basicstyle="\tiny\ttfamily"}
$ docker ps -a
CONTAINER ID IMAGE                     COMMAND                  CREATED             STATUS   PORTS NAMES
74b9b994c9bd sample-flask-rest-app   "/entrypoint.sh /sta..." 2m ago  Exited (137) 1m ago    infallible_mahavira
dc8cccf22216 35ffca69dcc3            "/entrypoint.sh /sta..." 10m ago Exited (137) 5m ago    romantic_sammet
e7a45c81b237 sample-flask            "/entrypoint.sh /usr..." 2d ago  Exited (0) 2d ago      silly_kare
a4b6419016af sample-flask            "/entrypoint.sh /usr..." 2d ago  Exited (0) 2d ago      musing_lamport
6eb7102a514e prakhar1989/static-site "./wrapper.sh"           5d ago  Exited (0) 5d ago      competent_borg
f7c6a4710ad2 prakhar1989/static-site "./wrapper.sh"           5d ago  Exited (0) 5d ago      static-site
361c8812ba90 busybox                 "echo 'hello from bu..." 5d ago  Exited (0) 5d ago      blissful_wing
350ec9a2609f busybox                 "sh"                     5d ago  Exited (0) 5d ago      nifty_mahavira
893cb11019f9 hello-world             "/hello"                 5d ago  Exited (0) 5d ago      competent_spence
1f90a411c746 hello-world             "/hello"                 11d ago Exited (0) 11d ago     reverent_raman
```

``` {.bash language="bash"}
$ docker rm 74b9b994c9bd
74b9b994c9bd
```

``` {basicstyle="\tiny\ttfamily"}
$ docker ps -a
CONTAINER ID IMAGE                     COMMAND                  CREATED             STATUS   PORTS NAMES
dc8cccf22216 35ffca69dcc3            "/entrypoint.sh /sta..." 10m ago Exited (137) 5m ago    romantic_sammet
e7a45c81b237 sample-flask            "/entrypoint.sh /usr..." 2d ago     Exited (0) 2d ago   silly_kare
a4b6419016af sample-flask            "/entrypoint.sh /usr..." 2d ago     Exited (0) 2d ago   musing_lamport
6eb7102a514e prakhar1989/static-site "./wrapper.sh"           5d ago     Exited (0) 5d ago   competent_borg
f7c6a4710ad2 prakhar1989/static-site "./wrapper.sh"           5d ago     Exited (0) 5d ago   static-site
361c8812ba90 busybox                 "echo 'hello from bu..." 5d ago     Exited (0) 5d ago   blissful_wing
350ec9a2609f busybox                 "sh"                     5d ago     Exited (0) 5d ago   nifty_mahavira
893cb11019f9 hello-world             "/hello"                 5d ago     Exited (0) 5d ago   competent_spence
1f90a411c746 hello-world             "/hello"                 11d ago    Exited (0) 11d ago  reverent_raman
```

``` {.bash language="bash"}
$ docker images
REPOSITORY                 TAG       IMAGE ID     CREATED        SIZE
sample-flask-rest-app      latest    8b3246425402 8m ago  697MB
<none>                     <none>    35ffca69dcc3 10m ago 697MB
sample-flask               latest    b763c65ae11b 2d ago     709MB
my-awesome-nginx           v3        56cb2d15e863 2d ago     16.8MB
tiangolo/uwsgi-nginx-flask flask     3ab637f17463 2 weeks ago    709MB
tiangolo/uwsgi-nginx-flask python2.7 ec43f17def9a 2 weeks ago    697MB
ubuntu                     16.04     0458a4468cbc 3 weeks ago    112MB
ubuntu                     latest    0458a4468cbc 3 weeks ago    112MB
busybox                    latest    5b0d59026729 3 weeks ago    1.15MB
nginx                      alpine    bb00c21b4edf 5 weeks ago    16.8MB
hello-world                latest    f2a91732366c 3 months ago   1.85kB
prakhar1989/static-site    latest    f01030e1dcf3 2 years ago    134MB
```

``` {.bash basicstyle="\tiny\ttfamily" language="bash"}
$ docker rmi 8b3246425402
Untagged: sample-flask-rest-app:latest
Deleted: sha256:8b3246425402b55aa5c4cf02cc5ad9ebd880b9fef639529b81495e778e3b3246
Deleted: sha256:639497d8f8bfa7cf497dfc142c8cc9d9b0b6b8689c777b9daa185c618b33d03c
```
