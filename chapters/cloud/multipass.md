# Multipass :o2:

:o2: Assignment Write what multipass is

* <https://multipass.run/>

## Install 

Follow the install instructions as documented at

* <https://multipass.run/docs>

## Sudo

Login as administrator

We recommend not to use your regular unpriviledged user name. Instead
create a new username that you use for multipass.

Edit the file 

    /etc/sudoers

In that file find following line: 

    %admin ALL=(ALL) ALL 

After that line add your user to the list of sudoers as follows: 

    username ALL=(ALL) ALL
    
    
## Experimenting with Multipass

Launch an instance with 

    $ multipass launch --name ubuntu-lts

Execute a command in the instance with 

    $ multipass exec ubuntu-lts -- lsb_release -a

List all instances with and specify the output in a particular format

    $ multipass list
    $ multipass list --format yaml
    $ multipass list --format json
    $ multipass list --format csv
    
Stop the instance with 
    
    $ multipass stop ubuntu-lts

Make sure its stopped

    $ multipass list --format yaml

Start the instance

    $ multipass start ubuntu-lts

Make sure its started

    $ multipass list --format yaml

Stop it again

    $ multipass stop ubuntu-lts

Start the primary

    $ multipass start 

List the running instances

    $ multipass list --format yaml

Delete all instances

    $ multipass delete --all

Make sure they are deleted

    $ multipass list --format yaml

Purge the instances

    $ multipass purge

Make sure they are purged

    $ multipass list --format yaml

Find other images

    $ multipass find


## Excersises

E.Multipass.1:

> Add instalation instruction for your operating system to this document.

E.Multipass.2: 

> What is Primary in multipass

E.Multipass.3: 

> What is snapcraft in multipass 

E.Multipass.4:

> How do you write a bibtex entry for <https://multipass.run/>

> Add all bibtex entries (e.g. the urls you see in multipass.md) into
> <https://github.com/cloudmesh-community/book/blob/master/bib/multipass.bib>

> Tip: see: <https://github.com/cloudmesh-community/book/blob/master/bib/refs.bib> 
> for examples.

> Answer:

> TBD

E.Multipass.5:

> Provide mor extensive examples for find.
>
> * <https://multipass.run/docs/find-command>
> * <https://launchpad.net/ubuntu/+series>
> 
> Provide a list which are supported on your system.

E.Multipass.6:

> Explain cloud-init. Provide an example

E.Multipass.7:

> Install MikroK8s in multipass and provide a users guide

