# e516: Engineering Cloud Computing

---

**:mortar_board: Learning Objectives**

* This is the syllabus of the class. It will be updated throughout the semester, so look here for changes.
* Identify if this is the right class for you.
* Enroll if you want to take this class.
* Avoid an incomplete.

---

* Lecture Notes: <https://github.com/cloudmesh-community/book/blob/master/vonLaszewski-cloud.epub>
* Piazza: <https://piazza.com/iu/fall2018/516>
* Indiana University
* Fall 2018
* Faculty: Dr. Gregor von Laszewski (laszewski@gmail.com)
* Credits: 3
* First online class released: Aug. 22, 2018
* Residential students Discussion:   11:15A-12:15P  Fridays  I2 150, bring your laptops
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

This is an introductory class. In case you like to do research and
more advanced topics, consider taking an independent study with Dr. von
Laszewski.

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
  contribute collaboratively to develop tutorials for clouds.

# Syllabus

For the syllabus table please see the
[Syllabus Table Section](#s-516-syllabus) [:cloud:](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-syllabus-table.md).

## Assessment

This course is focusing on the principal "Learning by Doing" which is
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
3. Working project code that can be installed and executed in reproducible manner by a third party 
4. Code developed by the project team distributed in github.com
5. Project progress notes checked into github throughout the semester. Each 
   week the project progress is reported and will be integrated
   into the final grade.
6. three discussions or progress reports with the instructors about your project

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
