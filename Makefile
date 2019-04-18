.PHONY: cloud

VERSION=1.8

all: cloud-epub bigdata-epub
	echo done

update:
	cd big-data-applications; make update
	cd pi; make update
	cd cloud; make update
	cd 222; make update
	cd draft; make update


publish: cloud-epub-publish bigdata-epub-publish
	echo done


cloud-epub:
	cd cloud; make; make publish

cloud-epub-publish:
	cd cloud; make publish

bigdata-epub:
	cd big-data-applications; make; make publish

bigdata-epub-publish:
	cd big-data-applications; make publish

communicate-epub:
	cd communicate; make; make publish

image:
	docker build -t cloudmesh/book:${VERSION} . 
	docker tag cloudmesh/book:${VERSION} cloudmesh/book:latest

image-push:
	docker push cloudmesh/book

shell:
	docker run -v `pwd`:/book -w /book --rm -it cloudmesh/book:${VERSION}  /bin/bash 

docker-clean:
	-docker kill $$(docker ps -q)
	-docker rm $$(docker ps -a -q)
	-docker rmi $$(docker images -q)

docker-push:
	docker push cloudmesh/book:${VERSION}

cloud:
	docker run -v `pwd`:/book -w /book cloudmesh/book:${VERSION} /bin/sh -c "cd /book/cloud; git pull; make"
