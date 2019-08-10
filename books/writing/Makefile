all: writing

# pdf

writing: clean version
	mkdir -p dest
	bookmanager writing.yaml get
	mv dest/vonLaszewski-writing.epub ../../docs
	open ../../docs/vonLaszewski-writing.epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-writing.epub \
	  ../../docs/vonLaszewski-writing.pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-writing.epub

clean:

	rm -rf dest




