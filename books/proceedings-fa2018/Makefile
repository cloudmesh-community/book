NAME=proceedings-fa2018

all: book pdf

book: clean version
	mkdir -p dest
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub ../../docs
	open ../../docs/vonLaszewski-$(NAME).epub

pdf:
	ebook-convert \
	  ../../docs/vonLaszewski-$(NAME).epub \
	  ../../docs/vonLaszewski-$(NAME).pdf

bib:
	mkdir -p dest
	cp ../../bib/*.bib dest

version:
	TZ=":US/Eastern"; date > ../../chapters/version.md

view:
	open ../../docs/vonLaszewski-$(NAME).epub

clean:

	rm -rf dest
