NAME=linux
HOME=../..
FINAL=$(HOME)/../pub

include ../makefile.sys

all: epub ppdf authors

epub: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	bookmanager $(NAME).yaml epub
	# cp dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

ppdf: clean
	bookmanager $(NAME).yaml get
	bookmanager $(NAME).yaml md
	cat $(HOME)/bib/*.bib > dest/all.bib
	# sed -i 's/:cloud:/\\faExternalLink/g' dest/book.md
	sed -i 's/:cloud://g' dest/book.md
	sed -i 's/smalltable//g' dest/book.md
	touch ./dest/linux.tex
	cp title-latex.md dest
	cp -r ../../images .
	cp -r images dest
	cp -r ../../chapters/linux/images .
	#cd dest; pandoc -s book.md --toc --number-sections --from markdown-auto_identifiers  -o linux.tex; sy
	# pandoc -s  --bibliography dest/all.bib --citeproc --csl dest/book/ieee-with-url.csl --number-sections --from markdown-auto_identifiers  --listings title-latex.md title.tex dest/book.md  -o dest/linux.tex
	pandoc -s --citeproc --from markdown-auto_identifiers --csl dest/book/ieee-with-url.csl --number-sections --listings --bibliography dest/all.bib  title-latex.md title.tex dest/book.md  -o dest/linux.tex 
	sed -i 's/\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}/\\hrulefill/g' dest/linux.tex
	pdflatex dest/linux.tex 
	# bibtex   dest/linux
	pdflatex dest/linux.tex
	pdflatex dest/linux.tex

	# xelatex --interaction=nonstopmode  dest/linux.tex

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
	rm -f *.aux *.ou *.log

include ../Makefile.bibtex
