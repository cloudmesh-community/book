 Anaconda
========

We do not recommend that you use anaconda as it may

interfere with your default python interpreters and setup.

This section about anaconda is experimental and has not

been tested.

You can add anaconda to your pyenv with the following commands:

    pyenv install anaconda2-4.3.1
    pyenv install anaconda3-4.3.1

Here we install both the version 2 and version 3 python environments
from anavconda. Please be aware that the install may tacke several
minutes. Make sure to install the latest release which you can find out
if you leave of the version after the 2 or 3.

When executing:

    pyenv versions

you will see after the install completed the anaconda versiosn
installed:

    pyenv versions
    system
    2.7.13
    2.7.13/envs/ENV2
    3.6.1
    3.6.1/envs/ENV3
    * ENV2 (set by PYENV_VERSION environment variable)
    ENV3
    anaconda2-4.3.1
    anaconda3-4.3.1

Let us now create virtualenv for anaconda:

    $ pyenv virtualenv anaconda2-4.3.1 ANA2
    $ pyenv virtualenv anaconda3-4.3.1 ANA3

Excersise
=========

Econda.1:

-   Write installation instructions for an operating system of your
    choice and add to this documentation.

Econda.2:

-   Replicate the steps above, so you can type in ENV2 and ENV3 in your
    terminals to switch between python 2 and 3.
