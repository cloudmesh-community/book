NAME=big-data-applications
HOME=../..
WEEK=e534
FINAL=$(HOME)/../pub

include ../makefile.sys

all: epub pdf

epub: clean version authors
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

pdf:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(NAME).epub \
	  $(FINAL)/docs/vonLaszewski-$(NAME).pdf

ci: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	ebook-convert \
	  dest/vonLaszewski-$(NAME).epub \
	  dest/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp $(HOME)/bib/*.bib dest

version:
	TZ=":US/Eastern"; date > $(HOME)/chapters/version.md

view:
	killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME).epub

authors:
	$(HOME)/bin/authors.py > $(HOME)/chapters/authors.md

week: epub-week pdf-week
	-echo done

epub-week: clean version authors
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(WEEK).yaml get
	mv dest/vonLaszewski-$(WEEK).epub $(FINAL)/docs

pdf-week:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(WEEK).epub \
          $(FINAL)/docs/vonLaszewski-$(WEEK).pdf

w:
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(WEEK).epub

g: week w
	-echo done

clean:

	rm -rf dest
