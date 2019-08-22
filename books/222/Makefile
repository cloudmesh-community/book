NAME=222

all: book pdf

book: clean version  authors
	mkdir -p dest
	bookmanager $(NAME).yaml get
	mv dest/vonLaszewski-$(NAME).epub ../../docs

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
	killall Books
	open $(HOME)/docs/vonLaszewski-$(NAME).epub

authors:
	../../bin/authors.py > ../chapters/authors.md

clean:

	rm -rf dest
