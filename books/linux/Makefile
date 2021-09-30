NAME=linux
HOME=../..
FINAL=$(HOME)/../pub

OPTIONS=--filter=pandoc-include --filter=pandoc-xnos


include ../makefile.sys

all: epub ppdf authors

epub: clean version
	mkdir -p dest
	cat $(HOME)/bib/*.bib > dest/all.bib
	bookmanager $(NAME).yaml get
	bookmanager $(NAME).yaml epub
	# cp dest/vonLaszewski-$(NAME).epub $(FINAL)/docs

pdf: clean
	mkdir dest
	bookmanager $(NAME).yaml get
	cat $(HOME)/bib/*.bib > dest/all.bib
	# sed -i 's/:cloud:/\\faExternalLink/g' dest/book.md
	cp title-latex.md dest
	cp -r ../../images .
	cp -r images dest
	cp pandoc-crossref-format.yaml dest
	cp title.tex dest
	cp -r ../../chapters/linux/images .
	touch ./dest/linux.tex
	# -r markdown-auto_identifiers \
	bookmanager $(NAME).yaml md
	sed -i 's/:cloud://g' dest/book.md
	sed -i 's/smalltable//g' dest/book.md
	sed -i 's/!\[Learning Objectives Image\](images\/learning.png)//g' dest/book.md

	# sed -i 's/\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}/\\hrulefill/g' dest/linux.tex


	${PANDOC} -F pandoc-crossref --number-sections --verbose --pdf-engine=pdflatex \
	    -M pandoc-crossref-format.yaml \
	    --bibliography=all.bib --csl=book/ieee-with-url.csl  \
	    -o vonLaszewski-linux.pdf \
	    title-latex.md title.tex book.md






xxx:
	${PANDOC} --toc --toc-depth=6  --number-sections --verbose \
	    --filter pandoc-crossref \
	    -f markdown+emoji \
	    --indented-code-classes=bash,python,yaml \
	    --resource-path=book/REFERENCES:book/INTRODUCTION_TO_LINUX  \
	    --citeproc \
	    --metadata link-citations=true \
	    --bibliography=all.bib --csl=book/ieee-with-url.csl  \
	    -o vonLaszewski-linux.pdf \
	    book/INTRODUCTION_TO_LINUX/HEADER-INTRODUCTION_TO_LINUX.md \
	    book/INTRODUCTION_TO_LINUX/ssh-windows.md \
	    book/REFERENCES/HEADER-REFERENCES.md \
	    book/REFERENCES/empty.md \
	    book/metadata.txt


ooo:

	${PANDOC} -s \
	    --listings \
	    --citeproc \
	    --csl book/ieee-with-url.csl \
	    --number-sections \
	    --bibliography all.bib  \
	    -r markdown-auto_identifiers \
	    title-latex.md title.tex book.md  \
	    -o linux.tex
	${PDFLATEX} linux.tex
	# cd dest; bibtex linux
	${PDFLATEX} linux.tex
	${PDFLATEX} linux.tex

	#gopen dest/linux.pdf &

	# xelatex --interaction=nonstopmode  dest/linux.tex

epub-pdf:
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
	rm -f *.aux *.ou *.log *.toc

include ../Makefile.bibtex
