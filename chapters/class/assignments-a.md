
### Assignment 0 - Organization and Communication

In order for us to communicate with you and you being able to use the
class resources we need you to register with various systems.  This
needs to be done immediately as it takes a while to get the systems set
up. It also requires approval steps that take some time and are not
immediate, thus do not just start this assignment on the due
date. Procrastination will not help you.

#### Account setup and survey

Please do the following:

Get access to piazza:

1. We have provided a detailed section about [piazza](#piazza) for you
   to explain how to get access to piazza. Please review this section
   carefully and create an account or use your existing piazza account
   to access the class piazza.

Next obtain some cloud accounts which you may use as part of the class:

2. Obtain an account on <https://github.com/>. Note this is not
   github.iu.edu and you may have a different account name on the
   systems. Please write down your *username* on github.com. Your
   username is not an e-mail.
3. Obtain an account on <https://portal.futuresystems.org/>. Please,
   write down your username.
4. Obtain an account on <https://www.chameleoncloud.org/>
5. Obtain an account on <https://portal.xsede.org/>. Please write down
   your username.

Make sure you chose strong passwords that you remember. Once you have
accees to Piazza do the following:

6. Post a **formal** bio on piazza in the bio folder so you introduce
   yourself to the class. It also serves as a verification that you
   have access to piazza and we can communicate with you. An example
   is available at:

   * <https://laszewski.github.io/bio.html>

7. Next fill out the class survey. Only do this after you have created
   all the accounts and you remember your usernames. The survey is
   located at

   * <https://goo.gl/forms/8Tkf2usxONZIEA182>

After you have submitted the survey we will create your github
repository that you will use for your deliverables. This will take
some time ...

7. **Wait till your HID directory on github.com is created**. Please
   do not send us e-mail, we will look at the survey within 1-2
   business days (Mon - Fri 9am-5pm EST) we will create your
   repository on github. Make sure to check on github as you will need
   to accept the invitation to gain access to the
   repository. github.com will also send you an e-mail. Check your
   spam folder.  make sure to **meet the deadline** for filling out
   the survey. It is typically the first Friday of the first week of
   class. Please be aware of this and conduct this task before Friday.

After your HID directory is created you can continue, with the next
tasks. But do not forget to upload them once you have access to the
other accounts.

8. Create a notebook.md file in your hid directory on github.com. An
   example is provided at

   * <https://github.com/cloudmesh-community/hid-sample/blob/master/notebook.md>

9. Create a README.yml file in the hid directory on github.com. Make
   sure to not use any TABS and use valid yaml. If you do not know
   what yaml is please find out, it is part of this assignment. An
   example README.yml can be found at:

   * <https://github.com/cloudmesh-community/hid-sample/blob/master/README.yml>

   You should remove the comments in your README.yml

Naturally, we want you to learn about the various systems. The one you will
need to use immediately is piazza. 

10. Learn about Piazza: please see [piazza](#piazza) for more details.


#### Class Computer Setup

Now it is time to buy some supplies and prepare your system. Obviously
this class will need a computer that you can use to login into the
remote machines and do your project. If you do not have such a
computer, you can purchase a Raspberry Pi with power plug for about
$50. Otherwise use your laptop or desktop. Detailed information about
such hardware are provided in the Raspberry PI section.

Residential students have access to about 100 Raspberry PIs in the
Raspberry PI Lab in Smith Research Center (which may be relocated to
MESH) Residential students will have mandatory projects for selected
classes that will have to be done on the Raspberry PIs. For online
students this is optional. Please refer to your specific class.

---

:warning: Please note that we do not provide support for Windows. You
can certainly use virtualbox and install a newer version of ubuntu on
it. Another option is to create a bootable USB stick or external HD on
which you install ubuntu. 

:warning: Windows 10 Home Edition has significant limitations at time
of writing of this document. For example it does not allow you to use
containers or proper virtualization. For this reason we recommend that
you upgrade to Windows 10 pro or education If you like to use
Windows. The education version is available for free via IU. Please
see (IUware)[https://iuware.iu.edu/Windows/title/2977] and share your
experience in piazza about your update. You must use the 64 bit
version. If your OS doe snot support 64 bit, you need to make sure you
update to 64 bit. Please consult the Windows documentation on
this. Whatever you do, make a backup first. It may be easier to boot
from an external HDD directly into ubuntu. 

:warning: macOS users have typically an easy time as all TAs have access
to macOS machines. However the version must be the latest version. We do
not support older versions.

---

#### Outcomes

Obviously this assignment has some implicit tasks and learning
outcomes such as 

* Learn how to use piazza.
* Learn how to use github.
* Learn how to write a formal bio.
* Set up a computer to be used for class.
* Learn on how to asks for help.
* Work with the fellow students to solve issues and give each other tips.

We expect that if you have difficulties with some of the technologies
to also consult with external resources that are for example searchable
with google. Using github is mandatory for your project and is a class
learning objective.

### Assignment 1 - Technology

Cloud and big data is an emerging field with lots of activities. To
gain an overview of the technologies used in the field you will be
tasked to do the following:

1. You will be downloading and studying the technology abstracts that
   we collected in

   * <https://github.com/cloudmesh/technologies/raw/master/vonLaszewski-cloud-technologies.epub>

2. You will be writing new or improving existing technology
   abstracts. A technology abstract is not plagiarized, does at most
   have 30% quotes in it and is between 150 to 450 words long. The
   text must address what the technology is about and how it is used
   in cloud and or big data. Each student will contribute till midterm
   10 such technologies. It is important that we make sure that each
   student has a unique list of technologies they work on. To
   coordinate this you will be first inspecting the git issues at

   * <https://github.com/cloudmesh/technologies/issues>

   For each technology that you will add or improve you will add a new
   issue. You will be using the title 

   ```Tech: Technology name```

   For new entries you will be using the label `new`, for issues that
   need improvement you will be using the label `open`. You will make
   sure you assign the issue to you.  It is in your responsibility to
   make sure you are the only and first one that this technology is
   assigned to. The organization of this is part of your learning
   experience. You will need to assign this technology to you.

   If you find in the git issues als technologies marked with the label
   `open` they are free for the taking and you can modify the issues
   and assign them to you.  Please also be reminded that all
   technologies in the technology book that are marked with a red
   circle need improvements. This is a long list

   All this is done on first come first serve.

   If you work in groups make sure to assign yourself 10
   technologies times the number of team members in your group. Make sure
   all group members are in github listed as assignee. The maximal
   number of group members is 3. In fact for this assignment we
   recommend that you work in groups as this usually increases the
   quality of of the submission. If you do not have a group find
   someone to review your submission.

   The technologies can be easily modified with pull requests that are
   managed by the TAs. We suggest that you work with your team and/or
   reviewer before you create the pull request. Each technology has a
   small cloud that when you click on it brings you to the github
   editor so you can create a pull request. Make sure that when
   working in a group you coordinate the contribution and do not
   create conflicts. Conflict resolution will be delegated to the team
   working on the technology.

   The epub publication will be updated typically once a day. So
   please check if your change is as expected.

   The entire technology handbook can be found at

   * <https://github.com/cloudmesh/technologies>


#### Outcomes

This assignment has the following outcomes

1. Learn about the many technologies as you should not just pick 10
   but read up on the once that you are interested in
2. Learn on how to write a small meaning full summary about a
   technology. This may also be required for you as part of you
   project. Hence, it is good to know how to do that.
3. Learn using gitissues
4. Learn how to self coordinate lots of tasks in a large group
5. Learn how to create pull requests via the git user interface
6. Learn how to use markdown which will be also used in your project
   to document how to replicate your project


### Assignment 2 - Programming Assignment & Chapter

In the handbook we have a large number of practical information that
describe a particular topic and include some information to explore
this topic with programs and scripts. Your task will be to improve or
create a substantial topic of your choice. The topics are included
in the following ebooks:

* <https://github.com/cloudmesh/book/raw/master/cloud-clusters/vonlaszewski-cloud-cluster.epub>

The source is located at


* <https://github.com/cloudmesh/book/tree/master/cloud-clusters>

You will be identifying an existing chapter or a new one that you will
improve. Just as in Assignment 0 we will use github issues to
coordinate this. Note that this is a different github issue so you
need to make sure you use the correct one for the correct task. For
this assignment the issues are managed at

* <https://github.com/cloudmesh/book/issues>

For chapter that you work on please use the title

```Chapter: Chapter name```

Make sure to assign it to you. Use the label `community` to make sure
to communicate that this contribution will be done by a community
member. As soon as you start working on this and there is text already
in the repository, please augment your issue with the url to the document.

TAs will also provide issues that are labeled with `open` that you can
take. Once you take it change the label to `community`. Note that the
Assignment 2 must be a significant contribution. Multiple smaller once
could add up to a significant contribution.

#### Outcomes

This assignment has the following outcomes


1. Inspect the chapters of the handbook
2. Learn how to document code and code execution
3. Learn python, bash, Makefiles and similar
4. Learn how to communicate on how to replicate a code
5. Learn how to benchmark (some contributions may require this)
6. Learn about libraries such as cmd5 and click
7. Learn about Python 2 vs 3
8. Learn about the limitations aof anaconda and why we should not use
   it (valid for some assignments).




### Assignment 3 - Project


The project deliverables depend on the class you take.  Please be
aware that the project or term paper constitute to a significant
portion of your grade of your class grade.  Please locate your class
number and read up on the section relevant for your class.

Please see our [Terminology](#terminology) Section about basic
requirements. The Report format is discussed in the Scientific Writing
Section.

Projects do require you to produce code for all classes the following
applies:

Report Format:

:   All reports will be using the our common format. This format is not
    the same as the ACM format, so if you use systems such as overleaf
    or sharelatex, you need to upload it and use it there.

    The format for LaTeX and Word found here:

    * <https://github.com/cloudmesh-community/hid-sample/tree/master/paper>

    There will be **NO EXCEPTION** to this format. In case you are in
    a team, you can use either github while collaboratively developing
    the LaTeX document or use MicrosoftOne Drive which allows
    collaborative editing features. All bibliographical entries must
    be put into a bibliography manager such as jabref, or Mendeley and
    exported to bibtex.  This will guarantee that you follow proper
    citation styles. You can use either ACM or IEEE reference
    styles. Your final submission will include the bibliography file
    as a separate document.

    :warning: Documents that do not follow the ACM format and are not
    accompanied by references managed with jabref or are not spell
    checked will be returned without review.


Code:

:   You must deliver the **source code** in github. The code must be
    compilable and a TA may try to replicate to run your code. You MUST
    avoid lengthy install descriptions and everything must be
    installable from the command line. We will check submission. All
    team members must be responsible for one or all parts of the
    project.

    Code repositories are for code, if you have additional libraries
    that are needed you need to develop a script or use a DevOps
    framework to install such software. Thus zip files and `.class`,
    `.o` files are not permissible in the project. Each project must be
    reproducible with a simple script. An example is:

        git clone ....
        make install
        make run
        make view

    Which would use a simple make file to install, run, and view the
    results. You are expected to integrate cmd5, which we teach in
    class. In addition you can use or are expected to us DOCKERFILES,
    ansible, or shell scripts. It is not permissible to use GUI based
    DevOps pre-installed frameworks. Everything must be installable and
    reproducible form the command line.

Cloud Resources:

:   Projects may be executed on your local computer, a cloud or other
    resources you may have access to. This may include:

    -   chameleoncloud.org
    -   furturesystems.org dockerswarm
    -   furturesystems.org kubernetes
    -   AWS (you will be responsible for charges)
    -   Azure (you will be responsible for charges)
    -   virtualbox if you have a powerful computer and like to prototype
    -   Raspberry PI's 
    -   other clouds, please confirm with us.

    Access to clouds must be scripted and a cmd5 extension must be
    developed as part of your project to receive full credit.  You
    must not just use your local PC as you need to use at least one
    cloud. If you work in a team each team member nedds to work at
    least on one cloud.


#### Class: E516 or E616

The objective of the project is to define a clear problem statement and
create a framework to address that problem. This framework must include
a docker packaged service that includes all necessary dependencies
necessary to perform the analysis. For example if you are using a
machine learning algorithm your docker packaged service will include the
machine learning algorithm which works on a particular dataset providing
clustered ,classified or regression outputs to the user. The final
objective is to obtain results in form of graphs or tabular mode. In
selecting a dataset, you can use a dataset from a public dataset like
and pick a suitable dataset according to your problem statement. Final
results must be exposed via a REST service. For instance if it is a
classification problem, the should have the capability of entering a new
test data set or single data point (meaning a single record) via a REST
API endpoint and get the expected output in form of a JSON object. UI
creation is an optional task. This is the overall expectation of the
project.

##### Deliverables

- Find a data set with reasonable size (this may depend on your
  resources and needs to include a benchmark in your paper for
  justification).

- Clean up the data set or make it smaller or find a bigger data set

- Identify existing algorithms and tools and technologies that you can
  use to analyze your data

- Develop a Swagger or Flask Rest Service to send a sample data set
  and get output. Provide benchmarks.

- Take results in two different cloud services and your local PC (ex:
  Chameleon Cloud, echo kubernetes). Make sure your system can be
  created and deployed based on your documentation. 

- Create a Makefile with the tags deploy, run, kill, view, clean that
  deploys your environment, runs application, kills it, views the
  result and cleans up after wards. You are allowed to have different
  makefiles for the different clouds and different directories. Keep
  the code and directory structure clean and document how to reproduce
  your results.

- For python use a requirements.txt file also

- For docker use a Dockerfile also 

- Write a report that includes the following sections

  * Abstract
  * Introduction
  * Architecture
  * Implementation
    * Technologies Used
  * Results
    * Deployment Benchmarks
    * Application Benchmarks
  * (Limitations)
  * Conclusion
  * (Work Breakdown)


#### Class: i423 i523 or E534 or i524

The objective of the project is to define a clear problem statement and
create a framework to address that problem as it relates to big data
your project must address the reproducibility of the deployment and
the application. A dataset must be chosen and you can analyze the
data. While in i423, i523, the data analysis has more weight, in e523
and i524 you must also address the deployment. For the later classes
see also the project requirements of E616.

You have plenty of time to make this choice and if you find you
struggle with programming you may want to consider a term paper
instead of a project.

In case you chose a project your maximum grade for the entire class
could be an A+. However, an A+ project must be truly outstanding and
include an exceptional project report. Such a project and report will
have the potential quality of being able to be published in a
conference.

In case you chose a term Paper for I524 your maximum grade for the
*entire* class will be an A-.


##### Deliverables

- Find a data set with reasonable size (this may depend on your
  resources and needs to include a benchmark in your paper for
  justification).

- Clean up the data set or make it smaller or find a bigger data set

- Identify existing algorithms and tools and technologies that you can
  use to analyze your data

- Develop a Swagger or Flask Rest Service to send a sample data set
  and get output. Provide benchmarks.

- Take results in two different cloud services and your local PC (ex:
  Chameleon Cloud, echo kubernetes). Make sure your system can be
  created and deployed based on your documentation. 

- Create a Makefile with the tags deploy, run, kill, view, clean that
  deploys your environment, runs application, kills it, views the
  result and cleans up after wards. You are allowed to have different
  makefiles for the different clouds and different directories. Keep
  the code and directory structure clean and document how to reproduce
  your results.

- For python use a requirements.txt file also

- For docker use a Dockerfile also 

- Write a report that includes the following sections

  * Abstract
  * Introduction
  * Architecture
  * Implementation
    * Technologies Used
  * Results
    * Deployment Benchmarks
    * Application Benchmarks
  * (Limitations)
  * Conclusion
  * (Work Breakdown)



#### Class: E222

For the final project in this class you need to do the following.

-   Find a dataset : A sample data repository can be found at the link
    below however you are free to use data from elsewhere, like scikit
    learn libraries.

-   Use Scikit Learn Library to run Machine Learning algorithm depending
    on your problem.

-   Do some classifications, clustering or a regression calculation
    using a machine learning algorithm.

-   Use the results from classification to draw charts. You can use
    matplotlib to do this.

-   Use REST api to tun ML algorithm i.e. in k-means the user should be
    able to change the cluster number (k) through a RESTful service.

-   Use Flask Rest API to expose the data to the viewers. So people can
    send a data set and get the outputs as a json object.

##### Deliverables

-   Find and clean up data set

-   Scikit Learn ML Algorithm Application to cleaned up data set

-   Clustering or Regression or Classification results in Graphical
    Format (Matplotlib) (GUI not needed, save graphs as png)

-   Flask Rest service to tune ML algorithm

-   Flask Rest Service to send a sample data set and get output
    (terminal output is enough)

-   Create a Makefile with running, setting up, sample test case running
    commands

-   requirement.txt file for pip installation

-   Package with Docker

- Write a report that includes the following sections

  * Abstract
  * Introduction
  * Architecture
  * Implementation
    * Technologies Used
  * Results
    * Deployment Benchmarks
    * Application Benchmarks
  * (Limitations)
  * Conclusion
  * (Work Breakdown)

