## REST in julia

The basic structure for creating a GET REST function in Julia is as follows. This can be typed directly in the REPL: 

```julia
using HTTP
function make_API_call(url)
    try
        response = HTTP.get(url)
        return String(response.body)
    catch e
        return "Error occurred : $e"
    end
end

response = make_API_call("http://jsonplaceholder.typicode.com/users")
println(response)
```

This example can be extended to include POST, PUT, and DELETE functions quickly. For more a robust web framework, we
turn to Genie.  <https://github.com/GenieFramework/Genie.jl>.  There are several other web frameworks for Julia,
including Mux.jl (<https://github.com/JuliaWeb/Mux.jl>), and HTTP.jl (<https://github.com/JuliaWeb/HTTP.jl>).

### Genie.jl

"Genie is a full-stack MVC web framework that provides a streamlined and efficient workflow for developing modern web
applications. It builds on Julia's strengths (high-level, high-performance, dynamic, JIT compiled), exposing a rich API
and a powerful toolset for productive web development." <https://github.com/GenieFramework/Genie.jl> Genie actively
supports Julia 1.0 and above.
 
#### Import Genie

To install Genie, in the Julia REPL in Atom IDE, issue the following command: 

```julia
julia> import Pkg; Pkg.add("Genie")
```

This step only needs to be completed once per environment. 

#### API Backend

Extending functionality for the app is similar to development in Django and Rails.  See
<https://genieframework.github.io/Genie.jl/guides/Simple_API_backend.html> for more detailed information.

In the example below, we create the API backend to retrieve data through REPL interaction with Genie.  In the REPL, we
create and edit a new file called for this example ```rest.jl```.  *Note*: The current working directory can be checked
with ```pwd()``` and changed with ```cd("path\\to\\files")```.  In the Atom editor, add the following to a new file
named ```rest.jl```:

```julia
#rest.jl
julia> using Genie
julia> import Genie.Router: route
julia> import Genie.Renderer: json

julia> Genie.config.run_as_server = true

julia> route("/") do
  (:message => "Hi there!") |> json
end

julia> Genie.startup()
```
Now the server can be started and accessed at <https://127.0.0.1:8000> via the REPL:

```julia
julia> include("rest.jl")
```


Now we have the template for a running server, which can be expanded.  The output of the code below will GET a JSON
object. In the ```rest.jl``` file, add the following code.

```julia
#rest.jl
route("/echo", method = POST) do
  message = jsonpayload()
  (:echo => (message["message"] * " ") ^ message["repeat"]) |> json
end

route("/send") do
  response = HTTP.request("POST", "http://localhost:8000/echo", [("Content-Type", "application/json")],
  """{"message":"hello", "repeat":3}""")


  response.body |> String |> json
end

Genie.AppServer.startup(async = false)
```

Save the above code above in the current project directory. Then from the REPL or IDE REPL, run the script again: 

```julia    
julia> include("rest.jl")
```

#### Adding Parameters to the URL
 
We can also pass in parameters via URL. For instance, a string to filter or pass into a function.  

```julia
#rest.jl
Base.convert(::Type{Float64}, s::SubString{String}) = parse(Float64, s)
route("/somefloats/:x::Float64/:y::Float64") do
    "x+y is $(Genie.Router.@params(:x) + Genie.Router.@params(:y))"
end
````

Then start the server by running the script, and request  <http://localhost:8000/somefloats?x=2.5&y=4.5> in a browser.

#### Create an app

Genie provides scalability and ease of management through a web framework similar to Rails and Django.  To create the
framework for a new app, issue the following commands in the REPL:

```julia
julia> mkdir("directory-name")
julia> cd("directory-name")
julia> using Genie
julia> Genie.newapp("TestGenieApp")
```

Verify the app was created by typing <https://127.0.0.1:8000> in a browser. The Genie welcome mat should appear. To shut
down the server, type ```ctrl + c```.  To restart the app via the IDE REPL, type:

```julia
julia> startup()
```

#### Train Test Split
Now we can extend functionality further by creating a Genie app. The app will be an API service including a GET
implementation, which will call a Julia library designed to split data into train and test datasets.

Adding routes and functionality can be done either via the REPL or by editing the ```routes.jl``` file directly.  For
instance, the ```somefloats()``` function above could be added directly into the ```routes.jl``` file as in the above
example.

Additionally, we can add a ```lib``` directory into the root directory and include pre-written code or modules in the
app.  In the following examples, Julia will be used to retrieve data from a website, then split that data into train and
test sets.

#### Getting, Shuffling, Splitting data: 

Syntax in Julia for gathering and manipulating data is similar to that in Python. For the purposes of this text, we will
download and process the well-known Iris dataset using the RDatasets package, then split the dataset into train and test
sets.  For a complete list of the data available in Rdatasets, visit the following website: 
<https://github.com/JuliaStats/RDatasets.jl>.  To begin, bring the RDatasets into scope by adding the following lines of
code to your ```routes.jl``` file.

```julia
#routes.jl
julia> using RDatasets
```

Next, define the frame of a simple function as follows: *Note* there is no colon after the parameter parenthesis as in
Python.

```julia
# routes.jl
route("/getdata") do
  data = data = dataset("datasets","iris")
  data = shuffleobs(data)
  train, test = splitobs(data, at = 0.7, obsdim=1)
  return train, test
end
```

After making this fundamental change to the ```routes.jl``` file in the project directory, the environment must be
re-activated. Ensure the project directory is the current working directory.  In Atom IDE, this can be set by selecting
in the menu: Julia -> Working Directory -> Select.  Then, access the ```Pkg``` mode by typing the right bracket ```]```.


```julia
# enter package mode by typing right bracket
julia>]
#activate the environment for the current working directory:
pkg> activate .

#backspace to get back to Julia REPL
julia> using Genie
julia> Genie.loadapp()
julia> startup()
```

As the app is further tested and modified, it can be stopped using ```Ctrl + c```, then started again using
```startup()```.  The response in the browser window should look like the entire unformatted Iris dataset.  Formatting,
and utilizing Genie's Model-View-Controller architecture is beynond the scope of this chapter.


#### Extending functionality

The application structure as is works with basic functionality, but could become unwieldy very quickly.  To scale the
app one step further, we can place custom modules and/or packages into the ```/lib``` directory.  Genie will then add
the custom content in the ```lib``` filepath into the ```LOAD_PATH``` environment variable recursively and automatically
load dependencies.  Add the filepath:

```julia
julia> mkdir("lib")
```

The directory should appear in the project environment. Add a file called ```myJuliaLib.jl```.  Add the functionality
previously developed, along with the ```module``` syntax to export the module to the rest of the environment.  This can
be extended and modified to include many functions and data structures.

```julia
#myJuliaLib.jl
module myJuliaLib

using RDatasets
using MLDataUtils

function getdata()
    data = dataset("datasets","iris")
    data = shuffleobs(data)
    train, test = splitobs(data, at=.7)
    return data
end
end
```

Finally, modify the ```routes.jl``` to call the custom content.  Remove the actual function from the ```/getdata```
route, and replace it with a call to the custom ```getdata()``` function in ```myJuliaLib```.

```julia
#routes.jl
route("/getdata") do
  myJuliaLib.getdata()
end
```

The entire routes.jl file should appear as follows: 

```julia
using Genie.Router
using RDatasets
using myJuliaLib
using MLDataUtils

route("/") do
  serve_static_file("welcome.html")
end

route("/error500") do
  error_500("Something went wrong")
end

route("/error404") do
  error_404("the page you want")
end

route("/getdata") do
  myJuliaLib.getdata()
end
```

Reload the environment, restart the app, and type <http://127.0.0.1:8000/getdata> into a browser window for the
response.  To continue development, utilize the Model-View-Controller approach to application development within Genie.