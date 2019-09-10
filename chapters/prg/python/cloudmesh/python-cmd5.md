# Cloudmesh Command Shell {#sec:cmd5}

## CMD5

Python's CMD (<https://docs.python.org/2/library/cmd.html>) is a very
useful package to create command line shells. However it does not allow
the dynamic integration of newly defined commands. Furthermore,
additions to CMD need to be done within the same source tree. To
simplify developing commands by a number of people and to have a dynamic
plugin mechanism, we developed cmd5. It is a rewrite on our earlier
efforts in cloudmesh client and cmd3.

### Resources

The source code for cmd5 is located in github:

* <https://github.com/cloudmesh/cmd5>

We have discussed in @sec:cloudmesh-cms-install how to install cloudmesh
as developer and have access to the source code in a directory called
`cm`. As you read this document we assume you are a developer and can
skip the next section.


### Installation from source

WARNING: DO NOT EXECUTE THIS IF YOU ARE A DEVELOPER OR YOUR ENVIRONMENT
WILL NOT PROPERLY WORK. 
 
If you were a user of cloudmesh you can install it however with 

```bash
$ pip install cloudmesh-cmd5
```

### Execution

To run the shell you can activate it with the cms command. cms stands
for cloudmesh shell:

```bash
(ENV2) $ cms
```

It will print the banner and enter the shell:

    +-------------------------------------------------------+
    |   ____ _                 _                     _      |
    |  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   |
    | | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  |
    | | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | |
    |  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| |
    +-------------------------------------------------------+
    |                  Cloudmesh CMD5 Shell                 |
    +-------------------------------------------------------+

    cms>

To see the list of commands you can say:

    cms> help

To see the manual page for a specific command, please use:

    help COMMANDNAME

### Create your own Extension

One of the most important features of CMD5 is its ability to extend it
with new commands. This is done via packaged name spaces. We recommend
you name is cloudmesh-mycommand, where mycommand is the name of the
command that you like to create. This can easily be done while using the
sys* cloudmesh command (we suggest you use a different name than
`gregor` maybe your firstname):

```bash
$ cms sys command generate gregor
```

It will download a template from cloudmesh called `cloudmesh-bar` and
generate a new directory `cloudmesh-gregor` with all the needed files
to create your own command and register it dynamically with cloudmesh.
All you have to do is to cd into the directory and install the code:

```bash
$ cd cloudmesh-gregor
$ python setup.py install
# pip install .
```

Adding your own command is easy. It is important that all objects are
defined in the command itself and that no global variables be use in
order to allow each shell command to stand alone. Naturally you should
develop API libraries outside of the cloudmesh shell command and reuse
them in order to keep the command code as small as possible. We place
the command in:

    cloudmsesh/mycommand/command/gregor.py

Now you can go ahead and modify your command in that directory. It will
look  similar to (if you used the command name `gregor`):


    from __future__ import print_function
    from cloudmesh.shell.command import command
    from cloudmesh.shell.command import PluginCommand

    class GregorCommand(PluginCommand):

        @command
        def do_gregor(self, args, arguments):
            """
            ::
              Usage:
                    gregor -f FILE
                    gregor list
              This command does some useful things.
              Arguments:
                  FILE   a file name
              Options:
                  -f      specify the file
            """
            print(arguments)
            if arguments.FILE:
               print("You have used file: ", arguments.FILE)
            return ""

An important difference to other CMD solutions is that our commands can
leverage (besides the standard definition), `docopts` as a way to define
the manual page. This allows us to use arguments as dict and use simple
if conditions to interpret the command. Using `docopts` has the advantage
that contributors are forced to think about the command and its options
and document them from the start. Previously we did not use but argparse
and click. However we noticed that for our contributors both systems
lead to commands that were either not properly documented or the
developers delivered ambiguous commands that resulted in confusion and
wrong usage by subsequent users. Hence, we do recommend that you use
docopts for documenting cmd5 commands. The transformation is enabled by
the \@command decorator that generates a manual page and creates a
proper help message for the shell automatically. Thus there is no need
to introduce a separate help method as would normally be needed in CMD
while reducing the effort it takes to contribute new commands in a
dynamic fashion.

### Bug: Quotes

We have one bug in cmd5 that relates to the use of quotes on the commandline

For example you need to say 

```bash
$ cms gregor -f \"file name with spaces\"
```

If you like to help us fix this that would be great. it requires the use
of [shlex](https://docs.python.org/3/library/shlex.html). Unfortuantly
we did not yet time to fix this "feature".


