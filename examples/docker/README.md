docker run --name travis-debug -dit travisci/ci-garnet:packer-1512502276-986baf0 /sbin/init

docker exec -it travis-debug bash -l
su - travis
git clone https://github.com/cloudmesh/book.git

pyenv versions
pyenv global 3.6.2

sudo apt update
sudo apt upgrade

sudo add-apt-repository ppa:jonathonf/texlive-2016
sudo apt-get texlive-full




docker run --name u16 -dit ubuntu:16.04 /sbin/init
docker exec -it u16 bash -l
apt-get update
apt-get upgrade -y
apt-get install -y build-essential
apt-get install -y software-properties-common
add-apt-repository universe

apt-get install -y dist-upgrade


# apt-get install -y python3
apt-get install -y wget
apt-get install -y texlive-full
apt-get install -y git
apt-get install -y curl
apt-get install -y pandoc
apt-get install -y latexmk
apt-get install -y emacs
apt-get install -y libssl-dev
#apt-get install -y bzip2-devel
apt-get install -y libpng-dev
apt-get install -y zlib1g-dev

# update-alternatives --install /usr/bin/python python /usr/bin/python3 10

curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

save to .bash_profile

export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

---
pyenv install -l

pyenv install 3.6.4
pyenv global 3.6.4
wget https://bootstrap.pypa.io/get-pip.py
python ./get-pip.py

WARNING: The Python bz2 extension was not compiled. Missing the bzip2 lib?
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
WARNING: The Python sqlite3 extension was not compiled. Missing the SQLite3 lib?




docker kill u16
docker rm u16
docker build -t u16 .
docker run --name u16 -dit u16 /sbin/init
docker exec -it u16 bash -l

docker build -t cloudmesh .
docker run --name u16 -dit cloudmesh /sbin/init
docker exec -it u16 bash -l
