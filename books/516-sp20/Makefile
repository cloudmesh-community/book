NAME=e516-sp20
HOME=../..
FINAL=$(HOME)/../pub
THIS=.
export FINAL
export NAME

include ../makefile.sys

all: authors syllabus epub pdf
	-killall Books
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME).epub

#publish:
#	$(shell cd $(FINAL); git commit -m "update 516" docs/vonLaszewski-$(NAME).epub)
#	$(shell cd $(FINAL); git commit -m "update 516" docs/vonLaszewski-$(NAME).pdf)
#	$(shell cd $(FINAL); git push)
#	$(shell cd $(FINAL); echo $(NAME).epub)
#	$(shell cd $(FINAL); echo $(NAME).pdf)

update:
	cd ../../..; cloudmesh-installer git pull 516
	cd ../../..; cloudmesh-installer git pull storage

killepub:
ifeq ($(OS), osx)
	-killall Books
endif

p:
	make -f Makefile proceedings
	make -f Makefile viewp

proceedings: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-proceedings.yaml get
	mv dest/vonLaszewski-$(NAME)-proceedings.epub $(FINAL)/docs

draft: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-draft.yaml get
	mv dest/vonLaszewski-$(NAME)-draft.epub $(FINAL)/docs
	make -f Makefile killeub
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-draft.epub

syllabus: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME)-syllabus.yaml get
	mv dest/vonLaszewski-$(NAME)-syllabus.epub $(FINAL)/docs/vonLaszewski-$(NAME)-syllabus.epub
	#make -f Makefile killeub

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


viewp:
	@make -f Makefile killeub | true
	$(OPEN_EPUB) $(FINAL)/docs/vonLaszewski-$(NAME)-proceedings.epub

view:
	make -f Makefile killeub
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
