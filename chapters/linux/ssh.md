# Secure Shell

Secure Shell is a network protocoll allowing users to securely connect
to remote resources over the internet. In many services we need to use
SSH to assure that we protect he messages send between the
communicating entities. Secure Shell is based on public key
technology requiering to generat ea public-private keypair on the
computer. The public key will than be uploaded to the remote machine
and whan a connection is establisched during authentication the public
private keypair is tested. If they match authetication is granted. As
many users may have to share a computer it is possible to add a list
of public keys so that a number of computers can connect to a server
that hosts such a list. This mechnism builds the basis for networked
computers.

In this section we will introduce you to some of the commands to
utilize secure shell. We will reuse this technology in other sections
to for example create a network of workstations to which we can log in
from your laptop.

---

:warning: Whatever others tell you, the private key should never be
copied to another machine.

---

## ssh-keygen

The first thing you will need to do is to create a public private
keypair. Before you do this check whether there are already keys on
the computer you are using:
	
	ls ~/.ssh

If there are files named id_rsa.pub or id_dsa.pub, then the keys are set up 
already, and we can skip the generating keys step. However you must
know the passphrase of the key. If you forgot it you will need to
recreate the key. However you will lose any ability to connect with
the old key to the respurces to which you uploaded the public key. So
be careful.

To generate a key pair use the command:

```bash
$ ssh-keygen -b 2048 -t rsa -C <your comment>
```

The comment will remind you where the key has been created, you could
for example use the hostname on which you created the Key. The command
will ask you to enter a *passphrase*. In most cases you **MUST**
provide one. Only for some system related services you may create
passwordless keys, but such systems need to be properly protected.

---

:warning: *Not using passhrases poses a security risk!*

---

Once you enter the passphrase and hit Enter, your public and private key will be
stored in the `~/.ssh` folder. The following files will be created:

* `id_rsa.pub`, which is your public key
* `id_rsa`, which is your private key

---

:warning: *Never, copy your private key to another machine or check it into a repository!*

---

To see what is in the .ssh directory, please use

```bash
$ ls ~/.ssh
```
    
Typically you will se a list of files such as

```
authorized_keys
id_rsa
id_rsa.pub
known_hosts
```

* The `id_rsa` file is your private key. Keep this on your computer and
  do not share this file.

* The `id_rsa.pub` file is your public key. This is what you share with
  machines you want to connect to. When the machine you try to connect
  to matches up your public and private key, it will allow you to
  connect.

To view public key:

	$ cat ~/.ssh/id_rsa.pub
	
It should be in the form:

    ssh-rsa <LONG STRING OF RANDOM CHARACTERS> <your comment>



## ssh-add

Often you wil find wrong information about passphrases on the internet
and peopel recommending you not to use one. However it is in almost
all cases better to craete a keypair and use `ssh-add` to add the key to
the current session so it can be used in behalf of you. This is
accomplished with an agent.

The `ssh-add` command adds SSH private keys into the SSH authentication
agent for implementing single sign-on with SSH. ssh-add allows the
user to use any number of servers that are spread across any number of
organizations, without having to type in a password every time when
connecting between servers. This is commonly used by system
administrators to login to multiple server.

`ssh-add` can be run without arguments. When run without arguments, it
adds the following default files if they do exist:

* `~/.ssh/identity` - Contains the protocol version 1 RSA authentication
  identity of the user.
* `~/.ssh/id_rsa` - Contains the protocol version 1 RSA authentication
  identity of the user.
* `~/.ssh/id_dsa` - Contains the protocol version 2 DSA authentication
  identity of the user.
* `~/.ssh/id_ecdsa` - Contains the protocol version 2 ECDSA
  authentication identity of the user.


To add a key you can provide the path of the key file as an
argument to ssh-add. For example,

    ssh-add ~/.ssh/id_rsa

would add the file `~/.ssh/id_rsa`

If the key being added has a passphrase, `ssh-add` will run the
`ssh-askpass` program to obtain the passphrase from the user. If the
`SSH_ASKPASS` environment variable is set, the program given by that
environment variable is used instead.

Some people use the `SSH_ASKPASS` environment variable in scripts to
provide a passphrase for a key. The passphrase might then be
hard-coded into the script, or the script might fetch it from a
password vault.

The command line options of `ssh-add` are as follows:

| Option  | Description |
| :-- | :------------- |
| `-c`| Causes a confirmation to be requested from the user every time the added identities are used for authentication. The confirmation is requested using ssh-askpass. |
| `-D` | Deletes all identities from the agent. |
| `-d` | Deletes the given identities from the agent. The private key files for the identities to be deleted should be listed on the command line.|
| `-e`  pkcs11 | Remove key provided by pkcs11 |
| `-L` | Lists public key parameters of all identities currently represented by the agent. |
| `-l` | Lists fingerprints of all identities currently represented by the agent. |
| `-s` pkcs11 |  Add key provided by pkcs11. |
| `-t` life | Sets the maximum time the agent will keep the given key. After the timeout expires, the key will be  automatically removed from the agent. The default value is in seconds, but can be suffixed for m for minutes, h for hours, d for days, or w for weeks. |
| `-X` | Unlocks the agent. This asks for a password to unlock. |
| `-x` | Locks the agent. This asks for a password; the password is required for unlocking the agent. When the agent is locked, it cannot be used for authentication. |



### Access a Remote Machine

Once the key pair is generated, you can use it to access a remote
machine. To dod so the public key needs to be added to the
`authorized_keys` file on the remote machine.


The easiets way to do tis is to use the command
`ssh-copy-id`.

	$ ssh-copy-id user@host

Note that the first time you will have to authenticate with your password.

Alternatively, if the ssh-copy-id is not available on your system, you
can copy the file manually over SSH:

	$ cat ~/.ssh/id_rsa.pub | ssh user@host 'cat >> .ssh/authorized_keys'

Now try:

	$ ssh user@host 

and you will not be prompted for a password. However, if you set a
passphrase when creating your SSH key, you will be asked to enter the
passphrase at that time (and whenever else you log in in the future).
To avoid typing in the password all the time we use the ssh-add
command that we described earlier.

	$ ssh-add


## SSH Port Forwarding :o:

:warning: this section has not beem vetted yet

TODO: Add images to illustrate the concepts

SSH Port forwarding (SSH tunneling) creates an encrypted secure
connection between a local computer and a remote computer through
which services can be relayed. Because the connection is encrypted,
SSH tunneling is useful for transmitting information that uses an
unencrypted protocol.

            
### Prerequisites

* Before you begin, you need to check if forwarding is allowed on the
  SSH server you will connect to.
* You also need to have a SSH client on the computer you are working
  on.

If you are using the OpenSSH server:

	$ vi /etc/ssh/sshd_config 

and look and change the following:

    AllowTcpForwarding = Yes 
    GatewayPorts = Yes

Set the `GatewaysPorts` variable only if you are going to use remote
port forwarding (discussed later in this tutorial). Then, you need to
restart the server for the change to take effect.

### How to Restart the Server 

If you are on:

* Linux, depending upon the init system used by your distribution, run:

  ```bash
   $ sudo systemctl restart sshd
   $ sudo service sshd restart
   ```
   
  Note that depending on your distribution, you may have to change the
  service to ssh instead of sshd.

* Mac, you can restart the server using:

  ```bash
  $ sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
  $ sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
  ```
  
* Windows and want to set up a SSH server, have a look at MSYS2 or Cygwin.

### Types of Port Forwarding

There are three types of SSH Port forwarding:

### Local Port Forwarding 

Local port forwarding lets you connect from your local computer to
another server. It allows you to forward traffic on a port of your
local computer to the SSH server, which is forwarded to a destination
server. To use local port forwarding, you need to know your
destination server, and two port numbers.

Example 1:

```bash
$ ssh -L 8080:www.cloudcomputing.org:80 <host>
```

Where `<host>` should be replaced by the name of your laptop.  The -L
option specifies local port forwarding.  For the duration of the SSH
session, pointing your browser at `http://localhost:8080/` would send
you to `http://cloudcomputing.com`

Example 2:

This example opens a connection to the www.cloudcomputing.com jump
server, and forwards any connection to port 80 on the local machine to
port 80 on `intra.example.com`.

```bash
$ ssh -L 80:intra.example.com:80 www.cloudcomputing.com
```

Example 3:

By default, anyone (even on different machines) can connect to the
specified port on the SSH client machine. However, this can be
restricted to programs on the same host by supplying a bind address:

```bash
$ ssh -L 127.0.0.1:80:intra.example.com:80 www.cloudcomputing.com
```

Example 4:

```bash
$ ssh -L 8080:www.Cloudcomputing.com:80 -L 12345:cloud.com:80 <host>
```

This would forward two connections, one to `www.cloudcomputing.com`, the
other to `www.cloud.com`. Pointing your browser at
`http://localhost:8080/` would download pages from
www.cloudcomputing.com, and pointing your browser to
`http://localhost:12345/` would download pages from www.cloud.com.

Example 5:

The destination server can even be the same as the SSH server.

```bash
$ ssh -L 5900:localhost:5900 <host>
```

The LocalForward option in the OpenSSH client configuration file can
be used to configure forwarding without having to specify it on
command line.

### Remote Port Forwarding

Remote port forwarding is the exact opposite of local port
forwarding. It forwards traffic coming to a port on your server to
your local computer, and then it is sent to a destination. The first
argument should be the remote port where traffic will be directed on
the remote system. The second argument should be the address and port
to point the traffic to when it arrives on the local system.

```bash
$ ssh -R 9000:localhost:3000 user@clodcomputing.com
```

SSH does not by default allow remote hosts to forwarded ports. To
enable remote forwarding add the following to: `/etc/ssh/sshd_config`

    GatewayPorts yes


```bash
$ sudo vim /etc/ssh/sshd_config
```

and restart SSH

	$ sudo service ssh restart
	
After above steps you should be able to connect to the server
remotely, even from your local machine. `ssh -R` first creates an SSH
tunnel that forwards traffic from the server on port 9000 to your
local machine on port 3000.
		
### Dynamic Port Forwarding

Dynamic port forwarding turns your SSH client into a SOCKS proxy
server.  SOCKS is a little-known but widely-implemented protocol for
programs to request any Internet connection through a proxy
server. Each program that uses the proxy server needs to be configured
specifically, and reconfigured when you stop using the proxy server.

```bash
$ ssh -D 5000 user@clodcomputing.com
```

The SSH client creates a SOCKS proxy at port 5000 on your local
computer. Any traffic sent to this port is sent to its destination
through the SSH server.

Next, you’ll need to configure your applications to use this server.
The *Settings* section of most web browsers allow you to use a SOCKS
proxy.

### ssh config

Defaults and other configurations can be added to a configuration file
that is placed in the system.  The ssh program on a host receives its configuration
 from 

* the command line options 
* a user-specific configuration file: `~/.ssh/config`
* a system-wide configuration file: `/etc/ssh/ssh_config`

Next we provide an example on how to use a config file



