# Bookmanager in Container

You may have noticed that the book is created as ePub by a tool called
bokmanager. Bookmanager is available natively on many systems including
macOS, Linux, and Windows. However, it does require the installation of
tools such as pandoc, pandoc-citref and if bibliography checking is
required biber.

Bookmanager is available on PyPI, and the source is managed in GitHub.

* <https://github.com/cyberaide/bookmanager>
* <https://pypi.org/project/cyberaide-bookmanager/>

There you can also find the installation instructions and a user manual.

As the install by some of these tools may be too complicated to the
novice developer, and user, it is possible to create a container that
includes all needed tools to start bookmanager via docker easily.

## Creaating the Container from Scratch

For this to work, we have developed a Dockerfile that is not only used
to run bookmanager, but also to explain to you how this Dockerfile works
so you can in future develop your own Dockerfiles to create your own
containers.

Please take a look at the Dockerfile:

* <https://github.com/cyberaide/bookmanager/blob/master/Dockerfile>

A good summary and explanation of the commands used are provided in our
Cloud Computing book. You can also look directly at the docker Web page
and for example, look at best practices on how to develop Docker files:

* <https://docs.docker.com/develop/develop-images/dockerfile_best-practices/> 

Here is how our Dockerfile is structured:

1. We start the Dockerfile with the FROM instruction from which we get
the base image. 2. We add an environment variable such as
`DEBIAN_FRONTEND noninteractive` so we do not get asked questions during
the installation of some packages. 3. Next, we add packages that we need to
install the packages in our image. We have provided here a significant
number. Not all the packages are needed for bookmanager. It is best to
just provide the minimal number. However, as we use bookmanager in
different activities, we added some packages such as `emacs-nox` so you
can use it for editing. To make the container smaller, you can disable
the installation of such packages, by removing that line.

As we want to showcase you also how to install software from source, we
have added the installation for pandoc and pandoc-crossref. You will
notice that we use WORKDIR to change into a directory and conduct the
following RUN commands there.

In the same way, we do install bookmanager from source, so you get the
the newest version at the time of the creation.

2. To create this image, we have provided a simple Makefile. That you can
use as follows

```
git clone https://github.com/cyberaide/bookmanager.git
cd bookmanager
make image
```

:o2: those on windows, could try if

```
nmake image works
```

If not look at the image target in the Makefile and replicate similar
commands on your commandline.
 

3. Next, use the bookmanager to compile the proceedings for this year:


```
mkdir -p cm/pub/docs
cd cm
git clone https://github.com/cloudmesh-community/book.git 
git clone https://github.com/cyberaide/bookmanager.git
cd bookmanager
make image
make cm
```

The `make cm` command logs you into the container interactively so you
can experiment on how to work with bookmanager. Remember that this also mounts your local file system, and you must be careful with what you delete.

Again, if you do not have `make` look at the cm and image tag and execute
commands similar to it. Maybe nmake works, please let us know.

In the container, you need to do the following:

```
/cm# cd book/books/516-sp20/

/cm/book/books/516-sp20# ls -1

    Makefile
    dest
    e516-datacenter.yaml
    e516-draft.yaml
    e516-sp20-proceedings.yaml
    e516-sp20-syllabus.yaml
    e516-sp20.yaml
    e516.yaml
    reports.md

/cm/book/books/516-sp20# time make proceedings
```
 

The output is in /cm/pub/docs

Here the time comparison on osx native vs container

Native:

```
real 0m34.948s
user 0m13.971s
sys 0m2.680s
```

Container with mount of cm in host system e.g., osx:

```
real 0m48.782s
user 0m16.872s
sys 0m2.428s
```

Container with locally checked out books folder
 
```
real 0m40.372s
user 0m13.606s
sys 0m1.670s
```

## Exercises:

E.container.bookmanager.1: 

> Create the proceedings from this on your computer. Note that your
computer using the docker container.

> The output is written into the pub/docs directory.


E.container.bookmanager.2:

> Remove all the sections that you do not need in the 
> `e516-sp20-proceedings.yaml` file by putting a # at the beginning 
> of the line. Also, exclude some of the unneeded subsections
> Rerun the bookmanager process and verify you see your own chapter.

> The output is written into the pub/docs directory.

E.container.bookmanager.3: 

Create a cloudmesh command `bookmanagerd` for windows that
downloads and installs bookmanager as a container for you. Everyone can
collaborate with each other. Develop it for your OS

```
bookmanagerd install 
```

A good example of how we did this in another project is provided in
`cloudmesh-cmsd`.

