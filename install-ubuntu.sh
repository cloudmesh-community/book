sudo apt-get install -y python3-dev
sudo apt-get install -y python3-venv

sudo apt-get install haskell-platform -y
sudo wget -qO- https://get.haskellstack.org/ | sh

sudo cabal update
sudo stack setup
PATH="$HOME/root/.local/bin:$HOME/.cabal/bin:${PATH}"

SOFTWARE=pandoc-2.5
cd $HOME
wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
tar xvzf ${SOFTWARE}.tar.gz
cd ${SOFTWARE}
RUN stack init
RUN stack install

SOFTWARE=pandoc-citeproc-0.15.0.1
cd $HOME
wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
tar xvzf ${SOFTWARE}.tar.gz
cd ${SOFTWARE}
stack init
stack install

SOFTWARE=pandoc-crossref-0.3.4.0
cd $HOME
wget http://hackage.haskell.org/package/${SOFTWARE}/${SOFTWARE}.tar.gz
tar xvzf ${SOFTWARE}.tar.gz
cd ${SOFTWARE}
stack init
stack install




