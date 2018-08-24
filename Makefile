all: cloud bigdata
	echo done

cloud:
	cd cloud; make; make publish

bigdata:
	cd big-data-applications; make; make publish
