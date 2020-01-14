# Multipass

TODO Write what multipass is

## Install 

Follow the install instructions as documented at

* ...

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

    multipass launch --name ubuntu-lts

Execute a command in the instance with 

    multipass exec ubuntu-lts -- lsb_release -a

List all instances with and specify the output in a particular format

    multipass list
    multipass list --format yaml
    multipass list --format json
    multipass list --format csv
    
Stop the instance with 
    
    multipass stop ubuntu-lts

Make sure its stopped

    multipass list --format yaml

Start the instance

    multipass start ubuntu-lts

Make sure its started

    multipass list --format yaml

Stop it again

    multipass stop ubuntu-lts

Start the primary

    multipass start 

List the running instances

    multipass list --format yaml

Delete all instances

    multipass delete --all

Make sure they are deleted

    multipass list --format yaml

Purge the instances

    multipass purge

Make sure they are purged

    multipass list --format yaml

Find other images

    multipass find
