
FILENAME=vonLaszewski-cloud-cluster-pi

OS=$(shell ../bin/sysinfo.py)

MARKUPALL=../bin/markup-all.py

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

CHAPTER_BIGDATA=\
 chapters/bigdata/SECTION.md\
 chapters/bigdata//algorithms/technology.md\
 chapters/bigdata//algorithms/clustering.md\
 chapters/bigdata//algorithms/plotviz.md\
 chapters/bigdata//applications/overview.md\
 chapters/bigdata//applications/physics.md\
 chapters/bigdata//applications/lifestyle.md\
 chapters/bigdata//applications/sport.md\
 chapters/bigdata//applications/cloud.md\
 chapters/bigdata//applications/usecases.md\
 chapters/bigdata//applications/sensor.md\
 chapters/bigdata//applications/web.md\
 chapters/bigdata//applications/health.md\

######################################################################
# i516
######################################################################

CHAPTER_OTHER=\
 chapters/icloud//course/old-fundamentals.md\
 chapters/icloud//course/iot.md\
 chapters/icloud//course/nosql.md\
 chapters/icloud//course/fundamentals.md\
 chapters/icloud//course/iaas.md\
 chapters/icloud//course/iterative-mapreduce.md\
 chapters/icloud//course/mapreduce.md\
 chapters/icloud//course/selected.draft.md\
 chapters/icloud//course/nosql-new.md\
 chapters/icloud//course/saas.md\
 chapters/icloud//project2.md\
 chapters/icloud//participation.md\
 chapters/icloud//assignment/assignment.md\
 chapters/icloud//assignment/exercise5/exercise5.md\
 chapters/icloud//assignment/exercise2/exercise2.md\
 chapters/icloud//assignment/exercise2/pagerank.md\
 chapters/icloud//assignment/exercise3/exercise3.md\
 chapters/icloud//assignment/exercise4/exercise4.md\
 chapters/icloud//assignment/exercise8/exercise8.md\
 chapters/icloud//assignment/exercise1/exercise1.md\
 chapters/icloud//assignment/exercise6/exercise6.md\
 chapters/icloud//assignment/exercise7/exercise7.md\
 chapters/icloud//assignment/deprecated/exercise-old7/exercise7.md\
 chapters/icloud//syllabus.md\
 chapters/icloud//preface.md\
 chapters/icloud//deprecated.md\
 chapters/icloud//evaluation.md




######################################################################
# chameleon
######################################################################

CHAPTER_CHAMELEON=\
 chapters/cloud/chameleon/baremetal.md\
 chapters/cloud/chameleon/resources.md\
 chapters/cloud/chameleon/faq-orig.md\
 chapters/cloud/chameleon/hardware.md\
 chapters/cloud/chameleon/cli.md\
 chapters/cloud/chameleon/faq.md\
 chapters/cloud/chameleon/user-guide.md\
 chapters/cloud/chameleon/heat.md\
 chapters/cloud/chameleon/start.md\
 chapters/cloud/chameleon/faq-orig.md\
 chapters/cloud/chameleon/horizon.md\
 chapters/cloud/chameleon/baremetal.md\
 chapters/cloud/chameleon/charge.md\

OLD=\
 chapters/cloud/iot.md\
 chapters/cloud/nosql.md\
 chapters/cloud/assignment/index.md\
 chapters/cloud/fundamentals.md\
 chapters/cloud/iaas.md\
 chapters/cloud/iterative-mapreduce.md\
 chapters/cloud/evaluation/index.md\
 chapters/cloud/mapreduce.md\
 chapters/cloud/participation/index.md\
 chapters/cloud/saas.md\


MAPREDUCE=\
 chapters/hadoop/hadoop-installation.md\
 chapters/mapreduce/hadoop-installation.md\
 chapters/mapreduce/hadoop-lectures.md\
 chapters/mapreduce/harp.md\
 chapters/mapreduce/spark-installation.md\
 chapters/mapreduce/spark-lectures.md\
 chapters/mapreduce/spark-streaming.md\
 chapters/mapreduce/twister-installation.md\
 chapters/mapreduce/twister.md\
 chapters/mapreduce/twister2-example.md\
 chapters/os/ubuntu-usb-osx.md\
 chapters/new/go.md\
 chapters/new/amqp.md\
 chapters/new/osx-tricks.md\
 chapters/faas/introduction.md\
 chapters/data/formats.md\
 chapters/ai/ai.md\
 chapters/devops/devops.md\
 chapters/devops/travis.md\
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
 chapters/container/index.md\
 chapters/container/kubernetes-fs.md\
 chapters/container/kubernetes-intro.md\
 chapters/container/qemu.md\
 chapters/iot/dexter.md\
 chapters/iot/easyplug.md\
 chapters/iot/esp8266.md\
 chapters/iot/fundamentals.md\
 chapters/iot/grovepi.md\
 chapters/iot/hardware.md\
 chapters/iot/introduction.md\
 chapters/iot/pi.md\
 chapters/iot/projects.md\
 chapters/iot/sensors.md\
 chapters/iot/tools.md\
 chapters/iot/turtle.md\
 chapters/iot/vnc.md\
 chapters/msg/mqtt.md\
 chapters/msg/graphql.md\
 chapters/rest/rest.md\
 chapters/rest/swagger-bravado.md\
 chapters/rest/swagger-codegen.md\
 chapters/rest/swagger-spec.md\
 chapters/rest/swagger.md\

CHAPTER_PYTHON=\
 chapters/prg/SECTION-PYTHON.md\
 chapters/prg/python.md\
 chapters/prg/python-install.md\
 chapters/prg/python-cloudmesh.md\
 chapters/prg/python-matplotlib.md\
 chapters/prg/python-editor.md\
 chapters/prg/python-libraries.md\
 chapters/prg/python-cmd5.md\
 chapters/prg/python-click.md\
 chapters/prg/python-big-data.md\
 chapters/prg/python-intro.md\
 chapters/prg/python-interactive.md\
 chapters/prg/python-data.md\
 chapters/prg/python-libcloud.md\
 chapters/references.md

DEPRECATED=\
 chapters/linux/ssh2.md

CHAPTER_PI=\
 chapters/SECTION-PREFACE.md\
 chapters/pi/preface.md\
 chapters/preface/notation.md\
 chapters/preface/contributors.md\
 chapters/preface/contributing.md

B=\
 chapters/preface/git.md\
 chapters/pi/board.md\
 chapters/pi/case.md\
 chapters/case/case.md\
 chapters/pi/links.md\
 chapters/pi/exercise.md\
 chapters/login-node.md\
 chapters/sd-card.md\
 chapters/linux/linux.md\
 chapters/SECTION-DRAFT.md\
 chapters/linux/ssh.md\
 chapters/linux/refcards.md\
 chapters/raspberry/config-display.md\
 chapters/raspberry/motherboard-led.md\
 chapters/run-at-boot.md\
 chapters/clusters/pi-now.md\
 chapters/modify-pi-image.md\
 chapters/pi/pi-passwordreset.md\
 chapters/clusters/pxe.md\
 chapters/clusters/pi-configure-cluster.md\
 chapters/clusters/pi-docker.md\
 chapters/clusters/pi-dockerswarm.md\
 chapters/clusters/kubernetes-526/readme-kube.md\
 chapters/clusters/kubernetes-417/pi-kubernetes.md\
 chapters/clusters/pi-spark.md\
 chapters/clusters/pi-software.md\
 chapters/pi/slurm.md\
 chapters/pi/setup.md\
 chapters/pi/software.md\
 chapters/SECTION-hadoop.md\
 chapters/SECTION-yarn.md\
 chapters/SECTION-spark.md\


CHAPTER_REFERNCES=\
 chapters/references.md


INDEX=\
 $(CHAPTER_PI)

A=\
 $(MAPREDUCE)\
 $(CHAPTER_PYTHON)\
 $(CHAPTER_REFERENCES)


X=\
	$(CHAPTER_OTHER) \
	$(CHAPTER_PYTHON) \
  $(CHAPTER_IN) \
  $(CHAPTER_BIGDATA)

MARKDOWN-OPTIONS=$(MERMAID) -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
RESOURCE=--resource-path=".:chapters:chapters/prg:chapters/iot:chapters/container:chapters/os:chapters/mapreduce:chapters/cloud/chameleon:chapters/doc:chapters/preface:chapters/class:chapters/case"

#	pandoc ./chapters/prg/python.md -o dest/chapters/prg/python.md --base-header-level=2

epub: dot refernces todo
	$(COPY) metadata.txt dest
	$(COPY) -r cover dest
	$(COPY) -r ../template dest
	$(COPY) -r ../template/fonts dest
	$(COPY) -r ../chapters dest	
	$(MARKUPALL)
	../bin/section.py 1 "Preface" > dest/chapters/SECTION-PREFACE.md
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
	../bin/section.py 1 ":construction::construction::construction::construction::construction::construction::construction::construction::construction::construction::construction:" > dest/chapters/SECTION-DRAFT.md
	cd dest; iconv -t utf-8 $(INDEX) > all.md
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md

refernces:
	mkdir -p dest
	cat ../bib/*.bib > dest/references.bib

html:
	pandoc $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) -o $(FILENAME).html metadata.txt $(INDEX)

pdf:
	pandoc -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' -V geometry:margin=1in --bibliography refernces.bib --csl=ieee.csl -o $(FILENAME).pdf metadata.txt $(INDEX)

tex:
	pandoc -f markdown+smart -f markdown+emoji --toc --epub-embed-font='fonts/*.ttf' --bibliography refernces.bib --csl=ieee.csl -o $(FILENAME).tex metadata.txt $(INDEX)
	pdflatex content.tex


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

