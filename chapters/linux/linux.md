# Linux

Now that you have Linux or a Linux like environment (such as `gitbash`)
on your computer it is time to learn a number of useful commands to
interact with the system.

In order for this task to enhance your knowledge you are encouraged to
find additional material and are required to complete the table of
useful Linux commands. You will do this as team and create pull
requests improving and completing this documentation. The TAs will
provide a mapping between students and commands to be documented. If
you find additional commands that aught to be listed here, please add.


## History

LINUX is a reimplementation by the community of UNIX which was developed
in 1969 by Ken Thompson and Dennis Ritchie of Bell Laboratories and
rewritten in C. An important part of UNIX is what is called the *kernel*
which allows the software to talk to the hardware and utilize it.

In 1991 Linus Trovalds started developing a Linux Kernel that was
initially targeted for PC's. This made it possible to run it on Laptops
and was later on further developed by making it a full Operating system
replacement for UNIX.

## Shell

One of the most important features for us will be to access the computer
with the help of a *shell*. The shell is typically run in what is called
a terminal and allows interaction to the computer with commandline
programs.

There are many good tutorials out there that explain why one needs a
linux shell and not just a GUI. Randomly we picked the first one that
came up with a google query. This is not an endorsement for the material
we point to, but could be a worth while read for someone that has no
experience in Shell programming:

<http://linuxcommand.org/lc3_learning_the_shell.php>

Certainly you are welcome to use other resources that may suite you
best. We will however summarize in table form a number of useful
commands that you may als find even as a RefCard.

<http://www.cheat-sheets.org/#Linux>

We provide in the next table a number of useful commands that you want
to explore. For more information simply type man and the name of the
command.

.<div class="smalltable">

| Command    | Description   |
| --------------------------------- | --------------------------------- |
| man *command*                     | manual page for the *command*     |
| apropos *text*                    | list all commands that have text in it  |
| ls                                | Directory listing                 |
| ls -lisa                          | list details                      |
| tree                              | list the directories in graphical form |
| cd *dirname*                      | Change directory to *dirname*     |
| mkdir *dirname*                   | create the directory              |
| rmdir *dirname*                   | delete the directory              |
| pwd                               | print working directory           |
| rm *file*                         | remove the file                   |
| cp *a* *b*                        | copy file *a* to *b*              |
| mv *a* *b*                        | move/rename file *a* to *b*       |
| cat *a*                           | print content of file*a*          |
| cat -n *filename*                 | print content of file*a* with     |
|                                   | line numbers                      |
| less *a*                          | print paged content of file *a*   |
| head -5 *a*                       | Display first 5 lines of file *a* |
| tail -5 *a*                       | Display last 5 lines of file *a*  |
| `du -hs .`                        | show in human readable form the space used by the current directory |
| `df -h`                           | show the details of the disk file system |
| wc *filename*                     | counts the word in a file         |
| sort *filename*                   | sorts the file                    |
| uniq *filename*                   | displays only uniq entries in the file |
| tar -xvf *dir*                    | tars up a compressed version of the directory  |
| rsync                             | faster, flexible replacement for rcp                      |
| gzip *filename*                   | compresses the file               |
| gunzip *filename*                 | compresses the file               |
| bzip2 *filename*                  | compresses the file with          |
|                                   | block-sorting                     |
| bunzip2 *filename*                | uncompresses the file with         block-sorting                     |
| clear                             | clears the terminal screen        |
| touch *filename*                  | change file access and             modification times or if file      does not exist creates file       |
| who                               | displays a list of users that are  currently logged on, for each      user the login name, date and time   of login, tty name, and hostname   if not local are displayed        |
| whoami                            | displays the users effective id    see also id                       |
| echo -n *string*                  | write specified arguments to       standard output                   |
| date                              | displays or sets date & time,      when invoked without arguments     the current date and time are      displayed                         |
| logout                            | exit a given session              |
| exit                              | when issued at the shell prompt     the shell will exit and terminate  any running jobs within the shell |
| kill                              | terminate or signal a process by   sending a signal to the specified  process usually by the pid        |
| ps                                | displays a header line followed    by all processes that have         controlling terminals             |
| sleep                             | suspends execution for an          interval of time specified in      seconds                           |
| uptime                            | displays how long the system has   been running                      |
| time *command*                    | times the command execution in     seconds                           |
| find */ \[-name\] file-name.txt*  | searches a specified path or       directory with a given expression  that tells the find utility what   to find, if used as shown the      find utility woud search the       entire drive for a file named      file-name.txt                     |
| diff                              | compares files line by line       |
| hostname                          | prints the name of the current     host system                       |
| which                             | locates a program file in the      users path                        |
| tail                              | displays the last part of the      file                              |
| head                              | displays the first lines of a      file                              |
| top                               | displays a sorted list of system   processes                         |
| locate *filename*                 | finds the path of a file          |
| grep *'word'* *filename*          | finds all lines with the word in   it                                |
| grep -v *'word'* *filename*       | finds all lines without the word   in it                             |
| chmod ug+rw *filename*            | change file modes or Access Control Lists. In this example user and group are changed to read and write |
| chown                             | change file owner and group                                  |
| history                           | a build-in command to list the past commands                     |
| sudo                              |  execute a command as another user   |
| su                                | substitute user identity                       |
| uname                             | print the operating system name   |
| set -o emacs                      | tells the shell to use Emacs commands.                         |
| chmod go-rwx *file*               | changes the permission of the file                              |
| chown *username* *file*           | changes the ownership of the file |
| chgrp *group* *file*              | changes the group of a file       |
| fgrep *text* *filename*           | searches the text in the given     file                              |
| grep -R *text* .                 | recursively searches for xyz in    all files                         |
| find . -name *.py                | find all files with `.py` at the   end                               |
| ps                                | list the running processes        |
| kill -9 1234                      | kill the process with the id 1234 |
| at                                | que commands for later execution                    |
| cron                              | daemon to execute scheduled commands   |
| crontab                           | manage the time table for execution commands with cron                     |
| mount /dev/cdrom /mnt/cdrom       | mount a filesystem from a cd rom   to /mnt/cdrom                     |
| users                             | list the logged in users                     |
| who                               | display who is logged in                      |
| whoami                            | print the user id                      |
| dmesg                             | display the system message buffer                      |
| last                              | indicate last logins of users and ttys                      |
| uname                             | print operating system name                      |
| date                              | prints the current date and time  |
| time *command*                    | prints the sys, real and user      time                              |
| shutdown -h "shut down"           | shutdown the computer                      |
| ping                              | ping a host                     |
| netstat                           | show network statu                    |
| hostname                          | print name of current host system                      |
| traceroute                        | print the route packets take to network host                      |
| ifconfig                          | configure network interface parameters                     |
| host                              | DNS lookup utility                     |
| whois                             | Internet domain name and network number directory service                      |
| dig                               | DNS lookup utility                      |
| wget                              | non-interactive network downloader                      |
| curl                              | transfer a URL                      |
| ssh                               | remote login program                      |
| scp                               | remote file copy program                      |
| sftp                              | secure file transfer program                      |

</div>

## Multi-command execution

One of the important features is that one can execute multiple commands
in the shell.

To execute command 2 once command 1 has finished use

    command1; command2

To execute command 2 as soon as command 1 forwards output to stdout use

    command1; command2

To execute command 1 in the background use

    command1 &

## Keyboard Shortcuts

These shortcuts will come in handy. Note that many overlap with emacs
short cuts.

.<div class="smalltable">

|  Keys       | Description |
|  ---------- | -------------------------------------------------------- |
|  Up Arrow   | Show the previous command |
|  Ctrl + z   | Stops the current command |
|             | Resume with `fg` in the foreground |
|             | Resume with `bg` in the background |
|  Ctrl + c   | Halts the current command |
|  Ctrl + l   | Clear the screen |
|  Ctrl + a   | Return to the start of the line |
|  Ctrl + e   | Go to the end of the line |
|  Ctrl + k   | Cut everything after the cursor to a special clipboard |
|  Ctrl + y   | Paste from the special clipboard |
|  Ctrl + d   | Logout of current session, similar to exit |

</div>

## bashrc and bash_profile

Usage of a particular command and all the attributes associated with it,
use `man` command. Avoid using `rm -r` command to delete files
recursively. A good way to avoid accidental deletion is to include the
following in your `.bash_profile` file:

```bash
alias e=open_emacs
alias rm='rm -i'
alias mv='mv -i' 
alias h='history'
```

More Information

<https://cloudmesh.github.io/classes/lesson/linux/refcards.html>

## Makefile

Makefiles allow developers to coordinate the execution of code
compilations. This not only includes C or C++ code, but any translation
from source to a final format. For us this could include the creation of
PDF files from latex sources, creation of docker images, and the
creation of cloud services and their deployment through simple workflows
represented in makefiles, or the coordination of execution targets.

As makefiles include a simple syntax allowing structural dependencies
they can easily adapted to fulfill simple activities to be executed in
repeated fashion by developers.

An example of how to use Makefiles for docker is provided at
<http://jmkhael.io/makefiles-for-your-dockerfiles/>.

An example on how to use Makefiles for LaTeX is provided at
<https://github.com/cloudmesh/book/blob/master/Makefile>.

Makefiles include a number of rules that are defined by a target name.
Let us define a target called hello that prints out the string "Hello
World".

```
    hello:
        @echo "Hello World"
```

Important to remember is that the commands after a target are not
indented just by spaces, but actually by a single TAB character. Editors
such as emacs will be ideal to edit such Makefiles, while allowing
syntax highlighting and easy manipulation of TABs. Naturally other
editors will do that also. Please chose your editor of choice. One of
the best features of targets is that they can depend on other targets.
Thus, iw we define

```
    hallo: hello
        @echo "Hallo World"
```

our makefile will first execute hello and than all commands in hallo. As
you can see this can be very useful for defining simple dependencies.

In addition we can define variables in a makefile such as

```
    HELLO="Hello World"

    hello: 
        @echo $(HELLO)
```

and can use them in our text with \$ invocations.

Moreover, in sophisticated Makefiles, we could even make the targets
dependent on files and a target rules could be defined that only
compiles those files that have changed since our last invocation of the
Makefile, saving potentially a lot of time. However, for our work here
we just use the most elementary makefiles.

For more information we recommend you to find out about it on the
internet. A convenient reference card sis available
at <http://www.cs.jhu.edu/~joanne/unixRC.pdf>.

### Makefiles on Windows

Makefiles can easily be accessed also on windows while installing
gitbash. Please reed to the internet or search in this handbook for more
information about gitbash.

## Exercises

E.Linux.1

> Familiarize yourself with the commands

E.Linux.2

> Find more commands that
>  you find useful and add them to this page.

E.Linux.3

> Use the sort command to sort all lines of a file while removing
>  duplicates.

E.Linux.4

> Should there be other commands listed in the table with the Linux commands
>  If so which? Create a pull request for them.

E.Linux.5

> Write a section explaining chmod. Use letters not numbers

E.Linux.6

> Write a section explaining chown. Use letters not numbers

E.Linux.7

> Write a section explaining su and sudo

E.Linux.8

> Write a section explaining cron, at, and crontab
