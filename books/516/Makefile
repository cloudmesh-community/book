

e516: clean version bib
	mkdir -p dest
	bookmanager e516.yaml get
	mv dest/vonLaszewski-e516.epub ../docs
	open ../docs/vonLaszewski-e516.epub

python: clean version
	mkdir -p dest
	bookmanager python.yaml get
	mv dest/vonLaszewski-python.epub ../docs
	open ../docs/vonLaszewski-python.epub

python-git: clean
	mkdir -p dest
	bookmanager python-local.yaml get
	mv dest/vonLaszewski-python.epub ../docs
	open ../docs/vonLaszewski-python.epub

pdf:
	ebook-convert \
	  ../docs/vonLaszewski-python.epub \
	  ../docs/vonLaszewski-python.pdf

bib:
	mkdir -p dest
	cp ../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../chapters/version.md

clean:

	rm -rf dest
