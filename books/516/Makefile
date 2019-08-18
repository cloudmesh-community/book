all: e516 pdf

e516: clean version
	mkdir -p dest
	bookmanager e516.yaml get
	mv dest/vonLaszewski-e516-e516.epub ../../docs
	open ../../docs/vonLaszewski-e516-e516.epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-e516-e516.epub \
	  ../../docs/vonLaszewski-e516-e516.pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-e516-e516.epub

clean:

	rm -rf dest
