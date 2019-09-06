# Extensions to Eve

A number of extensions have been developed by the community. This
includes eve-swagger, eve-sqlalchemy, eve-elastic, eve-mongoengine,
eve-neo4j, eve.net, eve-auth-jwt, and flask-sentinel.

Naturally there are many more.

Students have the opportunity to pic one of the community extensions and
provide a section for the handbook.

Pick one of the extension, research it and provide a small section for
the handbook so we add it.

## Object Management with Eve and Evegenie

<http://python-eve.org/>

Eve makes the creation of a REST implementation in python easy. We will
provide you with an implementation example that showcases that we can
create REST services without writing a single line of code. The code for
this is located at <https://github.com/cloudmesh/rest>

This code will have a master branch but will also have a dev branch in
which we will add gradually more objects. Objects in the dev branch will
include:

* virtual directories
* virtual clusters
* job sequences
* inventories

You may want to check our active development work in the dev branch.
However for the purpose of this class the master branch will be
sufficient.

### Installation

First we have to install mongodb. The installation will depend on your
operating system. For the use of the rest service it is not important to
integrate mongodb into the system upon reboot, which is focus of many
online documents. However, for us it is better if we can start and stop
the services explicitly for now.

On ubuntu, you need to do the following steps:

:o2: TODO: Section can be contributed by student.

On windows 10, you need to do the following steps:

:o2: TODO: Section can be contributed by student. If
  you elect Windows 10. You could be using the online documentation
  provided by starting it on Windows, or running it in a docker
  container.

On macOS you can use home-brew and install it with:

    $ brew update
    $ brew install mongodb

In future we may want to add ssl authentication in which case you may
need to install it as follows:

    $ brew install mongodb --with-openssl

### Starting the service

We have provided a convenient Makefile that currently only works for
macOS. It will be easy for you to adapt it to Linux. Certainly you can
look at the targets in the makefile and replicate them one by one.
Important targets are deploy and test.

When using the makefile you can start the services with:

    $ make deploy

IT will start two terminals. IN one you will see the mongo service, in
the other you will see the eve service. The eve service will take a file
called sample.settings.py that is base on sample.json for the start of
the eve service. The mongo service is configured in such a way that it
only accepts incoming connections from the local host which will be
sufficient for our case. The mongo data is written into the
`$USER/.cloudmesh` directory, so make sure it exists.

To test the services you can say:

    $ make test

You will se a number of json text been written to the screen.

### Creating your own objects

The example demonstrated how easy it is to create a mongodb and an eve
rest service. Now let us use this example to create your own. For this
we have modified a tool called evegenie to install it onto your system.

The original documentation for evegenie is located at:

-   <http://evegenie.readthedocs.io/en/latest/>

However, we have improved evegenie while providing a commandline tool
based on it. The improved code is located at:

-   <https://github.com/cloudmesh/evegenie>

You clone it and install on your system as follows:

    $ cd ~/github
    $ git clone https://github.com/cloudmesh/evegenie
    $ cd evegenie
    $ python setup.py install
    $ pip install .

This should install in your system evegenie. YOu can verify this by
typing:

    $ which evegenie

If you see the path evegenie is installed. With evegenie installed its
usage is simple:

    $ evegenie

    Usage:
      evegenie --help
      evegenie FILENAME

It takes a json file as input and writes out a settings file for the use
in eve. Lets assume the file is called sample.json, than the settings
file will be called sample.settings.py. Having the evegenie program
will allow us to generate the settings files easily. You can include
them into your project and leverage the Makefile targets to start the
services in your project. In case you generate new objects, make sure
you rerun evegenie, kill all previous windows in which you run eve and
mongo and restart. In case of changes to objects that you have designed
and run previously, you need to also delete the mongod database.
