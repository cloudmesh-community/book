# Shell

Python provides a sophisticated method for starting backen processe.
However in many cases it is quite complex to interact with it. It also
does not provide convenient wrappers that we can use to start them in a
pythonic fashion. For this reason we have written a primitive `Shell`
class that provides just enough functionality to be useful in many
cases.

Let us iterate its use over some examples where the value in result
returns the output of the command.


```python
from cloudmesh.common.Shell import Shell


Shell.execute('pwd')
print(result)

result = Shell.execute('ls', ["-l", "-a"])
print(result)

result = Shell.execute('ls', "-l -a")
print(result)
```

For many commands we also provide build in functions`

```python
result = Shell.ls("-aux")
print(result)

result = Shell.ls("-a", "-u", "-x")
print(result)

result = Shell.pwd()
print(result)
```

The list includes (naturally the commands must be available on your OS.
If the shell command is not available on your OS, please help us
improving the code to either provide functions that work on your OS or
develop with us platform independent functionality of a subset of the
functionality for the shell command that we may benefit from.

* `VBoxManage(cls, *args)`
* `bash(cls, *args)`
* `blockdiag(cls, *args)`
* `brew(cls, *args)`
* `cat(cls, *args)`
* `check_output(cls, *args, **kwargs)`
* `check_python(cls)`
* `cm(cls, *args)`
* `cms(cls, *args)`
* `command_exists(cls, name)`
* `dialog(cls, *args)`
* `edit(filename)`
* `execute(cls,*args)`
* `fgrep(cls, *args)`
* `find_cygwin_executables(cls)`
* `find_lines_with(cls, lines, what)`
* `get_python(cls)`
* `git(cls, *args)`
* `grep(cls, *args)`
* `head(cls, *args)`
* `install(cls, name)`
* `install(cls, name)`
* `keystone(cls, *args)`
* `kill(cls, *args)`
* `live(cls, command, cwd=None)`
* `ls(cls, *args)`
* `mkdir(cls, directory)`
* `mongod(cls, *args)`
* `nosetests(cls, *args)`
* `nova(cls, *args)`
* `operating_system(cls)`
* `pandoc(cls, *args)`
* `ping(cls, host=None, count=1)`
* `pip(cls, *args)`
* `ps(cls, *args)`
* `pwd(cls, *args)`
* `rackdiag(cls, *args)`
* `remove_line_with(cls, lines, what)`
* `rm(cls, *args)`
* `rsync(cls, *args)`
* `scp(cls, *args)`
* `sh(cls, *args)`
* `sort(cls, *args)`
* `ssh(cls, *args)`
* `sudo(cls, *args)`
* `tail(cls, *args)`
* `terminal(cls, command='pwd')`
* `terminal_type(cls)`
* `unzip(cls, source_filename, dest_dir)`
* `vagrant(cls, *args)`
* `version(cls, name)`
* `which(cls, command)`

For more features, please see [Shell](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=shell#module-cloudmesh.common.Shell)
