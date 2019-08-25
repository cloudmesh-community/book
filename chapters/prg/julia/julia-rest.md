##REST in julia

The basic structure for creating a GET REST function in Julia is as follows. This can be run directly in the REPL: 

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

This example can be extended to include POST, PUT, and DELETE functions quickly.  
For more a robust web framework, we turn to Genie.  <https://github.com/GenieFramework/Genie.jl>

### Genie

"Genie is a full-stack MVC web framework that provides a streamlined and efficient workflow for developing modern web applications. It builds on Julia's strengths (high-level, high-performance, dynamic, JIT compiled), exposing a rich API and a powerful toolset for productive web development." <https://github.com/GenieFramework/Genie.jl> Genie supports Julia 1.0 and above.
 
#### Installing Genie

To install Genie, in the Julia REPL or IDE REPL, issue the following command: 

```julia
julia> import Pkg; Pkg.add("Genie")
```

#### Simple API Backend
See <https://genieframework.github.io/Genie.jl/guides/Simple_API_backend.html> for detailed information.  

In the example below, we create the API Backend through REPL interaction with Genie.  In later examples, we modify the source route code for more complex functionality.  

In the REPL, bring the package dependencies into scope, and create the REST file in the current working directory.  Then we create the script to be run.  *Note: The current working directory can be checked with* ```pwd()``` and changed with ```cd("path\\to\\files")```.

```julia
julia> touch("geniews.jl")
julia> edit("geniews.jl")
```

In the editor, add the following to the file:

```julia
julia> Using Genie, Genie.Router, Genie.Renderer, Genie.Requests
julia> Using HTTP

Genie.config.run_as_server = true
Genie.config.session_auto_start = false

route("/") do
  Dict(:json => json(:message => "Hi there!")) |> respond
end
```

Now we have the template for a running server, which can be expanded with the following example code.  The output of the code below will GET a JSON object. 

```julia
route("/echo", method = POST) do
  message = jsonpayload()
  (:echo => (message["message"] * " ") ^ message["repeat"]) |> json
end

route("/send") do
  response = HTTP.request("POST", "http://localhost:8000/echo", [("Content-Type", "application/json")], """{"message":"hello", "repeat":3}""")

  response.body |> String |> json
end

Genie.AppServer.startup(async = false)
```

Save the above code above in the current project directory. Then from the REPL or IDE REPL, run the script (including quotes, where file-name.jl is the name of the file just created): 

```julia    
include("file-name.jl")
```
#### Adding Parameters to the URL
 
We can also pass in parameters via URL. For instance, a string to filter or pass into a function.  

```julia
route("/somefloats") do 
    "x+y is $(parse(Float64, @params(:x)) + parse(Float64, @params(:y)))"
end
````

Then start the server by running the script, and request  <http://localhost:8000/somefloats?x=2.5&y=4.5> in a browser.  

#### Train Test Split

Now we can extend functionality further by creating a Genie app. The app will be an API service including a GET implementation, which will call a Julia library designed to split data into train and test datasets. 
 
First, set up the project directory and load the Genie app file structure.  In the Julia REPL, create a new directory, change into the directory, and load a new app as follows: 

```julia
julia> mkdir("directory-name")
julia> cd("directory-name")
julia> using Genie
julia> Genie.newapp("testGenieapp")
```

