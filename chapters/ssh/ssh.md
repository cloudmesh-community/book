# Secure Shell

In many services we need to use SSH keys to securely communicate with
them.

TODO: provide a more detailed introduction

## ssh-keygen

To generate one use the command:

```bash
    $ ssh-keygen -b 2048 -t rsa -C <your comment>
```

The comment will remind you where the key has been created, you could
for example use the hostname on which you created the Key. The command
will ask you to enter a *passphrase*. In most cases you **MUST**
provide one. Only for some system related services you may create
passwordless keys, but such systems need to be properly protected.

---

:warning: *Not using pass[hrases poses a security risk!*

---

Once you enter the passphrase and hit Enter, your public and private key will be
stored in the `~/.ssh` folder. The following files will be created:

* `id_rsa.pub`, which is your public key
* `id_rsa`, which is your private key

---

:warning: *Never, copy your private key to another machine or check it into a repository!*

---




## ssh-add :o:

The `ssh-add` command adds SSH private keys into the SSH authentication
agent for implementing single sign-on with SSH. ssh-add allows the
user to use any number of servers that are spread across any number of
organizations, without having to type in a password every time when
connecting between servers. This is commonly used by system
administrators to login to multiple server.

### Adding Default Keys

ssh-add can be run without arguments. When run without arguments, it
adds the following default files if they do exist:

* `~/.ssh/identity` - Contains the protocol version 1 RSA authentication
  identity of the user.
* `~/.ssh/id_rsa` - Contains the protocol version 1 RSA authentication
  identity of the user.
* `~/.ssh/id_dsa` - Contains the protocol version 2 DSA authentication
  identity of the user.
* `~/.ssh/id_ecdsa` - Contains the protocol version 2 ECDSA
  authentication identity of the user.


### Adding a Key

To add a key you can provide the path of the key file as an
argument to ssh-add. For example,

    ssh-add ~/.ssh/my-key

would add the file `~/.ssh/my-key`

### Keys With Passphrases

If the key being added has a passphrase, ssh-add will run the
`ssh-askpass` program to obtain the passphrase from the user. If the
`SSH_ASKPASS` environment variable is set, the program given by that
environment variable is used instead.

Some people use the `SSH_ASKPASS` environment variable in scripts to
provide a passphrase for a key. The passphrase might then be
hard-coded into the script, or the script might fetch it from a
password vault.

### Command Line Options

`ssh-add` accepts the following command line options:

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

## ssh config :o:

SSH stands for Secure SHell. SSH allows you to connect to that other
system securely and the data exchanged between the servers are secured
and encrypted.  The ssh program on a host receives its configuration
from either the command line or from configuration files:
 
* ~/.ssh/config 
* /etc/ssh/ssh_config

ssh command gets the configuration data from the below three mentioned
sources in the order they are stated:
  
* command line options 
* user-specific configuration file (`~/.ssh/config`)
* system-wide configuration file (`/etc/ssh/ssh_config`)

Generating a key pair provides you with two long string of characters:
a public and a private key. You can place the public key on any
server, and then unlock it by connecting to it with a client that
already has the private key. When the two match up, the system unlocks
without the need for a password. You can also secure by protecting the
private key with a passphrase.

### Step 1: Check for Existing SSH Keys
  
Check whether there are already keys on the computer you are using:
	
	ls ~/.ssh

If there are files named id_rsa.pub or id_dsa.pub, then the keys are set up 
already, and we can skip the generating keys step (or delete these files with
rm id* and make new keys).

### Step 2: Generate new SSH Keys

To generate new SSH keys enter the following command:

	ssh-keygen

### Step 3: Store the Keys and Passphrase

Upon entering this command, you'll be asked where to save the key. You can 
either safe it in your default location or enter the location where you want
to save the file and then press Enter.

Next, You'll also be asked to enter a passphrase. This is an additional extra
security which will make the key unusable without your passphrase, so if 
someone else copied your key, they could not impersonate you to gain access. 
If you choose to use a passphrase, enter you passphrase and press Enter, then 
type it again when prompted. If you want, no passphrase, Leave the field empty.

#### To see what's in .ssh directory:

```bash
    $ ls ~/.ssh

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

#### To view public key:

	$ cat ~/.ssh/id_rsa.pub
	
It should be in the form:

    ssh-rsa <LONG STRING OF RANDOM CHARACTERS> user@host

### Step 4: Copy the Public Key

Once the key pair is generated, use the following command to append the public
key to `authorized_keys` on the server that you want to use. You can copy the
public key into the new machine's `authorized_keys` file with the `ssh-copy-id` 
command. 

	$ ssh-copy-id user@host

Note that this time you will have to authenticate with your password.

Alternatively, if the ssh-copy-id is not available on your system, you
can copy the file manually over SSH:

	$ cat ~/.ssh/id_rsa.pub | ssh user@host 'cat >> .ssh/authorized_keys'

Now try:

	$ ssh user@host 

and you will not be prompted for a password. However, if you set a
passphrase when creating your SSH key, you will be asked to enter the
passphrase at that time (and whenever else you log in in the future).

If you see a message *Agent admitted failure to sign using the key*
then add your RSA or DSA identities to the authentication agent
ssh-agent then execute the following command:

	ssh-add

If this did not work, delete your keys using the command:
	
	rm ~/.ssh/id* 
	
and follow the instructions again.


## SSH Port Forwarding :o:

TODO: Add images to ilustrate the concepts

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

	vi /etc/ssh/sshd_config 

and look and change the following:

    AllowTcpForwarding = Yes 
    GatewayPorts = Yes

Set the `GatewaysPorts` variable only if you are going to use remote
port forwarding (discussed later in this tutorial). Then, you need to
restart the server for the change to take effect.

### How to Restart the Server 

If you are on:

* Linux, depending upon the init system used by your distribution, run:

	  sudo systemctl restart sshd
	  sudo service sshd restart
	
 Note that depending on your distribution, you may have to change the service to ssh instead of sshd.

* Mac, you can restart the server using:

    sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
    sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist

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

		ssh -L 8080:www.cloudcomputing.org:80 <host>

Where `<host>` should be replaced by the name of your laptop.  The -L
option specifies local port forwarding.  For the duration of the SSH
session, pointing your browser at `http://localhost:8080/` would send
you to `http://cloudcomputing.com`

Example 2:

This example opens a connection to the www.cloudcomputing.com jump
server, and forwards any connection to port 80 on the local machine to
port 80 on `intra.example.com`.

		ssh -L 80:intra.example.com:80 www.cloudcomputing.com


Example 3:

By default, anyone (even on different machines) can connect to the
specified port on the SSH client machine. However, this can be
restricted to programs on the same host by supplying a bind address:

		ssh -L 127.0.0.1:80:intra.example.com:80 www.cloudcomputing.com

Example 4:

		ssh -L 8080:www.Cloudcomputing.com:80 -L 12345:cloud.com:80 <host>
		
This would forward two connections, one to `www.cloudcomputing.com`, the
other to `www.cloud.com`. Pointing your browser at
`http://localhost:8080/` would download pages from
www.cloudcomputing.com, and pointing your browser to
`http://localhost:12345/` would download pages from www.cloud.com.

Example 5:

The destination server can even be the same as the SSH server.

		ssh -L 5900:localhost:5900 <host>

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

		ssh -R 9000:localhost:3000 user@clodcomputing.com
		
SSH does not by default allow remote hosts to forwarded ports. To
enable remote forwarding add the following to: /etc/ssh/sshd_config

		GatewayPorts yes


	$ sudo vim /etc/ssh/sshd_config

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

		ssh -D 5000 user@clodcomputing.com
		
The SSH client creates a SOCKS proxy at port 5000 on your local
computer. Any traffic sent to this port is sent to its destination
through the SSH server.

Next, you’ll need to configure your applications to use this server.
The *Settings* section of most web browsers allow you to use a SOCKS
proxy.




