FROM ubuntu:18.04

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

RUN apt-get update -y
RUN apt-get install graphviz -y
RUN apt-get install python-pip -y
RUN apt-get install wget -y
RUN apt-get install curl -y
RUN pip install pip -U
RUN apt-get install git-core -y
RUN apt-get install dnsutils -y

RUN apt-get install haskell-platform -y
RUN apt-get install pandoc -y
RUN apt-get install pandoc-citeproc -y

RUN apt-get install -y build-essential libssl-dev libffi-dev

RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip setuptools
RUN pip3 install --upgrade pip setuptools


RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
RUN update-alternatives --config python

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10
RUN update-alternatives --config pip

RUN yes '' | update-alternatives --force --all


#RUN apt-get install -y python3-dev
#RUN apt-get install -y python3-venv





# RUN pip install pandoc-fignos

# RUN git clone https://github.com/cloudmesh-community/book.git

# RUN cd book; pip install -r requirements.txt