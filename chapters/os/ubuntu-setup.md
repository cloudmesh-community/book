# Ubuntu Setup

Prerequisit Ubuntu 19.10, it will likely work also with 18.04

Note this is an experimental Ubuntu setup on a vanilla 
Ubuntu machine. Although we have not tried this, this also 
works in a docker container (excluding graphics programs and 
installs. If you use a container you must have at least 2GB 
memory for it. If you do not have this you can set an Ubuntu VM 
up in a cloud. 

## Ip Address

``` bash
ip address show
```


## Update ubuntu

``` bash
sudo apt update && sudo apt upgrade -y
```

## System Hardware (general)

``` bash
$ sudo apt-get install -y hwinfo
$ hwinfo
$ free -m
$ vmstat -s
```

## System Hardware (Specific)

Do not execute, this is syetem specific if you have an NVIDIA card in
the computer.

``` bash
$ apt search nvidia-driver*
$ ubuntu-drivers devices
$ sudo ubuntu-drivers autoinstall
```

For an RTX2060 this can be done alternatively

``` bash
$ ubuntu-drivers devices
$ sudo apt install nvidia-driver-435
```

## Git

``` bash
$ sudo apt-get install git
```

## SSH Server

``` bash
$ sudo apt install openssh-server
$ sudo systemctl status ssh
$ ssh-keygen
```

### Some convenient SSH management commands

Not used was it seems to be on by default

``` bash
$ sudo ufw allow ssh
```

If you need to Stop ssh

``` bash
$ sudo systemctl start ssh
```

If you need to Start ssh

``` bash
$ sudo systemctl stop ssh
```

If you need to disable it (after a boot)

``` bash
$ sudo systemctl disable ssh
```

If you need to enable is (after a boot)

``` bash
$ sudo systemctl enable ssh
```

## LaTex 

``` bash
$ sudo apt-get install texlive-full
```

## Emacs

On Ubuntu you have `gedit`, put if you like to install 
emacs, please use.

``` bash
sudo apt install emacs
```

## Python

``` bash
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev     libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
$ mkdir /opt
$ cd /opt
$ sudo wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
$ sudo tar xzf Python-3.8.2.tgz
$ cd Python-3.8.2
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
$ sudo rm Python-3.8.2.tgz
$ python3.8 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
$ pip install pip -U 
```

## Cloudmeh

You must remmeber to have an ssh key generated.

``` bash
$ pip install cloudmesh-installer
$ time cloudmesh-installer get openstack
$ cms help
$ cms gui quick
$ cms init
```

## Cloudmesh and Chameleon cloud

1. We assume you do not have any keys on chameleoncloud. 
   If you do, please delete them. IN general you will not.
2. We assume that you have successfully logged into chameleon 
   cloud and used Horizon.
3. We assume you use and remember your chameleon cloud 
   password in `cms gui quick` that is the same username and 
   password from your `chameleon.org` dashboard
   
``` bash
$ cms key upload --cloud=chameleon
```   

Now you can use chameleon

``` bash
$ cms vm list --refresh
$ cms flavor list --refresh
$ cms image list --refresh
```

## VNC (Optional)

If you need to connect to this ubuntu via a remote app from another
computer and need the Desktop

Opion A: tightvnc

``` bash
sudo apt install tightvncserver
```

``` bash
sudo apt install tigervnc-standalone-server tigervnc-common
```

Using it. start 

``` bash
vncserver
```

Use 

```
ssh -L 5901:127.0.0.1:5901 -N -f -l username hostname
```

Then in real vnc, esablish a connection to

`localhost:5901`


## OpenStack

The instruction on their Web Page does not work

``` bash
$ sudo snap install microstack --classic --edge
$ sudo microstack.init --auto
```

Instead try 

```bash
$ sudo snap refresh microstack --devmode --edge
$ sudo microstack.init --auto
$ sudo snap alias microstack.openstack openstack
```

Now go to you web browser and type in 

10.20.20.1

username: admin
password: keystone

Chnage your password in horizon

Now you have your own openstack on your computer. However we have not 
done any configuration. For the class we recommend to use chameleon 
cloud as everything is set up there.

Disable

```
sudo snap disable microstack
```

Enable

```
sudo snap enable microstack
```

Access on a remote server

```
$ sudo ssh -N -L 8001:10.20.20.1:80 <user>@<server-ip>
```

## Docker

``` bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
```

## Monitoring

Here we introduce you to some commanlins sensor tools for Linux

Some additional tools can be found here:

* <https://linoxide.com/monitoring-2/10-tools-monitor-cpu-performance-usage-linux-command-line/>

### Top

```bash
$ top
```

![Top](images/top.png)


### Temperature Sensors

```bash
sudo apt install lm-sensors hddtemp
sudo sensors-detect
sudo /etc/init.d/kmod start
sensors
```

Continious watching 

``` bash
watch -n 1 sensors
```


![Nmon](images/sensors.png)


### Loadavg

```
cat /proc/loadavg
```

### Sysstat

```
apt-get install sysstat
```

### NMon

``` bash
sudo apt-get install nmon
nmon
```

![Nmon](images/nmon.png)


### Monitoring NVIDIA GPU

```
watch -n 2 nvidia-smi
````

![Nmon](images/nvidia-smi.png)

### Glances

```
$ curl -L https://bit.ly/glances | /bin/bash
$ glances
```

### CPU Info

```
$ lscpu
```

## AI


## CUDA

This seems not be needed as it was already installed?

If NVIDIA Card 

``` bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

### PyTorch


```
$ pip install torch torchvision
```

## Benchmark

* <https://linuxconfig.org/how-to-benchmark-your-linux-system>

### Sysbench

```
sudo apt install sysbench
```

```
$ sysbench cpu run
sysbench 1.0.17 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Prime numbers limit: 10000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:  1764.17

General statistics:
    total time:                 10.0003s
    total number of events:     17644

Latency (ms):
         min:                       0.56
         avg:                       0.57
         max:                       0.70
         95th percentile:           0.57
         sum:                    9998.87

Threads fairness:
    events (avg/stddev):         17644.0000/0.00
    execution time (avg/stddev): 9.9989/0.00
```

```
$ sysbench memory run
sysbench 1.0.17 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Running memory speed test with the following options:
  block size: 1KiB
  total size: 102400MiB
  operation: write
  scope: global

Initializing worker threads...

Threads started!

Total operations: 86544533 (8653618.73 per second)

84516.15 MiB transferred (8450.80 MiB/sec)


General statistics:
    total time:                          10.0000s
    total number of events:              86544533

Latency (ms):
         min:                                    0.00
         avg:                                    0.00
         max:                                    0.01
         95th percentile:                        0.00
         sum:                                 4856.67

Threads fairness:
    events (avg/stddev):           86544533.0000/0.00
    execution time (avg/stddev):   4.8567/0.00
```

### Geekbench

Will send in the free version information to its web server

``` bash
wget http://cdn.geekbench.com/Geekbench-5.1.0-Linux.tar.gz
tar xvf Geekbench-5.1.0-Linux.tar.gz 
```

Than you get a link such as

* <https://browser.geekbench.com/v5/cpu/1491413>
* <https://browser.geekbench.com/v5/cpu/1491459>

## Phoronix-test-suite
 
```
$ phoronix-test-suite install john-the-ripper
$ phoronix-test-suite run john-the-ripper
$ phoronix-test-suite install luxmark
$ phoronix-test-suite run luxmark
```

See also 

* <https://linuxconfig.org/benchmark-your-graphics-card-on-linux>


## Kubeflow

```
sudo snap install microk8s --classic

microk8s v1.17.3 from Canonical✓ installed

$ sudo microk8s.status --wait-ready
microk8s is running
addons:
cilium: disabled
dashboard: disabled
dns: disabled
fluentd: disabled
gpu: disabled
helm3: disabled
helm: disabled
ingress: disabled
istio: disabled
jaeger: disabled
juju: disabled
knative: disabled
kubeflow: disabled
linkerd: disabled
metallb: disabled
metrics-server: disabled
prometheus: disabled
rbac: disabled
registry: disabled
storage: disabled

$ sudo microk8s.enable dns dashboard registry
```

To disable

```
$ sudo microk8s.disable dns dashboard registry
```