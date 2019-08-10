all: syllabus pdf

syllabus: clean version
	mkdir -p dest
	bookmanager syllabus.yaml get
	mv dest/vonLaszewski-e516-syllabus.epub ../../docs
	open ../../docs/vonLaszewski-e516-syllabus.epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-e516-syllabus.epub \
	  ../../docs/vonLaszewski-e516-syllabus.pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-e516-syllabus.epub

clean:

	rm -rf dest
