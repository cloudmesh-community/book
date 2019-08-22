# Creating the ePubs from source

In case you wish to create the ePub from source, we have included this
section.

However the easiest way is to use our docker container as described in
@sec:docker-create-book.

## Docker {#sec:docker-create-book}

We recommend the docker creation method for

* Ubuntu
* Windows 10
* macOSX

### Using OSX

The easiest way to create a system that can compile the book on macOS,
is to use a docker container. To do so you will need to first install
docker on macOS while following the simple instructions at

* <https://docs.docker.com/docker-for-mac/install/>

Once you have docker installed, you can follow the instructions in
@sec:docker-create-book.

### Using the Docker Image

In case you have docker installed on your computer you can create
ePubs with our docker image. To create that image by hand, we have
included a simple makefile. Alternatively you can use our image from
dockerhub if you like, it is based on ubuntu and uses our
[Dockerfile](https://github.com/cloudmesh-community/book/blob/master/Dockerfile).

First, you need to download the repository:

```bash
$ git clone https://github.com/cloudmesh-community/book.git
cd book
```

To open an interactive shell into the image you say

```bash
$ make shell
```

Now you can skip to @sec:create-book and compile the book just as
documented there.

Please note that we have not integrated pandoc-mermaid and
pandoc-index at this time in our docker image. If you like to
contribute them, please try it and make a pull request once you got
them to work.

In case you want to create or recreate the image from our
[Dockerfile](https://github.com/cloudmesh-community/book/blob/master/Dockerfile)
(which is likely not necessary, you can use the command

```bash
$ make image
```

## Using the Native System

In case you like to use your native environment (which is typically
faster than the container) you need to make sure you have an up to date
environment.

Please note, that you must have at least Pandoc version 2.5 installed as
earlier versions will not work. We recommend that you use Python version
3.7.4 to run the scripts needed to assamble the document. However
eralier version of Python 3 may also work, but are not tested. You can
check the versions with

```bash
$ pandoc --version
$ python --version
```


## Using Vagrant {#sec:book-create-vagrant}

In case you have installed vagrant on your computer which is available
for macOS, Linux, and Windows 10, you can use our vagrant file to
start up a virtual machine that has all software installed to create
the ePub.

First, you need to download the repository:

```bash
$ git clone https://github.com/cloudmesh-community/book.git
$ cd book
```

Next you have to create the virtual machine with

```bash
$ vagrant up
```

You can loginto the VM with

```bash
$ vagrant ssh
```

The book folder will be mounted in the VM and you can can follow the
instructions in @sec:docker-create-book.



## Creating a Book {#sec:create-book}

Oncw you have decided for one of the methods, you can create a book.

To create a book, you have to first check out the book source from
github with if you have not yet done so (for example if you were to
use the docker container method):

```bash
git clone git@github.com:cloudmesh-community/book.git
```

Books are organized in directories. We currently have created the
following directories

    ./book/cloud/
    ./book/big-data-applications/
    ./book/pi
    ./book/writing
    ./book/222
    ./book/516

To compile a book go to the directory and make it. Let us assume you
like to create the cloud book for cloud

```bash
$ git clone https://github.com/cloudmesh-community/book.git
$ cd cloud
$ make new
```

To view it you say

```bash
$ make view
```

After you have done modifications, you need to do one of two
things. In case you add new images you need to use

```
$ make new
```

otherwise you can just use

```
$ make
```

The structure of the books is maintained in the yaml file
`chapters.yaml`. You can add this chapter to the yaml file, but
discuss this first with Gregor. In case you add a new chapter, you
have to say

```bash
$ make clean
$ make update
$ make
$ make view
```

## Publishing the Book to GitHub

> ![Warning](images/warning.png) *This task is only to be done by *Gregor von Laszewski*. You
>           will not have to do this step.*

To publish the book say

```bash
$ make publish
```


## Creating Unpublished Drafts

Developers of the manual can modify the `Makefile` and locate the
variable `DRAFT=` to add additional sections and chapters they work
on, but should not yet been distributed with the main publication.
Simply add them to the list and say

```bash
$ make draft
$ make view
```

to create the draft sections only and view them.

To conveniently call them in a lazy fashion in a terminal you could
use the following two aliases.

```bash
alias m='make; make view'
alias d='make draft; make view'
```

This allows you to typ `m` for the main volume and `q` for the draft.
Please note that all artifacts are written into the dest folder.


## Creating a New Book

Let us assume you like to create a new book. The easiest way to start is
to copy from an existing book. However, make sure not to copy old files
in dest. Let us assume you like to call the book gregor and you coppy
from the 222 directory.

You have to do the following

```bash
$ cd 222
$ make clean
$ cd ..
$ cp -r 222 gregor
```

Now edit the file chapters.yaml and copy the section with `BOOK_222=` to
`BOOK_gregor=`. Make modifications to the outline as you see fit.

Now you can create the book with

```bash
$ cd gregor
$ make update
$ make new
```

## Managing Images

In case you have added images to the book, they must be on the same
level as your contribution, but in a directory called images. E.g.

```
./chapters/cloud/mydocument.md
./chapters/cloud/images/myimage.md
```

In the document the image is than refered to as

```
![My imaage caption](images/myimage.md){#fig:cloud-myimage}
```

The label `#fig:cloud-myimage` must be unique in all of the documents.
While adding the directory cloud before the image name this is the case
in our example.



