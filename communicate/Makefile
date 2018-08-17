
FILENAME=vonLaszewski-communicate

OS=$(shell ../bin/sysinfo.py)
DOCKER=$(shell ../bin/isdocker.py)

MARKUPALL=../bin/markup-all.py

#
# removing mermaid filter from linux as we do not yet know how to use it in docker
#
ifeq ($(OS), osx)
OPEN_EPUB=open
MERMAID=-F mermaid-filter
COPY=rsync
endif
ifeq ($(OS), linux)
OPEN_EPUB=xdg-open
MERMAID=-F mermaid-filter
COPY=rsync
endif
ifeq ($(OS), windows)
OPEN_EPUB=open
MERMAID=-F mermaid-filter.cmd
COPY=cp
endif
ifeq ($(DOCKER), True)
MERMAID=
endif

######################################################################
# BEGIN BOOK CLASS
######################################################################

CHAPTER_PREFIX=\
 chapters/preface/update.md\
 chapters/preface/preface.md\
 chapters/preface/contributors.md\
 ./README.md\
# chapters/todo.md\
# todo.md\
# chapters/preface/issues.md

CHAPTER_GIT=\
	chapters/SECTION-PREFACE.md\
  chapters/preface/notation.md\
  chapters/doc/communicate.md\
	chapters/SECTION-COMMUNICATION.md\
  chapters/doc/piazza.md\
  chapters/git/github.md\
  chapters/preface/git.md\
  chapters/SECTION-PPT.md\
  chapters/doc/ppt.md\
  chapters/SECTIONN-REFERENCES.md

######################################################################
# END BOOK CLASS
######################################################################



INDEX=\
 $(CHAPTER_GIT)


MARKDOWN-OPTIONS=$(MERMAID) -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".:chapters:chapters/prg:chapters/iot:chapters/container:chapters/os:chapters/mapreduce:chapters/cloud/chameleon:chapters/doc:chapters/preface:chapters/class:chapters/case"

#	pandoc ./chapters/prg/python.md -o dest/chapters/prg/python.md --base-header-level=2

all: prepare epub 
	echo done


prepare: dot refernces todo
	$(COPY) metadata.txt dest
	$(COPY) -r cover dest
	$(COPY) -r ../template dest
	$(COPY) -r ../template/fonts dest
	$(COPY) -r ../chapters dest	
	$(MARKUPALL)
	../bin/section.py 1 "Preface" > dest/chapters/SECTION-PREFACE.md
	../bin/section.py 1 "References" > dest/chapters/SECTIONN-REFERENCES.md
	../bin/section.py 1 "Scientifc Writing" > dest/chapters/doc/SECTION.md
	../bin/section.py 1 "Classes" > dest/chapters/class/SECTION.md
	../bin/section.py 1 "Communication Services" > dest/chapters/SECTION-COMMUNICATION.md
	../bin/section.py 1 "Powerpoint" > dest/chapters/SECTION-PPT.md
	# ../bin/section.py 1 "Git" > dest/chapters/SECTION-GIT.md
	$(COPY) preface.md dest/chapters/doc/preface.md

epub:
	echo $(INDEX)
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(INDEX) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(INDEX) > all.md
endif
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md

refernces:
	mkdir -p dest
	cat ../bib/*.bib > dest/references.bib

html:
	cd dest; pandoc $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).html metadata.txt $(INDEX)

pdf:
	cd dest; pandoc -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' -V geometry:margin=1in --bibliography references.bib --csl=../../template/ieee.csl -o $(FILENAME).pdf metadata.txt $(INDEX)

tex:
	cd dest; pandoc -f markdown+smart -f markdown+emoji --toc --epub-embed-font='fonts/*.ttf' --bibliography references.bib --csl=../../template/ieee.csl -o $(FILENAME).tex metadata.txt $(INDEX)
	cd dest; pdflatex content.tex


clean:
	rm -rf $(FILENAME).*
	rm -rf dest

list:
	@echo "----"
	@find . -name "*.md"
	@echo "----"
	@echo "Markdown Files": `find . -name "*.md" | wc -l`
	@echo "----"
	@find . -name "*.md"	| sed -e 's/^/ /' | sed 's/$$/\\/'

view:
	$(OPEN_EPUB) dest/$(FILENAME).epub

todo:
	../bin/todo.py > dest/todo.md
	cat dest/todo.md

issues:
	python ../bin/issues.py > /tmp/issues.tex
	pandoc /tmp/issues.tex -o chapters/preface/issues.md
	bin/header.sh chapters/preface/issues.md 3
	head -1 chapters/preface/issues.md > /tmp/issues.md
	echo "<div class=\"smalltable\">" >> /tmp/issues.md
	tail -n +2 chapters/preface/issues.md >> /tmp/issues.md
	echo  >> /tmp/issues.md
	echo "</div>" >> /tmp/issues.md
	echo  >> /tmp/issues.md
	cp /tmp/issues.md chapters/preface/issues.md

dot:
	dot -Tpng ../chapters/class/graph-all.dot -o ../chapters/class/images/graph-all.png
	dot -Tpng ../chapters/class/graph-e222.dot -o ../chapters/class/images/graph-e222.png
	dot -Tpng ../chapters/class/graph-i523.dot -o ../chapters/class/images/graph-i523.png
	dot -Tpng ../chapters/class/graph-i524.dot -o ../chapters/class/images/graph-i524.png
	dot -Tpng ../chapters/class/graph-e516.dot -o ../chapters/class/images/graph-e516.png

publish: epub
	cp dest/$(FILENAME).epub ..
	git add ../$(FILENAME).epub
	git commit -m "update epub" ../$(FILENAME).epub
	git push

