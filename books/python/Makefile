NAME=python
HOME=../..
FINAL=$(HOME)/../pub

include ../makefile.sys

all: epub pdf authors

epub: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	bookmanager $(NAME).yaml epub
	mv dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

p: epub
	bookmanager $(NAME).yaml pdf
	cp dest/vonLaszewski-$(NAME).pdf $(FINAL)/docs


draft: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-draft.yaml get
	$(OPEN_EPUB) dest/vonLaszewski-$(NAME)-draft.epub


pdf:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(NAME).epub \
	  $(FINAL)/docs/vonLaszewski-$(NAME).pdf



dest: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	ebook-convert \
	  dest/vonLaszewski-$(NAME).epub \
	  dest/vonLaszewski-$(NAME).pdf

publish:
	cd $(FINAL); git commit -m "update python book" \
	  docs/vonLaszewski-$(NAME).epub \
	  docs/vonLaszewski-$(NAME).pdf; git push
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

clean:

	rm -rf dest

include ../Makefile.bibtex
