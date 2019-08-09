# Introduction to Julia for High Performance Computing ![No](images/no.png)

---

![](images/learning.png) **Learning Objectives**

* Get up and running with Julia
* Understand parallelization in Julia
* Learn about REST services in Julia
* Interact with external programs in Julia

---

![Julia logo](images/julia.png)

"Julia walks like Python and runs like C." [@www-julialang]

Because Julia is a relatively new programming language and documentation is
sparse, much of this chapter has been adapted from <[https://julialang.org>[@www-julialang]

## Introduction:

Julia is a high-performance computing language designed by Alan Edelman,
Jeff Bezanson, Stefan Karpinski, and Viral Shah. Released in 2012, Julia was
aimed at the frustration of having to use multiple languages for various
computing tasks; Matlab for linear algebra, R for statistics, Python for web
development, etc. Karpinski and Shah teamed up with Bezanson to develop a
high-level, human readable, all-purpose programming language that didn't
require translation into lower languages like C or Java."Using LLVM, a compiler
developed by University  of Illinois at Urbana-Champaign and enhanced by the 
likes of Apple and Google, Karpinski and company built the language so that it 
compiles straight to machine code on the fly, as it runs" [@www-wired]. ![No](images/no.png) ambiguous ref label

"Julia features optional typing, multiple dispatch, and good performance, 
achieved using type inference and just-in-time (JIT) compilation, implemented 
using LLVM" [@www-julialang].

Julia is a dynamically-typed language, much like Python or R, which tend to be
more human-readable than lower-level languages such as Java or C. Unfortunately,
due to the tasks of translating high-level into low-level, the performance cost
can be high  Depending on the task, dynamically-typed languages can be slow,
especially for memory-intensive operations.  Conversely, languages such as C are
compiled or statically-typed languages are fast, but much less human-readable.
Julia provides the best of both worlds. "Julia is fast because of careful 
language design and the right combination of carefully chosen technologies that 
work very well with each other" [@www-epubs-siam].


### Development Environments
In line with Julia's hybrid DNA of compiled and dynamic languages, a user can
either type commands into a shell, or create programs in a file with a .jl
extension, and call the files externally. Other editors and IDEs are also
available. 



## Module Management

Julia provides module and package management similar to Python's ```pip``` with
the ```Pkg.add("")``` function. [@getting-started] ![No](images/no.png) ambiguous ref label

 
 To use a package
in a working environment, simply issue the command ```using <Package>```. For
instance, to add a graphics package called Winston and plot 100 random numbers,
execute the following commands:

```julia
	Pkg.add("Winston")
	using Winston
	plot(rand(100))
```
[@getting-started] ![No](images/no.png) ambiguous ref label


## Multiple Dispatch: 
## Parallel Language Constructs

* Missing Values

```

## Interfacing with the System


* Environment variables

### Spark:
Spark and Julia have constructed an interface through the Spark.jl package. The
package "supports running pure Julia scripts on Julia data structures while
utilizing the data and code distribution capabilities of Apache Spark."
[@spark-jl]

```

response = make_API_call("http://jsonplaceholder.typicode.com/users")
println(response)



## OpenStack in Julia

TBD


	

## Azure in Julia

TBD

## FaaS in Julia

## References:
* [https://julialang.org/](https://julialang.org)[@www-julialang]
* <https://discourse.julialang.org/t/implement-a-rest-server-in-julia/9117>
* <https://codehandbook.org/make-rest-api-calls-julia/>
* <https://github.com/essenciary/Genie.j}

![No](images/no.png) ref labels are missing 
