# Docker Hub {#s:dockerhub}

Docker Hub is a cloud-based registry service which provides a
"centralized resource for container image discovery, distribution and
change management, user and team collaboration, and workflow
automation throughout the development
pipeline" [@hid-sp18-405-tutorial-dockerhub-overview]. There are both
private and public repositories. Private repository can only be used
by people within their own organization.

Docker Hub is integrated into Docker as the default registry. This
means that the docker pull command will initialize the download
automatically from Docker Hub
[@hid-sp18-405-tutorial-dockerhub-blog-use]. It allows users to
download (pull), build, test and store their images for easy
deployment on any host they may
have [@hid-sp18-405-tutorial-dockerhub-overview].

## Create Docker ID and Log In 

A log-in is not necessary for pulling Docker images from the Hub but
it is necessary for pushing images to dockerhub for sharing. Thus to
store images on Docker hub you need to create an account by visiting
[Docker Hub Web page](https://hub.docker.com/). Dockerhub offers in
general a free account, but it has restrictions. The free account
allows you to share images that you distriuute publically, but it only
allows one private Docker Hub Repository.  In case you need more, you
will need to upgrade to a paid plan.

For the rest of the tutorial we assume that you use the environment
variable DOCKERHUB to indicate yourusername. It is easiset if you set it in
your shell with

```bash
$ export DOCKERHUB=<PUT YOUR DOCKER USERNAME HERE> 
```

## Searching for Docker Images

There are two ways to search for Docker images on Docker Hub:

One way is to use the Docker command line tool. We can open a
terminal and run the *docker search* command. For example, the following
command searches for centOS images:

```bash
docker search centos
```

you will see output similar to:

| NAME            | DESCRIPTION        | STAR | OFFICIAL | AUTOMATED |
|-----------------|--------------------|------|----------|-----------|
| centos          | Official CentOS    | 4130 | [OK]     |           |
| ansible/centos7 | Ansible on Centos7 | 105  |          | [OK]      |

...


Official repositories in dockerhub are public, certified repositories
from vendors and contributors to Docker. They contain Docker images
from vendors like Canonical, Oracle, and Red Hat that you can use as
the basis to build your applications and services. There is one
official repository in this list, the first one, *centos*.

The other way is to search via the *Web Search Box* at the top of the
Docker web page by typing the keyword. The search results can be sorted
by number of stars, number of pulls, and whether it is an official
image. Then for each search result, you can verify the information of
the image by clicking the *details* button to make sure this is the
right image that fits your needs.

## Pulling Images

A particular image (take centos as an example) can be pulled using the
following command:

```bash
$ docker pull centos
```
Tags can be used to specify the image to pull. By default the tag is
latest, therefore the previous command is the same as the following:

```bash
$ docker pull centos:latest
```

You can use a different tag:

```bash
$ docker pull centos:6
```

To check the existing local docker images, run the following command:

```bash
$ docker images
```

The results show:

| REPOSITORY | TAG    | IMAGE ID     | CREATED     | SIZE  |
|------------|--------|--------------|-------------|-------|
| centos     | latest | 26cb1244b171 | 2 weeks ago | 195MB |
| centos     | 6      | 2d194b392dd1 | 2 weeks ago | 195MB |


## Create Repositories

In order to push images to Docker Hub, you need to have a and account
and create a repository.

When you first create a Docker Hub user, you see a *Get started with
Docker Hub* screen, from which you can click directly into *Create
Repository*. You can also use the *Create* menu to *Create Repository*.
When creating a new repository, you can choose to put it in your Docker
ID namespace, or that of any organization that you are in the owners
team [@hid-sp18-405-tutorial-dockerhub-repository].

As an example, we created a repository cloudtechnology with the name
space `$DOCKERHUB`. Hence the full name is `$DOCKERHUB`/cloudtechnology

## Pushing Images

To push an image to the repository created, the following steps can be
followed.

First, log into Docker Hub from the command line by specifying the username

```bash
$ docker login --username=$DOCKERHUB
```
          
Enter the password when prompted. If everything worked you will get
a message similar to:

```bash
Login Succeeded
```

Second, check the image ID using:

```bash
$ docker images
```

the result looks similar to:

| REPOSITORY    | TAG    | IMAGE ID     | CREATED     | SIZE   |
|---------------|--------|--------------|-------------|--------|
| cloudmesh-nlp | latest | 1f26a5f7a1b4 | 10 days ago | 1.79GB |
| centos        | latest | 26cb1244b171 | 2 weeks ago | 195MB  |
| centos        | latest | 2d194b392dd1 | 2 weeks ago | 195MB  |

Here, the the image with ID 1f26a5f7a1b4 is the one to push to Docker Hub.

Third, tag the image

```bash
$ docker tag 1f26a5f7a1b4 $DOCKERHUB/cloudmesh:v1.0
```

Here we have used a version number as a tag. However another good way
of adding a tag is to use a keyword/tag that will help you
understand what this container should be used in conjunction with, or
what it represents.

Fourth, now the list of images will look something like

| REPOSITORY       | TAG      | IMAGE ID     | CREATED  | SIZE   |
|------------------|----------|--------------|----------|--------|
| cloudmesh-nlp    | latest   | 1f26a5f7a1b4 | 10 d ago | 1.79GB |
| $DOCKERHUB/cloudmesh | v1.0 | 1f26a5f7a1b4 | 10 d ago | 1.79GB |
| centos           | latest   | 26cb1244b171 | 2 w ago  |  195MB |
| centos           | latest   | 2d194b392dd1 | 2 w ago  |  195MB |

Fith, push the image to the repository

```bash
$ docker push $DOCKERHUB/cloudmesh
```

It shows something similar to:

```bash
The push refers to repository [docker.io/$DOCKERHUB/cloudmesh]
18f9479cfc2c: Pushed 
e9ddee98220b: Pushed 
...
db584c622b50: Mounted from library/ubuntu 
a94e0d5a7c40: Mounted from library/ubuntu
...
v1.0: digest: sha256:305b0f911077d9d6aab4b447b... size: 3463
```

Sixth, now the image is available on Docker Hub. Everyone can pull it
since it is a public repository by using command:

```bash
$ docker pull USERNAME/cloudmesh
```

Please remember that the USERNAME is the username for the user that
makes this image publically available. If you are the user you will
see the value being the one from $DOCKERHUB, If not you will see here
the username of the user uploading the image
          
## Resources

* The offical
  [Overview of Docker Hub](https://docs.docker.com/docker-hub/#use-official-repositories)
  [@hid-sp18-405-tutorial-dockerhub-overview]
* Information about using docker repositories can be found at
  [Repositories on Docker Hub](https://docs.docker.com/docker-hub/repos/)
  [@hid-sp18-405-tutorial-dockerhub-repository]
* [How to Use DockerHub](https://www.linux.com/blog/learn/intro-to-linux/2018/1/how-use-dockerhub)
  [@hid-sp18-405-tutorial-dockerhub-blog-use]
* [Docker Tutorial Series](https://rominirani.com/docker-tutorial-series-part-4-docker-hub-b51fb545dd8e) [@hid-sp18-405-tutorial-dockerhub-series-part-4]
