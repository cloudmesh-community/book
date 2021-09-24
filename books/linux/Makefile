NAME=linux
HOME=../..
FINAL=$(HOME)/../pub

include ../makefile.sys

all: epub ppdf authors

epub: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	# mv dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

ppdf: epub
	bookmanager $(NAME).yaml md
	cd dest; sed -i 's/:cloud:/cloud/g' book.md
	cd dest; sed -i 's/smalltable//g' book.md
	touch ./dest/linux.tex
	cp title-latex.md dest
	#cd dest; pandoc -s book.md --toc --number-sections --from markdown-auto_identifiers  -o linux.tex; xelatex --interaction=nonstopmode  linux.tex
	cd dest; pandoc -s --template ../../../latex/eisvogel --toc --number-sections --from markdown-auto_identifiers  title-latex.md book.md  -o linux.tex
	cd dest; xelatex --interaction=nonstopmode  linux.tex

pdf:
	ebook-convert \
	  $(FINAL)/docs/vonLaszewski-$(NAME).epub \
	  $(FINAL)/docs/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp $(HOME)/bib/*.bib dest

dest: clean fonts version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	ebook-convert \
	  dest/vonLaszewski-$(NAME).epub \
	  dest/vonLaszewski-$(NAME).pdf

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
