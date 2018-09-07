# Secure Shell

[Secure Shell](http://openssh.com/manual.html) is a network protocol
allowing users to securely connect to remote resources over the
internet. In many services we need to use SSH to assure that we
protect he messages send between the communicating entities. Secure
Shell is based on public key technology requiring to generate a
public-private key pair on the computer. The public key will than be
uploaded to the remote machine and when a connection is established
during authentication the public private key pair is tested. If they
match authentication is granted. As many users may have to share a
computer it is possible to add a list of public keys so that a number
of computers can connect to a server that hosts such a list. This
mechanism builds the basis for networked computers.

In this section we will introduce you to some of the commands to
utilize secure shell. We will reuse this technology in other sections
to for example create a network of workstations to which we can log in
from your laptop. For more information please also consult with the
[SSH Manual](http://openssh.com/manual.html).

---

:warning: Whatever others tell you, the private key should never be
copied to another machine. YOu almost always want to have a passphrase
protecting your key.

---

## ssh-keygen

The first thing you will need to do is to create a public private
key pair. Before you do this check whether there are already keys on
the computer you are using:
	
	ls ~/.ssh

If there are files named id_rsa.pub or id_dsa.pub, then the keys are set up 
already, and we can skip the generating keys step. However you must
know the passphrase of the key. If you forgot it you will need to
recreate the key. However you will lose any ability to connect with
the old key to the resources to which you uploaded the public key. So
be careful.

To generate a key pair use the command
[ssh-keygen](http://linux.die.net/man/1/ssh-keygen).  This program is
commonly available on most UNIX systems and most recently even
Windows 10. 

To generate the key, please type:

```bash
$ ssh-keygen -t rsa -C <comment>
```

The comment will remind you where the key has been created, you could
for example use the hostname on which you created the key. 

In the following text we will use *localname* to indicate the username
on your computer on which you execute the command.

The command requires the interaction of the user. The first question
is:

    Enter file in which to save the key (/home/localname/.ssh/id_rsa): 

We recommend using the default location ~/.ssh/ and the default name
id_rsa. To do so, just press the enter key.


The second and third question is to protect your ssh key with a
passphrase. This passphrase will protect your key because you need to
type it when you want to use it. Thus, you can either type a passphrase
or press enter to leave it without passphrase. To avoid security
problems, you **MUST** chose a passphrase.

 It will ask you for the location and name of the new key. It will
also ask you for a passphrase, which you **MUST** provide. Please use
a strong passphrase to protect it appropriately. Some may advise you
(including teachers and TA's) to not use passphrases.  This is
**WRONG** as it allows someone that gains access to your computer to
also gain access to all resources that have the public key.
Only for some system related services you may create
passwordless keys, but such systems need to be properly protected.

---

:warning: *Not using passphrases poses a security risk!*

---

Make sure to not just type
return for an empty passphrase:

    Enter passphrase (empty for no passphrase):

and:

    Enter same passphrase again:

If executed correctly, you will see some output similar to:

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/localname/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/localname/.ssh/id_rsa.
    Your public key has been saved in /home/localname/.ssh/id_rsa.pub.
    The key fingerprint is:
    34:87:67:ea:c2:49:ee:c2:81:d2:10:84:b1:3e:05:59 localname@indiana.edu

    +--[ RSA 2048]----+
    |.+...Eo= .       |
    | ..=.o + o +o    |
    |O.  = ......     |
    | = .   . .       |
    +-----------------+

Once, you have generated your key, you should have them in the `.ssh`
directory. You can check it by:

    $ cat ~/.ssh/id_rsa.pub

If everything is normal, you will see something like:

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt
    6KlRh4kUOjgw9sc4Uu+Uwe/kshuispauhfsjhfm,anf6787sjgdkjsgl+EwD0
    thkoamyi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW
    4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiE
    xxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeim
    Uk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVc
    ynEPUegkp+qYnR user@myemail.edu

The directory `~/.ssh` will also contain the private key `id_rsa` which you
must not share or copy to another computer.

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

In case you need to change your change passphrase, you can simply run
`ssh-keygen -p` command. Then specify the location of your current key,
and input (old and) new passphrases. There is no need to re-generate
keys:

    ssh-keygen -p

You will see the following output once you have completed that step:

    Enter file in which the key is (/home/localname/.ssh/id_rsa):
    Enter old passphrase:
    Key has comment '/home/localname/.ssh/id_rsa'
    Enter new passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved with the new passphrase.


## ssh-add

Often you wil find wrong information about passphrases on the internet
and people recommending you not to use one. However it is in almost
all cases better to create a key pair and use `ssh-add` to add the key to
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

SSH Add and Agent
-----------------

To not always type in your password, you can use `ssh-add` as
previously discussed

It prompts the user for a private key passphrase and add it to a list of
keys managed by the ssh-agent. Once it is in this list, you will not be
asked for the passphrase as long as the agent is running.with your
public key. To use the key across terminal shells you can start an ssh agent.

To start the agent please use the following command:

    eval `ssh-agent`

or use

    eval "$(ssh-agent -s)"

It is important that you use the backquote, located under the tilde
(US keyboard), rather than the single quote. Once the agent is started
it will print a PID that you can use to interact with later

To add the key use the command

    ssh-add

To remove the agent use the command

    kill $SSH_AGENT_PID

To execute the command upon logout, place it in your `.bash_logout`
(assuming you use bash).

On OSX you can also add the key permanently to the keychain if you do
toe following:

    ssh-add -K ~/.ssh/id_rsa

Modify the file `.ssh/config` and add the following lines:

    Host *
      UseKeychain yes
      AddKeysToAgent yes
      IdentityFile ~/.ssh/id_rsa


### Using SSH on Mac OS X

Mac OS X comes with an ssh client. In order to use it you need to open
the `Terminal.app` application. Go to `Finder`, then click `Go` in the
menu bar at the top of the screen. Now click `Utilities` and then open
the `Terminal` application.

### Using SSH on Linux

All Linux versions come with ssh and can be used right from the
terminal.

### Using SSH on Raspberry Pi 3

SSH is available on Rasbian. However, to ssh into the PI you have to
activate it via the configuration menu. For a more automated
configuration, we will provide oreinformation in the Rasspberrry PI
section.k

### SSH on Windows :o:

:warning: THis section is outdated and should be replaced with
information from SSH in powershell

* <https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/>



In case you need access to ssh Microsoft has fortunately updated their
software to be able to run it directly from the Windows commandline
including PowerShell.

However it is as far as we know not activated by default so you need to
follow some setup scripts. Also this software is considered beta and its
development and issues can be found at

<https://github.com/PowerShell/Win32-OpenSSH>
<https://github.com/PowerShell/Win32-OpenSSH/issues>
What you have to do is to install it by going to

    Settings > Apps

and click

    Manage optional features

under

    Apps & features


Next, Click on the `Add feature`. You will be presented with a list in
which you scroll down, till you find `OpenSSH Client (Beta)`. Click on
it and invoke `Install`.

After the install has completed, you can use the `ssh` command. Just
type it in the commandshell or PowerShell

    PS C:\Users\gregor> ssh

Naturally you can now use it just as on Linux or OSX. and use it to
login to other resources

    PS C:\Users\gregor> ssh myname@example.com

## SSH and putty

We no longer recommend the usse of putty and instead you should be
using SSH over Powershell for this class.

### Access a Remote Machine

Once the key pair is generated, you can use it to access a remote
machine. To dod so the public key needs to be added to the
`authorized_keys` file on the remote machine.


The easiest way to do tis is to use the command
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

:warning: this section has not been vetted yet

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



### Tips


Use SSH keys

-   You will need to use ssh keys to access remote machines

No blank passphrases

-   In most cases you must use a passphrase with your key. In fact if we
    find that you use passwordless keys to futuresystems and to
    chameleon cloud resources, we may elect to give you an *F* for the
    assignment in question. There are some exceptions, but they will be
    clearly communicated to you in class. You will as part of your cloud
    drivers license test explain how you gain access to futuresystems
    and chameleon to explicitly explain this point and provide us with
    reasons what you can not do.

A key for each server

-   Under no circumstances copy the same private key on multiple
    servers. THis violates security best practices. Create for each
    server a new private key and use their public keys to gain access to
    the appropriate server.

Use SSH agent

-   So as to not to type in all the time the passphrase for a key, we
    recommend using ssh-agent to manage the login. This will be part of
    your cloud drivers license.

    But shut down the ssh-agent if not in use

keep an offline backup, put encrypt the drive

-   You may for some of our projects need to make backups of private
    keys on other servers you set up. If you like to make a backup you
    can do so on a USB stick, but make sure that access to the stick is
    encrypted. Do not store anything else on that key and look it in a
    safe place. If you lose the stick, recreate all keys on all
    machines.


### References


-   [The Secure Shell: The Definitive Guide, 2 Ed (O'Reilly and
    Associates)](http://shop.oreilly.com/product/9780596008956.do)

