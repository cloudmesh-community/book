all: clean
	bookmanager outline.yaml get
	cd dest; ebook-convert vonLaszewski-e516-syllabus.epub vonLaszewski-e516-syllabus.pdf --pdf-page-numbers --embed-all-fonts
	cp dest/vonLaszewski-e516-syllabus.epub ../docs/e516.epub
	cp dest/vonLaszewski-e516-syllabus.pdf ../docs/e516.pdf

#pdf:
	#bookmanager outline.yaml pdf


old:
	cp  ../chapters/class/e516-syllabus-table.md .
	perl -pi -e 's/\:cloud\:/ \$$\\hookrightarrow\$$ /g' e516-syllabus-table.md
	iconv -t utf-8 e516-syllabus-table.md | pandoc -o e516.tex   -f markdown+emoji  --from markdown --template "../template/eisvogel/eisvogel.latex" --toc -V "date=now" -V "urlcolor=cyan" -V "numbersections=true" --listings
	rm e516-syllabus-table.md

ascii:	
	perl -ane '{ if(m/[[:^ascii:]]/) { print  } }'  ../chapters/class/e516-syllabus-table.md

clean:
	rm -rf dest