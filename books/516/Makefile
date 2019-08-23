NAME=e516
HOME=../..

all: epub pdf authors

draft: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-draft.yaml get
	mv dest/vonLaszewski-$(NAME)-draft.epub $(HOME)/docs
	killall Books
	open $(HOME)/docs/vonLaszewski-$(NAME)-draft.epub

epub: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub $(HOME)/docs

pdf:
	ebook-convert \
	  $(HOME)/docs/vonLaszewski-$(NAME).epub \
	  $(HOME)/docs/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp $(HOME)/bib/*.bib dest

version:
	TZ=":US/Eastern"; date > $(HOME)/chapters/version.md

view:
	killall Books
	open $(HOME)/docs/vonLaszewski-$(NAME).epub

authors:
	$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

clean:

	rm -rf dest

include ../Makefile.bibtex
