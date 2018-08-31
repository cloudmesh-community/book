
FILENAME=vonLaszewski-cloud

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
# i516
######################################################################

#  chapters/iaas/azure/signup.md\
  chapters/iaas/watson/signup.md\
 chapters/iaas/aws/signup.md\

CHAPTER_516=\
  chapters/version.md\
  chapters/preface/notation.md\
  chapters/class/organization-516.md\
  chapters/cloud/gregor.md\
  chapters/class/e516-engineering-cloud-computing.md\
  chapters/class/e516-summary.md\
  chapters/class/volumes.md\
  chapters/class/e516-definition.md\
  chapters/cloud/datacenter.md\
  chapters/SECTION-DEVTOOLS.md\
  chapters/cloud/virtualbox.md\
  chapters/cloud/vagrant.md\
  chapters/git/github.md\
  chapters/linux/linux.md\
	chapters/prg/SECTION-PYTHON.md\
  chapters/prg/python-intro.md\
  chapters/prg/python-install.md\
  chapters/prg/python-interactive.md\
  chapters/prg/python-editor.md\
  chapters/prg/SECTION-PYTHON-LANG.md\
  chapters/prg/python.md\
  chapters/prg/python-libraries.md\
  chapters/prg/python-data.md\
  chapters/prg/python-matplotlib.md\
  chapters/prg/python-cmd5.md\
  chapters/SECTION-REFERENCES.md


#   chapters/iaas/services.md\



CHAPTER_CLASS=\
 chapters/class/SECTION.md\
 chapters/class/fall2018.md\
 chapters/class/syllabus.md\
 chapters/class/policy.md\
 chapters/class/assignments.md\
 chapters/class/grading.md\
 chapters/class/project-ideas.md

CHAPTER_SERVICES=\
  chapters/doc/piazza.md\
 chapters/preface/git.md

######################################################################
# END BOOK CLASS
######################################################################

CHAPTER_REFERNCES=\
 chapters/references.md

BOOK_CLASS=\
  $(CHAPTER_PREFIX)\
  $(CHAPTER_CLASS) \
  $(CHAPTER_DOC)\
  $(CHAPTER_SERVICES) \
  $(CHAPTER_REFERENCES)


INDEX=\
  $(CHAPTER_516)


MARKDOWN-OPTIONS=$(MERMAID) -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
CSS=--css=template/pandoc.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".:chapters:chapters/prg:chapters/iot:chapters/container:chapters/os:chapters/mapreduce:chapters/cloud/chameleon:chapters/doc:chapters/preface:chapters/class:chapters/case:chapters/cloud:chapters/iaas/aws:chapters/iaas/azure:chapters/iaas/watson"

#	pandoc ./chapters/prg/python.md -o dest/chapters/prg/python.md --base-header-level=2

all: prepare epub
	echo done


prepare: refernces todo
	$(COPY) metadata.txt dest
	$(COPY) -r cover dest
	$(COPY) -r ../template dest
	$(COPY) -r ../template/fonts dest
	$(COPY) -r ../chapters dest	
	$(MARKUPALL)
	../bin/date.py > dest/chapters/version.md
	../bin/header.py dest/chapters/git/github.md 2
	../bin/header.py dest/chapters/linux/linux.md 2
	../bin/header.py dest/chapters/prg/python-install.md 1
	../bin/header.py dest/chapters/prg/python.md 2
	../bin/header.py dest/chapters/cloud/vagrant.md 2
	../bin/header.py dest/chapters/prg/python-libraries.md 2
	../bin/header.py dest/chapters/prg/python-data.md 1
	../bin/header.py dest/chapters/cloud/virtualbox.md 2
	../bin/header.py dest/chapters/class/organization-516.md 2
	../bin/section.py 1 "Development Tools and Services" > dest/chapters/SECTION-DEVTOOLS.md
	../bin/section.py 1 "A Single Pi" > dest/chapters/SECTION-ONE-PI.md
	../bin/section.py 1 "[Preface]{.part}" > dest/chapters/SECTION-PREFACE.md
	../bin/section.py 1 "References" > dest/chapters/SECTION-REFERENCES.md
	../bin/section.py 1 "Kubernetes" > dest/chapters/SECTION-SSH.md
	../bin/section.py 1 "PXE" > dest/chapters/SECTION-PXE.md
	../bin/section.py 1 "SD Card" > dest/chapters/SECTION-sdcard.md      
	../bin/section.py 1 "Docker" > dest/chapters/SECTION-docker.md
	../bin/section.py 1 "Docker Swarm" > dest/chapters/SECTION-docker-swarm.md  
	../bin/section.py 1 "Kubernetes" > dest/chapters/SECTION-kubernetes.md
	../bin/section.py 1 "Hadoop" > dest/chapters/SECTION-hadoop.md
	../bin/section.py 1 "Yarn" > dest/chapters/SECTION-yarn.md  
	../bin/section.py 1 "Spark" > dest/chapters/SECTION-spark.md        
	../bin/section.py 1 "Big Data Applications" > dest/chapters/bigdata/SECTION.md
	../bin/section.py 1 "Scientifc Writing" > dest/chapters/doc/SECTION.md
	../bin/section.py 1 "Python" > dest/chapters/prg/SECTION-PYTHON.md
	../bin/section.py 2 "Language" > dest/chapters/prg/SECTION-PYTHON-LANG.md
	../bin/section.py 1 "Classes" > dest/chapters/class/SECTION.md


epub: 
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(INDEX) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(INDEX) > all.md
endif
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md

draft: prepare
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(DRAFT) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(DRAFT) > all.md
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

publish: epub
	cp dest/$(FILENAME).epub ..
	git add ../$(FILENAME).epub
	git commit -m "update epub" ../$(FILENAME).epub
	git push

