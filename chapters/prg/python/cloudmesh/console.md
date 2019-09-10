# Output

Cloudmesh provides a number of convenient API's to make output easier
or mor fancyful. 

These API's include

* [Console](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html#module-cloudmesh.common.console)
* [Banner](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=banner#cloudmesh.common.util.banner)
* [Heading](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=heading#cloudmesh.common.util.HEADING)
* [VERBOSE](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=verbose#cloudmesh.common.debug.VERBOSE)

## Console {#sec:cloudmesh-console}

Print is the usual function to output to the terminal. However often we
like to have colored output that helps us in the notification to the
user. For this reason we have a simple `Console` class that has several
build in features. you can even switch and devine your own color
schemas.

```python
from cloudmesh.common.console import Console


msg = "my message"

Console.ok(msg) # prins a green message
Console.error(msg) # prins a red message proceeded with ERROR
Console.msg(msg) # prins a regular black message
```

In case of the error message we also have convenient flags that allow us
to include the traceback in the output.

```python
Console.error(msg, prefix=True, traceflag=True)
```

The prefix can be switched on and off with the prefix flag, while the
traceflag switches on and of if the trace should be set.

The verbosity of the output is controlled via variables that are stored
in the `~/.cloudmesh` directory.

```python
from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

```

For more features, see API: [Console](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html#module-cloudmesh.common.console)


## Banner

In case you need a banner you can do this with

```python
from cloudmesh.common.util import banner

banner("my text")
```

For more features, see API: [Banner](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=banner#cloudmesh.common.util.banner)

## Heading

A particular useful function is `HEADING()` which prints the method name.

```python

from cloudmesh.common.util import HEADING

class example(object):

    def doit(self):
        HEADING()
        print ("Hallo")
```

The invocation of the `HEADING()` function doit prints a banner with the name
information. The reason we did not do it as a decorator is that you can
place the HEADIn in an arbitrary location of the method body.

For more features, see API: [Heading](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=heading#cloudmesh.common.util.HEADING)

## VERBOSE

VERBOSE is a very useful method allowing you to print a
dictionary. NOt only will it print the dict, but it will also provide
you with the information in which file it is used and which line
number. It even will print the name of the dict that you use in your
code.

To use this you will have to enable the debugging methods for
cloudmesh as discused in @sec:cloudmesh-console

```python
d = {"sample": "value"}
VERBOSE(d)
```

For more features, please see [VERBOSE](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=verbose#cloudmesh.common.debug.VERBOSE)



## Using print and pprint

In many cases it may just be sufficient to use `print` and `pprint` for
debugging. But as the code is big and you may forgot where you placed
print statements ore the print statements are added by others, we
recommend that you use the VERBOSE function instead. However if you
use `print` or `pprint` we recommend to put a unique prefix in it such as

```python
from pprint import pprint

d = {"sample": "value"}
print("MYDEBUG:")
pprint (d)

# or with print

print("MYDEBUG:", d)
```
