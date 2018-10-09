all:
	pandoc "book.md"   -o "book.pdf"   --from markdown --template "../../eisvogel.latex" --toc -V "numbersections=true" --listings
	pdftoppm -r 150 -png "book.pdf" > "book.png"
