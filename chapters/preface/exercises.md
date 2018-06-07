## Exercises - Preface

Preface.1:

:   Create a Github account and fill out the survey to communicate the
    account name to us


Preface.2:

:   If you find an md file that has an error, fix is and create a pull request.

Preface.3:

:   Identify a section that is not covered by this material, but could
    be useful. Add such a section and create a pull request so your
    contribution can be added. Work with others that review your section
    before submitting so we make sure no one else is working on this
    already. If they do we bring you in contact with them.

Preface.4:

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

