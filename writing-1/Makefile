
FILENAME=vonLaszewski-writing-1

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

CHAPTER_DOC=\
 chapters/doc/preface.md\
 chapters/preface/notation.md\
 chapters/doc/SECTION.md\
 chapters/doc/plagiarism.md\
 chapters/doc/emacs.md\
 chapters/doc/markdown.md\
 chapters/doc/report.md\
 chapters/doc/type.md

CHAPTER_CLASS=\
 chapters/class/SECTION.md\
 chapters/class/fall2018.md\
 chapters/class/organization.md\
 chapters/class/syllabus.md\
 chapters/class/policy.md\
 chapters/class/assignments.md\
 chapters/class/grading.md\
 chapters/class/project-ideas.md

CHAPTER_SERVICES=\
  chapters/doc/piazza.md\
 chapters/preface/git.md

BOOK_CLASS=\
  $(CHAPTER_PREFIX)\
  $(CHAPTER_CLASS) \
  $(CHAPTER_DOC)\
  $(CHAPTER_SERVICES) \
  $(CHAPTER_REFERENCES)

######################################################################
# END BOOK CLASS
######################################################################


######################################################################
# chameleon
######################################################################

CHAPTER_PI=\
 chapters/SECTION-PREFACE.md\
    chapters/pi/preface.md\
    chapters/preface/notation.md\
    chapters/preface/contributors.md\
    chapters/preface/contributing.md\
    chapters/preface/git.md\
    chapters/preface/exercises.md\

CHAPTER_REFERNCES=\
 chapters/references.md


INDEX=\
 $(CHAPTER_DOC)


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
	../bin/section.py 1 "[Preface]{.part}" > dest/chapters/SECTION-PREFACE.md
	../bin/section.py 1 "Scientifc Writing" > dest/chapters/doc/SECTION.md
	../bin/section.py 1 "Classes" > dest/chapters/class/SECTION.md
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

