all: cloud-epub bigdata-epub
	echo done

cloud-epub:
	cd cloud; make; make publish

bigdata-epub:
	cd big-data-applications; make; make publish

communicate-epub:
	cd communicate; make; make publish



image:
	docker build -t cloudmesh-community/book:1.0 . 

image-push:
	docker push cloudmesh/technologies

shell:
	docker run --rm -it cloudmesh-community/book:1.0  /bin/bash 

docker-clean:
	-docker kill $$(docker ps -q)
	-docker rm $$(docker ps -a -q)
	-docker rmi $$(docker images -q)

docker-push:
	docker push cloudmesh-community/book:1.0

run:
	docker run cloudmesh-community/book:1.0 /bin/sh -c "cd technologies; git pull; make"
