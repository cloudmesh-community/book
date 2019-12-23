# Extensions to Eve

Several extensions have been developed by the community. This
includes eve-swagger, eve-sqlalchemy, eve-elastic, eve-mongoengine,
eve-neo4j, eve.net, eve-auth-jwt, and flask-sentinel.

Naturally, there are many more.

Students have the opportunity to pick one of the community extensions and
provide a section for the handbook.

Pick one of the extension, research it and provide a small section for
the handbook, so we add it.

## Object Management with Eve and Evegenie

<http://python-eve.org/>

Eve makes the creation of a REST implementation in python easy. We will
provide you with an implementation example that showcases that we can
create REST services without writing a single line of code. The code for
this is located at <https://github.com/cloudmesh/rest>

This code will have a master branch but will also have a dev branch in which we will add gradually more objects. Objects in the dev branch will
include:

* virtual directories
* virtual clusters
* job sequences
* inventories

You may want to check our ongoing development work in the dev branch.
However, for the purpose of this class, the master branch is
sufficient.

### Installation

First, we have to install MongoDB. The installation will depend on your
operating system. For the use of the REST service, it is not essential to
integrate MongoDB into the system upon reboot, which is the focus of many
online documents. However, for us, it is better if we can start and stop
the services explicitly for now.

On ubuntu, you need to do the following steps:

:o2: TODO: Section can be contributed by a student.

On Windows 10, you need to do the following steps:

:o2: TODO: Section can be contributed by a student. If
  you elect Windows 10. You could be using the online documentation
  provided by starting it on Windows, or running it in a docker
  container.

On macOS you can use home-brew and install it with:

    $ brew update
    $ brew install mongodb

In future, we may want to add SSL authentication in which case you may
need to install it as follows:

    $ brew install mongodb --with-openssl

### Starting the service

We have provided a convenient Makefile that currently only works for
macOS. It is easy for you to adapt it to Linux. Certainly, you can
look at the targets in the makefile and replicate them one by one.
Important targets are deployed and test.

When using the makefile, you can start the services with:

    $ make deploy

It starts two terminals. In one you see the mongo service, in
the other, you see the eve service. The eve service takes a file
called sample.settings.py that is base on sample.json for the start of
the eve service. The mongo service is configured in such a way that it
only accepts incoming connections from the localhost, which is
sufficient for our case. The mongo data is written into the
`$USER/.cloudmesh` directory, so make sure it exists.

To test the services, you can say:

    $ make test

You will see several JSON messages be written to the screen.

### Creating your own objects

The example demonstrated how easy it is to create a MongoDB and an eve
rest service. Now let us use this example to create your own. For this,
we have modified a tool called evegenie to install it onto your system.

The original documentation for evegenie is located at:

-   <http://evegenie.readthedocs.io/en/latest/>

However, we have improved evegenie while providing a command line tool
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

It takes a JSON file as input and writes out a settings file for the use
in eve. Let us assume the file is called sample.json than the settings
file is called sample.settings.py. Having the evegenie program
allows us to generate the settings files easily. You can include
them in your project and leverage the Makefile targets to start the
services in your project. In case you generate new objects, make sure
you rerun evegenie, kill all previous windows in which you run eve and
mongo and restart. In case of changes to objects that you have designed
and run previously, you also need to delete the MongoDB database.
