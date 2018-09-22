# Travis

Travis CI is a continuous integration tool that is often used as part
of DevOps development. It is a hosted service that enables users to
test their projects on GitHub.

Once travis is activated in a GitHub project, the developers can place
a `.travis` file in the project root. Upon checkin the travis
configuration file will be interpreted and the commands indicated in
it will be executed.

In fact this book has also a travis file that is located at

* <https://github.com/cloudmesh-community/book/blob/master/.travis.yml>

Please inspect it as we will illustrate some concepts of
it. Unfortunately travis does not use an up to date operating system
such as ubuntu 18.04. Therefore it contains outdated
libraries. Although we would be able to use containers, we have
elected for us to chose mechanism to update the operating system as we
need.

This is done in the `install` phase that in our case installs a new
version of pandoc, as well as some additional libraries that we use.

in the `env` we specify where we can find our executables with the
`PATH` variable.

The last portion in our example file specifies the script that is
executed after the install phase has been completed. As our
installation contains convenient and sophisticated makefiles, the
script is very simple while executing the appropriate make command in
the corresponding directories.

## Exercises

E.travis.1:

> Develop an alternative travis file that in conjunction uses a
> preconfigured container for ubuntu 18.04

E.travis.2:

> Develop an travis file that checks our books on multiple operating
> systems such as macOS, and ubuntu 18.04.


## Resources

* <https://docs.travis-ci.com/>
