# Week 9: Containers - Docker :o2:


## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/e516/) [@las19e516]:
* [Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]:

Please read the section in [Cloud Computing](https://laszewski.github.io/book/cloud/)[@las19cloudcomputing]:
about **Containers**. We decided not to do a video as the material
in this section frequently changes and videos became too quickly
outdated. 


## Lab Activity Docker

Do the following assignments with all its questions:

* E.Docker.1
* E.Docker.2
* E.Docker.3

Place your solutions in your github hid directory 

## Lab Activity Container REST service

Develop a simple REST service using OpenAPI. Use the "Introspection"
principal with the conexion web service. Develop a container that runs
the REST service. Write a script or pytest that contacts the container
and returns the result from the REST service.

Write a Dockerfile that create the service

Write a cloudmesh command (remember we did this before) that manages and
interacts with the server, but it actually interacts with the container
and not just the native service.

Here is an example list sof commands (replace myservice with a comand
that is not used already in cloudmesh-cloud or cloudmesh-storage:

```
cms myservice start
   starts the service
   
cms myservice stop
   stops the service
   
cms myservice PATH
   Connects to the running service and returns the Object
   
curl ...
   Document how you interact with your service   
```
    
Obviously you can use services from your project. A more elaborate
version of tis will be in your final project. Develop commands that make
sense for you, This can include get, upload, delete, and update actions
for example.
   
   
