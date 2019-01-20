#
# DEVELOPMENT TOOLS
#
yes | pacman -Sy gcc
yes | pacman -Syu wget
yes | pacman -Sy curl
yes | pacman -Sy rsync
yes | pacman -Sy git
yes | pacman -Sy graphviz
yes | pacman -Sy make
#
# INSTALL PYTHON 3.7.2
#
yes | pacman -Sy python
yes | pacman -Sy python-pip
#
# INSTALL PANDOC
#
yes | pacman -S pandoc
yes | pacman -S pandoc-citeproc
yes | pacman -S pandoc-crossref
#
# INSTALL npm
#
#yes | pacman -S npm
