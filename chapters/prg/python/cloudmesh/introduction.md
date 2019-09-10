# Introduction

---

![](images/learning.png) **Learning Objectives**

* Introduction to the cloudmesh API
* Using cmd5 via cms
* Introduction to cloudmesh convenience API for output, dotdict, shell, stopwatch, 
  benchmark management
* Creating your own cms commands
* Cloudmesh configuration file
* Cloudmesh inventory

---

In this Chapter we like to introduce you to cloudmesh which provides you
with aa number of convenient methods to interface with the local system,
but also with cloud services. We will start while focussing on some
simple API's and than gradually introduce the cloudmesh shell which not
only provides a shell, but also a commandline interface so you can use
cloudmesh from a terminal. This dual ability is quite useful as we can
write cloudmesh scripts, but can also invoce the functionality from the
terminal. THis is quite an important distinction towards other tools
that only allow commandline interfaces.

Moreover we also sho you that it is easy to create new commands and add
them dynamically to the cloudmesh shell via simple pip installs. 

Cloudmesh is an evolving project and you have the opportunity to improve
it if you see some features missing.

The manual of cloudmesh can be found at 

* <https://cloudmesh.github.io/cloudmesh-manual>

The API documentation is located at

* <https://cloudmesh.github.io/cloudmesh-manual/api/index.html#cloudmesh-api>

We will initially focus on a subset of this functionality.
