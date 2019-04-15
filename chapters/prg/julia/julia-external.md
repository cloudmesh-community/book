
## 19.3.1 External programs

:o: most ref labels are ambiguous

Several implementations provide the ability to access Julia through external
programs such as Python, C, and Java, and vice versa.

### Resources

Pycall package by Steven G. Johnson <https://github.com/JuliaPy/PyCall.jl.>

Javacall package

### Python

Julia and Python express similar syntax, and both are dynamically-typed. The
Pycall package  enables interoperability between the two languages, extending
Julia functionality and reach while maintaining its desirable qualities. This
package creates the ability to call Python functions and import Python modules
from Julia, among other functions. [@www-pycall].

**Installation**

Start Julia, and run `Pkg.add("Pycall")`.

**Importing Python Modules**

To access Python with Julia, we use the Julia syntax `using Pycall`. Here is a
simple example [@www-pycall]:

       using PyCall
       math = pyimport("math")
       math.sin(math.pi / 4) # returns ≈ 1/√2 = 0.70710678...


This is in contrast to Julia's built in	`sin` function:

     sin(fill(1.0, (2,2)))
     2×2 Array{Float64,2}:
     0.454649  0.454649
     0.454649  0.454649

**Pycall in Virtualenvs**

This course recommends using virtualenvs in Python. It is therefore important to
note that Pycall "uses the virtualenv it was built with by default, even if you
switch virtualenvs." [@www-pycall]. This applies to virtual environments created
using [`venv`] and [`virtualenv`]. Python virtual environments created by conda
are not currently supported. 

To continue interoperability with Julia while using a different virtualenv,
Pycall recommends switching virualenvs and running `rm(Pkg.dir("PyCall","deps",
"PYTHON")); Pkg.build("PyCall")`

```
$ source PATH/TO/bin/activate  # activate virtual environment in system shell
$ # start Julia

    ENV["PYCALL_JL_RUNTIME_PYTHON"] = Sys.which("python")
    "PATH/TO/bin/python3"

    julia> using PyCall

    pyimport("sys").executable
    "PATH/TO/bin/python3"
```


### Java in Julia
Julia interacts with Java through the use of the JavaCall.jl package.
[@javacall] "Static and instance method with primitve or object arguments and 
return values are callable." [@www-javacall]. 

**Installation**
```
Pkg.add("JavaCall")
```

**Usage**
```
julia> using JavaCall

julia> JavaCall.init(["-Xmx128M"])

julia> jlm = @jimport java.lang.Math
JavaObject{:java.lang.Math} (constructor with 2 methods))

julia> jcall(jlm, "sin", jdouble, (jdouble,), pi/2) 1.0

julia> jnu = @jimport java.net.URL
JavaObject{:java.net.URL} (constructor with 2 methods)

julia> gurl = jnu((JString,), "http://www.google.com")
JavaObject{:java.net.URL}(Ptr{Void} @0x0000000108ae2aa8)

julia> jcall(gurl, "getHost", JString,())
"www.google.com"

julia> j_u_arrays = @jimport java.util.Arrays
JavaObject{:java.util.Arrays} (constructor with 2 methods)

julia> jcall(j_u_arrays, "binarySearch", jint, (Array{jint,1}, jint), [10,20,30,
40,50,60], 40)

## 19.3.2 Environment Variables