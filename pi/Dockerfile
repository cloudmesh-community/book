#
# create:
#    docker build -t cm-book  .
#
# run:
#   cd book/pi
#   docker run -v `pwd`/dest:/book/pi/dest  -it ubuntu-18 bash 
#
FROM ubuntu:18.04
MAINTAINER Gregor von Laszewski <laszewski@gmail.com>


RUN apt-get update -q && apt-get install -qy \
    build-essential \
    software-properties-common \
    git-core \
    wget \
    curl \
    emacs \
    python-dev \
    python-pip \
    graphviz \
    rsync \
    nodejs \
    npm \
    libnss3-dev \
    libxss1 \
    chromium-browser

RUN npm install minimatch@3.0.2 --save-dev

RUN wget https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-2.2.1-linux.tar.gz

RUN tar xvzf pandoc-2.2.1-linux.tar.gz --strip-components 1 -C /usr/local

RUN npm install --global mermaid-filter

RUN git clone https://github.com/cloudmesh-community/book.git