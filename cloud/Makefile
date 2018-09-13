include ../Makefile.sections

FILENAME=vonLaszewski-cloud

OS=$(shell ../bin/sysinfo.py)
DOCKER=$(shell ../bin/isdocker.py)
IMAGE_DIRS=$(shell ../bin/find-image-dirs.py)

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

KUBERNETES=\
 chapters/container/index.md\
 chapters/container/container.md\
 chapters/container/docker-fs.md\
 chapters/container/docker-hadoop-cluster.md\
 chapters/container/docker-hadoop.md\
 chapters/container/docker-hadoop3.md\
 chapters/container/docker-intro.md\
 chapters/container/docker-local.md\
 chapters/container/docker-pagerank-example-instruction.md\
 chapters/container/docker-rest.md\
 chapters/container/docker-spark.md\
 chapters/container/docker-swarm.md\
 chapters/container/exercise.md\
 chapters/container/glossary.md\
 chapters/container/kubernetes-fs.md\
 chapters/container/kubernetes-intro.md\
 chapters/container/qemu.md\

GO=\
  chapters/prg/go/go-intro.md\
  chapters/prg/go/go-install.md\
  chapters/prg/go/go-editor.md\
  chapters/prg/go/go-language.md\
  chapters/prg/go/go-libraries.md\
  chapters/prg/go/go-cmd.md


DRAFT=\
  $(KUBERNETES)\
  chapters/msg/mqtt.md\
  chapters/msg/mqtt1.md\
  chapters/msg/mqtt2.md\
  $(GO)


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

all: prepare epub
	echo done



sectionindent:
	../bin/authors.py > dest/chapters/authors.md
	../bin/header.py dest/chapters/assignment.md 1
	../bin/header.py dest/chapters/git/github.md 2
	../bin/header.py dest/chapters/linux/linux.md 2
	../bin/header.py dest/chapters/prg/python/python-install.md 1
	../bin/header.py dest/chapters/prg/python/python.md 2
	../bin/header.py dest/chapters/prg/python/python-cmd.md 3
	../bin/header.py dest/chapters/prg/scala/scala.md 1
	../bin/header.py dest/chapters/cloud/vagrant.md 2
	../bin/header.py dest/chapters/prg/python/python-libraries.md 2
	../bin/header.py dest/chapters/prg/python/python-data.md 1
	../bin/header.py dest/chapters/cloud/virtualbox.md 2
	../bin/header.py dest/chapters/class/organization-516.md 2
	../bin/header.py dest/chapters/class/policies.md 2
	../bin/header.py dest/chapters/preface/create.md 2
	../bin/header.py dest/chapters/linux/ssh.md 2
	../bin/header.py dest/chapters/linux/ssh-excerise.md 2
	../bin/header.py dest/chapters/linux/refcards.md 2
	../bin/header.py dest/chapters/iaas/aws/aws.md 2
	../bin/header.py dest/chapters/iaas/azure/azure.md 2
	../bin/header.py dest/chapters/iaas/watson/watson.md 1
	../bin/header.py dest/chapters/iaas/gcloud/gcloud.md 2
	../bin/header.py dest/chapters/os/ubuntu-usb-osx.md 2
	../bin/header.py dest/chapters/faq.md 2
	../bin/header.py dest/chapters/MSG.md 1
	../bin/header.py dest/chapters/prg/go/go-language.md 1
	../bin/header.py dest/chapters/prg/julia/julia-language.md 1
	../bin/header.py dest/chapters/msg/mqtt.md 2
	../bin/header.py dest/chapters/msg/graphql.md 2
	../bin/header.py dest/chapters/faq.md 1
	../bin/header.py dest/chapters/faq-516.md 2
	../bin/header.py dest/chapters/SECTION-DEVTOOLS.md 1
	../bin/header.py dest/chapters/rest/swagger-codegen.md 2
	../bin/header.py dest/chapters/rest/swagger-spec.md 2
	../bin/header.py dest/chapters/rest/swagger.md 2
	../bin/header.py dest/chapters/iaas/libcloud.md 2
	../bin/header.py dest/chapters/iaas/iaas.md 2
	../bin/header.py dest/chapters/iaas/aws/aws.md 1
	../bin/header.py dest/chapters/iaas/azure/azure.md 1
	../bin/header.py dest/chapters/iaas/watson/watson.md 2
	../bin/header.py dest/chapters/iaas/gcloud/gcloud.md 1
	../bin/header.py dest/chapters/iaas/azure/products.md 2
	../bin/header.py dest/chapters/iaas/aws/products.md 2
	../bin/header.py dest/chapters/SECTION-CHAMELEON.md 1 
	../bin/header.py dest/chapters/cloud/chameleon/baremetal.md 2
	../bin/header.py dest/chapters/cloud/chameleon/resources.md 2
	../bin/header.py dest/chapters/cloud/chameleon/hardware.md 2
	../bin/header.py dest/chapters/cloud/chameleon/cli.md 2
	../bin/header.py dest/chapters/cloud/chameleon/faq.md 2
	../bin/header.py dest/chapters/cloud/chameleon/user-guide.md 2
	../bin/header.py dest/chapters/cloud/chameleon/heat.md 2
	../bin/header.py dest/chapters/cloud/chameleon/start.md 2
	../bin/header.py dest/chapters/cloud/chameleon/horizon.md 2
	../bin/header.py dest/chapters/cloud/chameleon/baremetal.md 2
	../bin/header.py dest/chapters/cloud/chameleon/charge.md 2
	../bin/header.py dest/chapters/prg/python/opencv/opencv.md 2

sectionheaders:
	../bin/section.py 1 "Development Tools and Services" > dest/chapters/SECTION-DEVTOOLS.md
	../bin/section.py 1 "A Single Pi" > dest/chapters/SECTION-ONE-PI.md
	../bin/section.py 1 "Preface" > dest/chapters/SECTION-PREFACE.md
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
	../bin/section.py 1 "Scientific Writing" > dest/chapters/doc/SECTION.md
	../bin/section.py 1 "Python" > dest/chapters/prg/SECTION-PYTHON.md
	../bin/section.py 2 "Language" > dest/chapters/prg/SECTION-PYTHON-LANG.md
	../bin/section.py 1 "Classes" > dest/chapters/class/SECTION.md
	../bin/section.py 1 "Messaging" > dest/chapters/MSG.md
	../bin/section.py 1 "FAQ" > dest/chapters/SECTION-FAQ.md
	../bin/section.py 1 "Infrastructure as a Service" > dest/chapters/SECTION-IAAS.md
	../bin/section.py 1 "Appendix" > dest/chapters/SECTION-APPENDIX.md
	../bin/section.py 1 "Chameleon Cloud" > dest/chapters/SECTION-CHAMELEON.md

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
RESOURCE=--resource-path=$(IMAGE_DIRS)
#RESOURCE=--resource-path=".:chapters:chapters/prg:chapters/iot:chapters/container:chapters/os:chapters/mapreduce:chapters/cloud/chameleon:chapters/doc:chapters/preface:chapters/class:chapters/case:chapters/cloud:chapters/iaas/aws:chapters/iaas/azure:chapters/iaas/watson:chapters/iaas/gcloud:chapters/msg:chapters/nist"

#	pandoc ./chapters/prg/python.md -o dest/chapters/prg/python.md --base-header-level=2



draft: prepare epubdraft
	echo done


destination:
	mkdir -p dest
	$(COPY) metadata.txt dest
	$(COPY) -r cover dest
	$(COPY) -r ../template dest
	$(COPY) -r ../template/fonts dest
	$(COPY) -r ../chapters dest	

prepare: destination references todo
	$(MARKUPALL)
	../bin/date.py > dest/chapters/version.md
	echo "\n\nThis document can be downloaded from\n\n" >> dest/chapters/version.md
	echo "<https://github.com/cloudmesh-community/book/blob/master/$(FILENAME).epub?raw=true>\n\n" >> dest/chapters/version.md
	make -f Makefile sectionheaders
	make -f Makefile sectionindent



epub: prepare
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(INDEX) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(INDEX) > all.md
endif
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md

epubdraft: prepare
ifeq ($(OS), osx)
	cd dest; iconv -t utf-8 $(DRAFT) > all.md
endif
ifeq ($(OS), linux)
	cd dest; cat $(DRAFT) > all.md
endif
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md


references:
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

