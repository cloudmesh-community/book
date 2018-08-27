all: cloud-epub bigdata-epub
	echo done

cloud-epub:
	cd cloud; make; make publish

bigdata-epub:
	cd big-data-applications; make; make publish
