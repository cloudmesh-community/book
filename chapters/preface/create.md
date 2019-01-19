# Creating the ePubs from source

Although you will never likely to create the epub from source, we have
included this section for our most advanced contributors and those
that update the epub on github.

Please note that you must have at least Pandoc version 2.2.3
installed.  You will also need Python version 3.7.1 to run the scripts
needed to assamble the document.  Earlier versions will not work. You
can check the versions with

```bash
$ pandoc --version
$ python --version
```

However the easiest way is to use our docker container.

## Ubuntu requirements :o:

In case you use containers in ubuntu we recommend that you use the
docker container to compile the book as discussed in
@sec:docker-create-book.

:o: The next is yet untested

In case you like to use the ubuntu system directly, you can download a
script that installs the needed software.

You will first have to download the script with

```bash
$ wget https://raw.githubusercontent.com/cloudmesh-community/book/master/install-ubuntu.sh
```

Than you can run this [script](https://raw.githubusercontent.com/cloudmesh-community/book/master/install-ubuntu.sh) with

```bash
$ sh install-ubuntu.sh
```

:warning: please note that we have not yet tested this and are looking
for feedback and improvements to the `install-ubuntu.sh` script.

Once the software is installed you can scip to @sec:create-book

## OSX Requirements

The easiest way to create a system that can compile the book on macOS,
is to use a docker container. To do so you will need to first install
docker on macOS while following the simple instructions at

* <https://docs.docker.com/docker-for-mac/install/>

Once you have docker installed, you can follow the instructions in
@sec:docker-create-book.

## Docker {#sec:docker-create-book}

In case you have docker installed on your computer you can create
epubs with our docker image. To create that image by hand, we have
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

## Creating a book {#sec:create-book}

To create a book, you hae to first check out the book source from
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

To compile a book go to the directory and make it. Let us assume you
like to create the cloud book for 516

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

## Publishing the book to github

:warning: This task should only be done by with direct write
privileges. and never be part of a pull request. Please discuss with
*Gregor von Laszewski* the details of your update first. Typically
*Gregor* is the one who publishes it.

To publish the book say

```bash
$ make publish
```

## Creating Drafts that are not yet published

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


## Creating a new book

Let us assume you like to create a new book. The easiest way to start is to copy from an existing book. However, make sure not to copy old files in dest. Let us assume you like to call the book gregor and you coppy from the 222 directory.

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



