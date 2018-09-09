Contributing
------------

The document is managed in LaTeX and is stored on github. Thus creating
of the document is rather simple.

### Requirements

We assume you are using a an OS on which you have installed and can
execute pdflatex. Operating systems such as Linux, OSX, or Windows can
be set up for it. On Windows we recommend that you also install gitbash
and have make installed.

We assume that you are familiar with git and have git installed.

### Setting up Git

These instructions assume that you are using git from the commandline.
For Linux or OSX, please follow our instructions on how to install it
which is provided as part of the lessons.

If you use windows you can install git for windows
<https://git-for-windows.github.io/> and than you can open up Gitbash in
your classes directory.

It is important that you have set up git correctly, otherwise your pull
request may not show up properly. First you need to initialize your
directory for use with Git:

    git init

Next you need to set your user name and email to get credit for your
work:

    git config --global user.name "Firstname Lastname"
    git config --global user.email yourusername@iu.edu

Where you need to replace the firstname, lastname and the email with
your information. Next you need to pull the information down from your
forked repository. You will need to enter your Github username and
password when prompted:

### Adding Content

First, you have to **fork** the repository while going to the link:

-   <https://github.com/cloudmesh/book>

and press the fork icon. Now you can clone or directly manipulate your
fork from the web browser.

    git clone https://github.com/cloudmesh/book

Next we need to switch into the development branch called *dev*

Using the GITUSERNAME will guarantee that you first If you clone, you
need to make sure you clone from your fork.

Once you have cloned and forked, you will find in the directory `book`
the file:

    Makefile

This makefiles has som convenient targets include that allow you to
create the handbook. This is achieved most easily with

    make g

    git pull https://github.com/username/classes

With all the files downloaded to your local directory, you can begin
editing the rst files with a plain text editor.

When you have changes to commit to the repository, you will first have
to set the origin for the changes. You only need to do this the first
time you commit changes, so do not worry about this step every time you
push your changes:

    git remote add origin https://github.com/username/classes.git

Now you are ready to add the files you changed:

    git add -A

Then commit the changes with a meaningful comment explaining what you
did:

    git commit -m "A message indicating what you changed"

Finally you can push your changes up to Github:

    git push -u origin master

Once you have done that, open up a browser and go to your forked project
on Github. When you have verified that the changes are there, you can
issue a pull request for your work to be integrated into the original
repository by clicking the *Pull Request* field in the right hand corner
beneath the topics.

### Adding bibliographic references

We use a single reference file formatted in *bibtex*. The file is located
in docs/source/refs.bib. We use sphinx-bibtex to manage the references in
rst pages. However, it has the disadvantage that we can only have on
reference section per bib file. In order to simplify management as we may
cite the same references in different files it is not useful to develop a
bib file for each rst file. Instead we developed the following pragmatic
approach.

Here is the process that we automatically apply in the *Makefile*

-   We identify all rst files that have the cite command in it.
-   We copy the refs.bib file into the same directory as the originating
    rst file. Lets assume the file is called *filename.rst*
-   We than rename in the file for this directory to *filename-tmp.bib*
    indicating it is not checked into github
-   In gitignore we have a rule that excludes them

The only thing you have to do in order to use references is to make the
index unique and to add a section such as the following to your
document:

    References
    ----------

    .. bibliography:: filename-tmp.bib
       :style: unsrt
       :cited:
       :labelprefix: filename

Please note the unique filename. To properly generate the citations we
recommend you use:

    make clean; make

### Exercise

To do this assignment you need to learn about making small changes and
how to document them with 'gitchangelog':

-   if you fix a spelling error: your commit message must:

        chg:dev: corrected spelling error

-   if you try to add a larger text you added real content, you can use
    "chg:usr: added section about how to do this and that and the other"
    where you replace this and that and the other with what you actually
    contributed

do always create small pull request. They are easier to

:   accept. If you create many different changes in many different
    locations in files the likelihood is that we reject the pull request
    and you have to split it up and redo, costing time on your side.
    This is part of learning how we use git.

<!-- -->

EContrib.0:

:   If you find an md file and an rst file with the same prefix, which
    filed should you edit?

EContrib.1:

:   Identify a spelling error on the web page or another item to
    improve. Fork the Web page, fix the error and create a pull request.

EContrib.2:

:   Identify a section that is not covered by this material, but could
    be useful. Add such a section and create a pull request so your
    contribution can be added. Work with others that review your section
    before submitting so we make sure no one else is working on this
    already. If they do we bring you in contact with them.

EContrib.3:

:   How do you clone from your fork? What is the difference between your
    fork and the main repository? How do you identify it is your fork
    you clone from?

EContrib.4:

:   We use the creation of the class Web site on your computer to
    benchmark your machine. This benchmark will be used as part of some
    class assignments. To do so execute the following and write
    down/copy the times you get:

        make clean
        time make

    You will see something like:

        real   2m36.662s
        user   2m34.473s
        sys    0m1.467s

    Now we want you to run it again after you touched a file:

        touch docs/source/faq.rst

    Now rerun the timed make. You will see an output such as:

        real   0m27.853s
        user   0m27.394s
        sys    0m0.334s

    The only thing we are interested in is the time behind real, as well
    as some information about your computer, e.g.:

        computer: MacBook Pro, 15-in, 2016, 2.9GHz, 16GB, 2133Mhz, LPDDR3
        make clean: 2m36.662s
        make update: 0m27.853s
        python: 3.6.2

    We will post a form in which you can enter your information. We
    found that we can use this information to check if you may have an
    issue with your computer or your setup.

EContrib.5:

:   Why do we ask you to do multiple pull requests? What could be the
    consequence if you make hundreds of changes in one pull request?
