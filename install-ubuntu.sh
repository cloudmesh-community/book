#
# INSTALL FOR UBUNTU 18.10
#
#
# wget https://raw.githubusercontent.com/cloudmesh-community/book/master/install-ubuntu.sh
#
sudo apt-get install -y python3.7
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 10
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
sudo update-alternatives --config python3

sudo apt-get install -y python3-pip
pip3 install pip3 -U
ln -s /usr/bin/pip3 /usr/bin/pip


cd book
pip install -r requirements.txt
cd




sudo apt-get install haskell-platform -y

wget -qO- https://github.com/jgm/pandoc/releases/download/2.5/pandoc-2.5-linux.tar.gz
sudo tar xvzf pandoc-2.5-linux.tar.gz --strip-components 1 -C /usr/local

cabal update
cabal install pandoc-crossref

python --version
pip --version
pandoc --version

#sudo wget -qO- https://get.haskellstack.org/ | sh

# add this also to your .bashrc file
#export PATH="$HOME/root/.local/bin:$HOME/.cabal/bin:${PATH}"
#echo  'PATH="$HOME/root/.local/bin:$HOME/.cabal/bin:${PATH}' > .bashrc

#cabal update
# for vagrant
#stack setup

#sudo chown $USER .cabal
#sudo chgrp $USER .cabal

#
# install pandoc via cabal
#
#cabal install cabal-install
#cabal update
#cabal install pandoc
#cabal install pandoc-citeproc
#cabal install pandoc-crossref



