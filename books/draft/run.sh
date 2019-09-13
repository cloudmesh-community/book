#! /usr/bin/bash
HOME=../..
NAME=draft

rm -rf dest

TZ=":US/Eastern"; date > $(HOME)/chapters/version.md
$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

mkdir -p dest
cat $(HOME)/bib/*.bib > dest/all.bib
bookmanager $(NAME).yaml get

#ebook-convert \
#$(HOME)/docs/vonLaszewski-$(NAME).epub \
#$(HOME)/docs/vonLaszewski-$(NAME).pdf

