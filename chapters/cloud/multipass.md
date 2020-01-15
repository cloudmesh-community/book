# Multipass

Multipass is a command line tool to manage Ubuntu virtual machines on a
computer from the command line. With the help of multipass, we can
simulate a cloud that manages virtual machines on your computer.

Naturally, your computer needs to have enough main memory for running
multiple virtual machines. You need administrative privileges
to use multipass (for example, on OSX and Linux being able to run as
`sudo`).

More information about multipass can be found at 

* <https://multipass.run/>

## Install 

Follow the install instructions as documented at

* <https://multipass.run/docs>


## Sudo on OSX

On OSX, you need to be in the sudoer's list. Please consult on the Net to
understand what `sudo` is. We recommend that you create a separate user
with such privileges and use that for trying it out instead of using
your main account. To add this user to `sudo`, conduct the following steps.


First, login as administrator and edit the file 

	/etc/sudoers

In that file find the following line: 

    %admin ALL=(ALL) ALL 

After that line, add your username to the list of sudoers as follows: 

    username ALL=(ALL) ALL
    
    
## Experimenting with Multipass

Now let us experiment with multipass. Launch an instance with 

```bash
$ multipass launch --name ubuntu-lts
```

Execute a command in the instance with 

```bash
$ multipass exec ubuntu-lts -- lsb_release -a
```

List all instances with and specify the output in various formats

```bash
$ multipass list
$ multipass list --format yaml
$ multipass list --format json
$ multipass list --format csv
```

Stop the instance with 

```bash    
$ multipass stop ubuntu-lts
```

Make sure it is stopped

```bash
$ multipass list --format yaml
```

Start the instance

```bash
$ multipass start ubuntu-lts
```

Make sure its started

```bash
$ multipass list --format yaml
```

Stop it again

```bash
$ multipass stop ubuntu-lts
```

Start the primary

```bash
$ multipass start 
```

List the running instances

```bash
$ multipass list --format yaml
```

Delete all instances

```bash
$ multipass delete --all
```

Make sure they are deleted

```bash
$ multipass list --format yaml
```

Purge the instances

```bash
$ multipass purge
```

Make sure they are purged

```bash
$ multipass list --format yaml
```

Find other images

```bash
$ multipass find
```

## Exercises

E.Multipass.1:

> Add installation instruction for your operating system to this
> document.

E.Multipass.2: 

> What is Primary in multipass

E.Multipass.3: 

> What is snapcraft in multipass 

E.Multipass.4:

> How do you write a bibtex entry for <https://multipass.run/>

> Add all bibtex entries (e.g. the URLs you see in multipass.md) into
> <https://github.com/cloudmesh-community/book/blob/master/bib/multipass.bib>

> Tip: see: <https://github.com/cloudmesh-community/book/blob/master/bib/refs.bib> 
> for examples.

> Answer:

> Provided by students

E.Multipass.5:

> Provide more extensive examples for find
>
> * <https://multipass.run/docs/find-command>
> * <https://launchpad.net/ubuntu/+series>
> 
> Provide a list of images that are supported on your system.
>
> OSX:
>
> * ...
>
> Linux:
>
> * ...
>
> Windows:
>
> * ...


E.Multipass.6:

> Explain cloud-init. Provide an example

E.Multipass.7:

> Install MikroK8s in multipass and provide a users guide

