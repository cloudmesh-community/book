AUTHOR=--author="Gregor von Laszewski (laszewski@gmail.com)"
BASE=../chapters/prg/python
CHAPTERS=../chapters
CONVERT=python convert.py

all:
	mkdir -p python

	${CONVERT} --d=./python --w=10 --index=Python
	${CONVERT} --d=./python/introduction --w=12 --index=Introduction
	${CONVERT} --d=./python/installation --w=14 --index=Installation
	${CONVERT} --d=./python/first-step --w=16 --index="First Steps"
	${CONVERT} --d=./python/language --w=18 --index=Language
	${CONVERT} --d=./python/cloudmesh --w=20 --index=Cloudmesh
	${CONVERT} --d=./python/data --w=20 --index=Data
	${CONVERT} --d=./python/mongo --w=20 --index=Mongo
	${CONVERT} --d=./python/other --w=20 --index=Other
	${CONVERT} --d=./python/applications --w=20 --index=Applications
	${CONVERT} --file=${BASE}/python-intro.md --tags="python" ${AUTHOR} --d=./python/introduction --w=10
	${CONVERT} --file=${BASE}/python-install.md --tags="python" ${AUTHOR} --d=./python/installation --w=10
	#    - ${BASE}/python-install-pyenv.md"
	# FIRST_STEPS:
	${CONVERT} --file=${BASE}/python-interactive.md  --tags="python" ${AUTHOR} --d=./python/first-steps --w=10
	${CONVERT} --file=${BASE}/python-editor.md  --tags="python" ${AUTHOR} --d=./python/first-steps --w=10
	${CONVERT} --file=${BASE}/google-colab/python-google-colab.md  --tags="python" ${AUTHOR} --d=./python/first-steps --w=10
	# - LANGUAGE:
	${CONVERT} --file=${BASE}/python.md  --tags="python" ${AUTHOR} --d=./python/language --w=10
	#cloudmesh  - CLOUDMESH:
	${CONVERT} --file=${BASE}/cloudmesh/introduction.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=10
	${CONVERT} --file=${BASE}/cloudmesh/installation.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=12
	${CONVERT} --file=${BASE}/cloudmesh/console.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=14
	${CONVERT} --file=${BASE}/cloudmesh/dict.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=16
	${CONVERT} --file=${BASE}/cloudmesh/shell.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=18
	${CONVERT} --file=${BASE}/cloudmesh/stopwatch.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=20
	${CONVERT} --file=${BASE}/cloudmesh/python-cmd5.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=22
	${CONVERT} --file=${BASE}/cloudmesh/exercises.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=24
	#	${CONVERT} --file=${BASE}/cloudmesh/config.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=26
	#	${CONVERT} --file=${BASE}/cloudmesh/inventory.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=28
	#	${CONVERT} --file=${BASE}/cloudmesh/python-cloudmesh.md  --tags="python" ${AUTHOR} --d=./python/cloudmesh --w=30
	#  - LIBRARIES:
	${CONVERT} --file=${BASE}/python-libraries.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	${CONVERT} --file=${BASE}/python-data.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	${CONVERT} --file=${BASE}/python-matplotlib.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	${CONVERT} --file=${BASE}/python-docopts.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	${CONVERT} --file=${BASE}/opencv/opencv.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	${CONVERT} --file=${BASE}/opencv/secchi.md  --tags="python" ${AUTHOR} --d=./python/libraries --w=10
	# - DATA:
	${CONVERT} --file=${CHAPTERS}/data/formats.md  --tags="python" ${AUTHOR} --d=./python/data --w=10
	# - MONGO:
	${CONVERT} --file=${CHAPTERS}/data/mongodb.md  --tags="python" ${AUTHOR} --d=./python/mongo --w=10
	${CONVERT} --file=${CHAPTERS}/data/mongoengine.md  --tags="python" ${AUTHOR} --d=./python/mongo --w=10
	# - OTHER:
	${CONVERT} --file=${BASE}/python-wordcount.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/numpy/numpy.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/scipy/scipy.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/scikit-learn/scikit-learn.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/random-forest/random-forest.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/python-parallel.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	${CONVERT} --file=${BASE}/dask/dask.md  --tags="python" ${AUTHOR} --d=./python/other --w=10
	#- APPLICATIONS:
	${CONVERT} --file=${BASE}/fingerprint/fingerprint.md  --tags="python" ${AUTHOR} --d=./python/applications --w=10
	${CONVERT} --file=${BASE}/facedetection/facedetection.md  --tags="python" ${AUTHOR} --d=./python/applications --w=10
