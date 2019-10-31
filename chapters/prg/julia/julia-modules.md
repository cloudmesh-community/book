## Packages and Modules

Julia utilizes packages, modules, and functions.  Packages are comprised of Modules, Modules are comprised of functions,
and the concept of functions is similar to that in many other programming languages and will not be covered in depth in
this section.  See  <https://docs.julialang.org/en/v1/manual/modules/index.html> for more information. 

### Installing Registered Modules

To install modules via the REPL, it is easiest to enter the ```Pkg``` mode by typing the right bracket ```]```.  Then,
using the ```add``` command, bring packages and modules into scope. This avoids using dot notation and extra typing.

``` 
julia> ] 
pkg> add MLDataUtils 
# backspace to exit Pkg mode 
julia> using MLDataUtils 
```

Now the MLDataUtils module is available in the project environment. Check the status of all packages installed in the
current environment by entering ```Pkg``` mode, then typing ```status```.  This should list all available packages.

###Create Modules

Modules are typically comprised of functions and other data structures.  There are many packages and modules in active
development and well-maintained by the Julia community, many of which are registered, official modules that can be
accessed and used via the REPL.  A complete list of official packages is available at the Julia Registry
(<https://pkg.julialang.org/docs/>).

The syntax of a module is typically as follows: 

```julia
#dir/julia-lib.jl

module myJuliaLib
function some_func()
    do_something
    return x
end
end
```

### Custom Modules

Julia makes using not only official registered packages simple, but affords users the opportunity to create and utilize
their own packages and modules using both ```git``` and local file structures. To develop custom modules and bring them
into a project scope, create the module to be "exported" and modify the ```LOAD_PATH``` variable to include the filepath
(or URL if hosted on git) where the module file is.  In the example below, if the ```myJuliaLib``` module is in the
```\path\to\app``` directory, add the path into the environment variable as follows:

```julia
#first check the LOAD_PATH var: 
julia> LOAD_PATH
3-element Array{String,1}:
 "@"      
 "@v#.#"  
 "@stdlib"
 
julia> push!(LOAD_PATH, "/path/to/app")
4-element Array{String,1}:
 "@"      
 "@v#.#"  
 "@stdlib"                                                     
 "/path/to/app"  
 ``` 
 
 Alternatively: 
 
 ```julia
julia> push!(LOAD_PATH, https://github.com/mygitrepo.git)4-element Array{String,1}:
 "@"      
 "@v#.#"  
 "@stdlib"                                                     
 "mygitrepo.git"
```