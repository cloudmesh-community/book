# Output


## Console

Print is the usual function to output to the terminal. However often we
like to have colored output that helps us in the notification to the
user. For this reason we have a simple `Console` class that has several
build in features. you can even swith and devine your own color
schemas.

```python
from cloudmesh.common.console import Console


msg = "my message"

Console.ok(msg) # prins a green message
Console.error(msg) # prins a red messag proceeded with ERROR
Console.msg(msg) # prins a regular balck message
```

In case of the error message we also have convenient flags that allow us
to include th tracebak in the output.

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

## Banner

In case you need a banner you can do this with

```python
from cloudmesh.common.util import banner

banner("my text")
```

## Heading

A particular useful function is `HEADING()` which prints the method name.

```python

from cloudmesh.common.util import HEADING

class example(object):

    def doit(self):
        HEADING()
        print ("Hallo")
```

The infocation of the function doit prints a banner with the name
information. The reason we did not do it as a decorator is that you can
place the HEADIn in an arbitrary location of the method body.
