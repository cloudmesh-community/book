# Setting up Large PI clusters :o: :hand: fa18-516-03

## Setting up a Single Large Cluster with cm-burn :o:

cm-burn is a tool that has been developed specifically to make setting up
several PIs at once easier and less error prone. The cm-burn tool can
sequentially setup any number of SD cards to prepare them for use in a cluster
of PIs.

Before running cm-burn you must decide how to setup the networking configuration
and the SSH login configuration. cm-burn will make the same settings on each SD
card but can vary the host name and static IP addresses. cm-burn is also able to
setup SSH key-based authentication to the PI which is highly recommended.
Keeping track of passwords and/or using insecure passwords is a major security
risk for any network connected device. Using SSH key login avoids all of these
issues. Setting up SSH key login through cm-burn will disable password based
login. If you do not know how to generate an SSH key, please see section :o:.

Please see the cm-burn documentation for how to install cm-burn on your system.
Once installed, the following command will burn 5 SD cards in succession with
the names host names `blue00` - `blue04` on the `10.0.0.1` domain with IP
addresses from `10.0.0.101` to `10.0.0.105`. It will copy the current user's
public SSH key to the `~/.ssh/authorized_keys` file on the PI which will allow
SSH key-based authentication. The base image is the latest (as of writing)
Raspbian Stretch Lite.

```bash
./cm-burn.py create --name blue[00-04] \
    --ips 10.0.0.[101-105] --domain 10.0.0.1 \
    --key ~/.ssh/id_rsa.pub  \
    --image 2018-06-27-raspbian-stretch-lite.img
```

Follow all of the prompts to insert, eject, and re-insert the SD card as
required by cm-burn. When each card is finished it can be inserted back into the
PI and the power connected to the PI. If the setup is successful, the PI should
be able to connect to your network with the static IP address assigned to it and
you should be able to SSH to the PI. The user `pi` is setup with the given SSH
public key, so to connect you must use the `pi` user such as:

```bash
ssh pi@10.0.0.101
```

## Setting up a Cluster of Clusters with cm-burn

Here we discuss a class of students that each have 5 node clusters
that come in a room to place their clusters in a shelf then they plug
it into a power strip and a network, they replace the SD card of the
master with a worker SD card there is a special master that detects
new workers and inventories them with different states, so we can get
to them if they are registered.

