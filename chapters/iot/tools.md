Tools
=====

-   **Terminal**: On macOS, when you navigate to the search magnification
    glass, you can type in *terminal* to start it. A terminal allows you
    to execute a number of commands to interact with the computer from a
    commandline interface, e.g. the terminal.

-   [Bash](https://linuxconfig.org/bash-scripting-tutorial) it the
    command language used in terminal.

-   [Pyenv](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)
    allows to manage multiple versions of python easily. [Pyenv
    link](https://github.com/pyenv/pyenv#how-it-works)

-   [XCode](https://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osxhttps://cloudmesh.github.io/classes/lesson/prg/pyenv.html?highlight=xcode#install-pyenv-on-osx)
    is an integrated development environment for macOS containing a
    suite of software development tools developed by Apple for
    developing software for macOS, iOS, watchOS and tvOS.

-   [Homebrew](https://brew.sh) is a *package manager* for OS X which
    lets the user *install software* from *UNIX* and *open source
    software* that is not included in macOS.

-   [pyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC):
    is an Integrated Development Environment for Python.

-   *Matplotlib*: Matplotlib is a library that allows us to create nice
    graphs in python. As we typically install python with virtualenv, we
    need to configure matplotlib properly to use it. The easiest way to
    do this is to execute the following commands. After you run them you
    can use matplotlib.

        $ pip install numpy
        $ pip install matplotlib
        $ echo "backend : TkAgg" > ~/.matplotlib/matplotlibrc

-   [Macdown](https://macdown.uranusjr.com/) a macdown editor for macOS

-   [Markdown](https://blog.ghost.org/markdown/) (from Markdown)

-   [AquaEmacs](http://oracc.museum.upenn.edu/doc/help/usingemacs/aquamacs/)
    (from Aquamacs)

-   [Marvelmind](http://marvelmind.com/) (from Marvelmind if you have
    marvelmind positioning sensors which are optional)

-   [Arduino](https://www.arduino.cc/en/guide/macOSX) (from Arduino if
    you like to use their interface to access the esp8266 boards)

-   [40 OSX Terminal
    Tricks](https://computers.tutsplus.com/tutorials/40-terminal-tips-and-tricks-you-never-thought-you-needed--mac-51192)

Markdown
--------

MarkDown is a format convention that produces nicely formatted text with
simple ASCII text. Markdown has very good support for editors that
render the final output in a view window next to the editor pane. Two
such editors are

-   [Macdown](https://macdown.uranusjr.com/): MacDown provides a nice
    integrated editor that works well.

-   [pyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC):
    We have successfully used Vladimir Schhneiders [Markdown Navigator
    plugin](https://plugins.jetbrains.com/plugin/7896-markdown-navigator).
    Once installed you click on a .md file pycharm will automatically
    ask to install the plugins from Markdown for you.

A detailed set of syntax rules can be found at: **BUG: LINK TO MARKDOWN
SYNTAX MISSING**

The following are some basic examples

-   To *emphasise* a text you use `*emphasize*`

-   To make text **bold** use `**bold**`

-   To make text ***bold-and-emphasize*** use `***bold-and-emphasize***`

-   To create a hyperlink use `[Google](https://google.com)` which will
    result in [Google](https://google.com)

-   To include an image use `![Bracketed Text](link)`

A list can be created by item starting with \*, a - , or a + or a number

    1. one
    2. two

1.  one

2.  two

        * one
        * two

-   one

-   two

If you need to indent items underneath already bulleted items, precede
the indent items with four spaces and they will be nested under the item
above them.

To qoute textc precede it with a "\>".

    > Quote

> Quote

Other syntax options can be found in the Format drop-down at the top of
the screen between View and Plug-ins of macdown.

Aquamacs
--------

There are many different versions of emacs available on OSX. Aquamacs is
often used as it integrates nicely with the OSX GUI interface.

-   [AquaEmacs](http://aquamacs.org/download.shtml)

*Aquamacs* is a program for Mac devices which allows the user to edit
text, HTML, LaTeX, C++, Java, Python, R, Perl, Ruby, PHP, and more.
Aquamacs integrates well with OSX and provides many functions through a
menu. You will mostly be using the File, Edit, menus or toolbar icons.

Emacs provides convenient keyboard shortcuts, most of which are
combinations with the Control or Meta key (The Meta key is the ESC key).
If you accidentally end up doing something wrong simply press `CTRL-g`
to get out without issue. Other Keyboard Shortcuts include:

-   `CTRL-x u` or File\>Undo will cancel any command that you did not
    want done. (CHECK)

-   `ESC-g` will cancel any command you are in the middle of.

-   You can break paragraph lines with `Ctrl-x w`, where `w` will wrap
    text around word boundaries.

-   To delete text to the end of the current word, press `ESC-d`.

-   to delete the whole line from the position of the cursor to the end,
    press `CTRL-k`.

Bash
----

Bash is pre-installed in OSX. A *bash* script contains *commands* in
plain text. In order to create a bash script please decide for a
convenient name. Let us assume we name our script *myscript*. Than you can
create and edit such a script with

    $ touch myscript.sh
    $ emacs myscripts.sh

Next you need to add the following line to the top ogf the script:

    !# /bin/bash

To demonstrate how to continue writing a script we will be using the
bash `echo` command that allows you to print text. Lets make the second
line

    echo "Hello World"

You can now save and start executing your script. Click "File" and then
"Save". Open Terminal and type in `cd` followed by the name of the
folder you put the document in. Now we need to execute the script.

*Executing* a Bash script is rather easy. In order to execute a script,
we need to first execute the *permission set*. In order to give Terminal
permission to read/execute a Bash script, you have to type

    chmod u+x myscript.sh

After the script has been granted permission to be executed, you can
test it by typing

    ./myscript.sh

into the terminal. You will see it prints

    Hello World

Arduino
-------

This installation is optional. In the event that there is a TTY error,
you will need to install Arduino, since your Mac may be missing some
drivers that are included in Arduino. Simply go to
[Arduino](https://www.arduino.cc/en/guide/macOSX) and follow the
installation instructions.

OSX Terminal
------------

[CoolTerm](https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux)

download <http://freeware.the-meiers.org/CoolTermMac.zip>
