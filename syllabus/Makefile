all:
	cp  ../chapters/class/e516-syllabus-nodates.md .
	perl -pi -e 's/\:cloud\:/ \$$\\hookrightarrow\$$ /g' e516-syllabus-nodates.md
	iconv -t utf-8 e516-syllabus-nodates.md | pandoc -o e516.pdf   -f markdown+emoji  --from markdown --template "../template/eisvogel/eisvogel.latex" --toc -V "urlcolor=cyan" -V "numbersections=true" --listings
	rm e516-syllabus-nodates.md

ascii:	
	perl -ane '{ if(m/[[:^ascii:]]/) { print  } }'  ../chapters/class/e516-syllabus-nodates.md 
