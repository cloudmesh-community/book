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


## Course Syllabus


.<div class="smalltable">

| Dates  | Unit | Title  | Description |
| :------ | :--- | :------- | :--------------------- |
| :white_check_mark: 08/24    | 1       | Introduction      | [Gregor von Laszewski](#research-interests)[:cloud:][gregor.md] |
| :white_check_mark: 08/24    |         |                   | [Class summary](E516 Summary)[:cloud:][e516-summary.md] |
| :white_check_mark: 08/24    |         |                   | [Definition of Cloud Computing](#definition-of-cloud-computing)[:cloud:][e516-definition.md] |
| :white_check_mark: 08/31    | 2       | Tools             | **Tools and Services** |
| :white_check_mark: 08/31    |         |                   | - [Virtual Box](#virtual-box)[:cloud:][virtualbox.md] |
| :white_check_mark: 08/31    |         |                   | - [Vagrant](#vagrant)[:cloud:][vagrant.md] |
| :white_check_mark: 08/31    |         |                   | - [Github](#github)[:cloud:][github.md] |
| :white_check_mark: 08/31    |         |                   | - [Linux](#s-linux)[:cloud:][linux.md] |
| :white_check_mark: 08/31    | 3       | Python            | **Python** |
| :white_check_mark: 08/31    |         |                   | - [Introduction](#s-python-intro)[:cloud:][python-intro.md] |
| :white_check_mark: 08/31    |         |                   | - [Installation](#s-python-install)[:cloud:][python-install.md] |
| :white_check_mark: 08/31    |         |                   | - [Interactive Python](#interactve python)[:cloud:][python-interactive.md] |
| :white_check_mark: 08/31    |         |                   | - [Editors](#s-python-editor)[:cloud:][python-editor.md] |
| :white_check_mark: 08/31    |         |                   | - [Basic Language Features](#s-python-language)[:cloud:][python.md] |
| :white_check_mark: 08/31    |         |                   | - [Modules](#s-python-modules)[:cloud:][python-libraries.md] |
| :white_check_mark: 08/31    |         |                   | - [Data Management](s-python-data)[:cloud:][python-data.md] |
| :white_check_mark: 08/31    |         |                   | - [Matplotlib](#matplotlib)[:cloud:][python-matplotlib.md] |
| :white_check_mark: 08/31    |         |                   | - [Cloudmesh Commandshell CMD5](#cloudmesh-commandshell-cmd5)[:cloud:][python-cmd5.md] |
| :new: 09/13                 |         |                   | - [OpenCV](#s-opencv)[:cloud:][opencv.md] |
| :new: 09/13                 |         |                   |- [Secchi Disk](#s-secchi-disk)[:cloud:][secchi.md] |
| :white_check_mark: 09/03    |         |                   | [Data Center][datacenter.md] |
| :white_check_mark: 09/10    | 4       | Architectures     | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
| :new: 09/13                 |         |                   | - [Cloud Architectures](#s-cloud-architectures) [:cloud:][arch.md]
| :white_check_mark: 09/15    |         |                   | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
| :o: 09/24                   | 5       | Virtualization    | [Virtualization, Qemu, KVM, Virtual machines](#s-virtualization)[:cloud:][virtualization.md] |
| :o: 09/24                   | 5       | Virtualization I  | - [Qemu](#s-virtualization)[:cloud:][qemu.md] |
| :white_check_mark: 09/15    | 6       | Infrastructure    | [Infrastructure as a Service](#infrastructure-as-a-service)[:cloud:][iaas.md] |
| :white_check_mark: 09/17    |         |                   | - [Azure](#microsoft-azure) [:cloud:][azure.md] |
| :white_check_mark: 09/17    |         |                   | - [AWS](#amazon-web-services) [:cloud:][aws.md] |
| :o: 09/17                   |         |                   | - OpenStack Introduction |
| :white_check_mark: 09/17    |         | Chameleon Cloud   | - **Chameleon Cloud** |
| :white_check_mark: 09/17    |         |                   | - [Resources](#chameleon-cloud-security-warning)[:cloud:][resources.md] |
| :white_check_mark: 09/17    |         |                   | - [Hardware](#chameleon-cloud-hardware)[:cloud:][hardware.md] |
| :white_check_mark: 09/17    |         |                   | - [Charge](#chameleon-cloud-charge-rates)[:cloud:][charge.md] |
| :white_check_mark: 09/17    |         |                   | - [Quick start](#getting-started-on-chameleon-cloud)[:cloud:][start.md] |
| :white_check_mark: 09/17    |         |                   | - [KVM user guide](#openstack-virtual-machines)[:cloud:][user-guide.md] |
| :white_check_mark: 09/17    |         |                   | - [CLI](#openstack-command-line-interface)[:cloud:][cli.md] |
| :white_check_mark: 09/17    |         |                   | - [Horizon](#openstack-horizon)[:cloud:][horizon.md] |
| :white_check_mark: 09/17    |         |                   | - [Heat](#openstack-heat)[:cloud:][heat.md] |
| :white_check_mark: 09/17    |         |                   | - [Baremetal](#openstack-baremetal)[:cloud:][baremetal.md] |
| :white_check_mark: 09/17    |         |                   | - [FAQ](#chameleon-cloud-frequently-asked-questions)[:cloud:][faq.md] |
| :o: 09/24                   | 7       | Virtualization  II | Qemu, KVM, Virtual machines |
| :o: 10/01                   |         |                   | Containers, Docker, Kubernetes |
| :white_check_mark: 10/08    | 8       | Programming       | Python for Cloud Computing, |
| :white_check_mark: 10/08    |         |                   | - [Libcloud](#python-libcloud)[:cloud:][libcloud.md] |
| :o: 10/08                   |         |                   | - Github as a Cloud Service |
| :white_check_mark: 09/11    |         |                   | - [REST Services](#rest)[:cloud:][rest.md] |
| :white_check_mark: 09/11    |         |                   | - [Rest Services with OpenAPI](#rest-services-with-openapi)[:cloud:][swagger.md] |
| :white_check_mark: 09/11    |         |                   | - [OpenAPI Spec](#openapi-spec)[:cloud:][swagger-spec.md] |
| :white_check_mark: 09/11    |         |                   | - [OpenAPI Codegen](#openapi-codegen)[:cloud:][swagger-codegen.md] |
| :o: 10/22                   | 9       | Map/Reduce        | Map/Reduce, Hadoop, Spark |
| :white_check_mark: 10/29    | 10      | Messaging         | Messaging |
| :white_check_mark: 10/29    | 11      | Messaging         | - [MQTT](#mqtt)[:cloud:][mqtt.md]  |
| :o: 11/05                   |         |                   | - [Graphql][graphql.md]  |
| :o: 11/19                   | 12      | Go                | [Go Introduction](#s-go-intro)[:cloud:][go-intro.md] |
| :o: 11/19                   |         |                   | - [Go Links](#s-go-links)[:cloud:][go-links.md] |
| :o: 11/19                   |         |                   | - [Go Install](#s-go-install)[:cloud:][go-install.md] |
| :white_check_mark: 11/19    |         |                   | - [Go Editors](#s-go-editor)[:cloud:][go-editor.md] |
| :o: 11/19                   |         |                   | - [Go Language](#s-go-language)[:cloud:][go-language.md] |
| :o: 11/19                   |         |                   | - [Go Libraries](#s-go-libraries)[:cloud:][go-libraries.md] |
| :o: 11/19                   |         |                   | - [Go cmd](#s-go-cmd)[:cloud:][go-cmd.md] |
| :o: 11/19                   |         |                   | - [Go Cloud](#s-go-cloud)[:cloud:][go-cloud.md] |
| :o: 11/19                   |         |                   | - [Go REST](#s-go-rest)[:cloud][go-rest.md] |
| :o: 11/19                   |         |                   | - [Go for the Cloud](#s-go-cloud)[:cloud][go-cloud.md] |
| :o: 12/03                   | 13      | Edge Computing    | Edge Computing and the Cloud |
| 09/13-11/02*                | A1      | Tutorial          | Contribute a significant tutorial. Do not develop redundant or duplicated content. |
| 09/13-11/02*                | A2      | Chapter           | Contribute a significant chapter that may use your tutorial to the class documentation. Do not develop redundant or duplicated content. |
| 09/17-11/26*                | A3      | Project Type A    | Build a cloud out of Raspberry PIs |
| 09/17-11/26*                |         |                   | Kubernetes, Hadoop, SLURM + OpenAPI Service,  |
| 09/17-11/26*                |         | Project Type B    | Build a Significant OpenAPI REST Service |
| 09/17-11/26*                |         | Project Type C    | Build an Edge Service Interfacing with a Cloud |
| 09/17-11/26*                |         | Project Type D    | Your own Project Type A, B, or C [upon approval) |

Legend markings

* Class released :white_check_mark:
* Class under development :o:

</div> 
 

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


Students need only to do one project. The project is conducted thought
the entire semester.


* Dates may change as the semester evolves

* The project is a long term assignment (and are ideally worked on
weekly by residential students). It is the major part of the course
grade.

(*) Tutorials prepare you for documenting a technical aspect related
to cloud computing. It is a preparation for a document that explains
how to execute your project in a reproducible manner to others.

- all times are in EST

Additional Lectures will be added that allow easy management of the project. These lectures can be taken any time when needed

<div class="smalltable">

| Date     | Unit    | Title             | Description
| :----------- |:------- |:----------------- |:---------------------------
| :white_check_mark: anytime  | 1       | [Scientific Writing I](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-writing-1.epub) |
| :white_check_mark: anytime  |         | Plagiarism      | How to avoid plagiarism and cheating
| :white_check_mark: anytime  |         | Markdown        | How to use markdown
| :white_check_mark: anytime  | 1       | [Scientific Writing II](http://cyberaide.org/papers/vonLaszewski-latex.pdf) |
| :white_check_mark: anytime  |         | Writing a Project Report      | How to write a high quality Project report following our template
| :white_check_mark: anytime  |         | Bibliography Management      | How to easily manage bibliographies for your Project Report
| :white_check_mark: anytime  | 1       | [Class Communication](https://github.com/cloudmesh-community/book/raw/master/vonLaszewski-communicate.epub) |
| :white_check_mark: anytime  |         | Class Github      | How to use the class Github
| :white_check_mark: anytime  |         | Class Piazza      | How to use the class Piazza

</div>

If you follow our template writing the report is like filling out a
simple form. 


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
