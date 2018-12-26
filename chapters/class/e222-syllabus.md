---
title: "e516: Engineering Cloud Computing"
author: [Gregor von Laszewski]
date: "2018-05-10"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Indiana University"
titlepage: true
titlepage-color: "06386e"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
...

# e222: Intelligent Systems Engeneering II

In this undergraduate course students will be familiarized with different specific applications and
implementations of intelligent systems and their use in desktop and cloud solutions.

* Piazza: :o:
* Registrar: [Link](https://registrar.indiana.edu/browser/soc4182/ENGR/ENGR-E222.shtml)
* Lecture Notes: [ePub](https://github.com/cloudmesh-community/book/blob/master/vonLaszewski-e222.epub)
* Indiana University
* Faculty: Geoffrey C. Fox
* Credits: 3
* Hardware: You will need a computer to take this class, a phone,
  tablet, or chrome book is not sufficient.
* Prerequisite(s): Knowledge of a programming language, the ability to
  pick up other programming languages as needed, willingness to
  enhance your knowledge from online resources and additional
  literature. You will need access to a *modern* computer that allows
  using virtual machines and/or containers. If such a system is not
  available to you can also use IU computers or cloud virtual machines. 
  The later have to be requested.
* Course Description: [Link](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e222-syllabus.md)

This is an introductory class. In case you like to do research and
more advanced topics, consider taking an independent study with
Dr. Fox or Dr. von Laszewski.

## Teaching and learning methods

* Lectures
* Assignments including specific lab activities
* Final project

## Covered Topics

The topics covered in thie class include.

* Introduction to REST: Theory and Practice - develop a REST service
* Introduction to Clouds: Theory and Practice - create via a program virtual machines and start
on them the REST service
* Introduction to Kubernetes: Theory and Practice - create a container that runs a REST service
* Introduction to Advanced AI: Integrate your AI engine into a REST service and run on a
cloud and in Kubernetes

:o: If time allows we may in addition also cover:

* :o: Introduction to Hadoop: Theory and Practice - Run Hadoop in a container; run hadoop on a
futuresystems cluster
* :o: Cloud Edge Computing: Theory and Practice - Integrate Sensordata into Cloud Services via REST
and MQTT

## Grading

| Grade Item    | Percentage  |
| ------------- | ----------- |
| Assignments   | 30% |
| Final Project | 60% |
| Participation | 10% |


## Representative bibliography

:o: add and replace new lecture notes

OLD LECTURE NOTES: <http://cyberaide.org/papers/vonLaszewski-bigdata.pdf>

1. Cloud Computing for Science and Engineering By Ian Foster and Dennis B. Gannon
* <https://mitpress.mit.edu/books/cloud-computing-science-and-engineering>
2. (This document) Handbook of Clouds and Big Data, Gregor von Laszewski, Geoffrey C.
Fox, and Judy Qiu, Fall 2017, https://tinyurl.com/vonLaszewski-handbook
3. Use Cases in Big Data Software and Analytics Vol. 1, Gregor von Laszewski, Fall 2017,
https://tinyurl.com/cloudmesh/vonLaszewski-i523-v1.pdf
4. Use Cases in Big Data Software and Analytics Vol. 2, Gregor von Laszewski, Fall 2017,
https://tinyurl.com/cloudmesh/vonLaszewski-i523-v2.pdf
5. Use Cases in Big Data Software and Analytics Vol. 3, Gregor von Laszewski, Fall 2017,
https://tinyurl.com/vonLaszewski-projects-v3
6. Big Data Software Vol 1., Gregor von Laszewski, Spring 2017, https://github.
com/cloudmesh/sp17-i524/blob/master/paper1/proceedings.pdf
7. Big Data Software Vol 2., Gregor von Laszewski, Spring 2017,
* <https://github.com/cloudmesh/sp17-i524/blob/master/paper2/proceedings.pdf>
8. Big Data Projects, Gregor von Laszewski, Spring 2017,
* <https://github.com/cloudmesh/sp17-i524/blob/master/project/projects.pdf>

:o: add new epubs here from cloudmesh community

:o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o::o:

## EVERYTHING FROM HERE ON TO BE REPLACED.

## Weekly Schedule

## Week 1. Administration

We have explained how to use piazza which we will be using for class communication. Students
that missed that lecture are responible for working with TAs to catch up.


 
### Course Topics - Intelligent Systems Engineering II

#### Administratiion (Week 1)

* Accounts

  * Github
  * Chameleon Cloud (optional)
  * Piazza
  
* :o: Survey

#### Scientific Writing (Week 1)

* Bio (Due Week 1)
* Plagiarizm (Due Week 3)
* :o: Scientific Writing with Markdown
* :o: bibtex
* :o: jabref 
* Project Report (Due two weeks before semester ends)
  

#### Introduction to Cloud Computing

* Introduction - Part A 
* Introduction - Part B - Defining Clouds I 
* Introduction - Part C - Defining Clouds II 
* Introduction - Part D - Defining Clouds III 
* Introduction - Part E - Virtualization 
* Introduction - Part F - Technology Hypecycle I 
* Introduction - Part G - Technology Hypecycle II 
* Introduction - Part H - IaaS I 
* Introduction - Part I - IaaS II 
* Introduction - Part J - Cloud Software 
* Introduction - Part K - Applications I 
* Introduction - Part M - Applications III 
* Introduction - Part N - Parallelism 
* Introduction - Part O - Storage Released
* Introduction - Part P - HPC in the Cloud Released
* Introduction - Part Q - Analytics and Simulation Released
* Introduction - Part R - Jobs Released
* Introduction - Part S - The Future Released
* Introduction - Part T - Security Released
* Introduction - Part U - Fault Tolerance

#### Project  
  
* Assignment: AI REST Services
  
#### IaaS
 
* Virtual Machines
    
  * Cloudmesh CM4 - virtualbox
  * Assignment
       
* Containers
    
  * Docker
  * Assignment

#### Python Programming for Beginners

* Python 
  
  * Assignment
  * Why not anaconda?
  * Using python 3.7
  * pyenv
  * pip
  * Language
  * Numpy
  * Scipy
  * OpenCV
    
* Linux
   
   * Assignment
   * SSH 

* REST
    
  * Eve
  * OpenAPI
  * Assignment
 
#### Arificial Inteligence 

See #sec:ai

* :o: Theory 
* :o: Unsupervised Learning
* :o: Deep Learning
* :o: Forecasting 
  


### Week 3. REST for Cloud computing

We will be starting the class with introducing you to REST services that provide a foundation for
setting up services in the cloud and to intercat with these services. As part of this class we will be
revisiting the REST services and use them to deploy them on a cloud as well as develop our own
AI based rest services in the second half of the class.
To get you started you need to read the follwoing sections:
An introduction to rest is provided in Section 34. It also provides a video recording of the material
that was presented in class.

#### Overview of REST
 
Next, we present you with information on how to easily create a rest service with FlaskRESTFUL
a libraruy that makes the creation of web services in python useing an object oriented approach
easy. A Lab was held that introduced you to developing such a service

#### Flask RESTful Services

A number of contributions from students have since been made including the development effort
for this lab. Links to this work can be found at

* <https://github.com/cloudmesh-community/hid-sp18-505/tree/master/rest>
* <https://github.com/cloudmesh-community/hid-sp18-409/tree/master/rest>

Next, we introduced you to Python Eve which ia a framework that allows you to define rest services
with schemas. This is important as it first allows you to easily define them while having just to do a
very minimal set of programming. Second, it allows you via Eve to make sure you define a well
designed data model that you can communicate to the users of the REST service.

#### Rest Services with Eve 418

In the Lab that may spawn multiple weeks you will be developing a Flask or Eve rest service. The
REST service retrieves information form your computer and exposes it to the client. You can chose
what you like to present, but we want that all students in class do a different information. TAs are
working with you which information you expose. A detailed Assignment is posted and coordinated
in piazza about this. YOu will be writing two services. One that uses flask features, the other one
that uses a database schema using Eve. The entire class can openly collaborate with each other on
this task. The code is to be checcked in into your github repository. Information of interrest include
memory available of the computer, cpu type and so on. This is not read from a text file but life
queried.

TODO: Tyler:Describe how each student gets a unique assignment. Coordinate that assignment.
The link to the assignmnet in piazza is below, directions for each student will come out the week of
Febuary 4, 2018.


* https://piazza.com/class/jc9dcfnbi045kv?cid=27

#### Weeks 2-3. Setting up your development environment

It is important that you have a development environment to conduct the class assignments. We
recommend that you use virtual box and use ubuntu. We have provided an extensive set of material
for you to achieve this. Please consult additional resources form the Web
The material includes:

:o: Tyler: please include links to the sections

* Install virtual box
* Install ubuntu on the virtual box
* Virtual Box Week 2 243
* Install an editor to develop python programs. We recommend pyCharm or simply emacs.
* Basic Emacs Weeks 2-3 201
* Using pyenv for multi version python installs
* Managing Multiple Python Versions with Pyenv Weeks 2-3 301

Technologies covered: piazza, git, pycharm, virtualbox, pyenv, python

Exersise: Continue to work on REST service.

#### Week 5. Introduction to simple Containers
We will be providing an introduction to containers and container technologies. Excercises will
include to run the REST services that we developed earlier to start in containers and utilize them.

* Motivation - Microservices
* Motivation - Serverless Computing

#### Week 6. Introduction to Container Clusters

We will be providing you with an introduction on how to not use one server, but multiple servers
to run containers on. This includes docker swarm, kubernetes, (maybe mesos if time allows).
Exercises include the deployment of minikube that enables you to run kubernetes on your computers.
Alternatively access to a docker swarm cluster may be provided.

* Docker Released Feb 11, 2018 459
* Docker and Kubernetes Released Feb 11, 2018 460

(we will not do kubernetes, this time)

#### Week 7. Map Reduce

In this section we will introduce you to the concept of Map reduce. We will discuss systems such
as Hadoop and Spark and how they differ. You will be deploying via a container hadoop on your
machine and use it to gain hands on experience.
part/syllabus.tex


#### Week 8. Overview of Cloud Services

We will be introducing you how to use Cloud services offored via a number of Cloud providers.
Topics covered include: overview of AWS, overview of Openstack, libcloud, and boto

#### Week 9. Multi cloud environments

We will teach you how to create a multi cloud shell while leveraging an abstract programming
interface to easily switch betwen multiple clouds. You can practically participate in helping to
develop interfaces to AWS, Azure, and OpenStack. As you have also worked with containers, you
can develop such interfaces also for containers including frameworks such as kubernetes. We will
be using libcloud to simplify the abstraction.

#### Week 10. Cloud Data and Applications

We will cover a number of Application examples for Cloud computing. In the second part we will
focus on CLoud Data Services and how we access data on the cloud. Exercises will include moving
data between data services. THis includes your own computer, box and google which both are
offered at IU.

#### Other weeks

All excersises in these weeks will develop REST services that expose machine leraning algorithms
as service. Data will be either passed along directly through parameters to the call, or on case of
large data a URL to the data source. The lessons from the previous weeks will be helping you to
achive this. It is not sufficient to just run the algorithms, but you must be integrating them into a
REST service.
Other weeks are not yet included here but will cover Artificial Intelligence.

####\ Assignments

All assignments are summarized in the Section :o: but are posted earlier in piazza.com in the pinned
section.

#### Communication Track

* Documenting Scientific Research Week 1
* Plagiarism Week 1
* Other Results Week 1
* Markdown Week 1
* Basic Emacs Week 2
* Writing a Scientific Article or Conference Paper Week 3
* Introduction to LATEX Week 3
* Managing Bibliographies Week 4
* Set up the git repository 

If a paper is plagiarised you will receive an **F** and it is reported based on
University policies.

#### Theory Track

* IaaS - OpenStack
* PaaS - Hadoop
* SaaS - SaaS with REST

Evaluation Paper1: Create a paper about a cloud technology with our give class template in the
git repository. If a paper is plagiarized you will receive an ‘‘F’’ and it is reported based on
University policies. The paper is in a directory called paper1. All images are in the directory
paper1/images, the report is in report.tex, the content is in content.tex. It follows the template
we provided. Submission of report.pdf is not allowed. We will create the report and check
completness that way.

#### Programming Track

Development Environment

* Virtual Box Week 2
* Linux Week 2
* SSH Week 3
* Github Week 3

Python

* Introduction Week 3
* Install Week 2
* Language Week 2
* Libraries Week 3
* Cloudmesh Command Shell Week 4

Cloud

* Overview of REST Week 2
* Rest Services with Eve Week 2
* REST Service Generation with Swagger Week 3
* Build a Rest Service
* Build a program to create VMs on an OpenStack cloud.



----

## Course Description



## Course Objectives

The course has the following objectives:

* Provide a basic introduction to cloud computing
* Introduce the concept of cloud data centers 
* Get familiar with cloud infrastructure as a Service such as
  OpenStack, Azure, or AWS
* Get familiar with cloud infrastructure such as Docker and Kubernetes
* Program cloud services
* Understand the differences between virtual machines and containers
* Develop sophisticated programming language independent REST services
* Learn advanced programming models for clouds such as Map/Reduce,
  Messaging, and GraphQl
* Exploration of Go for cloud computing
* Demonstrate knowledge of clouds while developing a significant project
* Explore state-of-the-art cloud technologies and services while
  providing a section and summary and commenting on its use for the
  cloud
* Learn how edge computing is enhancing cloud services and
  infrastructure
* Learn how to set up a cloud based on using commodity hardware

## Learning Outcomes

* Be able to explain the concepts of the cloud computing paradigm
  including its paradigm shift, its characteristics, and the
  advantages. Contrast them with the challenges and disadvantages.
* Be able to identify infrastructure and programming models needed to
  support real world applications.
* Be able to implement a real world application or deploy a cloud and
  its services.
* Be able to conduct sophisticated performance analysis of cloud
  services.
* Be able to communicate the results through tutorials, manual, and
  reports.
* Be able to work in a team to develop collaboratively software or
  contribute collaboratively to develop sections explaining how to use clouds.

## Syllabus

The topics are subject to change.


|     | Dates  | Unit | Title  | Description |
| --- |------ | --- | ------- | --------------------- |
|   | Week 1    | 1   | Introduction       | [Gregor von Laszewski](#research-interests)[:cloud:][gregor.md] |
|   |           |     |                    | [Class summary](E516 Summary)[:cloud:][e516-summary.md] |
|   |           |     |                    | [Definition of Cloud Computing](#definition-of-cloud-computing)[:cloud:][e516-definition.md] |
|   | Week 2    | 2   | Tools              | **Tools and Services** |
|   |           |     |                    | - [Virtual Box](#virtual-box)[:cloud:][virtualbox.md] |
|   |           |     |                    | - [Vagrant](#vagrant)[:cloud:][vagrant.md] |
|   |           |     |                    | - [Github](#github)[:cloud:][github.md] |
|   |           |     |                    | - [Linux](#s-linux)[:cloud:][linux.md] |
|   | Week 3    | 3   | Python             | **Python** |
|   |           |     |                    | - [Introduction](#s-python-intro)[:cloud:][python-intro.md] |
|   |           |     |                    | - [Installation](#s-python-install)[:cloud:][python-install.md] |
|   |           |     |                    | - [Interactive Python](#interactve python)[:cloud:][python-interactive.md] |
|   |           |     |                    | - [Editors](#s-python-editor)[:cloud:][python-editor.md] |
|   |           |     |                    | - [Basic Language Features](#s-python-language)[:cloud:][python.md] |
|   |           |     |                    | - [Modules](#s-python-modules)[:cloud:][python-libraries.md] |
|   |           |     |                    | - [Data Management](s-python-data)[:cloud:][python-data.md] |
|   |           |     |                    | - [Matplotlib](#matplotlib)[:cloud:][python-matplotlib.md] |
|   |           |     |                    | - [Cloudmesh Commandshell CMD5](#cloudmesh-commandshell-cmd5)[:cloud:][python-cmd5.md] |
|   |           |     |                    | - [OpenCV](#s-opencv)[:cloud:][opencv.md] |
|   |           |     |                    | - [Secchi Disk](#s-secchi-disk)[:cloud:][secchi.md] |
|   | Week 4    | 4   |                    | [Data Center][datacenter.md] |
|   | Week 5    | 5   | Architectures      | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
|   |           |     |                    | - [Cloud Architectures](#s-cloud-architectures) [:cloud:][arch.md]
|   |           |     |                    | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
|   | Week 6    | 6   | Virtualization     | [Virtualization, Qemu, KVM, Virtual machines](#s-virtualization)[:cloud:][virtualization.md] |
|   |           |     | Virtualization I   | - [Qemu](#s-qemu)[:cloud:][qemu.md] |
|   | Week 7    | 7   | Infrastructure     | [Infrastructure as a Service](#infrastructure-as-a-service)[:cloud:][iaas.md] |
|   |           |     |                    | - [Azure](#microsoft-azure) [:cloud:][azure.md] |
|   |           |     |                    | - [AWS](#amazon-web-services) [:cloud:][aws.md] |
|   |           |     |                    | - [OpenStack](#s-openstack) [:cloud:][openstack.md] |
|   |           |     | Chameleon Cloud    | - Chameleon Cloud |
|   |           |     |                    | - [Resources](#chameleon-cloud-security-warning)[:cloud:][resources.md] |
|   |           |     |                    | - [Hardware](#chameleon-cloud-hardware)[:cloud:][hardware.md] |
|   |           |     |                    | - [Charge](#chameleon-cloud-charge-rates)[:cloud:][charge.md] |
|   |           |     |                    | - [Quick start](#getting-started-on-chameleon-cloud)[:cloud:][start.md] |
|   |           |     |                    | - [KVM user guide](#openstack-virtual-machines)[:cloud:][user-guide.md] |
|   |           |     |                    | - [CLI](#openstack-command-line-interface)[:cloud:][cli.md] |
|   |           |     |                    | - [Horizon](#openstack-horizon)[:cloud:][horizon.md] |
|   |           |     |                    | - [Heat](#openstack-heat)[:cloud:][heat.md] |
|   |           |     |                    | - [Baremetal](#openstack-baremetal)[:cloud:][baremetal.md] |
|   |           |     |                    | - [FAQ](#chameleon-cloud-frequently-asked-questions)[:cloud:][faq.md] |
|   | Week 8    |   8 | Virtualization  II | Containers, Docker, Kubernetes |
|   | Week 9    | 9   | Programming        | Python for Cloud Computing |
|   |           |     |                    | - [Libcloud](#python-libcloud)[:cloud:][libcloud.md] |
|   |           |     |                    | - [Github as a Cloud Service](#s-github-prg)[:cloud:][githubprg.md] |
|   |           |     |                    | - [REST Services](#rest)[:cloud:][rest.md] |
|   |           |     |                    | - [Rest Services with OpenAPI](#rest-services-with-openapi)[:cloud:][swagger.md] |
|   |           |     |                    | - [OpenAPI Spec](#openapi-spec)[:cloud:][swagger-spec.md] |
|   |           |     |                    | - [OpenAPI Codegen](#openapi-codegen)[:cloud:][swagger-codegen.md] |
|   |  Week 10  | 10  | Map/Reduce         | Map/Reduce, Hadoop, Spark, and others |
|   |  Week 11  | 11  | Messaging          | Messaging |
|   |  Week 12  | 12  | Messaging          | - [MQTT](#mqtt)[:cloud:][mqtt.md]  |
|   |           |     |                    | - [Graphql][graphql.md]  |
|   | Week 13   |  13 | Go                 | Go for the Cloud |
|   | Week 14,15   | 14  | Edge Computing  | Edge Computing and the Cloud |
|   | Week 16 | 15 | Project Selection | Project selection for inclusion in the Proceedings |


 

[arch.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/arch.md
[gregor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/gregor.md
[e516-summary.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-summary.md
[e516-definition.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-definition.md

[virtualbox.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/virtualbox.md
[vagrant.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/vagrant.md
[github.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/git/github.md
[linux.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md

[python-intro.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-intro.md
[python-install.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-install.md
[python-interactive.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-interactive.md
[python-editor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-editor.md
[python.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python.md
[python-libraries.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-libraries.md
[python-data.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-data.md
[python-matplotlib.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-matplotlib.md
[python-cmd5.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-cmd5.md
[datacenter.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/datacenter.md
[bdra.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/nist/bdra.md
[iaas.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/iaas.md
[openstack.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/openstack/opensatck.md
[azure.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/azure/azure.md
[aws.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md
[resources.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/resources.md
[hardware.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/hardware.md
[charge.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/charge.md
[start.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/start.md
[user-guide.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/user-guide.md
[cli.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/cli.md
[horizon.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/horizon.md
[heat.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/heat.md
[baremetal.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/baremetal.md
[faq.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/faq.md
[libcloud.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/libcloud.md
[rest.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/rest.md
[swagger.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger.md
[swagger-spec.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger-spec.md
[swagger-codegen.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger-codegen.md
[mqtt.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/msg/mqtt.md 
[graphql.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/msg/graphql.md
[go-cloud.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-cloud.md 
[go-rest.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-rest.md
[go-intro.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-intro.md
[go-cmd.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-cmd.md
[go-install.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-install.md
[go-libraries.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-libraries.md
[go-editor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-editor.md
[go-links.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-links.md
[go-language.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-language.md
[opencv.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/opencv/opencv.md
[secchi.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/opencv/secchi.md
[virtualization.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/virtualization.md
[qemu.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/qemu.md
[githubprg.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/github.md

Students need only to do one project. The project is conducted thought the entire semester.

* Example chapters are indicated with :cloud:

* Dates may change as the semester evolves

* The project is a long term assignment (and are ideally worked on
  weekly by residential students). It is the major part of the course
  grade.

* Sections and chapters prepare you for documenting a technical aspect
  related to cloud computing. It is a preparation for a document that
  explains how to execute your project in a reproducible manner to
  others.

* Additional lectures will be added that allow easy management of the
  project.  These lectures can be taken any time when needed.

## Assessment

This course is focusing on the principal "Learning by Doing" which is
assessed by simple graded and non-graded activities. The assessment
may include comprehension of the material taught, programming
assignments, participation in online discussion forums, or the
contribution of additional material to the class showcasing your
comprehension.

The comprehension is also measured by the development of a chapter and
sections in markdown that can be distributed and replicated to other
students. This is done in preparation for the project that must
include a simple deployment and runtime instruction set.

The main deliverable of the class is a project. The project is
assessed through the following artifacts:

1. Deployment and install instructions, 
2. Project report (typically 2-3 pages per month, tutorial and
   chapters can be reused if possible), 
3. Working project code that can be installed and executed in
   reproducible manner by a third party 
4. Code developed by the project team distributed in github.com
5. Project progress notes checked into github throughout the semester. Each 
   week the project progress is reported and will be integrated
   into the final grade.
6. Discussions or progress reports with the instructors can be conducted on 
   online and residential class hours.

The grade distribution is as follows 

* 10% Comprehension Activities
* 10% Sections
* 10% Chapter
* 70% Project

As the project is the main deliverable of the course it is obvious
that those starting a week before the deadline will not succeed in
this class. The project will take a significant amount of time and
fosters the principal of "Learning by Doing" at all stages throughout
the semester.

The class will not have a regular midterm, but it is expected that you
have worked on your project and can provide a snapshot of the progress
outlining the goals of the project and how you will achieve these
goals till the end of the semester.

The final Project is due 3 weeks before the semester ends. Issues with
your project ought to have been discussed before this deadline with
the TA's The TAs will in the next 3 weeks go over the projects and
evaluate mayor and minor issues that you may be able to fix without
penalty. Larger changes will receive a grade penalty. The last fix
(upon approval) possible will be 2 weeks before semester end without
penalty. It is recommended that you are available till the last day of
class. 


## Assignments

|     | Dates  | Unit | Title  | Description |
| --- |------ | --- | ------- | --------------------- |
|   | due Week 8                | A1      | Sections           | Contribute significant sections. Do not develop redundant or duplicated content. |
|   | due Week 8                | A2      | Chapter            | Contribute a significant chapter that may use your section to the class documentation. Do not develop redundant or duplicated content. |
|  | Due Week 13               | A3      | Project Type A     | Build a cloud out of Raspberry PIs |
|  |                 |         |                    | Kubernetes, Hadoop, SLURM + OpenAPI Service,  |
|  |                 |         | Project Type B     | Build a Significant OpenAPI REST Service |
|  |                 |         | Project Type C     | Build an Edge Service Interfacing with a Cloud |
|  |                 |         | Project Type D     | Contribute to the new Cloudmesh code |
|  |                 |         | Project Type E     | Your own Project Type A, B, C, D [upon approval) |



## Calendar 

  
|  Assignment #  | Event |     | Date 
| --- | ----- | --- | --- 
|    | Full Term           | | 16 Weeks |
|   | *Begins*            | | Week 1 |
| 1, 2 | **Bio, Notebook** | assigned | Week 1 |
| 1, 2 | **Bio, Notebook** |  due | Week 2 |
| 3 | **Sections**    | assigned | Week 3 |
| 4 | **Chapter**         | assigned | Week 3 |
| 5 | **Project**         | selection or proposal  | Week 4 |
| 5 | **Project** | Draft | Week 8 |
| 3 | **Section** | due | Week 10 |
| 4 | **Chapter** | due | Week 10 |
| 5 | **Project**         | due        | Week 12 |
| 5 | **Project** (no penalty) | improvements | Week 13 |
| 5 | **Project** (with penalty) | improvements | Week 14 |
|   | **Final Deliverables due**  |  | Week 14 |
|   | *Grading*           |  | Week 15, 16 |
|   | *Ends*              |  | Week 16 |


* TA's must be available till all grades have been submitted. 
* Bio: a formal 3 paragraph Bio
* Notebook: a markdown in which you record your progress of
  this class in bullet form
* All times are in EST
* Dependent on class progress Comprehension Assignments may be added

## Incomplete

Please see the university regulations for getting an incomplete.
However, as this class uses state-of-the-art technology that changes
frequently, you must expect that an incomplete may result in
significant additional work on your behalf as your project may need
significant updates on infrastructure, technology, or even programming
models used. It is best to complete the course within one semester.

## Other classes I423, I523, I524, B649, E516, E616 (ok)

IU offers other undergraduate classes in this topic area such as I423. If you are interested in taking it, 
please see when they are taught.  Additional graduate level classes related which can also be taken  
only by special permission including:

* CSCI B-649 Cloud Computing is the same as E516 but for computer science students.
* I524 is the same as E516 but for Data Engineering Students
* E516 Introdcustion to CLoud COmputing and CLoud Engeneering

All of these classes are project based and require a significant and consistent effort of time on your side.

## Resources

An incomplete list of videos is available at:

* <https://www.youtube.com/playlist?list=PLy0VLh_GFyz81ZFQ6Xrd1PHHI1EzjhhVb>

This document will be updated throughout the semester with up to date links.