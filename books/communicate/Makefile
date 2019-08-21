NAME=communicate
HOME=../..

all: epub pdf

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

clean:

	rm -rf dest
