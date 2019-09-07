NAME=big-data-applications
HOME=../..
WEEK=e534

include ../makefile.sys

all: epub pdf

epub: clean version authors
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub $(HOME)/docs

pdf:
	ebook-convert --markdown-extensions \
	  $(HOME)/docs/vonLaszewski-$(NAME).epub \
	  $(HOME)/docs/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp $(HOME)/bib/*.bib dest

version:
	TZ=":US/Eastern"; date > $(HOME)/chapters/version.md

view:
	killall Books
	$(OPEN_EPUB) $(HOME)/docs/vonLaszewski-$(NAME).epub

authors:
	$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

week: epub-week pdf-week
	-echo done

epub-week: clean version authors
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(WEEK).yaml get
	mv dest/vonLaszewski-$(WEEK).epub $(HOME)/docs

pdf-week:
	ebook-convert \
	  $(HOME)/docs/vonLaszewski-$(WEEK).epub \
          $(HOME)/docs/vonLaszewski-$(WEEK).pdf

w:
	-killall Books
	$(OPEN_EPUB) $(HOME)/docs/vonLaszewski-$(WEEK).epub

g: week w
	-echo done

clean:

	rm -rf dest
