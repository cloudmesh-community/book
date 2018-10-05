all:
	pandoc "book.md"   -o "book.pdf"   --from markdown --template "../../eisvogel.latex" -V "logo=logo-inverted.pdf" --listings
	pdftoppm -r 150 -png "book.pdf" > "book.png"
