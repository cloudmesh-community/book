# Julia :o:

All official Julia documentation can be found at the Julia website:
<https://julialang.org/>

"Julia walks like Python and runs like C." [www-julialang]

Because Julia is a relatively new programming language and documentation is
sparse, much of this chapter has been adapted from <https://julialang.org>

## Description of the Language:

### The Basics: 

Julia is a high-performance computing language designed by Alan Edelman,
Jeff Bezanson, Stefan Karpinski, and Viral Shah. Released in 2012, Julia was
aimed at the frustration of having to use multiple languages for various
computing tasks; Matlab for linear algebra, R for statistics, Python for web
development, etc. Karpinski and Shah teamed up with Bezanson to develop a
high-level, human readable, all-purpose programming language that didn't
require translation into lower languages like C or Java."Using LLVM, a compiler
developed by University  of Illinois at Urbana-Champaign and enhanced by the 
likes of Apple and Google, Karpinski and company built the language so that it 
compiles straight to machine code on the fly, as it runs." [www-wired]

"Julia features optional typing, multiple dispatch, and good performance, 
achieved using type inference and just-in-time (JIT) compilation, implemented 
using LLVM." [www-julialang] 

Julia is a dynamically-typed language, much like Python or R, which tend to be
more human-readable than lower-level languages such as Java or C. Unfortunately,
due to the tasks of translating high-level into low-level, the performance cost
can be high  Depending on the task, dynamically-typed languages can be slow,
especially for memory-intensive operations.  Conversely, languages such as C are
compiled or statically-typed languages are fast, but much less human-readable.
Julia provides the best of both worlds. "Julia is fast because of careful 
language design and the right combination of carefully chosen technologies that 
work very well with each other." [www-epubs-siam].

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
editing your ```/etc/environment``` file. [www-julialang]

Alternatively, you can use Linux's Personal Package Archive:
<https://launchpad.net/~staticfloat/+archive/ubuntu/juliareleases> and issuing
the following commands: 
```
sudo add-apt-repository ppa:staticfloat/juliareleases
sudo add-apt-repository ppa:staticfloat/julia-deps
sudo apt-get update
sudo apt-get install julia
```

You should now be able to activate Julia in your Bash session by typing
```$ julia```

### Development Environments
In line with Julia's hybrid DNA of compiled and dynamic languages, a user can
either type commands into a shell, or create programs in a file with a .jl
extension, and call the files externally. Other editors and IDEs are also
available. 

### Optional Typing:
Optional typing characteristic means that the user can decide whether or not to
specify  the type of a variable. [@getting-started] For instance:

```
include for loop, equation, etc... here. 
```
In the absense of type specification, Julia will automatically infer the
variable type. 


## Module Management
## Multiple Dispatch: 
## Parallel Language Constructs

* Missing Values
* Network Streams
* Parallel Computing
Though not intended as a replacement for Hadoop, parallelism in Julia is fairly
straight-forward. [www-wired]

### Coroutines, or Tasks. 
### Multi-threading,
### Green-threading
### Hadoop and Julia:
Julia is also optimized for high performance computing in a distributed
environment. While development and interactivity between Spark, Hadoop, and
Julia is robust, the documentation is limited. The Elly.jl package [@elly-jl]
is a Hadoop and Yarn client for Julia. We focus here on the Hadoop
functionality. 


```

## Interfacing with the System
* Docopts: 
https://github.com/docopt/DocOpt.jl

* External programs
A user can interact with Julia in several ways; through an interactive or non-
interactive command-line sessions, by using a local notebook similar to iPython
/Jupyter, or through a browser by going to JuliaBox.org.
Julia has several APIs available, and can communicate with Python, C, and Java.

### Java:
Julia interacts with Java through the use of the JavaCall.jl package.
[@javacall] "Static and instance method with primitve or object arguments and 
return values are callable." [@javacall]. 

* Installation
```
Pkg.add("JavaCall")
```
*insert JavaCall examples here*

* Environment variables

### Spark:
Spark and Julia have constructed an interface through the Spark.jl package. The
package "supports running pure Julia scripts on Julia data structures while
utilizing the data and code distribution capabilities of Apache Spark."
[@spark-jl]

## REST in julia
```
using HTTP
function make_API_call(url)
    try
        response = HTTP.get(url)
        return String(response.body)
    catch e
        return "Error occurred : $e"
    end
end
```

response = make_API_call("http://jsonplaceholder.typicode.com/users")
println(response)

https://discourse.julialang.org/t/implement-a-rest-server-in-julia/9117
https://codehandbook.org/make-rest-api-calls-julia/
https://github.com/essenciary/Genie.jl

## OpenStack in Julia

TBD

## AWS in Julia

JuliaCloud
	AWS.jl
	

## Azure in Julia

TBD

## FaaS in Julia

