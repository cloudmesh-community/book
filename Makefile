NAME=book

######################################################################
# DOCKER
######################################################################

#--no-cache=true

image:
	docker build  -t cloudmesh/$(NAME):0.2.19 .

shell:
	docker run --rm -it cloudmesh/$(NAME):0.2.19  /bin/bash

cms:
	docker run --rm -it cloudmesh/$(NAME):0.2.19

dockerclean:
	-docker kill $$(docker ps -q)
	-docker rm $$(docker ps -a -q)
	-docker rmi $$(docker images -q)

push:
	docker push cloudmesh/$(NAME):0.2.19

run:
	docker run cloudmesh/$(NAME):0.2.19 /bin/sh -c "cd technologies; git pull; make"
