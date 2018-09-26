# Twister2 Installation :o:

Prerequisites
-------------

:o: TODO fix the section links

-   Operating Systems = \[Red Hat Enterprise Linux Server release 7,
    Ubuntu 14.04 , Ubuntu 16.04\] `We only use Ubuntu 16.04`

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

For Twister2, the recommended version is `Open MPI 3.0.0`. Execute the
following commands to install Open MPI locally.

      mkdir -p ~/cloudmesh/bin/openmpi
      cd ~/cloudmesh/bin/openmpi
      wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz  

Add environmental variables to bashrc file.

      emacs ~/.bashrc
      mkdir ~/cloudmesh/bin/openmpi/build
      BUILD=~/cloudmesh/bin/openmpi/build
      OMPI_300=~/cloudmesh/bin/openmpi
      PATH=$BUILD/bin:$PATH
      LD_LIBRARY_PATH=$BUILD/lib:$LD_LIBRARY_PATH
      export BUILD OMPI_300 PATH LD_LIBRARY_PATH

      source ~/.bashrc

Next build the OpenMPI 3.0.0,

      cd $OMPI_300
      ./configure --prefix=$BUILD --enable-mpi-java
      make;make install

Make sure the installation is successful by executing,

      mpirun --version

Then you will see an ouput,

      mpirun (Open MPI) 3.0.0

Install the following command to add this as an maven artifact,

      mvn install:install-file -DcreateChecksum=true -Dpackaging=jar -Dfile=$OMPI_300/ompi/mpi/java/java/mpi.jar -DgroupId=ompi -DartifactId=ompijavabinding -Dversion=3.0.0

### Bazel Installation

For this installation, `Bazel 0.8.1` is recommended. Execute the
following commands to install Bazel,

      mkdir -p ~/cloudmesh/bin/bazel
      cd ~/cloudmesh/bin/bazel
      wget https://github.com/bazelbuild/bazel/releases/download/0.8.1/bazel-0.8.1-installer-linux-x86_64.sh
      chmod +x bazel-0.8.1-installer-linux-x86_64.sh
      ./bazel-0.8.1-installer-linux-x86_64.sh --user
      export PATH=$HOME/bin:$PATH

### Install Extras

Install the other requirements as follows,

      sudo apt-get install git build-essential automake cmake libtool-bin zip libunwind-setjmp0-dev zlib1g-dev unzip pkg-config python-setuptools -y
      sudo apt-get install  python-dev python-pip

Now you have successfully installed the required packages. Let us
compile Twister2.

Compiling Twister2
------------------

First clone the repository from Github.

      mkdir ~/cloudmesh/twister2
      cd ~/cloudmesh/twister2
      git clone git@github.com:DSC-SPIDAL/twister2.git
      cd twister2

Now compile the code as follows,

      bazel build --config=ubuntu twister2/...

In order to build packages run the following commands,

      bazel build --config=ubuntu //scripts/package:tarpkgs

You can extract the bazel-bin/scripts/package/twister2-client.tar.gz to
run Twister2.
