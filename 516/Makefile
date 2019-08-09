

e516: clean
	mkdir -p dest
	bookmanager e516.yaml get
	mv dest/vonLaszewski-e516.epub ../docs
	open ../docs/vonLaszewski-e516.epub

python: clean
	mkdir -p dest
	bookmanager python.yaml get
	mv dest/vonLaszewski-python.epub ../docs
	open ../docs/vonLaszewski-python.epub

python-local: clean
	mkdir -p dest
	bookmanager python-local.yaml get
	mv dest/vonLaszewski-python.epub ../docs
	open ../docs/vonLaszewski-python.epub


clean:

	rm -rf dest
