## Installing Julia

As an interactive, dynamically-typed language, there are many ways to run and
interact with Julia code, including directly in a browser using
<www.Juliabox.com>, which requires no installation. 

### Dependencies: 

First check to make sure that you have the required dependencies installed:
<https://github.com/JuliaLang/julia#required-build-tools-and-external-libraries>

On Ubuntu, you can easily install the required packages using the following
command [www-julialang]:

```
sudo apt-get install build-essential libatomic1 python gfortran perl wget m4
cmake pkg-config
```

To install Julia locally, first download and extract the appropriate 32 or 64-
bit binary installation package at <https://julialang.org/downloads/> into a
directory of your choice. You can then add Julia home to your PATH, or
include a soft reference by typing ```export PATH="$(pwd)/julia:$PATH"``` or by
editing your ```/etc/environment``` file. Finally, you can create a hard link
with:  ```sudo ln -s ~/JuliaPro-0.6.2.1/Julia/bin/julia /usr/local/bin/julia```
[www-julialang];  editing your ```/etc/environment``` file. [@www-julialang]


You should now be able to activate Julia in your Bash session by typing

```bash
$ julia
```
