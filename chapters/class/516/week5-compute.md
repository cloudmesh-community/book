# Week 5: Cloud VM Compute Service :o2:

## Videos

Watch the videos from week 4 related to Cloudmesh

## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/e516/) [@las19e516]
* [Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]

Please read the chapter in the book [Cloud Computing](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
about 

* **Hypervisor**
* **IaaS**, pick one cloud you like to get familiare with and focus on that


1. Do not read the sections marked with 

![Construction](images/construction.png) 

2. Do not use **Python LibCloud** we want you to find the vendors python
libraries whcih are typically superior and have better access to the
information related to IaaS for the provider. This will make your
projects much easier in the long run.

## Lab: VM Compute Services

## Exercise 

1. Find a cloud you like and identify the native Python API (but not 
   libcloud, in case of openstack use the openstack sdk which is new
   and not nova and the other api's).
2. Demonstrate a Python program to list images, flavors and virtual 
   machines. You can create a vm via the GUI on your cloud, name it
   with your firstname.
3. When it comes to credential management, please use cloudmesh.yaml 
   and Config(). Learn how to do that. Under NO CIRCUMSTANCES post your 
   passwords or add files to GitHub that include your passwords or other credentials.
4. Develop a python program that adds keys and security groups (difficult).
5. Showcase that you can ssh into the vm (difficult)

This exercise can be done openly in class and everyone can share code
with everyone, as long as you acknowledge the student with name and hid.
