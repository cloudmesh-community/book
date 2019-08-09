# Weekly Activities

In case you like to take the class with weekly activities you can look
at the Syllabus table at the sections that are released for a
particular date. The date means the activity is released on that date
and you have time to conduct the activity.

## Week 1: Activities Aug 26 - 30

In the first week we focus on the following activities:

1. Get familiar with the class and identify if you prefer to take the
   class in free form or in a more guided fashion. Contact us if you
   like to take it in more guided fashion via a private post to
   instructors. you will be able to use these weekly activity
   announcements to proceed. This weekly progress will be updated
   every Friday.

2. Understand that we have only 3 assignments. One of which is a
   significant project.

3. Download the Lecture notes ePub and install an ePub reader to read
   the lecture notes. Although we have a PDF version, this version is
   pretty large and will only be updated once a week. See in piazza the
   resource section to locate them

4. Learn piazza and do your bio post. Start a README.yml file (look at
   the assignment in piazza). Create a notebook.md file and keep it up
   to date on weekly basis.

5. Make sure to configure a computer on which you can do python 3.7.3.
   If you have not yet installed python we recommend you use pyenv. See
   our notes in the handbook about that. Pyenv allows you to install
   multiple python versions. Answer the question why anaconda is not a
   good version for python in the cloud. Explain why so many other
   courses recommend you to install and use anaconda. Discuss this on
   piazza if you like. If you do not understand this or question this
   attend the online hour. If you have issues with this talk to the TA's.

5. Make sure you have a git client installed from which you can
   interact with git. Initially you can just youse a web browser
   Find a spelling or grammar error in the lecture notes and correct
   it via the github.com Web browser while conducting a pull request.

6. Make sure to fill out the survey so we can create a github.com
   repository for your project

7. Start reviewing python. Especially do some language features as
   discussed in the notes and write a python module using setup.py and
   requirements.txt. Do a simple print hello world stat you install with
   `pip install .` What is the difference to `pip install -e .` How can
   you leverage this.

Remark: In this class everyone is allowed to help everyone. Each student
will have if they do not participate in a group have a different
assignment so cheating can be avoided. However if we detect that a
student is not doing their work and it delegates all their work to other
students this is considered cheating and an `F` will be assigned.
Please use git commits. It is not sufficient if just one student of a
group commits the entire project in case of group work.

## Week 2: Aug 30 - Sep 6

### Development machine

If you have not yet set up a computer with python 3.7.3 on it please
do so. Remember you can use virtual machines and use virtualbox so you
do not interfere with your base system or use a USB stick to boot into
ubuntu. If you do not have a system work with the TAs to identify
a solution that works for you

### Data Center

Please look at the data center section (see @#sec:data-center) and
read it. There are plenty of opportunities to contribute. Announce in
piazza if you work on a section so we minimize duplication of effort.
Data Center

#### Datacenter Table

Find concrete evidence for data centers from industry and
  complete the table with the many question marks as much as possible.
  As the information may change over time, please include a year for
  which the data is valid, we may need to add a year column.

#### Data Center sections

As we got already some positive feedback about
this section, I added some additional opportunities for more sections
that can even evolve to a chapter if you like to focus on this.

#### Datacenter Exercises

Some of you asked what Exercises they can do for this week to do some
work bejond reading the section. Please do not plagiarize. or just
quote entire sections to avoid plagiarism. Work in a group to discuss
and come up with high quality content.

The assignments are listed in @sec:exercises-energy

* E.Datacenter.2, A form link will be posted.
* E.Datacenter.3, A Form link will be posted.
* E.Datacenter.4

Please also pick from either assignments one. As this is a group
assignment, please improve with the group.

* E.Datacenter.5 
* E.Datacenter.6

### Remarks: Sections

Although it is sufficient to just read the chapter we provide, its fun
to do some google searches including just to look at images ... If you
see something you think we should add, propose a new section if you
like. Please remember that you will need to do some sections that will
be graded. We recommend that you contribute at least 5 sections. This
is equivalent to one section every three weeks which is actually not
much. Typically you will spend the first week researching and writing
a draft. The second week experimentation or creating an example if
applicable and the third week you will engage with other students and
the TAs on reviews and improvements if needed.

### Python till rest of the semester

Python 3.7.3: Set up a computer on which you can execute python 3.7.3.
Some did not complete that taks yet (see @sec:python-install,
@sec:python-intro, @sec:python-language).

Review Python: start reviewing python. See our handbook. Some of the
chapters are not that important and can be skipped. Focus on classes,
modules, basic language things. learn about pip (possibly from google)
learn how to write requirements.txt and setup.py for your own programs
use pycharm for program development, configure it so it uses python
3.7.3 when executing the python programs do it in a terminal not from
within pycharm (see @sec:python-editors).

We recommend that you install pycharm and use it. We have simple
videos in the python section that showcases this.

You do not have to do some of the more advanced python concepts. Focus
initially on the language and learn how to do classes as this will be
extremely helpful.

## Week 3: Sep 6 - Sep 13

### Cloud Architectures

This week we will focus on architectural definitions of cloud
computing. We like that the class engages in a discussion about a very
short definition of *cloud computing* and *mainframes* in piazza.
We will jointly develop an answer and add it to the handbook at the
spots marked with a red circle.

Read the sections:

* Architectures (see @sec:cloud-architectures)
* NIST Big Data Reference Architecture (see @sec:nist-bdra)

Students and TA's please complete the red cicles, e.g. mostly bibtex
references.

### REST services

Read the REST Service section. This section includes some parts that
are not that relevant for this class and we llike you to focus on
in @sec:rest on the sections

* Overview
* OpenAPI REST Services with Swagger (see @sec:swagger)
* OpenAPI Specification (see @sec:openapi-spec)
* OpenAPI REST Service via Introspection (see @sec:openapi-introspection)

You do not in this class need to look at the other Sections about REST,
however, if you like to you can. For the project, all projects will be
using for REST services the framework used in
sec:openapi-introspection.

## Week 4: Sep 13 - Sep 20

### Github as REST service

Read:

* Github REST Services (@sec:Github-REST)

Recommended:

* Do E.github.issues.6 as this is directly relevant for your projects
  and can be generalized to other REST services.

Optional:

* Do exercise E.github.issues.5:

> ![Warning](images/warning.png) *The week 4 is under construction and additional items will
> be added.*

### Practical OpenAPI

Develop an OpenAPI service with not trivial functionality that uses
GET, PUT, PATCH and other functions. Make sure to properly secure it.
Explore the use of MongoDB as database (MongoDB will be used in your
REST services, so it may take some time to master this). We will
provide additional material throughout the semester on this. So this
task may take multiple weeks and may overlap with your project. Get
started early.

## Week 5: Sep 20 - Sep 27

In this week you will start exploring virtual machines. For this you
will read the section about virtualization (@sec:virtualization). You
will be asked to understand what virtualization is and how it differes
from typical workstations.
You will identify the different levels of virtualization.

You will need to do one of two assignments dependent on which class
you are in (naturally you can contribute to both):

All options must be covered by students of the class so please
coordinate via github where these tasks will be filed.

Due data is when al sections and chapters are due, but early
submissions will be awarded bonus points.

Assignment python virtualenv (Residential studnets of this class): In
addition, we have started the class asking you to use python
virtualization while using pyenv. This is not just a recommendation,
but also serves as a learning tool in this class. As such we like yo
to engage in a discussion on Piazza to explain to us what the
difference is between virtual machines and python virtual
environments. We also like you to explain the difference between pyenv
and venv from python version 3. Make sure you do not plagiarize.

Assignment Online Students (Option A): If you have not yet taken any
section, you will explore Libvirt on your computer and write a small
section on using it practically. Make sure you do not plagiarize.

Assignment Online Students (Option B): If you have not yet taken any
section, you will explore Hyper-V on your computer and write a small
section on using it practically. Make sure you do not plagiarize.

Assignment Online Students (Option C, for Windows 10 users): If you
have not yet taken any section, you will explore Linux Subsystem on
your computer and write a small section on using it practically. Make
sure you do not plagiarize.  Describe how to install python (hopefully
pyenv) if there are any differences and cloudmesh cm.

Assignment Online Students (Option D): If you have not yet taken any
section, you will explore Hyper-V on your computer and write a small
section on using it practically. Make sure you do not plagiarize.

## Week 5 and 6: Sep 27 - Oct 4 - Oct 11

### Sections and Chapters

Online students must select sections and chapters. This is optional
for residential students and can be substituted by contributing to the
manual page of cloudmesh v4. If a residential student like to do a
chapter or section please let us know. However we recently observed
that some assignments, (see the previous week) must be done by
everyone as we observed that this will increase understanding among
all class members.

### IaaS

Please read (@sec:iaas-intro). In these weeks you will be exploring
IaaS frameworks. As there are many and we like you to program them in
python, you will first apply for at least one cloud. One of these
clouds must be chameleon cloud as some of our initial implementations
can be tested on it easily.  In addition to chameleon, you will apply
for another cloud account. The free tier from the providers are
sufficient.

The clouds can be for example: AWS, Azure, Google, Watson, ...

In addition we recommend that you install and use virtualbox as this
simulates a local cloud on your computer.

Thus you have access to 3 infrastructure as a service frameworks

OpenStack, virtualbox, and one more public cloud

We will ask you to run a small program in each of the clouds so that
you can compare runtime benchmarks between them. We also ask you tu
run the same program on your local computer so you have a comparison.

We will announce the program soon but in the meanwhile get your
accounts and try out the IaaS services.



### Libcloud and MongoDB

You will be using libcloud which is introduced in
@sec:libcloud-python for much of your interaction with the IaaS
services. Although all of them provide their own python libraries, we
like to develop a service mesh and libcloud allows us to provide
mostly a uniform interface to virtual machine and other service
management.

As we want to store information about the clouds and virtual machines
locally, we also like you to study MongoDB which we will be using for
the duration of the class including your class projects (see
@sec:mongodb-python).

So the interaction we typically will have

```
IaaS <---> libcloud <---> MongoDB <---> client
```

At a later point in your project you will also do

```
MongoDB <---> REST <---> OpenAPI <---> client
```

For your convenience we have provided a simple mongodb management
command in cloudmesh. Please explore it and if you find issues with it
improve it. It requires that you fill out the
`~/.cloudmesh/cloudmesh4.yaml` file.

For more information, see also

* <https://cloudmesh-community.github.io/cm/>

All of you will contribute commands and services to cloudmesh to
enable a community driven service mesh as part of your project.

As we have provided as part of cloudmesh you already with the basic
management functions for MongoDB, as well as a decorator that allows
to store any dict into MongoDB very easily.

We would like you to explore this functionality

Your assignment is to first generate a `cmd5` command with your first
name. This assignment is mandatory for all students

Than grenrate some dict, that you will return as part of a function
that you decorate with the database decorator `@DatabaseUptate`

The data must have values for `cloud`, `kind` which are used to
identify the collection as well as ideally a `name` for each entry in
the collection.

For more information see @sec:mongodb-python and
@sec:mongodb-cloudmesh.

## Week 7: Oct 11 - Oct 18

### MapReduce

This week you will start learning the basics of MapReduce concept and
its use-cases to understand what MapReduce is. The MapReduce section
(see @sec:map-reduce) gives an introduction and describes the basics
of the MapReduce concept.

Watch the video lecture that describes the software echo system around
MapReduce which is listed in @sec:map-reduce.

Understand the Wordcount example discussed in the, word count example
can be thought of as a "Hello world" example into MapReduce.


## Fall Break: Oct 18 - Oct 20

We recommend that you spend your time wisely and if you are behind
evaluate if this break can be used to catch up.


## Week 8: Oct 20 - Oct 25

### Hadoop and Spark This week you will further look into MapReduce
through Apache Hadoop, Hadoop is one of the earliest open source
implementations of the MapReduce concept.  Even though Hadoop has now
been replaced by faster frameworks such as Spark, Flink and
Twister2. It is still important to understand the basic concepts
around Apache Hadoop.

Read and understand the Hadoop echo system as described in
@sec:hadoop-introduction.  Even though Hadoop is rarely used as a
MapReduce framework, other parts of the echo system such as
HDFS(HaDoop File System) and Yarn are still very popular.

Watch and understand the pagerank example which is a popular and
important algorithm which can be solved cleanly with MapReduce

Install Hadoop and try out some of the examples to get a better
understanding about how the framework operates.

Read the Spark section to understand how spark was developed to
improve upon Apache Hadoop and how it achieves better performance for
Iterative MapReduce applications

MANDATORY: Read the Scientific Writing with markdown ePub, this is
required before you make and contributions to the book to make sure
that you understand the format of the book and the correct
notations. The ePub is available in
[Scientific Writing](https://github.com/cloudmesh-community/book/blob/master/vonLaszewski-writing-markdown.epub?raw=true)

MANDATORY Project Milestone: Review of your cloudmesh commandline
commands specified in docopt. Please make sure you have your command
either specified in the cm directory or in your hid. make sure to add
it to your README, so i can find it. The command ust be available Next
week Friday Mar 8, 9am.



## Week 9: Oct 25 - Nov 1

### Containers

Container technology is an important topic in cloud computing and has
been gaining more and more traction and demand over the past few
years. This week you will learn container technology and the concepts
and tools that you would need to master. see @sec:container-intro to
get a introduction into container technology and its motivations

Docker is one of the most important tools in container technology,
@sec:docker-intro provides an introduction into docker technology and
internal details of docker.

Read the installation instructions that are provided to install docker
locally on your machines to test docker commands

@sec:docker-file describes how docker image files are
constructed. Create your own docker images and run it to grasp the
concepts

Read about docker hub and its capabilities, check how to push and pull
images as needed from docker hub

Docker swam allows user to manage large amounts of docker containers,
read about docker swarm in @sec:docker-swarm

Kubernetes is another widely used container management framework. See
@sec:kub-intro to read about Kubernetes in more detail

MANDATORY Project Milestone: OpenAPI specification, We like to review
your OpenAPI specification that is motivated by your cloud mesh
command. Have your openAPI specification ready Mar 15, 9am.

MANDATORY: comprehension assignment VM management, All students in
class must be showcasing for one cloud that they can start, stop, and
login into a VM in a cloud. This has to be demonstrated through a
scipt or python program. The program must read the credentials from a
configuration file.  The script must demonstrate that a command can be
run on your vm with ssh.Starting and stopping the VM via the GUI does
not count. This must be done by Mar 15

## Week 10: Docker Cluster Nov 1 - Nov 8 

See @sec:docker-cluster for an introduction to terminology and
mechanisms for managing multiple containers across multiple hosts. Get
hands on experience with with docker clusters by creating a Docker
container with Hadoop to explore the Map/Reduce framework. See
@sec:hadoop-docker for MapReduce examples.

## Week 11: Kubernetes Nov 8 = Nov 15

See @sec:kub-intro for an introduction to Kubernetes and install
`minikube` for development on a local machine.  This `minikube` allows
users to play with virtual machines managed by either virtual box
drivers and docker containers.  Learn those terminologies and
setup/shutdown virtual machines with Kubernetes.

## Week 12: Kubernetes Nov 15 - Nov 22

See @sec:kub-fs for using Kubernetes on futuresystems. It introduces
you on how to use the Kubernetes cluster on FutureSystems using
multiple nodes. Learn to build a service in a cluster environment.

## Thangsgiving break Nov 24 - Dec 1

We recommend that you spend your time wisely and if you are behind
evaluate if this break can be used to catch up. THis is also a good
time to continue to work on your project.


## Project Due Date Dec 1

YOur project will be reviewed and based on feedback you need to
improve it. Last day to submit improvements is Dec 13. 


## Week 13: Go or Julia Dec 1 - Dec 6 

This week allows you to experiment with either Go or Julia. Please,
select one and try to develop a RES service in either one of the languages.

Go:
See @sec:go-intro and @sec:go-language for the introduction to the Go
programming language.  Install Go development environment from the
section @sec:go-installation. Learn the concurrent programming and
message chain communication in Go. Learn to develop the rest service
with OpenAPI in Go from the sections: @sec:go-openapi and
@sec:go-links.

Julia: TBD

## Week 14: Dec 6 - Dec 13

Improve the project


## Week 15: Dec 13 - 20

Project improvements accepted but may not be reflected in the
project. We encourage you to finish the project Dec 1. Review of the
project is typically one week. Submission after Dec 13. may result in
an incomplete.

