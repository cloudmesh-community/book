build:
	docker build . -t cms-mongo

start:
	docker run --rm -d -p 27017:27017/tcp --name cms-mongo cms-mongo:latest

stop:
	docker container ls -q --filter name=cms-mongo | xargs docker stop