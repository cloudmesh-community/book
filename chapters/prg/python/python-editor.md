# Editors {#sec:python-editors}

This section is meant to give an overview of the python editing tools
needed for doing for this course. There are many other alternatives,
however, we do recommend using PyCharm.

## Pycharm

PyCharm is an Integrated Development Environment (IDE) used for
programming in Python. It provides code analysis, a graphical debugger,
an integrated unit tester, integration with git.

[![Video](images/video.png) Python 8:56 Pycharm](https://youtu.be/X8ZpbZweJcw)

## Python in 45 minutes

An additional community video about the Python programming language that
we found on the internet. Naturally, there are many alternatives to this
video, but the video is probably a good start. It also uses PyCharm
which we recommend.

[![Video](images/video.png) Python 43:16 PyCharm](https://www.youtube.com/watch?v=N4mEzFDjqtA)

How much you want to understand Python is a bit up to you.
While it is good to know classes and inheritance, you may be able for this
class to get away without using it. However, we do recommend that you
learn it.

PyCharm Installation:

Method 1: Download and install it from the pyCharm website. This is easy and if
no automated install is required we recommend this method. Students and
teachers can apply for a free professional version. Please note that Jupyter
notebooks can only be viewed in the professional version.

Method 2: PyCharm Installation on ubuntu using umake

```python
$ sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
$ sudo apt-get update
$ sudo apt-get install ubuntu-make
```

Once the `umake` command is installed, use the next command to install PyCharm community edition:

```python
$ umake ide pycharm
```

If you want to remove PyCharm installed using umake command, use this:

```python
$ umake -r ide pycharm
```

Method 2: PyCharm installation on ubuntu using PPA

```python
$ sudo add-apt-repository ppa:mystic-mirage/pycharm
$ sudo apt-get update
$ sudo apt-get install pycharm-community
```

PyCharm also has a Professional (paid) version that can be installed
using the following command:

```python
$ sudo apt-get install pycharm
```

Once installed, go to your VM dashboard and search for PyCharm.
