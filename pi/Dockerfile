#
# create:
#    docker build -t cm-book  .
#
# run:
#   cd book/pi
#   docker run --user='cm' -v $PWD/dest:/home/cm/book/pi/dest  -it cm-book bash 
#
FROM ubuntu:18.04
MAINTAINER Gregor von Laszewski <laszewski@gmail.com>




RUN apt-get update -q && apt-get install -qy \
    build-essential \
    software-properties-common \
    sudo \
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
    chromium-browser \
    yarn


RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list


RUN groupadd --gid 1000 cm \
  && useradd --uid 1000 --gid cm --shell /bin/bash --create-home cm \
  && echo "cm:cm" | chpasswd
  
RUN adduser cm sudo



RUN wget -q https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-2.2.1-linux.tar.gz

RUN tar xvzf pandoc-2.2.1-linux.tar.gz --strip-components 1 -C /usr/local


RUN npm install --global mermaid-filter
RUN npm install -g minimatch

USER cm

WORKDIR /home/cm

RUN git clone https://github.com/cloudmesh-community/book.git

WORKDIR /home/cm/book/pi


