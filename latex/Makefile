.PHONY: book images dot

FILE=vonLaszewski-latex
#FLAGS=-interaction nonstopmode -halt-on-error -file-line-error
#FLAGS=-interaction nonstopmode  -file-line-error
FLAGS=-shell-escape
CLOUD=cloud
FLAGS=-shell-escape -output-directory=dest -aux-directory=dest --max-print-line=140


DEFAULT=$(CLOUD)

LATEX=pdflatex

#LATEX=pdfflatex
#LATEX=pydflatex -k

g: dest markdown graphicspath
	latexmk -jobname=$(FILE) $(FLAGS) -pvc -view=pdf $(FILE)

setup:
	export max_print_line=1000

graphicspath:
	bin/list-images-dirs.py > graphicspath.tex

once: setup clean dest markdown graphicspath
	latexmk -jobname=$(FILE) $(FLAGS) -view=pdf $(FILE)
	# make html

travis: dest markdown graphicspath
	latexmk -pdflatex='pdflatex -file-line-error -synctex=1' -jobname=$(FILE) $(FLAGS) -pdf $(FILE)

issues: clean dest
	python bin/issues.py > section/preface/issues.tex
	pdflatex issues
	#latexmk -jobname=issues $(FLAGS) -view=pdf issues

dot:
	cd dot; dot -Tpdf gr.dot -o gr.pdf

markdown:
	bin/md-all-to-tex.py

test: dest markdown
	pdflatex $(FILE)

gg: setup dest markdown graphicspath
	pdflatex -shell-escape $(FILE)

check:
	make gg

pdflatex: dest
	make gg

google:
	gdrive update 1Mdd_TJcbXurJYRpG2gKCVqWmbhvED2Mp dest/$(FILE).pdf

single: dest graphicspath
	latexmk -jobname=single $(FLAGS) -pvc -view=pdf single

draft: clean dest graphicspath
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-503/master/sd-card-ubuntu.md > tmp/sd-card-ubuntu.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-508/master/cluster/sd-card-osx.md > tmp/sd-card-osx.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-602/master/sd-card-windows.md > tmp/sd-card-windows.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-421/master/ssh-keygen.md > tmp/ssh-keygen.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-412/master/cluster/readme-spark.md > tmp/readme-spark.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-526/master/cluster/readme-kube.md > tmp/readme-kube.md
	curl -s https://raw.githubusercontent.com/cloudmesh-community/hid-sp18-405/master/Cluster/pi-dhcp.md > tmp/pi-dhcp.md
	bin/md-tmp-to-tex.py
	latexmk -jobname=draft $(FLAGS) -view=pdf draft

dd: dest graphicspath
	cd tmp; python ../bin/md-all-to-tex.py
	latexmk -jobname=draft $(FLAGS) -pvc -view=pdf draft

cloud: dest markdown graphicspath
	$(LATEX) $(FLAGS) $(CLOUD)
	makeindex $(CLOUD).idx -s format/StyleInd.ist
	biber $(CLOUD)
	$(LATEX) $(FLAGS)  $(CLOUD) 
	$(LATEX) $(FLAGS)  $(CLOUD)

skim: dest
	echo $(DEFAULT)
	open -a /Applications/skim.app $(DEFAULT).pdf

all: dest makedown graphicspath
	$(LATEX) $(FLAGS) $(FILE)
	makeindex $(FILE).idx -s format/StyleInd.ist
	biber $(FILE)
	$(LATEX) $(FLAGS)  $(FILE) 
	$(LATEX) $(FLAGS)  $(FILE) 


all2:
	$(LATEX) $(FLAGS) $(FILE)
	makeindex $(FILE).idx -s format/StyleInd.ist
	biber $(FILE)
	$(LATEX) $(FLAGS)  $(FILE) x 2
	$(LATEX) $(FLAGS)  $(FILE) x 2

simple:
	$(LATEX) $(FLAGS) $(FILE)
#|fgrep -v "Underfull" |fgrep -v "Overfull" | fgrep -v "undefined on input"
#	makeindex $(FILE).idx -s format/StyleInd.ist
#	biber $(FILE)
#	$(LATEX) $(FLAGS)  $(FILE) x 2
#	$(LATEX) $(FLAGS)  $(FILE) x 2

book:
	python book.py

images:
	cp -r ~/github/cloudmesh/classes/docs/source/images/ images

fetch:
	cd chapter; make

old:
	$(LATEX) $(FILE)
	makeindex $(FILE).idx -s StyleInd.ist
	biber $(FILE)
	$(LATEX) $(FILE) x 2

clean:
	rm -fr single
	rm -fr $(FILE)
	rm -f *.aux
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.idx
	rm -f *.ilg
	rm -f *.ind
	rm -f *.pdf
	rm -f *.ptc
	rm -f *.run.xml
	rm -f *.toc
	rm -f *.log
	rm -f *.markdown.out
	rm -f *.markdown.lua
	rm -f *.markdown.err
	rm -f *.fls
	rm -f *.listing
	rm -f *.fdb_latexmk
	rm -f *.synctex.gz
	rm -rf _markdown_*
	rm -rf dest
	rm -rf *.tdo
	find . -name '*.aux' -delete
	find . -name ".#*" -delete
	rm -fr _minted-*
	rm -f tmp/*
	rm -f *-dot2tex-*
	rm -f *.out
	bin/md-clean-tex.py

view:
	open dest/$(FILE).pdf

publish: 
	echo pdf document copied to google
#	cp dest/$(FILE).pdf .
#	cp $(FILE).pdf ~/github/laszewsk/papers/
#	cd ~/github/laszewsk/papers; git add $(FILE).pdf; git commit -m "update $(FILE)"; git push
#	cp $(FILE).pdf ~/github/laszewsk/laszewski.github.io/papers/$(FILE).pdf
#	cd ~/github/laszewsk/laszewski.github.io/papers; git add $(FILE).pdf; git commit -m "update $(FILE)"; git push
	make -f Makefile.publish
	make -f Makefile google

html:
	mkdir -p ~/pdf
	cp dest/$(FILE).pdf ~/pdf
	docker run -ti --rm -v ~/pdf:/pdf bwits/pdf2htmlex pdf2htmlEX --zoom 1.3 $(FILE).pdf 
	# gdrive update 10zA34VsM-WnsQo31rHzDOtqdU3rqvkvQ ~/pdf/$(FILE).html

size:
	du -c -h dest/vonLaszewski-bigdata.pdf | fgrep total > dest/size.txt
	du -c -h dest/vonLaszewski-bigdata.pdf | fgrep total 


watch:
	latexmk -pvc -view=pdf ${FILE}

dest: setup
	python bin/create-dirs.py 
