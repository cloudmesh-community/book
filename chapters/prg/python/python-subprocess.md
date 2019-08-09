# Subprocess

A module which allows us to start a new process and connect to their
input, output, error nodes and get the return values is called a
subprocess.

## Cloudmesh Subprocess

The easiset way to use subprocesses is simply to use the cloudmesh `Shell`.

```python
form cloudmesh.common3.Shell import Shell

result = Shell.run("ls -lisa")
print (result)
``` 

The nice thing about this function is that the return result will be
converted to a string which yuo may often need to do. This allows you to
also convert the result into a list with the split function:

```python
lines = result.split("\n")
```

Now you can iterate through the lines with

```python
for line in lines:
    print (line)
```

## Popen Class :o:

If you need more featureful interaction you may have to use the Popen class.

Internally starting subprocesses is facilitated with the `Popen` class.
Additional convenient helper functions are `check_output`, and
`check_call`. The  method  signature of this class is as follows:

```python
class subprocess.Popen(
    args,
    bufsize=0,
    executable=None,
    stdin=None,
    stdout=None,
    stderr=None,
    preexec_fn=None,
    close_fds=False,
    shell=False,
    cwd=None,
    env=None,
    universal_newlines=False,
    startupinfo=None,
    creationflags=0
)
```

The following program demonstrates how to start the Unnix command 
`ls -lisa`.

## Subprocess communicate()

```python
from subprocess import Popen, PIPE

process = Popen(['cat', '-lisa'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)
print(stderr)
```
	
`process.communicate()` reads the input and output from the process.
`stderr` will only get populated if there is some error. `stdout` is the
output for this process. Please note that the content of the output in
python 3 is returned as binary.

The `communicate()` method returns a tuple (stdoutdata, stderrdata).
`Popen.communicate()` interacts with process: 

1. Send data to stdin. 
2. Read data from stdout and stderr, until end-of-file is reached.
3. Wait for process to terminate.

## Subprocess call()

The convenient `call()` method simplifies ineraction with subprocesses.

```python
subprocess.call(args, *,
                stdin=None,
                stdout=None,
				stderr=None,
				shell=False)
## Run the command described by args. 
## Wait for command to complete, then return the returncode attribute.
```


```python
subprocess.call(['ls', '-l'])
```

Here we simple pass a list and asure that the commands and arguments are
elements in the list.

As you will execute the commands in a shell, you may also sometimes
interrested in loading the environment that you have set up with
`.bashrc` or  `.bash_profile`. For this reason you can pass along the
`shell` flag and set it to `True`. On Linux the default shell is
`/bin/sh` and on Windows it is `cmd.exe`. In this case you can either
use a string which will be parsed accordingly or use a list

```python
subprocess.call('ls -lisa', shell=True)
subprocess.call(['ls', '-l'], shell=True)
```

## Save process output (stdout)

We can get the program output using check_output and store it in a
string which we can later print. Method definition is as follows:

```python
subprocess.check_output(
    args, 
    *, 
    stdin=None, 
    stderr=None, 
    shell=False, 
    universal_newlines=False
)

## Run command with arguments and return its output as a byte string.
```

Example:

```python
>>> import subprocess
>>>
>>> s = subprocess.check_output(["echo", "Hello World!"])
>>> print("s = " + s)

# 's = Hello World!\n'
```

If we want to get the standard error output, use stderr = subprocess.STDOUT

```python
>>> subprocess.check_output(
    "ls non_existent_file; exit 0", 
    stderr=subprocess.STDOUT, 
    shell=True)

# ls: non_existent_file: No such file or directory\n'
```

## Getting the return code (OR exit status)

If we get a non-zero return code, then it will raise a
CalledProcessError. This object will have return code in returncode
attribute and output will be in output attribute.
	
```python
>>> subprocess.check_output("exit 1", shell=True)
Traceback (most recent call last):
   
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

Exception subprocess.CalledProcessError

Exception raised when a process run by check_call() or check_output()
returns a non-zero exit status.
```

* returncode: Exit status of the child process.

* cmd: Command that was used to spawn the child process.

* output: Output of the child process if this exception is raised by
  check_output(). Otherwise, None.

* `subprocess.PIPE`: Special value that can be used as the stdin,
  stdout or stderr argument to Popen and indicates that a pipe to the
  standard stream should be opened. Most useful with
  Popen.communicate().

* `subprocess.STDOUT`: Special value that can be used as the stderr
  argument to Popen and indicates that standard error should go into
  the same handle as standard output.

  Do not use stdout=PIPE or stderr=PIPE with this function as that can
  deadlock based on the child process output volume. Use Popen with
  the communicate() method when you need pipes.
	

## Popen Constructor

The process creation and its management is handled by this class -
Popen. Its signature is as follows:

```python
class subprocess.Popen(args, 
                       bufsize=0, 
                       executable=None, 
                       stdin=None, 
                       stdout=None, 
                       stderr=None, 
                       preexec_fn=None, 
                       close_fds=False, 
                       shell=False, 
                       cwd=None, 
                       env=None, 
                       universal_newlines=False, 
                       startupinfo=None, 
                       creationflags=0)
```
This will execute a child program in a new process. The arguments to
Popen is as follows:

* args are a sequence of program arguments or it can be a single string. 

If the arguments is a sequence, then by default, the first item in args
is the program to execute. If args is a string, the interpretation is
platform-dependent which will see next. Unless stated specifically, it
is recommended to pass args as a sequence.

On Unix, if args is a string, the string is interpreted as the name or
path of the program to execute. However, this can only be done if not
passing arguments to the program.


Note that `shlex.split()` can be useful when determining the correct
tokenization for args, especially in complex cases:

Source: <https://docs.python.org/2/library/subprocess.html>

```
>>> import shlex, subprocess
>>> command_line = raw_input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', 
 '-input', 
 'eggs.txt', 
 '-output', 
 'spam spam.txt', 
 '-cmd', 
 "echo '$MONEY'"]
>>> p = subprocess.Popen(args) ## Success!
```

Options (such as -input) and arguments (such as eggs.txt) that are
separated by whitespace in the shell go in separate list elements,
while arguments that need quoting or backslash escaping when used in
the shell (such as filenames containing spaces or the echo command)
are single list elements.

On Windows, if args is a sequence then it will be converted to a
string. This is because the underlying CreateProcess() operates on
strings. Parsing the string after conversion uses the following rules:

1. Arguments are delimited by white space, which is either a space or
   a tab.
2. A string surrounded by double quotation marks is interpreted as a
   single argument, regardless of white space contained within. A
   quoted string can be embedded in an argument.
3. A double quotation mark preceded by a backslash is interpreted as a
   literal double quotation mark.
4. Backslashes are interpreted literally, unless they immediately
   precede a double quotation mark.
5. If backslashes immediately precede a double quotation mark, every
   pair of backslashes is interpreted as a literal backslash. If the
   number of backslashes is odd, the last backslash escapes the next
   double quotation mark as described in rule 3.

The shell argument is by default set to False, this argument specifies
whether to use the shell as the program to execute. If shell is True,
it is recommended to pass args as a string rather than as a sequence.


## Exceptions in Subprocess

If a child process raises any exception before the new program starts,
that exception will be raised again in the parent
process. Additionally, the exception object will have one extra
attribute called child_traceback, which is a string containing
traceback information from the child’s point of view.

* OSError - This occurs, for example, when trying to execute a
  non-existent file. Applications should prepare for OSError exceptions.

* ValueError - This will be raised if Popen is called with invalid
  arguments.

* CalledProcessError - check_call() and check_output() will raise
  CalledProcessError if the called process returns a non-zero return
  code.

## Security

Its very important for the application to handle security aspect explicitly. 

## Popen Objects

* `Popen.poll()`: Check if child process has terminated. Set and return
  returncode attribute.

* `Popen.wait()`: Wait for child process to terminate. Set and return
  returncode attribute.

  :warning: *This will deadlock when using
  `stdout=PIPE` and/or `stderr=PIPE` and the child process generates
  enough output to a pipe such that it blocks waiting for the OS pipe
  buffer to accept more data. Use `communicate()` to avoid that.*
	
* `Popen.communicate(input=None)`: Interact with process: Send data to
  stdin. Read data from stdout and stderr, until end-of-file is
  reached. Wait for process to terminate. The optional input argument
  should be a string to be sent to the child process, or None, if no
  data should be sent to the child.  communicate() returns a tuple
  (stdoutdata, stderrdata).

  Note that if you want to send data to the process’s stdin, you need
  to create the Popen object with stdin=PIPE. Similarly, to get
  anything other than None in the result tuple, you need to give
  stdout=PIPE and/or stderr=PIPE too.  The data read is buffered in
  memory, so do not use this method if the data size is large or
  unlimited.
	
* `Popen.send_signal(signal)`: Sends the signal signal to the child.

	On Windows, SIGTERM is an alias for terminate(). CTRL_C_EVENT
    and CTRL_BREAK_EVENT can be sent to processes started with a
    creationflags parameter which includes `CREATE_NEW_PROCESS_GROUP`.
	
* `Popen.terminate()`: Stop the child. On Posix OSs the method sends
  SIGTERM to the child. On Windows the Win32 API function
  TerminateProcess() is called to stop the child.

* `Popen.kill()`: Kills the child. On Posix OSs the function sends
  SIGKILL to the child. On Windows kill() is an alias for terminate().

The following attributes are also available:

:warning: *Use `communicate()` rather than< .stdin.write, .stdout.read or
.stderr.read to avoid deadlocks due to any of the other OS pipe
buffers filling up and blocking the child process.*
	
* `Popen.stdin`: If the stdin argument was PIPE, this attribute is a
  file object that provides input to the child process. Otherwise, it
  is None.

* `Popen.stdout`: If the stdout argument was PIPE, this attribute is a
  file object that provides output from the child process. Otherwise,
  it is None.

* `Popen.stderr`: If the stderr argument was PIPE, this attribute is a
  file object that provides error output from the child
  process. Otherwise, it is None.

* `Popen.pid`: The process ID of the child process. If you set the
  shell argument to True, this is the process ID of thespawned shell.

* `Popen.returncode`: The child return code, set by poll() and wait()
  (and indirectly by communicate()). A None value indicates that the
  process hasn’t terminated yet.

A negative value `-N` indicates that the child was terminated by signal
N (Unix only).

