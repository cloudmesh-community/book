# Creating the ePubs from source

In case you wish to create the ePub from source, we have included this
section.

The creation of the book is based on
[bookmanager](https://pypi.org/project/cyberaide-bookmanager/).

The easiest way is to use our docker container as described in
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

The container image includes 

* [Python 3.7.4](https://python.org)
* [Pandoc 2.7.3](https://pandoc.org/)
* [pandoc-citeproc](https://github.com/jgm/pandoc-citeproc/blob/master/man/pandoc-citeproc.1.md)

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
earlier versions will not work. We recommend that you use pandoc version
2.7.3 or newer. We recommend that you use Python version 3.7.4 to run
the scripts needed to assamble the document. However eralier version of
Python 3 may also work, but are not tested. You can check the versions
with

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

Once you have decided for one of the methods, you can create a book.

To create a book, you have to first check out the book source from
github with if you have not yet done so (for example if you were to
use the docker container method):

```bash
git clone git@github.com:cloudmesh-community/book.git
```

Books are organized in directories. We currently have created the
following directories

    ./book/books/cloud/
    ./book/books/big-data-applications/
    ./book/books/pi
    ./book/books/writing
    ./book/books/222
    ./book/books/516

To compile a book go to the directory and make it. Let us assume you
like to create the cloud book for cloud

```bash
$ git clone https://github.com/cloudmesh-community/book.git
$ cd book/books/cloud
$ make
```

To view it you say

```bash
$ make view
```

After you have done modifications, you need to do one of two
things. In case you add new images you need to use

```
$ make
```

The structure of the books is maintained in the yaml file in the
directory where you execute the make in. It typically has the form
`NAMEOFDIR.yaml`. Simply do an ls in the directory to see its anme or
inspect the Makefile. You can add new chapters to the yaml file, but
discuss this first with Gregor. TYpicallly, we have for incomming or
draft chapters a special `draft` book to make sure the integration is
done smoothly first in the draft.


## Publishing the Book to GitHub

> ![Warning](images/warning.png) *This task is only to be done by *Gregor von Laszewski*. You
>           will not have to do this step.*

To publish the book say

```bash
$ make publish
```

## Creating  Drafts

Drafts are maintained in the draft folder

```bash
$ cd book/books/cloud
$ make
```

We recommend that you use the following tools to clean up your files.

* [mdl](https://github.com/markdownlint/markdownlint) - markdownlint to cleanup your markdown
* [biber](http://biblatex-biber.sourceforge.net/) - to cleanup your bibtex file

We still only use bibtex and not biblatex, but can use biber for doing
some verification. Once you have installed them, you can verify your documents with.

```bash
mdl filename.md
biber -V -tool filename.bib
```

Please remember that we have many thausends of refernces in our bib
folder, so before you add a duplicate entry, please check in that
forlder. An easy way to do this is to use jabref loading the bibfiles.


## Creating a New Book

Let us assume you like to create a new book. The easiest way to start is
to copy from an existing book. However, make sure not to copy old files
in dest. Let us assume you like to call the book gregor and you coppy
from the python directory.

You have to do the following

```bash
$ cd book/books/python
$ make clean
$ cd ..
$ cp -r python gregor
$ cd ../gregor
$ mv python.yaml gregor.yaml
```

edit the Makefile and replace the NAME with gregor. make modifications
to the table of contents in that yaml file and then compile with 

```bash
$ make
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

## Managing Refernces

Referncesa are all managed in bibtex format while using pandoc-crosreff
to cite them. There are many examples of the different entry types
available in the bib directory. DO not duplicte entries, instead reuse
them. Make sure you have a unique and meaningful label. 

