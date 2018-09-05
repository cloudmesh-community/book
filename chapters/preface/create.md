# Createing the epubs from source :o:

THis section explains how to create the epub from source.

## OSX Requirements

This is just a guess I for got how to install all of this, it may be documented in another md file, grep -R for brew

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

Books are organize in directoried. We currently have

```
cloud/
big-data-applications/
```

To compile a book go to the directory and make it. Lets assume you like to creat ethe cloud book for 516

```
$ cd cloud
$ make
```

To view it you say

```
make view
```

## Publishing the book to github

:warning: This task should only be done by those with direct write priviledges. and never be part of a pull request.

To publish the buuk say

```
$ make publish
```
