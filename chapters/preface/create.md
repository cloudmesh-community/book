# Creating the ePubs from source

Although you will never likely to create the epub from source, we have
included this section for our most advanced contributors and those
that update the epub on github.

## OSX Requirements

This is just a guess I for got how to install all of this, it may be
documented in another md file, grep -R for brew

```
$ brew install graphviz
$ brew install pandoc # needs version >2.2.3 of pandoc see travis for
                      # proper install if brew does not work
$ brew install pandoc-citeproc
$ npm install --global mermaid-filte                      
```

## Ubuntu requirements

```
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
```

## Creating a book

Books are organize in directories. We currently have

```
./book/cloud/
./book/big-data-applications/
```

To compile a book go to the directory and make it. Lets assume you
like to create the cloud book for 516

```
$ git clone https://github.com/cloudmesh-community/book.git
$ cd cloud
$ make images
$ make
```

To view it you say

```
make view
```

## Publishing the book to github

:warning: This task should only be done by those with direct write
privileges. and never be part of a pull request.

To publish the book say

```
$ make publish
```

## Creating Drafts that are not yet published

Developers of the manual can modify the `Makefile` and locate the
variable `DRAFT=` to add additional sections and chapters they work
on, but should not yet been distributed with the main publication.
Simply add them to the list and say

```
$ make draft
$ make view
```

to create the draft sections only and view them. 

To conveniently call them in a lazy fashion in a terminal you could
use the following two aliases.

```
alias m='make; make view'
alias d='make draft; make view'
```

This allows you to typ `m` for the main volume and `q` for the draft.
Please note that all artifacts are written into the dest folder.
