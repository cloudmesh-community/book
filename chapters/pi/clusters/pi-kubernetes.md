# Kubernetes :hand: fa18-516-03

In this section we will discuss how to set up a Kubernetes cluster on a
number of Raspberry Pis.

## Todo

- [ ] all the simple setup with sd cards, ssh, keys, and so on should be moved to the NOW cluster section. This way we can require simply a NOW and start without duplication on the real Kubernetes install.
- [x] we have two sections of Kubernetes contributed by two students. What we need is to merge them and save the usable things. We need to identify if the setup is significantly different before we can do this.
- [ ] so before you can work on the Kubernetes section you need to make sure the NOW section is up to date.

## Resources Needed
In [Network of Pis](#pi-now-main) section we explained how to set up a network
of Pis. Here we assume that we start from such a network. We recommend that the
cluster will have at least one master and three worker nodes. The test should
not use too many resources otherwise the system may be unnecessarily slow. In
particular we should have one dedicated master. We use three nodes to support
testing the distribution of containers. (It may work with two, but we have not
tested it). Please give us feedback on this and let us know what works for you.
We will integrate your feedback.

## Overview of Kubernetes Cluster Setup

A Kubernetes cluster is made of one master and several worker nodes. Each node
must have the standard Kubernetes setup completed and the master must also have
additional setup. Once the master and worker nodes are setup then the worker
nodes can join the network created by the master node. For the Raspberry Pi we
support two modes of setting up the master and workers. The first method is to
use the scripts that we provide to do the required installations. The second
method is to perform each step by hand. We will begin by explaining how to use
the scripts to setup your cluster quickly.

## Kubernetes Cluster Setup with Scripts

These steps have been verified with the latest build of Raspbian
Stretch which is
[2018-11-13-raspbian-stretch-lite](https://downloads.raspberrypi.org/raspbian_lite_latest).
If you have installed Raspbian Stretch with Desktop or Raspbian Stretch with
Desktop and Recommended Software then some of these steps will not be required,
but repeating them will not be a problem.

The required scripts are stored in the
[Cloudmesh Community Pi](https://github.com/cloudmesh-community/pi) repository
and must be copied to each Raspberry Pi in order to run. This guide assumes that
each Pi has internet access which is required to download the necessary tools.
The first steps to setup the Pi tools is listed on the 
[README.md](https://github.com/cloudmesh-community/pi/blob/master/README.md)
for the Pi tools repository. We will repeat those steps here for convenience.

### Pi Tools Prerequisites {#pi-cluster-tools-setup}

To use the Cloudmesh Pi tools you need `git` to download the tools from the
github repository. You must also update the Pi's list of software, install
`git`, and then download or clone the `git` repository. Run these steps at the
Pi command prompt:

```bash
$ sudo apt-get update; sudo apt-get install -y git
$ git clone https://github.com/cloudmesh-community/pi.git
```

When that successfully completes you will have a copy of the Pi tools on your Pi
and you can now run them.


### Kubernetes Shared Setup {#kubernetes-shared-setup}

Every Kubernetes node, whether master or worker, needs to complete the following
setup steps. The Pi scripts are stored in the `bin` directory. Every
Kubernetes Pi master and worker must run the `kubernetes-setup.sh` script which
will download and install Docker and Kubernetes and make the necessary system
changes to support both. When this script completes the Pi must be rebooted to
properly configure its memory system for Kubernetes. Execute the following
commands:

```bash
$ sudo pi/bin/kubernetes-setup.sh
$ sudo reboot
```

If you are connected to the Pi over `ssh` your session may hang at this point.
You can either wait for `ssh` to timeout or kill the session by typing a tilde
then a period. The tilde on a new line is a special command to `ssh` and the
period means to disconnect the session.

```bash
~.
```

At this point the worker is ready to connect to the Kubernetes master node.
The command to connect to the master node is `kubeadm join` but we need to
finish setting up the master node in order to get the token necessary to
authenticate with it.

### Kubernetes Master Setup {#kubernetes-master-setup}

To setup the Kubernetes master node you should first complete the
[Kubernetes Shared Setup](#kubernetes-shared-setup). After the Pi reboots you
can run the master setup script:

```bash
$ sudo pi/bin/kubernetes-master-setup.sh
```

The master setup script will run `kubeadm init` which can take a long time and
will occasionally timeout on the Raspberry Pi without completing. This does not
indicate a failure of the Pi setup. If the command finishes with the error

```
Unfortunately, an error has occurred:
        timed out waiting for the condition
```

then it is possible to restart the setup and it will usually complete
successfully the second time. To do this (only if the master setup failed) run
`kubeadm reset` and be sure to answer `y` to the prompts. Then run the master
setup script again:

```bash
$ sudo kubeadm reset
$ sudo pi/bin/kubernetes-master-setup.sh
```

When the master setup successfully completes you should see:

```
Your Kubernetes master has initialized successfully!
```

and there will be further instructions on how to setup the master. These steps
have already been performed by the setup scripts so you do not need to do them.
The output will also list the required `kubeadm join` command that can be issued
on each worker node that wishes to join this Kubernetes master node. In
addition, the scripts have stored the join command, the master IP address, the
join token, and the CA Hash in a YAML file `kubeadm-settings.yml` in the current
directory. If you need to add nodes in the future, you may refer to this file
for the required parameters.

## Join Workers to Master {#pi-kubernetes-join-workers}

Now login to each of the workers and issue the `kubeadm join` command from the
master node. If you have not successfully completed the master node setup,
please see [Kubernetes Master Setup](#kubernetes-master-setup) for the required
steps.

As of this writing there is a version incompatibility between the latest
Kubernetes and the latest Docker. Kubernetes has not yet verified Docker version
18.09 which is installed by the default Docker install script. If you use our
provided setup script then the version of Docker will be automatically
downgraded to 18.06.1 which is verified by Kubernetes. You can follow the steps
to downgrade your Docker version given in [Install Docker](#pi-install-docker) or
you can skip the version check by specifying
`--ignore-preflight-errors=SystemVerification` on the command line. An example
`kubeadm join` command would be:

```bash
$ sudo kubeadm join 10.0.0.101:6443 \
    --token vstt3y.faa67q2dp383xhgv \
    --discovery-token-ca-cert-hash \
    sha256:7fa06185f14b89234235aa9f03ef60835ade825e2553cd97a52b5894566edeb5
```

Once the worker nodes have joined the cluster, you can login to the master node
and see their status with the following command:

```bash
$ sudo kubectl get nodes
NAME     STATUS   ROLES    AGE     VERSION
blue00   Ready    master   4h56m   v1.12.2
blue01   Ready    <none>   4h44m   v1.12.2
blue02   Ready    <none>   4h46m   v1.12.2
blue03   Ready    <none>   4h42m   v1.12.2
blue04   Ready    <none>   4h1m    v1.12.2
```

When the workers are joining the cluster they will initially be in a `NotReady`
state for a while as they complete their setup. This is the normal expected
behavior and each node should reach the `Ready` state within a few minutes. To
continue experimenting with your Kubernetes cluster, please see the
[Kubernetes First Steps](#kubernetes-first-steps) section.

## Manual Kubernetes Cluster Setup

If you do not want to use our setup scripts or would like to change some steps
in the installation you can use the following steps to manually setup a
Kubernetes cluster on several Pis. First, each node in the cluster must have
Docker and Kubernetes installed along with some system configurations. Then the
master should be launched and each worker node connected to the master. Please
follow these instructions carefully and you should have a working Kubernetes
cluster.

### Install docker {#pi-install-docker}

Kubernetes depends on a containerization platform to run applications. The
standard platform used with Kubernetes is Docker, although other container
platforms are also support. We will use Docker on the Pi. Install Docker with
the convenience script at `get.docker.com`. You may also download the script
manually and see what operations it performs. The basic steps in the script are
to detect your operation system and computer architecture, setup the proper
Docker package repositories and keys for your system, and finally install the
Docker packages and dependencies. The current version of Docker 18.09 has not
been verified by Kubernetes, so after installation we will downgrade this
package to 18.06 in the following steps. Once the installation finishes we
recommend running the following `usermod` command to run Docker as a non-root
user. This is an optional but recommended step.

```bash
$ curl -sSL get.docker.com | sudo sh
$ sudo usermod -aG docker pi
```

The current version of Docker 18.09 installed by the convenience script has not
been verified by Kubernetes v1.12.2 yet so it will give an error and Kubernetes
will fail to start. You can fix this by giving the
`--ignore-preflight-errors=SystemVerification` flag to `kubeadm init` and
`kubeadm join`. However, a better solution is to downgrade the Docker version
installed. The Docker install script will also setup the proper `apt-get`
repositories that host previous versions of Docker. To downgrade, first stop
the `docker.service` that is running, then downgrade the package and restart the
service. The Docker service should restart automatically after the downgrade, so
restarting the service with `systemctl` is just done in case of a problem.

```bash
$ sudo systemctl stop docker.service
$ sudo apt-get install -qy --allow-downgrades \
  docker-ce=18.06.1~ce~3-0~raspbian
$ sudo systemctl start docker.service
```

### Install Kubernetes

After installing Docker we must also install Kubernetes. The Kubernetes package
sources and GPG keys need to be added to the `apt-get` package manager first,
then we must update the `apt-get` package list with the new sources before we
can finally install the Kubernetes services and administration package
`kubeadm`.

```bash
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg |\
  sudo apt-key add -
$ echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" |\
  sudo tee /etc/apt/sources.list.d/kubernetes.list
$ sudo apt-get update -q; sudo apt-get install -qy kubeadm
```

Once Kubernetes and Docker are correctly installed there are some system
configuration changes necessary for Kubernetes.

### System configuration {#pi-kubernetes-system-config}

Kubernetes is not compatible with SWAP memory and as of version 1.8 it will 
[fail if swap is enabled on a node](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.8.md#before-upgrading),
therefore we need to disable swap memory on Raspbian. It is possible that
disabling swap on the Pi could cause other issues, especially due to the low
memory on the Raspberry Pi, but it is accepted practice for running any
Kubernetes cluster to disable swap. There is a flag `--fail-swap-on=false` that
can be passed to `kubeadm` to skip the check for swap but we have not tested
with this setting.  To disable swap execute the following commands on the Pi:

```bash
$ sudo dphys-swapfile swapoff && \
  sudo dphys-swapfile uninstall && \
  sudo update-rc.d dphys-swapfile remove
```

You should now not see any entries in this command:

```bash
$ sudo swapon --summary
```

Next some kernel cgroup settings need to be changed for Kubernetes. This is a
boot-time option that can only be changed by altering the options passed to the
Linux kernel during boot. These options are stored in the file
`/boot/cmdline.txt` on the Raspberry Pi. This file only contains a single line
that specifies the kernel options. The following three options must be added to
the end of the line `cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory`.
You may edit the file in a text editor if you are confident that you can make
the change correctly or simply run the following lines at the command prompt.
They will first backup the current file, then then append the new options and
finally write the entire string back to the original file:

```bash
$ sudo cp /boot/cmdline.txt /boot/cmdline.bak.txt
$ new_options="$(head -n1 /boot/cmdline.txt) \
cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory"
$ echo "$new_options" | sudo tee /boot/cmdline.txt
```

Kubernetes also expects certain kernel modules to be loaded. It will enable
these kernel modules during setup but we can also specify them to always be
loaded on boot which removes the warning messages. To enable the required kernel
modules, execute the following lines which will append these modules to the list
of enabled kernel modules stored in `/etc/modules`.

```bash
$ cat << EOF | sudo tee -a /etc/modules
ip_vs
ip_vs_sh
ip_vs_rr
ip_vs_wrr
nf_conntrack_ipv4
EOF
```

Since these changes only take place at boot time, you *must reboot* before
continuing with the rest of the section. If you do not reboot then Kubernetes
will refuse to run and issue an error.

### Setup Kubernetes Cluster

After the Pi reboots and you reconnect to it there are a few steps to perform on
the master Kubernetes node to prepare it for the worker nodes to connect to.
First we recommend pulling (downloading) the Kubernetes images so that this step
is separate from initializing the cluster. You can issue the following command
and note that it will take several minutes depending on your network connection:

```bash
$ sudo kubeadm config images pull
```

Once that is complete we can now initialize the Kubernetes master. You need to
know the IP address of the master node and you should choose a CIDR for the pod
network. Note that in this case we are setting the join token to have a
time-to-live of 0 which means it will never expire. This is reasonable for
initial setup and testing but in any permanent system the token should be
allowed to expire in a few hours or days to prevent unauthorized nodes from
joining the cluster should the token accidentally be leaked. The following
command will setup the master:

```bash
$ POD_CIDR=10.244.0.0/16
$ APISERVER_IP=10.0.0.101
$ sudo kubeadm init --token-ttl=0 \
  --pod-network-cidr="$POD_CIDR" \
  --apiserver-advertise-address="$APISERVER_IP"
```

When the master setup completes successfully then you should see output similar
to the following:

```
Your Kubernetes master has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
as root:

  kubeadm join 10.0.0.101:6443 --token vstt3y.faa67q2dp383xhgv --discovery-token-ca-cert-hash sha256:7fa06185f14b89234235aa9f03ef60835ade825e2553cd97a52b5894566edeb5
```

You should follow these instructions, running these commands:

```bash
$ mkdir -p "$HOME/.kube"
$ sudo cp -i /etc/kubernetes/admin.conf "$HOME/.kube/config"
$ sudo chown "$(id -u)":"$(id -g)" "$HOME/.kube/config"
```

The `kubeadm join` command should be copied and stored for later use. If you
lose the details you can view the existing tokens with `kubeadm token list`

```bash
$ sudo kubeadm token list
```

And you can find the sha256 hash of the CA Cert with:

```bash
$ openssl x509 -in /etc/kubernetes/pki/ca.crt -noout -pubkey |\
  openssl rsa -pubin -outform DER 2>/dev/null | sha256sum |\
  cut -d' ' -f1
```

The original token is for development use and so we set it to have an unlimited
time-to-live. This is not recommended for a production system, however, a
shorter TTL of a few hours or days should be specified and a new token should be
generated when the previous one has expired. A new token can be created with the
following command.

```bash
$ sudo kubeadm token create --print-join-command
```

This will not retrieve the original token but will generate a new one. These
tokens should be carefully managed as they allow a node to join the Kubernetes
cluster which is a potentially unsafe operation for untrusted nodes.

The final step is setting up the networking. These instructions use
[Weave Net](https://www.weave.works/oss/net/) to enable the Kubernetes network
architecture. Another recommended solution to use with the Raspberry Pi is
[Flannel](https://github.com/coreos/flannel). Here is the command to setup Weave
Net on the Kubernetes cluster.

```
  kubectl apply -f \
 "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```


After waiting a minute or so, you should see the following output from this
command:

```
 $ sudo kubectl get pods --namespace=kube-system
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

Now that the master is running and networking is enabled, you can run the
`kubeadm join` command on each Pi in the cluster and issue the identical command
for them to join the master. Please see the section [Join Workers to
Master](#pi-kubernetes-join-workers) for more details.

## Kubernetes First Steps {#kubernetes-first-steps}

Now that you have the Kubernetes cluster running you can deploy pods on the
cluster. For production use of Kubernetes it is recommended to use a Controller
which will manage the details of deploying pods to nodes and ensuring
replication and self-healing. Please see the 
[Kubernetes Pod Overview](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/#pods-and-controllers)
section of the Kubernetes documentation for information on creating 
[Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/),
[StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
or
[DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
on your cluster. For our simple use case we will create a few pods by hand.

### Kubernetes Pods

The [Cloudmesh Community Pi](https://github.com/cloudmesh-community/pi)
repository has several pod definition files that you can use directly or
customize to your particular use case for experimenting with the Kubernetes
cluster. If you used our install scripts you should already have these on your
Kubernetes master. If you did the setup by hand you can get the repository by
installing `git` and then cloning it onto the Pi using the instructions in the
[Pi Tools Prerequisites](#pi-cluster-tools-setup) section.

As an initial test you can create the markdown renderer deployment on your
cluster with the command:

```bash
$ cd pi/kubernetes
$ sudo kubectl create -f markdownrender.yml
service/markdownrender created
deployment.apps/markdownrender created
```

If you look at the markdownrender.yml file you will see that it defines a
Service and a Deployment and it maps port 8080 from the Service to the external
port 31118. The Deployment specifies that it should have one replica of the
application which runs a Docker container from Docker Hub titled
[functions/markdownrender:latest-armhf](https://hub.docker.com/r/functions/markdownrender/).
This container supplies a simple service to translate a markdown document into
an HTML document. You can test it with the following commands to see it working:

```bash
$ curl -4 http://localhost:31118 -d "# test"
$ curl -4 http://localhost:31118 --data-binary @../README.md
```

The 31118 port will also be accessible to any computer that can reach the
Kubernetes master (unless firewall rules dictate otherwise) so you can also test
this from your own computer if it is on the same network as the Kubernetes
master. For example you could run:

```bash
$ curl -4 http://blue00:31118 -d "# test"
$ curl -s \
  https://raw.githubusercontent.com/cloudmesh-community/pi/master/README.md |\
  curl -4 http://blue00:31118 --data-binary @-
```

You can see the status of your pods by using `kubectl get pods` on the master.
Adding the `-o wide` parameter will also output the node and node ip of the node
that the pod is deployed to.

```bash
$ sudo kubectl get pods -o wide
NAME                              READY   STATUS    RESTARTS   AGE   IP
NODE     NOMINATED NODE
markdownrender-7d8d6f74d6-67bsg   1/1     Running   0          20m   10.44.0.1
blue01   <none>
```

```bash
sudo kubectl get pods -o jsonpath='{.items[*].spec.nodeName}'
```

### Removing a node from a cluster

To remove a Kubernetes node from a cluster, you must first drain the node which
will evict every pod in the node and cordon it off so that no new pods will be
scheduled in it. For cluster setup each node will be running the Weave daemon so
it is necessary to specify `--ignore-daemonsets` to drain the node. The drain
command should complete without errors.

```bash
$ sudo kubectl drain --ignore-daemonsets <node>
```

If there are pods scheduled to the node then you should wait until those pods
complete and are shutdown and removed from the node. You can observe the node
state using `kubectl get nodes` and `kubectl get pods`. You could see a sequence
of events such as this when draining a node that has a deployed pod.

```bash
$ sudo kubectl drain blue01 --ignore-daemonsets
node/blue01 cordoned
WARNING: Ignoring DaemonSet-managed pods: kube-proxy-2zplz, weave-net-r7b85
pod/markdownrender-7d8d6f74d6-67bsg evicted
$ sudo kubectl get pods -o wide
NAME                              READY   STATUS              RESTARTS   AGE   IP       NODE     NOMINATED NODE
markdownrender-7d8d6f74d6-lqk58   0/1     ContainerCreating   0          14s   <none>   blue03   <none>
$ sudo kubectl get pods -o wide
NAME                              READY   STATUS    RESTARTS   AGE   IP          NODE     NOMINATED NODE
markdownrender-7d8d6f74d6-lqk58   1/1     Running   0          24s   10.39.0.1   blue03   <none>
```

When the node has no pods scheduled to it you can remove it from the cluster
permanently by issuing the `delete` command on the master. The node should be in
the `Ready,SchedulingDisabled` status. For example, in this output the node
`blue04` has been drained and is ready to be deleted from the cluster.

```
$ sudo kubectl get nodes
NAME     STATUS                     ROLES    AGE     VERSION
blue00   Ready                      master   40h     v1.12.2
blue01   Ready                      <none>   40h     v1.12.2
blue02   Ready                      <none>   40h     v1.12.2
blue03   NotReady                   <none>   40h     v1.12.2
blue04   Ready,SchedulingDisabled   <none>   4m10s   v1.12.2
```

```bash
$ sudo kubectl delete node <node>
```

Once this is complete you can login to the node itself and reset it so that it
can join another cluster or be used for other purposes. The `kubeadm reset`
command will accomplish this. At this point Kubernetes should be shut down on
the Pi and you should not see any entries in the `systemctl` table for
`kubernetes` or `kubelet` and you should not see any running Docker images that
are related to Kubernetes. This can be confirmed with the following commands run
_on the node_ not on the master:

```bash
$ sudo kubeadm reset
$ sudo systemctl list-units | grep -E 'kubernetes|kubelet'
$ docker ps
```

Remember that Kubernetes required swap to be disabled and it may need to be
re-enabled if you are planning to use the Raspberry Pi for other uses. There is
some debate about whether swap on a Pi is actually a good idea in general,
however, since the SD Card is rather slow and doesn't handle repeated reads and
writes well. If you have a USB hard drive this could be a good solution to
increasing swap. The memory and cpuset cgroups were also enabled for Kubernetes
by modifying the `/boot/cmdline.txt` kernel options file. Leaving these enabled
will not cause problems for other uses but they can be easily turned off by
removing the lines that were added in the
[System configuration](#pi-kubernetes-system-config) section.
Here are the required commands to re-enable swap.

```bash
$ sudo dphys-swapfile install && \
  sudo dphys-swapfile swapon && \
  sudo update-rc.d dphys-swapfile defaults
```

Swap will be enabled immediately and the changes will persist after reboot.

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


