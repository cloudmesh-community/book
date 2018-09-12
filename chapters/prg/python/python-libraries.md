# Python Modules

Often you may need functionality that is not present in Python's
standard library. In this case you have two option:

-   implement the features yourself
-   use a third-party library that has the desired features.

Often you can find a previous implementation of what you need. Since
this is a common situation, there is a service supporting it: the
[Python Package Index](https://pypi.python.org/pypi) (or PyPi for
short).

Our task here is to install the [autopep8]() tool from PyPi. This will
allow us to illustrate the use if virtual environments using the pyenv
or virtualenv command, and installing and uninstalling PyPi packages
using pip.

Updating Pip
-------------

It is important that you have the newest version of pip installed for your 
version of python. Let us assume your python is registered with python and 
you use pyenv, than you can update 
pip with 

```bash
pip install -U pip
```

without interfering with a potential system wide installed version of p
ip that may be needed by the system default version of python. See the 
section about pyenv for more details

Using pip to Install Packages
-----------------------------

Let's now look at another important tool for Python development: the
Python Package Index, or PyPI for short. PyPI provides a large set of
third-party python packages. If you want to do something in python,
first check pypi, as odd are someone already ran into the problem and
created a package solving it.

In order to install package from PyPI, use the pip command. We can
search for PyPI for packages:

```bash
$ pip search --trusted-host pypi.python.org autopep8 pylint
```

It appears that the top two results are what we want so install them:

```bash
$ pip install --trusted-host pypi.python.org autopep8 pylint
```

This will cause pip to download the packages from PyPI, extract them,
check their dependencies and install those as needed, then install the
requested packages.

You can skip '--trusted-host pypi.python.org' option if you have

:   patched urllib3 on Python 2.7.9.

GUI
---

### GUIZero

Install guizero with the following command:

```bash
sudo pip install guizero
```

For a comprehensive tutorial on guizero, [click
here](https://lawsie.github.io/guizero/howto/).

### Kivy

You can install Kivy on OSX as follows:

```bash
brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
pip install -U Cython
pip install kivy
pip install pygame
```

A hello world program for kivy is included in the cloudmesh.robot
repository. Which you can fine here

-   <https://github.com/cloudmesh/cloudmesh.robot/tree/master/projects/kivy>

To run the program, please download it or execute it in cloudmesh.robot
as follows:

```bash
cd cloudmesh.robot/projects/kivy
python swim.py
```

To create stand alone packages with kivy, please see:

    -  https://kivy.org/docs/guide/packaging-osx.html

Formatting and Checking Python Code
-----------------------------------

First, get the bad code:

```bash
$ wget --no-check-certificate http://git.io/pXqb -O bad_code_example.py
```

Examine the code:

```bash
$ emacs bad_code_example.py
```

As you can see, this is very dense and hard to read. Cleaning it up by
hand would be a time-consuming and error-prone process. Luckily, this is
a common problem so there exist a couple packages to help in this
situation.

Using autopep8
--------------

We can now run the bad code through autopep8 to fix formatting problems:

```bash
$ autopep8 bad_code_example.py >code_example_autopep8.py
```

Let us look at the result. This is considerably better than before. It
is easy to tell what the example1 and example2 functions are doing.

It is a good idea to develop a habit of using autopep8 in your
python-development workflow. For instance: use autopep8 to check a file,
and if it passes, make any changes in place using the -i flag:

```bash
$ autopep8 file.py    # check output to see of passes
$ autopep8 -i file.py # update in place
```

If you use pyCharm you have the ability to use a similar function while
pressing on Inspect Code.

Writing Python 3 Compatible Code
--------------------------------

To write python 2 and 3 compatible code we recommend that you take a
look at: <http://python-future.org/compatible_idioms.html>

Using Python on FutureSystems
-----------------------------

This is only important if you use Futuresystems resources.

In order to use Python you must log into your FutureSystems account.
Then at the shell prompt execute the following command:

```bash
$ module load python
```

This will make the python and virtualenv commands available to you.

The details of what the module load command does are described in the
future lesson modules.

Ecosystem
---------

### pypi

The Python Package Index is a large repository of software for the
Python programming language containing a large number of packages,
many of which can be found on
[pypi](https://pypi.python.org/pypi). The nice thing about pypi is
that many packages can be installed with the program 'pip'.

To do so you have to locate the \<package_name\> for example with the
search function in pypi and say on the commandline:

```bash
$ pip install <package_name>
```

where `package_name` is the string name of the package. an example would
be the package called cloudmesh_client which you can install with:

```bash
$ pip install cloudmesh_client
```

If all goes well the package will be installed.

### Alternative Installations

The basic installation of python is provided by python.org. However
others claim to have alternative environments that allow you to install
python. This includes

-   [Canopy](https://store.enthought.com/downloads/#default)
-   [Anaconda](https://www.continuum.io/downloads)
-   [IronPython](http://ironpython.net/)

Typically they include not only the python compiler but also several
useful packages. It is fine to use such environments for the class, but
it should be noted that in both cases not every python library may be
available for install in the given environment. For example if you need
to use cloudmesh client, it may not be available as conda or Canopy
package. This is also the case for many other cloud related and useful
python libraries. Hence, we do recommend that if you are new to python
to use the distribution form python.org, and use pip and virtualenv.

Additionally some python version have platform specific libraries or
dependencies. For example coca libraries, `.NET` or other frameworks are
examples. For the assignments and the projects such platform dependent
libraries are not to be used.

If however you can write a platform independent code that works on
Linux, OSX and Windows while using the python.org version but develop it
with any of the other tools that is just fine. However it is up to you
to guarantee that this independence is maintained and implemented. You
do have to write requirements.txt files that will install the necessary
python libraries in a platform independent fashion. The homework
assignment PRG1 has even a requirement to do so.

In order to provide platform independence we have given in the class a
*minimal* python version that we have tested with hundreds of students:
python.org. If you use any other version, that is your decision.
Additionally some students not only use python.org but have used iPython
which is fine too. However this class is not only about python, but also
about how to have your code run on any platform. The homework is
designed so that you can identify a setup that works for you.

However we have concerns if you for example wanted to use chameleon
cloud which we require you to access with cloudmesh. cloudmesh is not
available as conda, canopy, or other framework package. Cloudmesh client
is available form pypi which is standard and should be supported by the
frameworks. We have not tested cloudmesh on any other python version
then python.org which is the open source community standard. None of the
other versions are standard.

In fact we had students over the summer using canopy on their machines
and they got confused as they now had multiple python versions and did
not know how to switch between them and activate the correct version.
Certainly if you know how to do that, than feel free to use canopy, and
if you want to use canopy all this is up to you. However the homework
and project requires you to make your program portable to python.org. If
you know how to do that even if you use canopy, anaconda, or any other
python version that is fine. Graders will test your programs on a
python.org installation and not canopy, anaconda, ironpython while using
virtualenv. It is obvious why. If you do not know that answer you may
want to think about that every time they test a program they need to do
a new virtualenv and run vanilla python in it. If we were to run two
installs in the same system, this will not work as we do not know if one
student will cause a side effect for another. Thus we as instructors do
not just have to look at your code but code of hundreds of students with
different setups. This is a non scalable solution as every time we test
out code from a student we would have to wipe out the OS, install it
new, install an new version of whatever python you have elected, become
familiar with that version and so on and on. This is the reason why the
open source community is using python.org. We follow best practices.
Using other versions is not a community best practice, but may work for
an individual.

We have however in regards to using other python version additional
bonus projects such as

-   deploy run and document cloudmesh on ironpython
-   deploy run and document cloudmesh on anaconda, develop script to
    generate a conda package form github
-   deploy run and document cloudmesh on canopy, develop script to
    generate a conda package form github
-   deploy run and document cloudmesh on ironpython
-   other documentation that would be useful

Resources
---------

If you are unfamiliar with programming in Python, we also refer you to
some of the numerous online resources. You may wish to start with [Learn
Python](https://www.learnpython.org) or the book [Learn Python the Hard
Way](http://learnpythonthehardway.org/book/). Other options include
[Tutorials Point](http://www.tutorialspoint.com/python/) or [Code
Academy](http://www.codecademy.com/en/tracks/python), and the Python
wiki page contains a long list of [references for
learning](https://wiki.python.org/moin/BeginnersGuide/Programmers) as
well. Additional resources include:

-   <https://virtualenvwrapper.readthedocs.io>
-   <https://github.com/yyuu/pyenv>
-   <https://amaral.northwestern.edu/resources/guides/pyenv-tutorial>
-   <https://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/>
-   <https://www.accelebrate.com/blog/the-many-faces-of-python-and-how-to-manage-them/>
-   <http://ivory.idyll.org/articles/advanced-swc/>
-   <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>
-   <http://www.youtube.com/watch?v=0vJJlVBVTFg>
-   <http://www.korokithakis.net/tutorials/python/>
-   <http://www.afterhoursprogramming.com/tutorial/Python/Introduction/>
-   <http://www.greenteapress.com/thinkpython/thinkCSpy.pdf>
-   <https://docs.python.org/3.3/tutorial/modules.html>
-   <https://www.learnpython.org/en/Modules/_and/_Packages>
-   <https://docs.python.org/2/library/datetime.html>
-   <https://chrisalbon.com/python/strings/_to/_datetime.html>

A very long list of useful information are also available from

-   <https://github.com/vinta/awesome-python>
-   <https://github.com/rasbt/python_reference>

This list may be useful as it also contains links to data visualization
and manipulation libraries, and AI tools and libraries. Please note that
for this class you can reuse such libraries if not otherwise stated.

### Jupyter Notebook Tutorials

A Short Introduction to Jupyter Notebooks and NumPy To view the
notebook, open this link in a background tab
<https://nbviewer.jupyter.org/> and copy and paste the following link in
the URL input area
<https://cloudmesh.github.io/classes/lesson/prg/Jupyter-NumPy-tutorial-I523-F2017.ipynb>
Then hit Go.

Exercises
---------

E.Python.Lib.1:

> Write a python program called iterate.py that accepts an integer n
> from the command line. Pass this integer to a function called iterate.

> The iterate function should then iterate from 1 to n. If the i-th number
> is a multiple of three, print *multiple of 3*, if a multiple of 5 print
> *multiple of 5*, if a multiple of both print *multiple of 3 and 5*, else
> print the value.

E:Python.Lib.2:

> 1.  Create a pyenv or virtualenv ~/ENV

> 2.  Modify your ~/.bashrc shell file to activate your environment upon
>     login.

> 3.  Install the docopt python package using pip

> 4.  Write a program that uses docopt to define a commandline program.
>    Hint: modify the iterate program.

> 5.  Demonstrate the program works and submit the code and output.
