NAME=book
VERSION=0.2.19
######################################################################
# DOCKER
######################################################################

#--no-cache=true

image:
	docker build  -t cloudmesh/$(NAME):$(VERSION) .

shell:
	docker run -v `pwd`:/book -w /book --rm -it cloudmesh/book:${VERSION}  /bin/bash

cms:
	docker run --rm -it cloudmesh/$(NAME):$(VERSION)

dockerclean:
	-docker kill $$(docker ps -q)
	-docker rm $$(docker ps -a -q)
	-docker rmi $$(docker images -q)

push:
	docker push cloudmesh/$(NAME):$(VERSION)

run:
	docker run cloudmesh/$(NAME):$(VERSION) /bin/sh -c "cd technologies; git pull; make"

