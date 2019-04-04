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
	$(call banner, "bbuild")
	bump2version --allow-dirty patch
	python setup.py sdist bdist_wheel
	# git push origin master --tags
	twine check dist/*
	twine upload --repository testpypi  dist/*
	$(call banner, "install")
	sleep 10
	pip install --index-url https://test.pypi.org/simple/ cloudmesh-$(package) -U

minor: clean
	$(call banner, "minor")
	bump2version minor --allow-dirty
	@cat VERSION
	@echo

release: clean
	$(call banner, "release")
	git tag "v$(VERSION)"
	git push origin master --tags
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository pypi dist/*
	$(call banner, "install")
	@cat VERSION
	@echo
	sleep 10
	pip install -U cloudmesh-common


dev:
	bump2version --new-version "$(VERSION)-dev0" part --allow-dirty
	bump2version patch --allow-dirty
	@cat VERSION
	@echo

reset:
	bump2version --new-version "4.0.0-dev0" part --allow-dirty

upload:
	twine check dist/*
	twine upload dist/*

pip:
	pip install --index-url https://test.pypi.org/simple/ cloudmesh-$(package) -U

#	    --extra-index-url https://test.pypi.org/simple

log:
	$(call banner, log)
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push