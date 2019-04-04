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


######################################################################
# PYPI
######################################################################


twine:
	pip install -U twine

dist:
	python setup.py sdist bdist_wheel
	twine check dist/*

patch: clean
	$(call banner, patch to testpypi)
	bumpversion --allow-dirty patch
	python setup.py sdist bdist_wheel
	git push origin master --tags
	twine check dist/*
	twine upload --repository testpypi https://test.pypi.org/legacy/ dist/*

release: clean dist
	$(call banner, release to pypi)
	bumpversion release
	python setup.py sdist bdist_wheel
	git push origin master --tags
	twine check dist/*
	twine upload --repository testpypi https://test.pypi.org/legacy/ dist/*


upload:
	twine check dist/*
	twine upload dist/*

pip: patch
	pip install --index-url https://test.pypi.org/simple/ \
	    --extra-index-url https://pypi.org/simple cloudmesh-$(package)

log:
	$(call banner, log)
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push