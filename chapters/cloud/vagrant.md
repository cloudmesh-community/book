# Vagrant


FROM <https://www.vagrantup.com/intro/index.html>:
"Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.

If you are already familiar with the basics of Vagrant, the documentation provides a better reference build for all available features and internals."

<https://app.vagrantup.com/ubuntu/boxes/bionic64>


```
vagrant init ubuntu/bionic64
vagrant up
vagrant ssh
```

Default verssion:

vagrant@ubuntu-bionic:~$ python3 --version
Python 3.6.5


sudo apt-get install python3.6
sudo apt-get install idle-python
sudo apt-get install python3-pip

sudo apt-get install python3.7

python3.7 --version

alias python=python3


vagrant status
vagrant destroy
vagrant suspend
vagrant resume
