# Docker Compose

## Introduction

Docker compose is a tool for defining and running multi-container
using docker container to package them as an application. Docker
compose uses a YAML file to specify the dependencies between the
containers and their configuration. The nice feature is taht with a
single command you create and start all the services from your
configuration file and can maage the application including shutting it
down.

Using docker compose includes a four-step process:

1. Define your application's environment with a `Dockerfile` so it can be
   reproduced anywhere.

2. Define the services that make up your application in a
   `docker-compose.yml` file so they can be specified in a single file
   and run with simple docker compose commands.

3. To start the application use the command `docker-compose up`

4. To shut down the application use the command `docker-compose down`

## Installation

Docker compose can be installed on Windows 10  EDU/PRO, Linux, and
macOS.

### Install on MacOS

For macOS please go to this link to download a desktop version:

* <https://docs.docker.com/docker-for-mac/install/>

### Install on Linux

On Linux you can run the command.

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Please note that you use the newest version which can be found on the
download Web page. After downloading, make sure that you apply
executable permissions to binary:

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

### Install on Windows 10

#### System Requirements

In case you use Windows you need the follwing minimal requirements:

* Windows 10 64-bit
* Pro, Enterprise, or Education (Build 15063 or later).
* Hyper-V and Containers Windows features must be enabled.

The following hardware prerequisites are required to successfully run
Client Hyper-V on Windows 10:

* 64 bit processor with Second Level Address Translation (SLAT)
* 4GB system RAM,
* BIOS-level hardware,
* Virtualization support must be enabled in the BIOS settings.

Go to this link to download a desktop verion:

* <https://hub.docker.com/?overlay=onboarding>

### Test the installation

It is important that you test your instalation before you move
forward.This can be done on the commandline with the command. More
involved tests can be conducted while using the simple example
depicted in this section.

```bash
$ docker-compose --version
docker-compose version 1.24.1, build 1110ad01
```

## Docker Compose File Directives

To use docker compose, you will need a file that contains 
specifications of the containers and their dependencies.
We will demonstrate this concept with a simple example. 

We are starting a `redis` cache server, a `postgresql` database
server, and containers `vote`, `result`, `worker`, `visualizer` to
provide frontend an backend services that interacte with the
containers.

After you have reviewed the yaml file, we will explain the different
parts in more detail.

```yaml
version: "3.7"
services:

  redis:
    image: redis:alpine
    ports:
      - "6379"
    networks:
      - frontend
    deploy:
      replicas: 2
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure

  db:
    image: postgres:9.4
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    deploy:
      placement:
        constraints: [node.role == manager]

  vote:
    image: dockersamples/examplevotingapp_vote:before
    ports:
      - "5000:80"
    networks:
      - frontend
    depends_on:
      - redis
    deploy:
      replicas: 2
      update_config:
        parallelism: 2
      restart_policy:
        condition: on-failure

  result:
    image: dockersamples/examplevotingapp_result:before
    ports:
      - "5001:80"
    networks:
      - backend
    depends_on:
      - db
    deploy:
      replicas: 1
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure

  worker:
    image: dockersamples/examplevotingapp_worker
    networks:
      - frontend
      - backend
    deploy:
      mode: replicated
      replicas: 1
      labels: [APP=VOTING]
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 3
        window: 120s
      placement:
        constraints: [node.role == manager]

  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    stop_grace_period: 1m30s
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]

networks:
  frontend:
  backend:

volumes:
  db-data:
```

### Configuration

#### `build`

The `build` attribute specifies either a string containing a path to the
build context:

```yaml
version: "3.7"
services:
  webapp:
    build: ./dir
```

#### `context`

The `context` attribute introduces either a path to a directory
containing a Dockerfile, or a url to a git repository. This
information is used during the build phase.


```yaml
build:
  context: ./dir
```

#### `ARGS`

The `ARGS` attribute introduces environment variables accessible only
during the build process.

```yaml
ARG buildno
ARG gitcommithash
```

```yaml
build:
  context: .
  args:
    buildno: 1
    gitcommithash: cdc3b19
```

#### `command`

The `command` attribute overrides the default command.

```yaml
command: bundle exec thin -p 3000
```

#### `depends_on`

The `depends_on` attribute introduces dependencies between
services. The container that depends on other containers, waits for
them to become available. In the following example the web serviec
depends on the db and redis services:

```yaml
version: "3.7"
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: postgres
```
	
#### image

The `image` attribute specifies the image for the container.  You can
either use a repository/tag or a partial image ID to identify the
image

```yaml
image: redis
image: ubuntu:14.04
image: mongo
```

#### ports

The `ports` attribute expose ports ports of teh container. However,
please note that the port mapping is incompatible with `network_mode: host`.

```yaml
ports:
 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
 - "6060:6060/udp"
```

#### volumes

The `volume` attribute mounts ahost paths or named volumes. A volume
is specified as sub-options to a service.

You can mount a host path as part of a definition for a single
service, and there is no need to define it in the top level `volumes`
key.

## Usages

### Build A Service depending on MongoDB

```yaml
version: "3"
services:
  web:
    build: .
    ports:
    - "8080:8080"
    depends_on:
    - mongo
  mongo:
    image: mongo
    ports:
    - "27017:27017"
```

By default, `web` service can reach the `mongo` service by using the
service’s name as we configured the database URI to be

`mongodb://mongo:27017`.

To start the two docker containers you can use the command:

```bash
$ docker-compose up
```

We can close both docker containers with:

```bash
$ docker-compose down
```
