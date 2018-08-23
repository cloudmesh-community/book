# E516 Summary

---

**:mortar_board: Learning Objectives**

* Obtain an overview of the topics we explore.
* Odentify topics that you are especially interested in.
* The main deliverable of this class is a project. 
* You **must** dedicate sufficent time on continious basis for this class.

---

Presentation about this Document

* [:clapper: Introduction](https://www.youtube.com/watch?v=w3o2EHaFx3o)


## Introduction

### Research participation

Research activities by Gregor von Laszewski are directly related to
this course allowing you to not only learn about cloudcomputing, but
practically participate in ongoing cloud research. Besides the
research topics provided, you can also suggest your own as part of a
project that you chose. PhD students could benefit from using cloud
computing as part of an activity they do plan to do within their
PhD. We would expect that you write a paper in collaboration with
Dr. von Laszewski and your advisor.

Some short overview about this is provided in
[Gregor von Laszewski](https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/gregor.md)

In general we are interested in any project that uses the cloud. This
can also include some topics that may not be related to Big Data but
to enabling services that are just hosted on the cloud or in some
cases could be hosted on a cloud but may actually use local clusters
or even your Laptop.

Topics of interrest include:

* Cloud Computing 
* Cloud Computing Architectures

  * NIST Big Data Architecture
  * Federated Cloud Computing
  * Mulit Cloud and Hybrid Cloud Architectures
  * HPC in the Cloud
  
* Cloud and Edge Computing

  * Example: Environmental Autonomous Robot Boat

* Big Data Applications

  * Example: Scientific Impact Analysis

* Monitoring and Visualizing Clouds
* Cloud Portals
* Other Topics

## Class communication

We are using for class communication piazza and github. As all
projects are supposed to be done as open source projects, we will use
github for managing them.

Please see 
[Class Communication](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-communicate.epub)
for more details.

### Tools and Services

* Piazza
* Github

### Definition of Cloud Computing

* NIST definition
* History of Clouds
* Technologies enabling Clouds
* Service Model

  * IaaS
  * PaaS
  * SaaS

### Data Centers 

* Evolution of the Data Center
* Today's Data Center
* Academic Data Centers

### NIST Big Data Reference Architecture

* Composable Services
* NIST Big Data Reference Architecture

  * You can contribute!
  * You can benefit!

## Infrastructure

### Infrastructure as a Service

* What is infrastructure
* How to manage infrastructure
* How to use infrastructure
  * GUI vs commandline vs programming
* Overview of commercial and educational IaaS 

#### OpenStack

* What is OpenStack?
* How can you use OpenStack?
* ChameleonCloud

#### Azure

* What is Azure?
* How can you use Azure?

#### AWS

* What is AWS?
* How can you use AWS?

#### Google

* What is Google?
* How can you use Google?

#### Watson

*We may not have time to cover this topic*

* What is AWS?
* How can you use AWS?


## Virtualization

* Introduction to virtualization

### Qemu

* Introduction to Qemu

### KVM

* Introduction to KVM

### Virtual machines

* Virtual Box
* Vagrant

### Containers

* Introduction to Containers

#### Docker


* Introduction to Docker
* Dokerfiles
* Dockerhub
* Create your own docker images

#### Kubernetes

* Managing containers in kubernetes

## Programming

### Python for Cloud Computing

* Python 2 and Pyton 3
* Introduction to Python
* Classes
* DocOpts
* CMD, CMD5
* YAML
* JSON
* Module Management
* setup.py
* Hosting code on github
* Installing code from github

#### LibCloud

* Introduction to lib clous
* Managing



### REST Services

#### Github as a Cloud Service

* Accessing Github REST services
* Mine Github

#### Eve

* Using Eve to develop REST serices
* Integrating swagger docs into Eve

#### OpenAPI

* Abstracting REST services
* OpenAPI Specification
* Generating code from OpenAPI

## Map/Reduce

* Map Reduce

### Hadoop

* Overview of Hadoop

### Spark

* Overview of Spark

## Messaging

### MQTT

* MQTT Services
* MQTT in the cloud
* Develop your own MQTT Service

## GraphQL

* Introduction to GraphQL
* Advantages and disadvantages of GraphQL

## Go for the Cloud Computing

* Introduction to Go
* Developing REST Services with Go
* Go and Kubernetes

## Julia for Cloud Computing

We may not have time to cover this topic. However this could be chosen
by a student as Chapter and tutorial contribution.

* Language motivation
* DocOpts with Julia
* Distributed computing with Julia
* Cloud Computing with Julia
* Reimplementing cloudmesh with Julia
* Accessing MongoDB
* REST services in Julia
* Containers and Julia

## Edge Computing and the Cloud

* Introduction to PI as Edge device
* Streaming data from a PI
* Sensors
* Autonomous Robot Boat (Can be chosen as Project)

## Other topics

Optional but very fun and useful:

* Maker Lab introduction for residential students.
* Maker Lab certification to operate the laser cutter
* Creating a case for the Raspberry Pi cluster
* Creating laser cut peaces for the Robot boat

We try to set up a 1-2 hour class with certification on Wednesday or
Thursday Aug. 22 or Aug. 23, 2018. Certification means you could go to
the maker lab by yourself outside of the class. 

## Assignments

Notebook

: You are expected to maintain a notebook in github, that outlines
  your progress in class. You can either use github, or provide a link
  to a shared google docs document that you link to the github
  `notebook.md` page

Bio

: You will develop a formal Bio and post it to Piazza. 

Chapters

: Contribute a significant chapter that may use your tutorial to the
  class documentation. Do not develop redundant or duplicated content.
  The chapter can developed as a team to also allow review by more
  than one person. However each team member has to develop their own
  chapter.  Plagiarism is not allowed.

  Examples:

  * Overview of AWS Cloud Services. This chapter provides an
    overview of AWS Web services.
  * Heroku. This chapter provides an overview of Heroku

  A chapter must be a reasonable contribution to the class and related
  to cloud or edge computing.

Tutorials

: Contribute a significant tutorial. Do not develop redundant or
  duplicated content. The tutorial can developed as a team to also
  allow review by more than one person. However each team member has
  to develop their own tutorial. Plagiarism is not allowed.

  Example:

  * Installation of kubernetes on a Raspberry Pi cluster. This
    tutorial shows practically how to do the installation
  * Heroku. This tutorial  provides guidance on how to use Heroku
  * Improvement of existing class tutorials are allowed
  
  A tutorial must be a reasonable contribution to the class and related
  to cloud or edge computing. Multiple small tutorials could
  be a reasonable contribution. Typically tutorials are correlated
  within a chapter, you could have however multiple smaller chapters
  and tutorials.

Projects

: Develop a project in the area of cloud computing. Make sure your
  project uses a REST services while using OpenAPI as introduced in
  class. A project report will showcase your comprehension and
  summarize your result to others. Alternatively you could use a
  Project Chapter format that is integrated into the class
  material. However in this case you need to distinguish your
  contribution from the regular tutorial and chapter assignment

  The project types include 

  * Project Type A: Build a cloud out of Raspberry PIs while
    enabling and showcasing an application in nKubernetes, Hadoop,
    SLURM + OpenAPI Service. It must contain an OpenAPI Rest service.
  * Project Type B: Build a Significant OpenAPI REST Service on an
    existing cloud. As the cloud may already be provisioned your
    application must be more involved.
  * Project Type C: Build an Edge Service Interfacing with a Cloud using
    OpenAPI Rest services.
  * Project Type D: Your own Project upon approval. It must use an
    OpenAPI REST service.


:warning: Tutorials, chapters, and especially Projects are multiweek
projects. Do not be tempted to think that other classes are more
important and start with your assignments the week before the
deadline. 


## Scientific Writing

We have made scientific writing extremely simple while using standard
tools used by millions of engineers to document their activities. If
you follow our templates they are just like forms and you can simply
clone the template and fill it out with content you develop. We focus
on content and not on the beauty of the text. However as we use
templates you will see that the result will be highly professional.

For more information please see our two publications:


* [Scientific Writing I](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-writing-1.epub),
  which will introduce you to how to avoid plagiarism and cheating,
  and use markdown.

* [Scientific Writing II](http://cyberaide.org/papers/vonLaszewski-latex.pdf),
  which will introduce you to how to write a high quality Project
  report following our template and how to easily manage
  bibliographies for your Project Report

These skills will be extremely useful for many other classes you may take.
