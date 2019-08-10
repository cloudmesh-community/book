python: clean version
	mkdir -p dest
	bookmanager python.yaml get
	mv dest/vonLaszewski-python.epub ../../docs
	open ../../docs/vonLaszewski-python.epub

python-git: clean
	mkdir -p dest
	bookmanager python-local.yaml get
	mv dest/vonLaszewski-python.epub ../../docs
	open ../../docs/vonLaszewski-python.epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-python.epub \
	  ../../docs/vonLaszewski-python.pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-python.epub

clean:

	rm -rf dest
