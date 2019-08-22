# Parallel Computing

Though not intended as a replacement for Hadoop, parallelism in Julia is fairly
straight-forward. [www-wired]

## Coroutines or Tasks

Julia is optimized for high performance computing in a distributed environment.

One method of parallelism in Julia is constructed via Coroutines which use communication primitives  to communicate between processes. The Channel function in
Julia makes passing variables, results, and objects between tasks possible.
[@www-julialang]. To create a Channel of size(int) we pass in:

```julia
c1 = Channel(32)
```

We can also specify a Type{T} before the size, though if not specified, the
Channel can hold any type object. Type declaration in Julia is important. The Julia documentation [@www-julialang] provides a simple example of creating results in one Channel and taking them into a second Channel.

```julia

c1 = Channel{Int}(32)
c2 = Channel{Tuple}(32)

# and a function `foo` which reads items from c1, processes the item read
# and writes a result to c2,
function foo()
    while true
        data = take!(c1)    # process data
        put!(c2, result)    # write out result
    end
end

# we can schedule `n` instances of `foo` to be active concurrently.
for i in 1:3
    @async foo()
end
```

The ```put!``` method appends an item to a Channel, unless the Channel is full
in which case it blocks until a ```take!``` is issued against that Channel.

The documentation provides are more complex example which we develop here. This
application creates the asynchronous channels "jobs" and "results", creating a
job in one and storing the results in the second, along with a simulated amount
of time.

```julia
# first we create the channels of type {T} and size (int).
julia> const jobs = Channel{Int}(32);
julia> const results = Channel{Tuple}(32);

julia> function do_work()
          for job_id in jobs
	      exec_time = rand()
	      sleep(exec_time)
	      put!(results, (job_id, exec_time))
	  end
	end;

julia> function make_jobs(n)
          for i in 1:n
	      put!(jobs,i)
	  end
	end;

julia> n=12

julia> @async make_jobs(n)

julia> for i in 1:4
          @async do_work()
	end

julia> @elapsed while n > 0
          job_id, exec_time = take!(results)
	  println("$job_id finished in $(round(exec_time; digits=2)) seconds")
	  global n = n-1
	end
```

## Multi-threading

:o2:

## Green-threading

:o2:

## Hadoop and Julia

While development and interactivity between Spark, Hadoop, and Julia is also
optimized for high performance computing in a distributed environment. While
development and interactivity between Spark, Hadoop, and Julia is robust, the
documentation is limited. The Elly.jl package [@elly-jl] is a Hadoop and Yarn
client for Julia.
