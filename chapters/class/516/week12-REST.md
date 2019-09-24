# Week 12: REST

## Lecture Material 

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/e516/) [@las19e516]
* [Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
* [Chameleon Cloud](https://laszewski.github.io/book/chameleon/)
* [Introduction to Python for Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/python/) [@las19python]

Go through **Section 6 - REST** of the [Cloud Computing](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
book. This section includes, 

* 6 REST
    * 6.1 Introduction to REST 
    * 6.2 REST Frameworks 
        * 6.2.1 OPENAPI
        * 6.2.2 RAML
        * 6.2.3 API Blueprint
        * 6.2.4 JsonAPI
        * 6.2.5 Tinyspec
        * 6.2.6 Tools
            * 6.2.6.1 Connexion
    * 6.3 OPENAPI 3.0
        * 6.3.1 Open API 3.0 Specification 
        * 6.3.2 OpenAPI REST Service via Introspection 
        * 6.3.3 REST AI services Example 
    * 6.4 Flask RESTful Services 
    * 6.5 Django REST Framework 
    * 6.6 Github REST Services 
    * 6.7 OpenAPI REST Services with Swagger 
    * 6.8 REST WITH EVE
    * 6.9 OPENAPI 2.0
        * 6.9.1 OpenAPI 2.0 Specification 
        * 6.9.2 OpenAPI REST Service via Introspection 
        * 6.9.3 OpenAPI REST Service via Codegen 
    * 6.10 Excersises 

## Lab Activities 

* Implement the REST service explained in the Section *6.3.2 OpenAPI REST 
Service via Introspection* in your local machine 

* Complete the exercises in *Section 6.2.2.4* :
    * OpenAPI.Conexion.1
    * OpenAPI.Conexion.2
    * OpenAPI.Conexion.3
    * OpenAPI.Conexion.4
    * OpenAPI.Conexion.5 

* Complete the exercises in *Section 6.9* :
    * E.OpenAPI.1
    * E.OpenAPI.2
    * E.OpenAPI.3
    * E.OpenAPI.4
    * E.OpenAPI.5 

## Graded Lab Activity

In this lab activity you will be adding more functionality to the REST cpu 
example and deploying the service in the Chameleon Cloud.

You may need to install [py-cpuinfo](https://pypi.org/project/py-cpuinfo/0.2.3/) 
library to help you collect information for the service implementation. 

1. Change the *cpu* GET method, to work in a operating system invariant way
   (i.e. use python libraries to determine the CPU name, rather than system calls) 

1. Add a GET method to get cache size of the CPU. URL parameter *{level}* should 
  specify the cache level.        
  
    **GET http://localhost:8080/cloudmesh/cpu_cache/{level}**
  
    * level = 'l3' for l3 cache size
    * level = 'l2' for l2 cache size
   
   The return should be a dictionary as follows. 
   
   ```
   { 
       "l3" : "8448 KB"    
   } 
    ```
   
2. If cache level is not specified, the following dictionary should be returned. 
  
    ```
    { 
       "caches":{ 
          "l3":"8448 KB",
          "l2":"1024 KB"
       }
    } 
    ```
 
 3. Add these methods to the *cpu.yaml* definition. 
 
 4. Deploy the service locally and test the services using *swagger-UI* and curl. 
 
 5. Create a **m1.small** instance in Chameleon Cloud with **ubuntu 18.04** 
    image. Deploy your new web service in the cloud instance. 
    
 6. Use *[swagger editor](https://editor.swagger.io/)* or curl to call the 
    webservice in the cloud from your own laptop. 
    
 7. Capture the outputs for each service paths in a meaningful way (images, 
    screenshots, etc) and compile a Markdown file. The Markdown should include, 
    the new cpu.yaml file, server.py, and cpu.py files together with outputs. 
    Furthermore, you may include improvements to the service such as handling 
    malformed requests, etc. 
 
 8. In the Markdown file, discuss what are the ways you could add security for 
    these services (You do NOT need to implement this).    