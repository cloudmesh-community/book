Project Ideas
-------------

A god way to start identifying a project is to look at previous
student projects. For this reason we provide here a list of class
proceedings that have been authored by previous students of cloud
classes.  Please remember that the proceedings could include papers
that do not fulfill the class requirements or are incomplete. It is up
to you to identify excellent project and use them as a yardstick.

Volumes include (with highlighted contributions, there are many more
so please look at the volumes):


2. [Use Cases in Big Data Software and Analytics Vol. 3, Gregor von Laszewski, Fall 2017](https://drive.google.com/file/d/1PyEzfyXz0tnudMQn-AhWbbbiwc3SUjHa/view) (426 pages)
   * Predicting Housing Prices, Murali Cheruvu, Anand Sriramulu
   * There a many other good examples in this volume. This volume focusses more on Analysing and identifying a big data proplem. Also it includes some nice Raspberry PI applications.
3. [Projects in Big Data Software and Applications, Gregor von Laszewski, Spring 2017](https://github.com/cloudmesh/sp17-i524/blob/master/project/projects.pdf) (196 pages)
   * *Automated Sharded MongoDB Deployment and Benchmarking for Big Data Analysis*, Mark McCombe, Gregor von Laszewski
4. [Cloud and Big Data Technologies Vol 9, Gregor von Laszewski, Spring 2018](http://cyberaide.org/papers/vonLaszewski-cloud-vol-9.pdf) (189 pages)
   * *Location based crime data search and analysis with Spark UDF*, 
     Kadupitiya Kadupitige, Gregor von Laszewski
   * *Big Data Reference Architecture using Python Celery*, 
     Sabra Ossen, Gregor von Laszewski
   * *Benchmarking a Sentiment Analysis Algorithm Using Hadoop
     on Multiple Platforms*, 
     Min Chen, Bertolt Sobolik, Gregor von Laszewski
   * *Leveraging REST for cloud portability*, 
     Michael Robinson, Sushant Athaley, Harshad Pitkar

One important policy we have in the class is that all projects must be
unique from each other. Thus you should identify different data sets,
algorithms or infrastructure from all current and previously produced
reports. That should not be an issue as there is a lot of different
opportunities for you. Finding a unique project is part of the class
goal.

There will be a number of project topics available that are of
interest to us. However, it is your responsibility to expand them to
make them project worthy.


The paper format is included in hid-sample project-report (e.g. same as
paper):

-   <https://github.com/cloudmesh-community/hid-sample/tree/master/project-paper>
    The code and the paper are to be added in your hid folder. YOu will
    be creating lower case directories called `project-paper` and
    `project-code`. You will not check in any data, but instead create
    scripts that fetch the data.

For an example directory structure, please see

-   <https://github.com/cloudmesh-community/hid-sample> Certainly, you
    can chose from many different topics and we hope you pick one that
    is suitable for you and you enjoy doing. You have the opportunity to
    definitely pick a project that you enjoy doing. However it must be
    related to the course. This course is not about finding the best
    algorithm or copying a project from your AI or other cloud classes
    you have taken at IU. It is about finding a novel project that is
    related to cloud computing, big data and the deployment of the
    system on cloud resources.

### Project Data Restrictions

We will not accept any project using the Titanic,
Wordcount. Furthermore we observed that many students that used Kaggle
datasets did not focus on deployment issues, but only on
data set analysis. Please remember you need to deploy your code on a
cloud and make that deployment reproducible. It is not sufficient to
show that you are the only one being able to run your programs.


### Register Your Idea

Please register your project idea you need to do two things. Fist you
file a github issue with the title

	Project: Coursenumber: Meaningful Project title
	
You assign it to all team members in your project. An abstract is
submitted in that issue that describes what you do in your
project. THe course number is the number of your course. We will be
commenting on your project idea. It is your responsibility to see if
this project has already been done. Please do not jut go ahead an copy
someone else's code, try to do something that you do. However you can
leverage toolkits such as scikit learn, tensorflow, and others.

### Example Ideas

Next we list some project ideas that are suitable for the classes. At
this time we are especially interested in creating a big data
reference architecture. Thus your project could be incredible valuable
to contribute to this. This is done in collaboration with NIST. Other
projects include the deployment of cloud clusters This might includes
the following technology tech

1. Slurm/mpi 
2. Docker 
3. Docker swarm 
4. Kubernetes 
5. Ssh worker 
6. OpenFaas 
7. OpenWhisk 
8. Hadoop 
9. Spark. 

Naturally they need to be *reproducible* deployments. To test out such
projects, you will also need to demonstrate a benchmark on an
application.

We provide some more details next.

#### Project Type A: NIST Rest Services Project

This project idea is the simplest one of the once listed in this section
as we have extensively discussed it and provided all important
information to succeed in this activity. However, this task must not be
underestimated as it requires some non trivial work as any of our other
tasks. We believe however that the efforts for it is smaller than with
other project ideas.

We have provides you with the NIST big data reference architecture. As
part of this we have identified how to create rest services. In this
project you will define a **SIGNIFICANT** set of resources and implement
the rest services for them. IN contrast to your previous assignment this
is a set of services and not just a single service. (for example just
implementing a key value store abstraction is not sufficient). A proper
project scope includes for example an abstraction of resources related
to VMs on AWS with libcloud, or VMs on Openstack with libcloud, or VMs
on Azure with libcloud, or An abstraction for data storage (not just
files, but also objects and key value pairs), the abstraction of an
accounting framework, and so forth.

In case you have not completed your swagger REST service a portion of
this project will be used to satisfy that requirement.

One nice project would for example be the automated creation of rest
services while using a function specification of python. THis way you
could for example look at scikit learn, write 10 use cases, use your
code generator and create for each of them the rest service. Important
would be a scalability test.

#### Project Type B: Reproducible Raspberry PI Projects

The raspberry PI projects are divided topically by class. 
In this project you will be developing or leveraging form an existing
tutorial developed as part of the class. You will be focusing on how to
create for each tem member on one of the following technologies

1. Slurm/mpi 
2. Docker 
3. Docker swarm 
4. Kubernetes 
5. Ssh worker 
6. OpenFaas 
7. OpenWhisk 
8. Hadoop 
9. Spark

You will create a reproducible deployment and work towards the
implementation of a deployment.  In previous tutorials for the class
students focused on setting this up for a small number of nodes. What
we need to do now is to expand this to a scalable solution with many
hundreds of Pi's in the cluster. Naturally login in by hand on these
machines is not suitable, but you need to automatize this process as
much as possible. Your ideas on how to do this are most welcome. There
are different strategies, such as burning all SD cards with a program
on your laptop and modifying the file system of the sd card after the
burning, setting up a simple minimal system with ssh enabled and DHCP
so you can log into a named host and use parallel commands to further
provision the system, or even PXE boot. Once you have figured out and
documented this you will be documented how to deploy a Hadoop and/or a
spark cluster on the Pis.

You will then pick a data set and do a application and measure
the performance.

In case you work in a team, each person in the team needs to add a new
deployment. Example, if you are in a 3 person team you need to do not
only do a single deployment but multiple. This could even mean that you
need to deploy it on echo which is a non Pi cluster, but you can get
great performance comparisons between your analysis on echo and the one
on the PI. Other examples could include the comparison of spark with
hadoop on PI and echo

As this project contains a significant of tutorial like activities (just
do not use the term tutorial, but in this section we describe) we
recommend that you develop the setup procedure in markdown. and not
directly in latex. However use *clean* markdown and follow the markdown
rules. We have seen in the tutorial to be delivered for this class many
wrong examples on how to not use markdown.

For this reason the length of the paper may be reduced by one page if
the set up procedure is excellent, and includes automated deployment
scripts with minimal input by hand (this requires programming).


#### Project Type C: Reproducible Data Analysis 

This project requires you to use one cloud IaaS resource such as
chameleon, Futuresystems Echo, AWS, or Azure. You will be deploying on
the IaaS and conducting based on a data set that you conduct an
analysis of the data. You will be benchmarking the time it takes to
set up this environment as well as benchmarking how fast the analysis
is.


#### Project Type D: Define Your Own

Define your own project and discuss with us in the Monday meeting with
Gregor. A good example is a student that has chosen graphQL as the major
infrastructure component. He is developing a contributed chapter for the
handbook, a tutorial, and a deployment and benchmark of data of his
choice.

### Special Projects

Some projects that you may be interested in and should be done
throughout the entire semester in order to be successfully. This
includes making sure that Assignment 0 - 3 all integrate with each
other.

#### Project Cloud Security

Please read up on security and attribute base security. Take a look at
the already developed Web services to showcase how we develop flask
and swagger servers with basic auth (needed to understand the
attribute based security).

-   <https://en.wikipedia.org/wiki/Attribute-based_access_control>

This project has three parts and could be used throughout the class for
all assignments.

Technologies

: Identify and summarize technologies related to cloud or big data and
  security. Do more than 10.

Paper

:   Survey of Attribute based security and other security for clouds
    pages = number of people * 2 maximal 3 people (no images as usual
    in page number. Integrate this in a general overview about cloud, big data and security<

Tutorial

:   find frameworks in Python that do this. If they exist to develop a
    tutorial

Swagger

:   develop a swagger rest service managing the attributes and entities
    in the framework

Alternative A: Project VM based.

:   showcase this in a project that does this in a cloud framework
    using distributed virtual machines and services. Develop a tool that
    autogenerates services based on a function definition while also
    adding attribute based security.

Alternative B. Container based

:   do the same project but instead of using VMs do it in containers.

This project has enormous potential as (a) NIST Is highly interested in
this. Publication potential of one or two papers. (b) security is hot,
and (c) cloud is hot.


#### Hadoop 3.0

Hadoop was recently updated to Hadoop 3.0. Develop reproducible
deployment scripts for a variety of infrastructures (container, PI,
OpenStack, AWS, Azure, google, ...)

Start with docker. 

-   <https://github.com/sequenceiq/hadoop-docker/blob/master/Dockerfile>

Max 3 people can work on this, while deploying it on 3 platforms and
showcasing it works with a benchmark.

Expand this project to do benchmarking on various
infrastructures. This project is bets done in a team of 2, do as many
infrastructures as you can achieve. Keep the benchmark simple. Develop
cloudmesh commands to interface with it. If time allows develop rest
services.
