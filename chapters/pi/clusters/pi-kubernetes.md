# Kubernetes (A) :o: :hand: fa18-516-03

In this section we will discuss how to set up a Kubernetes cluster on a
number of Raspberry Pis.

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real Kubernetes install.
- [ ] we have two sections of Kubernetes contributed by two students. What we need is to merge them and save the usable things. We need to identify if the setup is significantly different before we can do this.
- [ ] so before you can work on the Kubernetes section you need to make sure the NOW section is up to date.

## Resources Needed

We recommend that the cluster will have at least one master and three worker
nodes. The test should not use too many resources otherwise the system may be
unnecessarily slow. In particular we should have one dedicated master. We use
three nodes to support testing the distribution of containers. (It may work with
two, but we have not tested it). Please give us feedback on this and let us know
what works for you. We will integrate your feedback.

We assume that you have installed docker and disabled swap

First install docker, disable swap, install kubeadm

All the following steps are made automatically by the
[`526/docker_kubernetes_install.sh`](526/kubernetes/docker_kubernetes_install.sh) script.

### Install docker

First install Docker with
  
  ``
  $ curl -sSL get.docker.com | sh && \
  sudo usermod pi -aG docker
  ``

  [optional] Command to run Docker as a non root user:
  ``
  $ sudo usermod -aG docker pi
  ``

### Disable swap memory

Kubernetes is **not compatible with SWAP memory**, therefore we need to disable
swap. This might create some other issues. If you encounter them you should try
to reboot the cluster again, if that fails change line 16 in the
`docker_kubernetes_install.sh`

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1"
```

to

```
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=memory"
```

Now Edit /boot/cmdline.txt and add the following with a space
[no new line]

```
 cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory
```

Next turn off swap for Kubernetes:

  ```
  $ sudo dphys-swapfile swapoff && \
  sudo dphys-swapfile uninstall && \
  sudo update-rc.d dphys-swapfile remove
  ```

You should now not see any entries in this command:

```
$ sudo swapon --summary
```

Now you *must reboot* before continuing with the rest of the section.

### Installing Kubernetes administrator

Finally, to configure Kubernetes you'll need kubeadm. Now the Pi needs to be 
rebooted.

---

:warning: **All of this will be done by the script, do not worry** (maybe worry)

---

### Cluster setup

Setup kubeadm with
  
```
  $ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && \
  echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list && \
  sudo apt-get update -q && \
  sudo apt-get install -qy kubeadm
```
  
The process till now stays the same for both workers and master
  
## Master setup

If your network is slow, you can pull the images first with:

```
$ sudo kubeadm config images pull
```

If you do not pull them , they will be downloaded during the master node initiation:

```
    $ sudo kubeadm init --token-ttl=0 --apiserver-advertise-address=<internal master ip>
```

This will initiate the kubectl head. At the end of the this process,
there should be an echo with the following text. Save this join token
as you will joining the workers later:

```
    $ sudo kubeadm join --token <token> --discovery-token-ca-cert-hash <ca hash>
```

TODO: jobranam (fa18-e516-03):
Received the following error/warning:
```
[WARNING RequiredIPVSKernelModulesAvailable]: the IPVS proxier will not
be used, because the following required kernel modules are not loaded: [ip_vs_sh
nf_conntrack_ipv5 ip_vs ip_vs_rr ip_vs_wrr] or no builtin kernel ipvs support:
map[ip_vs:{} ip_vs_rr:{} ip_vs_wrr:{} ip_vs_sh:{} nf_conntrack_ipv4:{}]
you can solve this problem with following methods:
 1. Run 'modprobe -- ' to load missing kernel modules;
2. Provide the missing builtin kernel ipvs support
```

This does not seem to be a problem, but it can be fixed by first running:

```bash
$ sudo modprobe ip_vs && \
  sudo modprobe ip_vs_sh && \
  sudo modprobe ip_vs_vs && \
  sudo modprobe ip_vs_rr && \
  sudo modprobe ip_vs_wrr && \
  sudo modprobe nf_conntrack_ipv4
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
  

After waiting a minute or so, you should see the following output from this
command:

```
 $ kubectl get pods --namespace=kube-system
NAME                             READY   STATUS    RESTARTS   AGE
coredns-576cbf47c7-hn55k         1/1     Running   0          4m51s
coredns-576cbf47c7-nvmm4         1/1     Running   0          4m51s
etcd-blue00                      1/1     Running   0          3m55s
kube-apiserver-blue00            1/1     Running   0          4m7s
kube-controller-manager-blue00   1/1     Running   0          4m5s
kube-proxy-9xwdn                 1/1     Running   0          4m51s
kube-scheduler-blue00            1/1     Running   0          4m
weave-net-xj4tc                  2/2     Running   0          73s
```


### Configure the nodes

All of the above needs to be done in each node as well. The script

* [kubernetes/526/bin/copy_dk_kub_install_script_to_nodes.sh](kubernetes/526/bin/copy_dk_kub_install_script_to_nodes.sh)

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


* [kubernetes/526/bin/adm_kub_config.yaml](https://github.com/cloudmesh-community/book/tree/master/chapters/pi/kubernetes/526/bin/adm_kub_config.yaml)
* [kubernetes/526/bin/config_kub.sh](https://github.com/cloudmesh-community/book/tree/master/chapters/pi/kubernetes/526/bin/config_kub.sh)
* [kubernetes/526/bin/copy_dk_kub_install_script_to_nodes.sh](https://github.com/cloudmesh-community/book/tree/master/chapters/pi/kubernetes/526/bin/copy_dk_kub_install_script_to_nodes.sh)
* [kubernetes/526/bin/docker_kubernites_install.sh](https://github.com/cloudmesh-community/book/tree/master/chapters/pi/kubernetes/526/bin/docker_kubernites_install.sh)


* [docker_setup.sh](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/install_docker.sh)
* [README.md](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/README.md)
* [dhcp_setup.sh](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/dhcp_setup.sh)
* [join](417/bin/join)
* [kube_head_setup.sh](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/kube_head_setup.sh)
* [kube_worker_setup.sh](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/kube_worker_setup.sh)
* [kubeadm_conf.yaml](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/kubeadm_conf.yaml)
* [opt_setup.sh](https://github.com/cloudmesh-community/book/blob/master/chapters/pi/kubernetes/417/bin/opt_setup.sh)



## References

* <https://gist.github.com/alexellis/fdbc90de7691a1b9edb545c17da2d975>
* <https://cloud.google.com/solutions/real-time/kubernetes-redis-bigquery>
* <https://kubecloud.io/setup-a-kubernetes-1-9-0-raspberry-pi-cluster-on-raspbian-using-kubeadm-f8b3b85bc2d1>
* <https://www.hanselman.com/blog/HowToBuildAKubernetesClusterWithARMRaspberryPiThenRunNETCoreOnOpenFaas.aspx>
* <https://marcussmallman.io/2018/02/18/diy-rasberry-pi-kubernetes-cluster/>
* <https://blog.hypriot.com/post/setup-kubernetes-raspberry-pi-cluster/>
* <https://blog.sicara.com/build-own-cloud-kubernetes-raspberry-pi-9e5a98741b49>


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

See Network of PIs

## Worker setup

After Kubernetes installation, join the workers using the saved join token.

Use `get nodes` in the master to check the status

```
$ kubectl get nodes
NAME     STATUS     ROLES    AGE     VERSION
blue00   Ready      master   22m     v1.12.2
blue01   Ready      <none>   7m37s   v1.12.2
blue02   NotReady   <none>   14s     v1.12.2
```

  `kubectl get pods --namespace=kube-system`

can be used to check the pod status of the cluster


## NOT SURE WE NEED THIS (fa18-516-03)

## Configure Head Node (port forwarding and DNS)

Install Dependencies:

    $ apt-get update
    $ apt-get install -qy dnsmasq clusterssh iptables-persistent

#### Create Static IP

TODO: Verify: This should already be done by `cm-burn`

Copy old config (-n flag prevents overwrite):

    $ \cp -n /etc/dhcpcd.conf /etc/dhcpcd.conf.old
    
To update DHCP configuration, add the following to **/etc/dhcpd.conf**:
 
    interface wlan0
    metric 200

    interface eth0
    metric 300
    static ip_address=192.168.50.1/24
    static routers=192.168.50.1
    static domain_name_servers=192.168.50.1

#### Configure DHCP Server:

Copy old config (-n flag prevents overwrite):

    $ \cp -n /etc/dnsmasq.conf /etc/dnsmasq.conf.old
    
To update DNS configuration, add the following to **/etc/dhcpd.conf**
    
    interface=eth0
    interface=wlan0

    dhcp-range=eth0, 192.168.50.1, 192.168.50.250, 24h
    
#### NAT Forwarding

To Setup NAT Forwarding, uncomment the following line in **/etc/sysctl.conf**:

    net.ipv4.ip_forward=1
    
#### IP Tables

Create IP Tables:

    $ sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
    $ sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    $ sudo iptables -A FORWARD -i $INTERNAL -o wlan0 -j ACCEPT
    $ sudo iptables -A FORWARD -i $EXTERNAL -o eth0 -j ACCEPT

Make rules permanent:

    $ iptables-save > /etc/iptables/rules.v4


### SSH Configuration

Generate SSH keys:

    $ ssh-keygen -t rsa
    
Copy key to each compute node:

    $ ssh-copy-id <hostname>
    
For hostnames rp1-4 (final node names will be: rp0, rp1, rp2, rp3, rp4).

### Configure Cluster SSH

To update Cluster SSH configuration, add the following to **/etc/clusters**:

    $ rpcluster rp1 rp2 rp3 rp4

Now you can run commands to all clusters by:

    $ cssh rpcluster

NOTE: This seems to be related to using `cssh` 
[Cluster SSH](https://github.com/duncs/clusterssh/wiki) to update all the nodes
together. I would suggest this is better down by using Docker or Ansible.
