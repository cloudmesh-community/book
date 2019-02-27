# Twister2 Installation

## Prerequisites

Because Twister2 is still in the early stages of development a binary release is not available as of yet, therefore to
try out Twister2 users need to first build the binaries from the source code. 

-   Operating System : 
    * Twister2 is tested and known to work on,
    * Red Hat Enterprise Linux Server release 7
    * Ubuntu 14.05, Ubuntu 16.10 and Ubuntu 18.10

-   Java (Jdk 1.8) Covered in Section
    [\[s:hadoop-local-installation\]](#s:hadoop-local-installation){reference-type="ref"
    reference="s:hadoop-local-installation"}.

-   G++ Compiler `sudo apt-get install g++`

-   Maven Installation Explained in
    Section [Maven](#s:s:twister2-maven){reference-type="ref"
    reference="s:s:twister2-maven"}

-   OpenMPI Installation Explained in
    Section [OpenMPI](#s:s:twister2-openmpi){reference-type="ref"
    reference="s:s:twister2-openmpi"}

-   Bazel Build Installation Explained in
    Section [Bazel](#s:s:twister2-bazel){reference-type="ref"
    reference="s:s:twister2-bazel"}

-   Additional Libraries Explained in
    Section [Twister Extra](#s:s:twister2-extras){reference-type="ref"
    reference="s:s:twister2-extras"}

### Maven Installation

Execute the following commands to install Maven locally.

      mkdir -p ~/cloudmesh/bin/maven
      cd ~/cloudmesh/bin/maven
      wget http://mirrors.ibiblio.org/apache/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz
      tar xzf apache-maven-3.5.2-bin.tar.gz  

Adding environmental variables

      emacs ~/.bashrc  

Add the following line at the end of the file.

      MAVEN_HOME=~/cloudmesh/bin/maven/apache-maven-3.5.2
      PATH=$MAVEN_HOME/bin:$PATH
      export MAVEN_HOME PATH

      source ~/.bashrc

### OpenMPI Installation

When you compile Twister2 it will automatically download and compile OpenMPI 3.1.2 with it. If you don't like this 
version of OpenMPI and wants to use your own version, you can compile OpenMPI using following instructions.

* We recommend using OpenMPI 3.1.2
* Download OpenMPI 3.0.0 from https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.2.tar.gz
* Extract the archive to a folder named openmpi-3.1.2
* Also create a directory named build in some location. We will use this to install OpenMPI
* Set the following environment variables

```bash
BUILD=<path-to-build-directory>
OMPI_312=<path-to-openmpi-3.1.2-directory>
PATH=$BUILD/bin:$PATH
LD_LIBRARY_PATH=$BUILD/lib:$LD_LIBRARY_PATH
export BUILD OMPI_312 PATH LD_LIBRARY_PATH
```

* The instructions to build OpenMPI depend on the platform. Therefore, we highly recommend looking into 
the `$OMPI_1101/INSTALL` file. Platform specific build files are available in `$OMPI_1101/contrib/platform` directory.

* In general, please specify `--prefix=$BUILD` and `--enable-mpi-java` as arguments to configure script. 
If Infiniband is available (highly recommended) specify `--with-verbs=<path-to-verbs-installation>`. Usually, the path 
to verbs installation is `/usr`. In summary, the following commands will build OpenMPI for a Linux system.

```bash
cd $OMPI_312
./configure --prefix=$BUILD --enable-mpi-java
make -j 8;make install
```

* If everything goes well `mpirun --version` will show `mpirun (Open MPI) 3.1.2`. Execute the following command 
to instal `$OMPI_312/ompi/mpi/java/java/mpi.jar` as a Maven artifact.

```bash
mvn install:install-file -DcreateChecksum=true -Dpackaging=jar -Dfile=$OMPI_312/ompi/mpi/java/java/mpi.jar -DgroupId=ompi -DartifactId=ompijavabinding -Dversion=3.1.2
```

### Install Extras

Install the other requirements as follows,

   sudo apt-get install g++ git build-essential automake cmake libtool-bin zip libunwind-setjmp0-dev zlib1g-dev unzip pkg-config python-setuptools -y
   sudo apt-get install  python-dev python-pip

Now you have successfully installed the required packages. Let us
compile Twister2.

### Compiling Twister2

Now lets get a clone of the source code.

```bash
git clone https://github.com/DSC-SPIDAL/twister2.git
```

You can compile the Twister2 distribution by using the bazel target as follows.
```bash
cd twister2
bazel build --config=ubuntu scripts/package:tarpkgs
```

This will build twister2 distribution in the file
```bash
bazel-bin/scripts/package/twister2-client-0.1.0.tar.gz
```

If you would like to compile the twister2 without building the distribution packages use the command
```bash
bazel build --config=ubuntu twister2/...
```

For compiling a specific target such as communications
```bash
bazel build --config=ubuntu twister2/comms/src/java:comms-java
```

### Twister2 Distribution

After you've build the Twister2 distribution, you can extract it and use it to submit jobs.

```bash
cd bazel-bin/scripts/package/
tar -xvf twister2-0.1.0.tar.gz
```
