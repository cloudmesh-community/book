## Installing Julia

To find the correct installation file for a given platform, visit <https://julialang.org/downloads/>.  There are several ways to run and interact with Julia: 
- In the terminal using the Julia REPL
- In a browser using JuliaBox with Jupyter Notebooks
- Using Docker images provided on DockerHub and provided by the Docker community
- By subscribing to JuliaPro by Julia Computing, which includes Juno IDE, discussed later in this chapter.  

### Julia REPL

#### Linux

First, check whether the required dependencies are installed:
<https://github.com/JuliaLang/julia#required-build-tools-and-external-libraries>

On Ubuntu, you can easily install the required packages using the following
command [@www-julialang]:

```bash
$ sudo apt-get install build-essential libatomic1 python gfortran perl wget m4
$ cmake pkg-config
```

To install Julia locally, first download and extract the appropriate 32 or 64-
bit binary installation package at <https://julialang.org/downloads/> into a
directory of your choice. Extract the tarball or gzip binary file.  

```bash
$ wget https://julialang-s3.julialang.org/bin/linux/x64/1.0/julia-1.0.1-linux-x86_64.tar.gz
$ tar xvfz julia-1.0.1-linux-x86_64.tar.gz
```

You can then add Julia home to your PATH, or include a soft reference as follows: 

```bash
$ export PATH="$(pwd)/julia:$PATH"
``` 

Alternatively, bring the REPL into scope by editing your ```/etc/environment``` file. Finally, you can create a "hard" link with the following command:  

```bash
$ sudo ln -s ~/JuliaPro-0.6.2.1/Julia/bin/julia /usr/local/bin/julia
```

Where the last ```julia``` is input into bash to start the REPL.  Creating a link will enable you to call different versions of Julia directly from the bash or shell.  For instance, if both Julia 0.6 and Julia 1.0 are required, it is possible to create separate links to both as follows:

```bash
$ sudo ln -s ~/JuliaPro-0.6.2.1/Julia/bin/julia /usr/local/bin/julia0.6
$ sudo ln -s ~/JuliaPro-1.1.3/Julia/bin/julia /usr/local/bin/julia1.0
```

[@www-julialang]

#### Windows

Download the appropriate installer file from <https://julialang.org/downloads/> and run the installer.  You should now be able to activate Julia in your Bash or Shell session by typing

```bash
$ julia
```

### JuliaBox

Additionally, a user can interact with Julia directly in a browser by using <https://www.Juliabox.com>.  This method requires no installation, and provides the familiar look and feel of Jupyter Notebooks without installing any additional software.  This method allows creation and local storage of Jupyter Notebooks for later use in JuliaBox.  Type the URL into a browser, log in or create an account, and select the tier or subscription level to begin. 