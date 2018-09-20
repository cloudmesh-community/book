# Draft: Enhanced Cloudmesh

In this chapter we will be using some advanced Python features to
enhance Cloudmesh. Cloudmesh is supposed to easily manage multiple
clouds. We will be explicitly using python 3 and do not worry about
backwards compatibility. It is a reimplementation of earlier versions of
cloudmesh, including cloudmesh client.

We will be developing it as community so that new features can be
integrated and loaded on demand while adding an extensible package
management system based on pythons shared namespace. To do so we will
rely on `cmd5` that includes a generate command to add new packages on
demand. We will not use all features of cmd5.

We are trying to develop the following:

Configuration:

> so that we can easily configure and add various clouds to our
> multi-cloud environment.

Database: \> of virtual machines and clouds so that they can be managed
across \> different clouds in a multi cloud environment

API Classes: \> so that we can use python as a convenient programming
environment.

Context: \> libraries so that in python we can easily apply context for
clouds \> and virtual machines on a block of statements

Command Shell: \> so that we can similar to matlab and other shells
execute multiple \> commands

REST Services: \> so that we can access the features form other
programming \> environments and different programming languages.

Parallel Services: \> so that we can issue commands in parallel and
manage virtual \> machines in a multi cloud environment.

## Configuration

As we are developing a multi-cloud environment, we need some mechanism
to define the clouds easily. To make our development effort simpler, we
like to point out that the configuration file must be stored in a
particular location relative to the home directory. We store the file in
`~/.cloudmesh/class.yaml`. Additionally we store our cloud passwords in
this file in cleartext and thus we must make sure our machine is not
compromised and that we properly protect the file. On a unix system you
do this with:

    mkdir ~/.cloudmesh
    touch ~/.cloudmesh/class.yaml
    chmod go-rw ~/.cloudmesh
    chmod go-rw ~/.cloudmesh/class.yaml

In that directory we store a file similar to the following file:

    version: 5.0
    profile:
      firstname: Gregor
      lastname: von Laszewski
      email: laszewski@gmail.com
    cloudmesh:
      default:
      - chameleon 
      active:
      - chameleon
    clouds:
      uc:
        name: Chameleon UC
        host: chameleoncloud.org
        type: openstack
        version: liberty
        credentials:
          OS_AUTH_URL: https://openstack.uc.chameleoncloud.org:5000/v3
          OS_PASSWORD: TBD
          OS_TENANT_NAME: CH-818664
          OS_TENANT_ID: CH-818664
          OS_PROJECT_NAME: CH-818664
          OS_PROJECT_DOMAIN_ID: default
          OS_USER_DOMAIN_ID: default
          OS_USERNAME: TBD
          OS_VERSION: liberty
          OS_REGION_NAME: RegionOne
        default:
          flavor: m1.small
          image: Ubuntu-Server-14.04-LTS
      tacc:
        name: Chameleon TACC
        host: chameleoncloud.org
        type: openstack
        version: liberty
        credentials:
          OS_AUTH_URL: https://openstack.tacc.chameleoncloud.org:5000/v3
          OS_PASSWORD: TBD
          OS_TENANT_NAME: CH-818664
          OS_TENANT_ID: CH-818664
          OS_PROJECT_NAME: CH-818664
          OS_PROJECT_DOMAIN_ID: default
          OS_USER_DOMAIN_ID: default
          OS_USERNAME: TBD
          OS_VERSION: liberty
          OS_REGION_NAME: RegionOne
        default:
          flavor: m1.small
          image: Ubuntu-Server-14.04-LTS

Important to note is that this file defines multiple clouds and uses the
attribute value TBD for password and username which you may want to
change. However, we also would like to support a mode that when the
password is defined to be TBD that it is asked from the terminal. This
way we do not necessarily have to store the password here. In future we
will enhance this file to be encrypted and decrypted with a password
protected ssh key.

The file is a yaml file as the typical configuration in python is not
suitable to easily store hierarchical data. YAML is also more readable
than json so it provides a really good way of defining the configuration
data. Problematic with yaml readers however are that they typically do
not preserver the read order. Your task will be to write a *short* yaml
configuration reader that preserves the order. You are encouraged to
reuse methods. What your are not supposed to do is to reimplement yaml.

There are some special properties of this file that we need to discuss.

-   clouds are listed in the clouds section

-   the credentials section to each cloud defines how to connect to the
    cloud with python libraries such as libcloud. Each cloud type will
    have different parameters.

-   

## Storage

As we need to store some of the data we must identify a suitable
database for storing information about virtual machines and other
information related to the clouds. Although shelve comes in mind, we
found out that it is not compatible between python 2 and 3 which may be
an issue in future. Also when considering services such as mongodb they
have to be started and properly secured. THis naturally can be done with
containers. We also do not want to use large frameworks such as django
which come with build in object models as they are not lightweight.
Hence, we start we just use a file based sql database as provided with
sqlite3.

### sqlite3

While we keep the configuration in the configuration yaml file we intend
to create a database entry for virtual machines we start in the cloud.
In order to store hierarchical information that we may obtain in dict
format from a virtual machine we can easily create flattened out data
structures, by simple connecting the attribute names and separate them
by `_`.

Let us assume we want to store an object of the following form:

    element = {
       'id': 1,
       'cloud': 'chameleon',
       'name': 'vm1',
       'data': {
           "image": 'ubuntu',
           "flavor": "small"
        }
    }

A table that could store such an object could be

    create table element (
        id           integer primary key,
        name         text
        cloud        text,
        data_image:  text,
        data_flavor: text
    );

Obviously, we could create the table automatically from recursively
iterating through the dict to make our approach generalized for any
dict. As for the primary key, we simply assume it is always the id which
is an integer that always increases and is stored in the database. as a
separate element.

Thus we probably want a table generator such as

``` {.python}
class Database (object):
   @staticmethod
   def generate (dictionary):
      # implement me
```

Additionally we want to create convenience methods for adding, deleting,
and searching information

### Context

Python provides the feature of a context that we are well familiar with
from file management. An example is:

``` {.python}
with open('/tmp/gregor.txt', 'wt') as f:
    f.write('Hello Gregor')
# after this, the file is automatically closed
```

If we look at this example it is desirable to develop at least two
context for multicloud environments. The first is to manage virtual
machines on named clouds and issue action on it, such as *start, stop,
suspend, resume, delete*. In the other context we like to issue such
action on named virtual machines.

To illustrate what we have in mind, please take a look at our initial
examples.

#### Cloud Context

When defining the following cloud context

``` {.python}
class Cloud (object):
        
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print ('Running on:', self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')

    def machine(self, name, action):
        print (name, action)
```

we can issue conveniently commands such as the following

``` {.python}
cloud = 'chameleon'
with Cloud(cloud) as c:
    vm = c.machine('vm1', 'start')
```

It is obvious that through this abstraction we can formulate a templated
behavior such as starting a virtual machine and through the switch of a
single variable (`cloud`) issue the command on other clouds.
