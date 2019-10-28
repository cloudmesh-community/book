# Docker Compose

## Introduction

Compose is a tool for defining and running multi-container Docker applications. With Compose, a YAML file is used to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Using Compose is basically a four-step process:

1. Define your app’s environment with a `Dockerfile` so it can be reproduced anywhere.

2. Define the services that make up your app in `docker-compose.yml` so they can be run together in an isolated environment.

3. Run `docker-compose up` and Compose starts and runs your entire app.

4. Run `docker-compose down` to shutdown your entire app.

## Installation

### Install on MacOS

Go to this link to download a desktop version:
https://docs.docker.com/docker-for-mac/install/

### Install on Linux

1. Run this command to download the current stable release of Docker Compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

2. Apply executable permissions to the binary:

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

### Install on Windows

#### System Requirements

Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later).
Hyper-V and Containers Windows features must be enabled.
The following hardware prerequisites are required to successfully run Client Hyper-V on Windows 10:
64 bit processor with Second Level Address Translation (SLAT), 4GB system RAM,
BIOS-level hardware virtualization support must be enabled in the BIOS settings.

Go to this link to download a desktop verion:
https://hub.docker.com/?overlay=onboarding

### Test the installation

```bash
$ docker-compose --version
docker-compose version 1.24.1, build 1110ad01
```

## Docker Compose File Directives

Docker-compose file a yaml file with specific formats. Here shows an example to start a `redis` cache server, `postgresql` as a database server, and `vote`, `result`, `worker`, `visualizer` as either the frontend or backend services.

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

### Configurations

#### `build`

Configuration options that are applied at build time.

build can be specified either as a string containing a path to the build context:

```yaml
version: "3.7"
services:
  webapp:
    build: ./dir
```

#### `context`
Either a path to a directory containing a Dockerfile, or a url to a git repository.

Compose builds and tags it with a generated name, and uses that image thereafter.

```yaml
build:
  context: ./dir
```

#### `ARGS`

Add build arguments, which are environment variables accessible only during the build process.

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

Override the default command.

```yaml
command: bundle exec thin -p 3000
```

#### `depends_on`
Express dependency between services, Service dependencies cause the following behaviors:

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
Specify the image to start the container from. Can either be a repository/tag or a partial image ID.

```yaml
image: redis
image: ubuntu:14.04
image: mongo
```

#### ports

Expose ports.

Note: Port mapping is incompatible with `network_mode: host`.

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

Mount host paths or named volumes, specified as sub-options to a service.

You can mount a host path as part of a definition for a single service, and there is no need to define it in the top level `volumes` key.

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

By default, “web” service can reach “mongo” service by using the service’s name. That is why we configured the database URI to `mongodb://mongo:27017`.

To run the two dockers using the compose file execute the command:

```bash
$ docker-compose up
```

We can close both dockers with:

```bash
$ docker-compose down
```
