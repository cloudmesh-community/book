# Publications for classes


Link |  Class | Description
|------ | --- | -------------
[<img src="cloud/cover/cover.jpg" width="100px">](vonLaszewski-cloud.epub?raw=true)| E516, E416, B649 | Evolving Lecture notes for class E516, E416, B649
[<img src="big-data-applications/cover/cover.jpg" width="100px">](vonLaszewski-bigdata-application.epub?raw=true)| e534, I523, I423 | Evolving Lecture notes for class e534, I523, I423
[<img src="writing-1/cover/cover.jpg" width="100px">](vonLaszewski-writing-1.epub?raw=true)| all | Scientific Writing I for all classes
[<img src="latex/cover-latex.png" width="100px">](http://cyberaide.org/papers/vonLaszewski-latex.pdf)| all | Scientific Writing II for all classes
[<img src="communicate/cover/cover.jpg" width="100px">](vonLaszewski-communicate.epub?raw=true)| all | Class Communication Services (update version can be found in the Lecture notes for the class)
![Bibliographies I](bib) | all | BibTeX files directory I


## Files

### Build files and dirs

* README.md - this readme
* bin - some convenient scripts to manipulate the content
* template - dir with the templates in it including fonts


### Bib

* bib - bibliography goes here.

### Chapters

* chapters - all chapters from which we can chose

### Books

* class - class handbook (finished)
* cluster - cluster handbook (just a collection)
* pi (just a collection)


## Creating the Document

This document is for the ebooks only

The documentation is very easy to create as it relies on pandoc. To
install it you can do the following:

Windows 10, Debian, Ubuntu, and derivatives use package published at

* <https://github.com/jgm/pandoc/releases/latest>

Mac OSX use homebrew and node

```bash
$ brew install node.
$ brew install graphviz
$ npm install --global mermaid-filter
$ brew install pandoc
$ brew install pandoc-citeproc
```

Once you have installed pandoc you can create the book with our simple
`Makefile` contained in the source directory. Simply clone the source
and call make in the source dir

```bash
$ mkdir -p ~/github/cloudmesh-community
$ cd ~/github/cloudmesh-community
$ git clone https://github.com/cloudmesh-community/book.git
$ cd book
$ pip install -r requirements
```

Then chose the book you like to compile. Let us assume the book is in
the cloud directory. Than you can create it with

```
$ cd cloud
$ make images
$ make
```

In case you need to use latex you need to download the full
version. For OSX this is

* <http://www.tug.org/mactex/mactex-download.html>

The Raspberry PI is to small to run LaTeX, so use it to log into a
remot resource and run it there.


Go to a dir (example)

```bash
$ cd pi
```

To look at the book, open the text with your favorite e-book
reader. On OSX you can say

```bash
$ open *.epub
```

or simply

```bash
$ make view
```


