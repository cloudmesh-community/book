# Creating the ePubs from source

Although you will never likely to create the epub from source, we have
included this section for our most advanced contributors and those
that update the epub on github.

Please note that you must have at least pandoc version 2.2.3 installed. 
Earlier versions will not work. YOu can check the version of pandoc with 

```bash
$ pandoc --version
```

## OSX Requirements

This is just a guess I for got how to install all of this, it may be
documented in another md file, grep -R for brew

```bash
$ brew install graphviz
# needs version >2.2.3 of pandoc see travis.yml for
# proper install if brew does not work
$ brew install pandoc 
                      
$ brew install pandoc-citeproc
$ brew install node
$ npm install --global mermaid-filter
$ npm install --global pandoc-index
$ git clone https://github.com/tomduck/pandoc-fignos.git
$ cd pandoc-fignos/
$ pip install .
```

## Ubuntu requirements

```bash
$ sudo apt-get update
$ sudo apt-get install graphviz
$ wget https://hackage.haskell.org/package/pandoc-2.2.3.2/pandoc-2.2.3.2.tar.gz
$ git clone https://github.com/jgm/pandoc-citeproc.git
$ wget -qO- https://get.haskellstack.org/ | sh
$ tar xvzf pandoc-2.2.3.2.tar.gz
$ cd pandoc-2.2.3.2
$ stack setup
$ stack install
$ cd ..
$ cd pandoc-citeproc
$ stack setup
$ stack install
$ npm install --global mermaid-filter
$ npm install --global pandoc-index
```

## Creating a book

First you have to check out the book source from github with:

```bash
git clone git@github.com:cloudmesh-community/book.git
```

Books are organize in directories. We currently have

    ./book/cloud/
    ./book/big-data-applications/
    ./book/pi
    ./book/writing
    ./book/222

To compile a book go to the directory and make it. Lets assume you
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

After you have done modifications, you need to do one of two things. In case you add new images you need to use 

```
$ make new
```

otherwise you can just use 

```
$ make 
```

The structure of the books is maintained in chapters.yaml.

In case you add a new chapter, you have to say 

```bash
$ make update
$ make new
$ make view
```

## Publishing the book to github

:warning: This task should only be done by those with direct write
privileges. and never be part of a pull request.

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
`BOOK_gregor`. Make modifications to the outline as you see fit.

Now you can create the book with

```bash
$ cd gregor
$ make update
$ make new
```


$ cd gregor



