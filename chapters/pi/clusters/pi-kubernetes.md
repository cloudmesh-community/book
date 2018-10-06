# Kubernetes (A) :o: :hand: fa18-516-03

In this section we discuss how to set up a kubernetes cluster on a
number of Raspberry Pi's.

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real kubernetes install.
- [ ] we have two sections of kubernetes contributed by two students. What we need is to merge them and safe the usable things. We need to identify if the setup is significantly different before we can do this.
- [ ] so before you can work on the kubernetes section you need to make sure the NOW section is up to date.

## Resources Needed

We recommend that the cluster will have at least one master and three
worker nodes. Using less resources so the system is not unnecessarily
slow. Please give us feedback on this and let us know what works for
you. So we integrate your feedback.

We assume that you have installed docker and disabled swap

First install docker, disable swap, install kubeadm

All the following steps are made automatically by the
[`526/docker_kubernetes_install.sh`](526/kubernetes/docker_kubernetes_install.sh) script.

### Install docker

In order to install kubernetes you first need to have docker installed. This is
very straightforward.

### Disable swap memory

(TODO `fa18-516-03`: Where is this information from? I don't see this online - I
see that kubernetes does not support swap memory but not Docker. It looks like
Docker can be configured directly to disable swap memory
[--memory-swap](https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details) instead
of disabling swap for the entire OS.)

Docker is **not compatible with SWAP memory**, therefore we need to disable swap.
This might create some other issues. If you encounter them you should
try to reboot the cluster again, if that fails change line 16 in the
`docker_kubernetes_install.sh`

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1"
```

to

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=memory"
```

### Installing kubernetes administrator

Finally, to configure kubernetes you'll need kubeadm. Now the Pi needs to be 
rebooted.

---

:warning: **All of this will be done by the script, donot worry** (maybe worry)

---


### Configure the nodes

All of the above needs to be done in each node as-well. The script

* [kubernetes/copy_dk_kub_install_script_to_nodes.sh](kubernetes/copy_dk_kub_install_script_to_nodes.sh)

should copy the needed script to each of them and run it. It is set up
to work with 4 nodes named `rp<number>` with pi as the username (the
numbers start at 1 because the head node is rp0). Changing the number
of nodes is trivial, if all of your nodes have the same username it is
also trivial.


If your nodes are not configured like that you'll need to change this
script or copy `docker_kubernetes_install.sh` to each of the nodes
manually.  We plan on making this script independent on the number of
nodes.

## Files


* [417/kubernetes/adm_kub_config.yaml](417/kubernetes/adm_kub_config.yaml)
* [417/kubernetes/config_kub.sh](417/kubernetes/config_kub.sh)
* [417/kubernetes/copy_dk_kub_install_script_to_nodes.sh](417/kubernetes/copy_dk_kub_install_script_to_nodes.sh)
* [417/kubernetes/docker_kubernites_install.sh](417/kubernetes/docker_kubernites_install.sh)
* [417/kubernetes/issues_todo.md](417/kubernetes/issues_todo.md)
* [417/kubernetes/kube_install_and_config_readme.md](417/kubernetes/kube_install_and_config_readme.md)
* [417/kubernetes/useful_links.txt](417/kubernetes/usefull_links.txt)

## Refernces

* <https://gist.github.com/alexellis/fdbc90de7691a1b9edb545c17da2d975>
* <https://cloud.google.com/solutions/real-time/kubernetes-redis-bigquery>
* <https://kubecloud.io/setup-a-kubernetes-1-9-0-raspberry-pi-cluster-on-raspbian-using-kubeadm-f8b3b85bc2d1>
* <https://www.hanselman.com/blog/HowToBuildAKubernetesClusterWithARMRaspberryPiThenRunNETCoreOnOpenFaas.aspx>
* <https://marcussmallman.io/2018/02/18/diy-rasberry-pi-kubernetes-cluster/>


# Raspberry Pi Kubernetes Cluster (B) :o: :hand: fa18-516-03

This section will guide the steps towards setting up a Kubernetes Pi cluster.
The steps are:

a. Setting up static IP
b. Secure ssh key setup for communication
c. Kubernetes cluster setup
d. Automating the process

Cluster needs:

*  One head/master Pi
*  number of follower nodes Pi
*  router [optional]

Pis can be connected directly to the home's Internet router.
Please note that a router is needed when portability is a criteria. 

## Initial Setup

Some Pi kits come with pre installed SD card if not then:

1. format the SD card: <https://www.sdcard.org/downloads/formatter_4/eula_windows/>
2. Download the package from: <https://www.raspberrypi.org/downloads/noobs/>
3. Download and unzip the package and copy it to the SD card
   (Copy only the files inside NOOBS_{version})
4. Connect the power cable, keyboard and mouse to the Pi
5. Insert the SD card and the installed will walk you through the
   installation process
6. Once the installation is through make sure the time and keyboard
   setting are updated according to your local settings Normally they
   come in UK settings
   

## Setting up Static IP and HostName

The hostname can be given by clicking the top right

`wifi icon> network setting>`

The window can be launched by

```bash
    $ raspi-config
```

command i the terminal or by:

```
    $ sudo nano /etc/hostname
```
    
static IP similarly can be given by

:warning: TODO: sentence incomplete

Hostname can be given by clicking the top right

`wifi icon> network setting>`

make sure you give both `eth0` and `wlan0` setting for both LAN and
Wifi communication

or by ensuring the following in for LAN and Wifi
config `/etc/dhcpcd.conf`

:warning: TODO no I in the text

I have added the following alternatively eth0 block can be added if
wired setup is preferred

```
interface wlan0
static ip_address=<desired IP>/24
static routers=<router IP>
static domain_name_servers=<DNS server IP>
```

Ensure that the desired IP falls with in the assigned IP range of your
router.  As we will be automating the process later, its advised to
follow a naming sequence for the hostname or IP address.

Example:

`kub00[192.168.56.100], kub01 [192.168.56.101], kub02 [192.168.56.102]...`

It is essential to `reboot` the system for the changes to take
effect.


## SSH setup


* Ensure that ssh is enabled in the Pi:

  - Click on the ```Raspberry Pi Configuration``` from the ```Preferences``` on run the command 
      
    ```sudo raspi-confi``` 
        
    in the terminal. Go to Interface tab and enable SSH
  - In the terminal run:
    ```
    sudo systemctl enable ssh
    sudo systemctl start ssh
    ```

  With the static ip setup and ssh enabled you should be able to ssh
  in to the Pi. For passwordless access setup the SSH key as per the
  following step

* Generate the ssh key; make sure you give a passcode:
        ```
          ssh-keygen -t rsa 
        ```
  Copy the generated public key ``~/.ssh/id_rsa.pub` to the other computers for passwordless acess
  ``ssh-copy-id`` or ``ssh-import-id`` can be used for the purpose as well
  
## Cluster setup

First install Docker with 
  
  ``
  curl -sSL get.docker.com | sh && \
  sudo usermod pi -aG docker
  ``
  
  [optional] Command to run Docker as a non root user:
  ``
  sudo usermod -aG docker pi
  ``
  
Next turn off swap:
  
  ```
  sudo dphys-swapfile swapoff && \
  sudo dphys-swapfile uninstall && \
  sudo update-rc.d dphys-swapfile remove
  ```

Now Edit /boot/cmdline.txt and add the following with a space
[no new line]

```
cgroup_enable=cpuset cgroup_memory=1
```

Setup kubeadm with
  
```
  $ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
  echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list && \
  sudo apt-get update -q && \
  sudo apt-get install -qy kubeadm
```
  
The process till now stays the same for both workers and master
  
## Master setup
  
In the master node initiate the master:
  
```
    $ sudo kubeadm init --token-ttl=0 --apiserver-advertise-address=<internal master ip>
```
  
This will initiate the kubectl head. At the end of the this process,
there should be an echo with the following text. Save this join token
as you will joining the workers later:

```
    $ kubeadm join --token <token> --discovery-token-ca-cert-hash <ca hash>
```

Once the master is initiated, now set up the kubectl admin config

```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

The final step is setting up the networking. I have used weave.

```
  kubectl apply -f \
 "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```
  
## Worker setup
  
After Kubernetes installation, join the workers using the saved join token.
  
Use `get nodes` in the master to check the status
  
  `kubectl get pods --namespace=kube-system` can be used to check the pod status of the cluster
  
