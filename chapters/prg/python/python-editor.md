Editors
-------

This section is meant to give an overview of the python editing tools
needed for doing for this course. There are many other alternatives,
however, we do recommend to use PyCharm.

### Pycharm

PyCharm is an Integrated Development Environment (IDE) used for
programming in Python. It provides code analysis, a graphical debugger,
an integrated unit tester, integration with git.

[:clapper: Python 8:56 Pycharm](https://youtu.be/X8ZpbZweJcw)

### Python in 45 minutes

An additional community video about the Python programming language that
we found on the internet. Naturally there are many alternatives to this
video, but the video is probably a good start. It also uses PyCharm
which we recommend.

[:clapper: Python 43:16 PyCharm](https://www.youtube.com/watch?v=N4mEzFDjqtA)

How much you want to understand of python is actually a bit up to you.
While its good to know classes and inheritance, you may be able for this
class to get away without using it. However, we do recommend that you
learn it.

PyCharm Installation:
Method 1: PyCharm Installation on ubuntu using umake

    sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
    sudo apt-get update
    sudo apt-get install ubuntu-make

Once umake command is run, use below command to install Pycharm community edition:

    umake ide pycharm
    
If you want to remove PyCharm installed using umake command, use this:

    umake -r ide pycharm
    
Method 2: PyCharm installation on ubuntu using PPA

    sudo add-apt-repository ppa:mystic-mirage/pycharm
    sudo apt-get update
    sudo apt-get install pycharm-community
    
PyCharm also has a Professional (paid) version which can be installed using following command:

    sudo apt-get install pycharm
    
Once installed, go to your VM dashboard and search for PyCharm.
