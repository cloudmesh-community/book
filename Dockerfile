#
# USE ARCHLINUX
#
FROM archlinux/base:latest

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

#
# DEVELOPMENT TOOLS
#
#RUN yes | pacman -Sy cc
#RUN yes | pacman -Sy yy
RUN yes | pacman -Sy gcc
RUN yes | pacman -Syu wget
RUN yes | pacman -Sy curl
RUN yes | pacman -Sy rsync
RUN yes | pacman -Sy git
RUN yes | pacman -Sy graphviz
RUN yes | pacman -Sy make
RUN yes | pacman -Sy biber
RUN yes | pacman -Sy emacs
RUN yes | pacman -Sy lsb-release

ENV PATH="${PATH}:/usr/bin/vendor_perl"
#
# INSTALL PYTHON 3.7.2
#
RUN yes | pacman -Sy python
RUN yes | pacman -Sy python-pip

RUN pip install pandoc-mustache
RUN pip install pprint
RUN pip install oyaml
RUN pip install treelib
RUN pip install docopt
RUN pip install mkdocs
RUN pip install emoji

#
# INSTALL PANDOC
#
RUN yes | pacman -Sy pandoc
RUN yes | pacman -Sy pandoc-citeproc
RUN yes | pacman -Sy pandoc-crossref

RUN yes | pacman -Sy which
RUN yes | pacman -Sy openssh
RUN yes | pacman -Sy calibre 

RUN pip install cyberaide-bookmanager
#
# INSTALL npm
#
#RUN yes | pacman -S npm
