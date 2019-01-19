#
# USE ARCHLINUX
#
FROM base/archlinux

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
#
# INSTALL PYTHON 3.7.2
#
RUN yes | pacman -Sy python
RUN yes | pacman -Sy python-pip
#
# INSTALL PANDOC
#
RUN yes | pacman -S pandoc
RUN yes | pacman -S pandoc-citeproc
RUN yes | pacman -S pandoc-crossref
#
# INSTALL npm
#
RUN yes | pacman -S npm
