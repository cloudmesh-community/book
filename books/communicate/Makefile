all: communicate

# pdf

communicate: clean version
	mkdir -p dest
	bookmanager communicate.yaml get
	mv dest/vonLaszewski-communicate.epub ../../docs
	open ../../docs/vonLaszewski-communicate.epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-communicate.epub \
	  ../../docs/vonLaszewski-communicate.pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-communicate.epub

clean:

	rm -rf dest




