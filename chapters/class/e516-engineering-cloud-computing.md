# e516: Engineering Cloud Computing

* Indiana University
* Fall 2018
* Faculty: Dr. Gregor von Laszewski (laszewski@gmail.com)
* Credits: 3
* Prerequisite(s): Knowledge of a programming language, the ability to
  pick up other programming languages as needed, willingness to
  enhance your knowledge from online resources and additional
  literature. You will need access to a "modern" computer that allows
  using virtual machines and/or containers. If such a system is not
  available to you can also use cloud vms we provide and if you opt 
  to do so one or more Raspberry's PI. All residential students will 
  have access to a total
  of 200 Raspberry PIs. Online students can opt to purchase one or
  more based on our materials list that we will release throughout the
  semester. All students will have access to a cloud.
* This page is maintained and updated at 
  [e516: Engineering Cloud Computing](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-engineering-cloud-computing.md)
* Course Description URL: 
  <https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-engineering-cloud-computing.md>
* [Registrar information and Other related classes](https://github.com/cloudmesh-community/book/blob/master/chapters/class/fall2018.md)

## Course Description

This course covers basic concepts on programming models and tools of
cloud computing to support data intensive science
applications. Students will get to know the latest research topics of
cloud platforms, parallel algorithms, storage and high level language
for proficiency with a complex ecosystem of tools that span many
disciplines.

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
  providing a tutorial and summary and commenting on its use for the
  cloud
* Learn how edge computing is enhancing cloud services and
  infrastructure
* Lern how to set up a cloud based on using commodity hardware

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
  contribute collaboratively to develop tutorials for clouds.


## Course Sylabus


E516 Summary

<div class="smalltable">

| Dates          | Unit    | Title             | Description
| -------------- | ------- | ----------------- | --------------
| 08/24     | 1       | Introduction      | [Gregor von Laszewski](https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/gregor.md)
| 08/24     | 1       | Introduction      | [Class summary](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-summary.md)
| 08/24     |         |                   | [Definition of Cloud Computing](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-definition.md)
| 08/31     |         |                   | Tools and Services
| 09/03     |         |                   | Data Center, NIST Big Data Reference Architecture
| 09/10     | 2       | Infrastructure    | Infrastructure as a Service
| 09/17     |         |                   | OpenStack, Azure, AWS
| 09/24     | 3       | Virtualization    | Qemu, KVM, Virtual machines
| 10/01     |         |                   | Containers, Docker, Kubernetes
| 10/08     | 3       | Programming       | Python for Cloud Computing, LibCloud
| 10/08     |         |                   | Github as a Cloud Service
| 10/15     |         |                   | REST Services, Eve, OpenAPI
| 10/22     |         |                   | Map/Reduce, Hadoop, Spark
| 10/29     |         |                   | Messaging with MQTT
| 11/05     |         |                   | GraphQL
| 11/19|         |                   | Go for the Cloud I
| 11/19|         |                   | Go for the Cloud II
| 12/03| 4       | Edge Computing    | Edge Computing and the Cloud
| 09/03-11/02* | 5       | Tutorial          | Contribute a significant tutorial. Do not develop redundant or duplicated content.
| 09/03-11/02* | 5       | Chapter          | Contribute a significant chapter that may use your tutorial to the class documentation. Do not develop redundant or duplicated content.
| 09/03-11/26* | 6       | Project Type A    | Build a cloud out of Raspberry PIs
| 09/03-11/26* |         |                   | Kubernetes, Hadoop, SLURM + OpenAPI Service, 
| 09/03-11/26* |         | Project Type B    | Build a Significant OpenAPI REST Service
| 09/03-11/26* |         | Project Type C    | Build an Edge Service Interfacing with a Cloud
| 09/03-11/26* |         | Project Type D    | Your own Project Type A, B, or C (upon approval)

</div>

Students need only to do one project. The project is conducted thought
the entire semester.

* Dates may change as the semester evolves

* The project is a long term assignment (and are ideally worked on
weekly by residential students). It is the major part of the course
grade.

(*) Tutorials prepare you for documenting a technical aspect related
to cloud computing. It is a preparation for a document that explains
how to execute your project in a reproducable manner to others.

- all times are in EST

Additional Lectures will be added that allow easy management of the project. These lectures can be taken any time when needed

<div class="smalltable">

| Date     | Unit    | Title             | Description
| -------- | ------- | ----------------- | --------------
| anytime  | 1       | [Scientific Writing I](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-writing-1.epub) |
| anytime  |         | Plagiarizm      | How to avoid plagiarizm and cheating
| anytime  |         | Markdown        | How to use markdown
| anytime  | 1       | [Scientific Writing II](http://cyberaide.org/papers/vonLaszewski-latex.pdf) |
| anytime  |         | Writing a Project Report      | How to write a high quality Project report following our template
| anytime  |         | Bibliography Management      | How to easily manage bibliographies for your Project Report
| anytime  | 1       | [Class Communication](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-communicate.epub) |
| anytime  |         | Class Github      | How to use the class Github
| anytime  |         | Class Piazza      | How to use the class Piazza

</div>

If you follow our template writing the report is like filling out a
simple form. 


## Assessment

This course is focussing on the principal "Learning by Doing" which is
assessed by simple graded and non-graded act-ivies. The assessment may
include comprehension of the material taught, programming assignments,
participation in online discussion forums, or the contribution of
additional material to the class showcasing your comprehension.

The comprehension is also measured by the development of a tutorial in
markdown that can be distributed and replicated to other
students. This is done in preparation for the project that must
include a simple deployment and runtime instruction set.

The main deliverable of the class is a project. The project is
assessed through the following artifacts:

1. Deployment and install instructions, 
2. Project report (typically 2-3 pages per month, tutorial and
   chapters can be reused if possible), 
3. Working project code that can be installed and executed in reproducable manner by a third party 
4. Code developed by the project team distributed in github.com
5. Project progress notes checked into github throughout the semester. Each 
   week the project progress is reported and will be integrated
   sinto the final grade.
6. three discusssions or progress reports with the instructors about your project

The grade distribution is as follows 

* 10% Comprehension Activities
* 10% Tutorial
* 10% Chapter
* 70% Project

As the project is the main deliverable of the course it is obvious
that those starting a week before the deadline will not succeed in this
class. The project will take a significant amount of time and fosters
the principal of "Learning by Doing" at all stages throughout the
semester.

The class will not have a regular midterm, but it is expected that you
have worked on your project and can provide a snapshot of the progress
outlining the goals of the project and how you will achieve these
goals till the end of the semester.

The final Project is due Dec. 1st. Issues with your project ought to
have been discussed before this deadline with the TA's The TAs will in
the next 14 days go over the projects and evaluate mayor and minor
issues that you may be able to fix without penalty. Larger changes
will receive a grade penalty. The last fix (upon approval) possible
will be Dec 7th.

### Incomplete

Please see the university regulations for getting an
incomplete. However, as this class uses state-of-the-art technology
that changes frequently, you must expect that an incomplete may result
in significant additional work on your behalf as your project may need
significant updates on infrastructure, technology, or even programming
models used. It is best to complete the course within one semester.


### Calendar 

<div class="smalltable">
  
|  Assignment #  | Event |     | Date 
| --- | ----- | --- | --- 
|    | Full Term           | | 16 Weeks |
|   | *Begins*	          | | Mon 08/20 |
| 1, 2 | **Bio, Notebook**   | assigned | Mon 08/20 |
| 1, 2 | **Bio, Notebook**   | due  | Mon 08/27 9am |
| 3 | **Tutorial**    | assigned | Mon 09/03 |
| 4 | **Chapter**         | assigned | Mon 09/03 |
| 5 | **Project**         | selection or proposal  | Mon 09/03 |
|   | *Labor Day*	      |  | Mon 09/03 |
| 5 | **Project** | update | 10/05 9am EST |
|   | *Fall Break*	      | | 10/05 - 10/07 |
|   | *Auto W*	          | | Sun 10/21 |
| 5 | **Project** | update | 11/02 9am EST |
| 3 | **Tutorial** | due | 11/02 9am EST |
| 4 | **Chapter** | due | 11/02 9am EST |
|   | *Thanksgiving*	  |    | 11/18 - 11/25 |
| 5 | **Project**         | due	       | 11/26 9am EST |
| 5 | **Project** (no penalty) | improvements | 11/26 - 12/03 9am EST |
| 5 | **Project** (with penalty) | improvements | 12/04 - 12/07 9am EST |
|   | **Final Deliverables due**  |  | 12/07 9am EST|
|   | *Grading*	          |  | 12/01 - 12/14 |
|   | *Ends*	          |  | Fri 12/14 |
|   | grade submission to school | | Fri 12/14 |
|   | grade posting by registrar | | 12/31 |

</div>

* TA's must be available till all grades have been submitted. 
* Bio: a formal 3 paragraph Bio
* Notebook: a markdown in which you record your progress of
  this class in bullet form
* All times are in EST
* Dependent on class progress Comprehension Assignments may be added
