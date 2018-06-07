## Contributing

The document is written in markdown and managed with a Makefile
developed by Gregor von Laszewski. Contributing  content is easy as
everything is stored in github in the following directory:

* <https://github.com/cloudmesh-community/book/>

Content can be contributed via pull requests that are either created
while you directly edit the content via the github Web interface, or a
cloned version of the document.

For simplicity we focus on contribution via the Web interface.
Naturally you need to have a github.com account and login. After you
have found a text that you like to improve, please edit it via the
Web interface and than generate a pull request. We will than review the
request and approve or comment on it. To make it even easier the ebook
contains cloud symbols (:cloud:) that indicate the start of a document 
that you can modify. You can simply click on it and you will be automatically
redirected the the file for editing. As you can see it is rather
simple.

In case you clone and use command line or other GUI tools, please
create a pull request for each fix. Remember multiple students work in
parallel and fixes could conflict with each other. to minimize this
we recommend to to a pull request immediately after you corrected an
issue.

## Exercises

Contrib.1:

:   If you find an md file that has an error, fix is and create a pull request.

Contrib.2:

:   Identify a section that is not covered by this material, but could
    be useful. Add such a section and create a pull request so your
    contribution can be added. Work with others that review your section
    before submitting so we make sure no one else is working on this
    already. If they do we bring you in contact with them.

Contrib.3:

:   We use the creation of the class Web site on your computer to
    benchmark your machine. This benchmark will be used as part of some
    class assignments. To do so execute the following and write
    down/copy the times you get:

        echo "CLONE"
        time git clone https://github.com/cloudmesh-community/book.git

    Next change in to the directory that containes the make file for
    your volume you like to compile. Let us assume you like to compile
    the volume pi. Than do the following
    
        cd pi
        make clean
        echo MAKE
        time make

    You will see something like:

        CLONE
        real   2m36.662s
        user   2m34.473s
        sys    0m1.467s
        MAKE
        real   2m36.662s
        user   2m34.473s
        sys    0m1.467s

    We are only interested in the real time you measured. In addition provide also deatiled information
    about your computer, e.g.:

        volume: pi
        computer: MacBook Pro, 15-in, 2016, 2.9GHz, 16GB, 2133Mhz, LPDDR3
        clone: 0m36.662s
        make: 0m27.853s

    You will submit this information in a FORM and will be graded upon
    submission. 

