# OVERVIEW


---

![](images/learning.png) **Learning Objectives**

* Gain an overview what currently is in this book
* Review the high level goals
* Be aware that this book is not complete and is worked on as we speack
* Be aware to check out the book on a weekly basis to stay up to date
* Be aware that additional material is dictributed in separate books 
  such as Linux, Python, and Writing in Markdown.
* Be aware that books you may purchase may already be outdated by the 
  time you order them.

---



In this book we provide a number of chapters that will allow you to
easily get knowledge in cloud computing on theoretical and practical
levels.

Although the following was originally covered in this book, we decided
to split out its contents as to make the core cloud engineering book
smaller. In case you take one of our classes using the book, we expect
that you pick up the material covered also by these additional books.
Please be aware that some of the class material is based on Python and
Linux. YOu will need no knowledge of them as you can pick it up while
reading this book.

* Linux  :o: to be added
* [Python](https://laszewski.github.io/book/python/)
* [Scientific writing with Markdown](https://laszewski.github.io/book/writing/)


The book is organized as follows:


**Data Center**

: This chapter will explain you why we need cloud
  data centers, how a cloud data center look likes and which environmental
  impact such data centers have.

**Architecture**

: This chapter will introduce you to the basic architectural features
  and designs of cloud computing. We will discuss architectures for
  IaaS, and contrast it to other architectures. We will discuss the
  NIST definition of the cloud and the Cloud Security Alliance
  Reference Architecture. We will discuss the multi-cloud architecture
  introduced by cloudmesh as well as the Big Data Reference
  Architecture.

**REST**

: This chapter will introduce you to a way on how to define services
  in the cloud that you can easily access via language independent
  client APIs. It will introduce you to the fundamental concepts of
  REST. We will more importantly introduce you to OpenAPI that allows
  you to specify REST services via a specification document so you can
  create APIs and clients form the document automatically. We will
  showcase you how to do that with `flask`.

: We will showcase you on a very popular service such as GitHub how to
  easily interface with REST services in Python.

: :o: This chapter also includes information on how to achieve this with
  `eve`, but this framework is no longer supported. In a future
  version of the document we will remove this eve section.

**GraphQL**

: In this chapter we will intorduce you to GraphQL whic alloes you to
  access data through a query language. It allows clients to easily
  formulate queries that retrieve desired data. Restrictions to the
  queries can be formulated to download what is needed. Other features
  include a type system. Github has added in addition to its REST service
  also a GraphQL interface. YOu will have the opertunity to explore
  GraphQl while interfaceing with GitHub.

**Hypervisors**

: Virtualization is one of the important technologies that started the
  cloud revolution. It provides the basic underlying principles for
  the development and adoption of clouds. The concept, although old
  and already used in the early days of computing, has recently been
  exploited to lead to better utilization of servers as part of data
  centers, but also the local desktops.

: In this chapter we introduce you to the basic concepts and distinguish
  the various forms of virtualization.

: We list virtualization frameworks such as Libvirt, Qemu, KVM, Xen,
  and Hyper-V. Dependent on your hardware you will be encouraged to
  experiment with one or more of them.

**IaaS**

: In the IaaS chapter we will be reviewing many of the services
  offered by providers usch as AWS, Azure, Google, and OpenStack that
  is used by some academic clouds such as chameleon cloud.

: In addition we will introduce you to elementary command line tools and
  programs to access this infrastructure.

: :o: A new section will be added pointing you to the cloudmesh API
  which can become a project for students using this book in
  class.

: Important to note is that the appendix contains very useful
  information that augments this section. THis includes a more detailed
  list of services for some IaaS providers as well as information on
  how to use chameleon cloud which has been adapted by us for this
  chapter.


**Map/Reduce**

: In this chapter we discuss about the background of Mapreduce along
  with Hadoop and core components of Hadoop. We will also introduce
  you in this section to Spark.

: You will be presented on how you can use the systems on a single
  resource so you can explore them more easily, but we will also let
  you know how to install them on a cluster in principal.

: We conclude this section with some important Map/Reduce frameworks
  used as part of the larger Map/Reduce ecosystem such as AWS Elastic
  Map/Reduce (AWS EMR). This also includes a discussion about Twister2
  which is a version of Map/Reduce that could perform even faster then
  Spark.

: :o: In fact we have here two sections that need to be delineated a bit
  batter which we hope we can do with your help.

**Container**

: In the container chapter we will introduce you to the basic concepts
  of a container and delineate it from virtual machines as we have
  introduced you earlier. We will start the chapter with an
  introduction to Docker and than introduce you how to manage clusters
  capable of running many containers with the help of docker swarm and
  kubernetes.  To showcase you its use on other PaaS and applications
  we even show you how to run Hadoop with docker as well as how to
  conduct a pagerank analysis.  Kubernetes will be discussed in its
  own section.

: As many academic datacenters do run queuing system, we will also
  showcase Singularity allowing you to use containers within a batch
  queuing system.

: :o: you will help us improving this section if you elect to conduct
  a project on comet.

: We conclude the section with letting you know how to run tensorflow
  via singularity,

**Serverless Computing**

: Recently a new paradim in cloud computing has been introcuced. Instead
  of using virtual machines or containers functions with limited resource
  requirements are specified that can than be executed on function capable
  execution services hosted by cloud providers.

: We will introduce you to this concept and showcase you some examples of
  FaaS services and farmeworks.

**Messaging Services**

: Many devices in the cloud need to communicate with each other. In this
  chapter we look into how we can provide alternatives to REST services
  that provide messaging capabilities. We will focus on MQTT which is
  ovetn used to connect cloud edge deveices between each other and the cloud.

**GO**

: Go is a programming language used by Google and has been most famiously
  used to implement Kubernetes. IN this chapter we introduce you to the
  elementary features of Go, but take also a closer look on how we can
  define REST services, use OpenAPI, and interface with clouds.
