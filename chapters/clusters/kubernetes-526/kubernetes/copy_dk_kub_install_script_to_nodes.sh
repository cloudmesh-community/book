#!/bin/sh

#copying the script to nodes
for number in {1..4}
	do 
		scp /home/pi/docker_kubernites_install.sh \
			pi@rp$number:/home/pi/docker_kubernites_install.sh
	done
exit 0

#running the script in the nodes
cssh -a "sh docker_kubernites_install.sh"