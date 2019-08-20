#REST in julia

:o: text is missing

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
