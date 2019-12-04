NAME=e516
HOME=../..
FINAL=$(HOME)/../pub
THIS=.


include ../makefile.sys

all: syllabus epub pdf authors

update:
	cd ../../..; cloudmesh-installer git pull 516
	cd ../../..; cloudmesh-installer git pull storage


proceedings: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-proceedings.yaml get
	mv dest/vonLaszewski-$(NAME)-proceedings.epub $(FINAL)/docs
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-proceedings.epub

draft: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-draft.yaml get
	mv dest/vonLaszewski-$(NAME)-draft.epub $(FINAL)/docs
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-draft.epub

syllabus: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-syllabus.yaml get
	mv dest/vonLaszewski-$(NAME)-syllabus.epub $(FINAL)/docs
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-syllabus.epub
	#killall Books
	#$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-syllabus.epub

epub: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

dest: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	ebook-convert \
	  dest/vonLaszewski-$(NAME).epub \
	  dest/vonLaszewski-$(NAME).pdf

pdf:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(NAME).epub \
	  $(FINAL)/docs/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp $(HOME)/bib/*.bib dest

version:
	TZ=":US/Eastern"; date > $(HOME)/chapters/version.md

view:
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME).epub

authors:
	$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

fonts:
	#mkdir -p dest/book/
	#-cp -r ../../../bookmanager/bookmanager/template/epub/fonts dest/book/fonts
	echo "ignoring font embedding"

clean:
	rm -rf dest

include ../Makefile.bibtex
