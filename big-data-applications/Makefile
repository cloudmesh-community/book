
FILENAME=vonLaszewski-bigdata-application

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
 chapters/doc/SECTION.md\
 chapters/doc/plagiarism.md\
 chapters/doc/emacs.md\
 chapters/doc/markdown.md\
 chapters/doc/report.md\
 chapters/doc/type.md

# chapters/class/fall2018.md\
# chapters/class/SECTION.md\

CHAPTER_CLASS=\
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


CHAPTER_DRAFT=\
 chapters/SECTION-DRAFT.md

GRAPHICS=\
 chapters/doc/graphviz.md

ART=\
 chapters/art/sentient.md
 
CHAPTER_IN=\
 chapters/linux/ssh-futuresystems.md\
 chapters/in/ansible.md\
 chapters/in/assignments.md\
 chapters/in/box.md\
 chapters/in/cm-hadoop.md\
 chapters/in/course1.md\
 chapters/in/datasets.md\
 chapters/in/futuresystems.md\
 chapters/in/hadoop-comet.md\
 chapters/in/hadoop-rdma.md\
 chapters/in/hadoop-ubunto.md\
 chapters/in/old.md\
 chapters/in/pyenv-anaconda.md\
 chapters/in/python-cmd.md\
 chapters/in/ubuntu.md\
 chapters/in/virtualbox.md\
 chapters/in/vis.md\
 chapters/in/wordcount.md

######################################################################
# i523
######################################################################

# chapters/class/fall2018.md\
# chapters/class/SECTION.md\
# chapters/bigdata/SECTION.md\
# chapters/bigdata/intro-cloud.md\

CHAPTER_BIGDATA=\
 chapters/preface/notation.md\
 chapters/class/e534-i523.md\
 chapters/bigdata/intro-fall-2018.md\
 chapters/bigdata/applications/overview.md\
 chapters/bigdata/applications/physics.md\
 chapters/bigdata/applications/lifestyle.md\
 chapters/bigdata/applications/sport.md\
 chapters/bigdata/applications/cloud.md\
 chapters/bigdata/applications/usecases.md\
 chapters/bigdata/applications/sensor.md\
 chapters/bigdata/applications/web.md\
 chapters/bigdata/applications/health.md\
 chapters/bigdata/algorithms/technology.md\
 chapters/bigdata/algorithms/clustering.md\
 chapters/bigdata/algorithms/plotviz.md\

DEPRECATED=\
 chapters/linux/ssh2.md

REVIEW=\
 chapters/pi/software2.md

DRAFT=\
 chapters/pi/kubernetes/pi-kubernetes.md\
 chapters/pi/kubernetes/526/readme-kube.md\
 chapters/pi/kubernetes/417/pi-kubernetes.md\



OTHER=\
 chapters/SECTION-DRAFT.md\
 chapters/clusters/pi-now.md\
 chapters/pi/setup.md\
 chapters/modify-pi-image.md\
 chapters/pi/pi-passwordreset.md\
 chapters/clusters/pxe.md\
 chapters/clusters/pi-configure-cluster.md\
 chapters/clusters/pi-spark.md\
 chapters/pi/slurm.md\
 chapters/SECTION-hadoop.md\
 chapters/SECTION-yarn.md\
 chapters/SECTION-spark.md\


CHAPTER_REFERNCES=\
 chapters/references.md


INDEX=\
 $(CHAPTER_BIGDATA)
# $(CHAPTER_PI)

INDEX_OTHER=\
 $(OTHER)\
 $(MAPREDUCE)\
 $(CHAPTER_PYTHON)\
 $(CHAPTER_REFERENCES)


X=\
	$(CHAPTER_OTHER) \
	$(CHAPTER_PYTHON) \
  $(CHAPTER_IN) \
  $(CHAPTER_BIGDATA)

MARKDOWN-OPTIONS=$(MERMAID) -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".:chapters:chapters/prg:chapters/iot:chapters/container:chapters/os:chapters/mapreduce:chapters/cloud/chameleon:chapters/doc:chapters/preface:chapters/class:chapters/case"

#	pandoc ./chapters/prg/python.md -o dest/chapters/prg/python.md --base-header-level=2

all: prepare epub other
	echo done


prepare: dot refernces todo
	$(COPY) metadata.txt dest
	$(COPY) -r cover dest
	$(COPY) -r ../template dest
	$(COPY) -r ../template/fonts dest
	$(COPY) -r ../chapters dest	
	$(MARKUPALL)
	../bin/section.py 1 "A Single Pi" > dest/chapters/SECTION-ONE-PI.md
	../bin/section.py 1 "[Preface]{.part}" > dest/chapters/SECTION-PREFACE.md
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


other:
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(INDEX_OTHER) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(INDEX_OTHER) > all.md
endif
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME)-other.epub metadata.txt all.md

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

pdf:
	ebook-convert dest/$(FILENAME).epub ../$(FILENAME).pdf
