#!/bin/sh

#sudo kubeadm init --config adm_kub_config.yaml
sudo  kubeadm init --apiserver-advertise-address=192.168.50.1
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
echo "configuration should be working. testig by getting nodes"
kubectl get nodes#i'm not sure if this will work
echo "don't worry if it says NotReady"