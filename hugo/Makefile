AUTHOR=--author="Gregor von Laszewski (laszewski@gmail.com)"
EDITOR=--author="Editor: Gregor von Laszewski (laszewski@gmail.com)"
BASE=../chapters/prg/python
CHAPTERS=../chapters
CONVERT_PLAIN=python convert.py
CONVERT=python convert.py --crossref true
DEST=.
DEST=../../cybertraining-dsc.github.io/content/en/docs/book
URL=https://github.com/cloudmesh-community/book/raw/main/chapters


all:
	${CONVERT_PLAIN} --d=${DEST}/python --w=10 --index=Python ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/cloudmesh --w=11 --index=Cloudmesh ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/data --w=12 --index=Data ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/mongo --w=13 --index=Mongo ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/other --w=14 --index=Other ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/applications --w=15 --index=Applications ${AUTHOR}
	${CONVERT_PLAIN} --d=${DEST}/python/libraries --w=16 --index=Libraries ${AUTHOR}
	#
	${CONVERT} --file=${BASE}/python-intro.md \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=1 \
		--url=${URL}/prg/python/python-intro.md
	${CONVERT} --file=${BASE}/python-install.md \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=2 \
		--url=${URL}/prg/python/python-install.md 
	${CONVERT} --file=${BASE}/python-interactive.md \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=3 \
		--url=${URL}/prg/python/python-interactive.md
	${CONVERT} --file=${BASE}/python-editor.md \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=4 \
		--url=${URL}/prg/python/python-editor.md
	${CONVERT} --file=${BASE}/google-colab/python-google-colab.md \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=5 \
		--url=${URL}/prg/python/google-colab/python-google-colab.md 
	# - LANGUAGE:
	${CONVERT} --file=${BASE}/python.md  \
		--tags="python" ${AUTHOR} --d=${DEST}/python --w=6 \
		--url=${URL}/prg/python/python.md


	#cloudmesh  - CLOUDMESH:
	${CONVERT} --file=${BASE}/cloudmesh/introduction.md  \
		--tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=10 \
		--url=${URL}/prg/python/cloudmesh/introduction
	${CONVERT} --file=${BASE}/cloudmesh/installation.md  \
		--tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=12 \
		--url=${URL}/prg/python/cloudmesh/installation.md
	${CONVERT} --file=${BASE}/cloudmesh/console.md  \
		--tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=14 \
		--url=${URL}/prg/python/cloudmesh/console.md
	${CONVERT} --file=${BASE}/cloudmesh/dict.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=16 \
		--url=${URL}/prg/python/cloudmesh/dict.md
	${CONVERT} --file=${BASE}/cloudmesh/shell.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=18 \
		--url=${URL}/prg/python/cloudmesh/shell.md
	${CONVERT} --file=${BASE}/cloudmesh/stopwatch.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=20 \
		--url=${URL}/prg/python/cloudmesh/stopwatch.md
	${CONVERT} --file=${BASE}/cloudmesh/python-cmd5.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=22 \
			  --url=${URL}/prg/python/cloudmesh/python-cmd5.md
	${CONVERT} --file=${BASE}/cloudmesh/exercises.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=24 \
		--url=${URL}/prg/python/cloudmesh/exercises.md
	#	${CONVERT} --file=${BASE}/cloudmesh/config.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=26
	#	${CONVERT} --file=${BASE}/cloudmesh/inventory.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=28
	#	${CONVERT} --file=${BASE}/cloudmesh/python-cloudmesh.md  --tags="python" ${AUTHOR} --d=${DEST}/python/cloudmesh --w=30
	#  - LIBRARIES:
	${CONVERT} --file=${BASE}/python-libraries.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=25 \
		--url=${URL}/prg/python/python-libraries.md
	${CONVERT} --file=${BASE}/python-data.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=26 \
		--url=${URL}/prg/python/python-data.md
	${CONVERT} --file=${BASE}/python-matplotlib.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=27 \
		--url=${URL}/prg/python/python-matplotlib.md
	${CONVERT} --file=${BASE}/python-docopts.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=28 \
		--url=${URL}/prg/python/python-docopts.md
	${CONVERT} --file=${BASE}/opencv/opencv.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=29 \
		--url=${URL}/prg/python/python-opencv.md
	${CONVERT} --file=${BASE}/opencv/secchi.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=30 \
		--url=${URL}/prg/python/opencv/secchi.md
	# - DATA:
	${CONVERT} --file=${CHAPTERS}/data/formats.md  --tags="python" ${AUTHOR} --d=${DEST}/python/data --w=31 \
		--url=${URL}/data/formats.md

	# - MONGO:
	${CONVERT} --file=${CHAPTERS}/data/mongodb.md  --tags="python" ${AUTHOR} --d=${DEST}/python/mongo --w=32 \
		--url=${URL}/data/mongodb.md
	${CONVERT} --file=${CHAPTERS}/data/mongoengine.md  --tags="python" ${AUTHOR} --d=${DEST}/python/mongo --w=33 \
		--url=${URL}/data/mongoengine.md
	# - OTHER:
	${CONVERT} --file=${BASE}/python-wordcount.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=34 \
		--url=${URL}/prg/python/python-wordcount.md
	${CONVERT} --file=${BASE}/numpy/numpy.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=35 \
		--url=${URL}/prg/python/numpy/numpy.md
	${CONVERT} --file=${BASE}/scipy/scipy.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=36 \
		--url=${URL}/prg/python/scipy/scipy.md
	${CONVERT} --file=${BASE}/scikit-learn/scikit-learn.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=37 \
			--url=${URL}/prg/python/scikit-learn/scikit-learn.md
	${CONVERT} --file=${BASE}/random-forest/random-forest.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=38 \
		--url=${URL}/prg/python/random-forest/randomforest.md
	${CONVERT} --file=${BASE}/python-parallel.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=39 \
		--url=${URL}/prg/python/python-parallel.md
	${CONVERT} --file=${BASE}/dask/dask.md  --tags="python" ${AUTHOR} --d=${DEST}/python/other --w=40 \
		--url=${URL}/prg/python/dask/dask.md
	#- APPLICATIONS:
	${CONVERT} --file=${BASE}/fingerprint/fingerprint.md  --tags="python" ${AUTHOR} --d=${DEST}/python/applications --w=41 \
		--url=${URL}/prg/python/fingerprint/fingerprint.md
	${CONVERT} --file=${BASE}/facedetection/facedetection.md  --tags="python" ${AUTHOR} --d=${DEST}/python/applications --w=42 \
		--url=${URL}/prg/python/facedetection/facedetection.md



t:
	${CONVERT} --file=${BASE}/google-colab/python-google-colab.md  --tags="python" ${AUTHOR} --d=${DEST}/python --w=45 \
		--url=${URL}/prg/python/google-colab/python-google-colab.md

s:
	${CONVERT} --file=${BASE}/opencv/secchi.md  --tags="python" ${AUTHOR} --d=${DEST}/python/libraries --w=30 \
		--url=${URL}/prg/python/opencv/secchi.md --crossref true


	#    - ${BASE}/python-install-pyenv.md"
