CONTENT=writing

all: epub pdf


epub: clean version
	mkdir -p dest
	bookmanager $(CONTENT).yaml get
	mv dest/vonLaszewski-$(CONTENT).epub ../../docs
	open ../../docs/vonLaszewski-$(CONTENT).epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-$(CONTENT).epub \
	  ../../docs/vonLaszewski-$(CONTENT).pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-$(CONTENT).epub

clean:

	rm -rf dest

