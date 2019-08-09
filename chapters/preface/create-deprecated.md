In case you use containers in ubuntu we recommend that you use the
docker container to compile the book as discussed in
@sec:docker-create-book.

![No](images/no.png) The next is yet untested

In case you like to use the ubuntu system directly, you can download a
script that installs the needed software.

You will first have to download the script with

```bash
$ wget https://raw.githubusercontent.com/cloudmesh-community/book/master/install-ubuntu.sh
```

Than you can run this [script](https://raw.githubusercontent.com/cloudmesh-community/book/master/install-ubuntu.sh) with

```bash
$ sh install-ubuntu.sh
```

![Warning](images/warning.png) please note that we have not yet tested this and are looking
for feedback and improvements to the `install-ubuntu.sh` script.

Once the software is installed you can scip to @sec:create-book
