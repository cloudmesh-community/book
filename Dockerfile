#
# USE UBUNTU 18.10
#
FROM base/archlinux

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

#RUN yes | pacman -Sy cc
#RUN yes | pacman -Sy yy
RUN yes | pacman -Sy gcc
RUN yes | pacman -Syu wget
RUN yes | pacman -Sy curl
RUN yes | pacman -Sy rsync
RUN yes | pacman -Sy git
RUN yes | pacman -Sy graphviz
RUN yes | pacman -Sy python
RUN yes | pacman -Sy python-pip
RUN yes | pacman -Sy make

RUN yes | pacman -S pandoc
RUN yes | pacman -S pandoc-citeproc
RUN yes | pacman -S pandoc-crossref

RUN yes | pacman -S npm

#RUN npm install --save-dev puppeteer
#RUN npm install --global mermaid-filter
#RUN npm install --global pandoc-index


#
# DEVELOPMENT TOOLS
#
#RUN apt-get update -y
#RUN apt-get install graphviz -y
#RUN apt-get install python-pip -y
#RUN apt-get install wget -y
#RUN apt-get install curl -y
#RUN apt-get install rsync -y
#RUN pip install pip -U
#RUN apt-get install git-core -y
#RUN apt-get install dnsutils -y
#RUN apt-get install -y build-essential libssl-dev libffi-dev

#
# INSTALL PYTHON 3.7.1
#
#RUN apt-get install -y python3.7
#RUN apt-get install -y python3-pip
#RUN pip install --upgrade pip setuptools
#RUN pip3 install --upgrade pip setuptools
#RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
#RUN update-alternatives --config python
#RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10
#RUN update-alternatives --config pip
#RUN yes '' | update-alternatives --force --all

#
# INSTALL PANDOC
#
#RUN apt-get install haskell-platform -y
#RUN wget -qO- https://get.haskellstack.org/ | sh

#RUN cabal update
#RUN stack setup
#ENV PATH="$HOME/root/.local/bin:$HOME/.cabal/bin:${PATH}"

#ENV SOFTWARE=pandoc-2.5
#RUN cd $HOME
#RUN wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
#RUN tar xvzf ${SOFTWARE}.tar.gz
#RUN cd ${SOFTWARE}
##RUN stack init
##RUN stack install

#ENV SOFTWARE=pandoc-citeproc-0.15.0.1
#RUN cd $HOME
#RUN wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
#RUN tar xvzf ${SOFTWARE}.tar.gz
#RUN cd ${SOFTWARE}
#RUN stack init
#RUN stack install

#ENV SOFTWARE=pandoc-crossref-0.3.4.0
#RUN cd $HOME
#RUN wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
#RUN tar xvzf ${SOFTWARE}.tar.gz
#RUN cd ${SOFTWARE}
#RUN stack init
#RUN stack install

#RUN cabal install pandoc-crossref
#RUN cabal install pandoc-citeproc

# RUN pip install pandoc-fignos

#RUN apt-get install -y python3-dev
#RUN apt-get install -y python3-venv


# RUN git clone https://github.com/cloudmesh-community/book.git
# RUN cd book; pip install -r requirements.txt