## Kubernetes Cluster in Rasberry Pi - automation
This section of the tutorial is targetting to automate the Kubernetes cluster setup in Rasberry pi.

# opt_setup.sh
This is an optional setup if its required to download the cloudmesh code from 417 repo

``
sh opt_setup.sh
``

# dhcp_setup.sh

This Script will help setting up the dhcp static ip.

Please note that the shell script will excute the recommneded reboot after the static IP assignment.

It needs four params:
   - hostname
   - desired static ip
   - router ip
   - dns server ip

``
sh dhcp_setup.sh <hostname> <nodeIP> <routerIP> <dnsIP> 
``

# docker_setup.sh

Now Install docker and turn off the swap memory.
This shell will reboot the node per recommendadtion of the referneces. 

``
sh docker_setup.sh
``

The above shell scripts are common in both worker and head.

# kube_head_setup.sh

To be executed only on the master.
This will initiate kubectl master and setup networking[debugging now]

``
sh kube_head_setup.sh
``
Please save the join token for the workers

 # kube_worker_setup.sh
 To be executed in the worker nodes

``
sh kube_worker_setup.sh
``

