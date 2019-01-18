.PHONY: cloud

VERSION=1.4

all: cloud-epub bigdata-epub
	echo done

cloud-epub:
	cd cloud; make; make publish

bigdata-epub:
	cd big-data-applications; make; make publish

communicate-epub:
	cd communicate; make; make publish



image:
	docker build -t cloudmesh/book:${VERSION} . 

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
