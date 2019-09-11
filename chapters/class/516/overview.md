# OVERVIEW {#sec:book-overview}

---

![](images/learning.png) **Learning Objectives**

* Gain an overview what currently is in this book
* Review the high level goals
* Be aware that this book is not complete and is worked on as we speak
* Be aware to check out the book on a weekly basis to stay up to date
* Be aware that additional material is distributed in separate books 
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
Linux. You will need no knowledge of them as you can pick it up while
reading this book.

* [Cloud Computing](https://laszewski.github.io/book/cloud/)
* [Linux for Cloud Computing](https://laszewski.github.io/book/linux/)
* [Python for Cloud Computing](https://laszewski.github.io/book/python/)
* [Scientific Writing with Markdown](https://laszewski.github.io/book/writing/)

The book is organized as follows:

**Definition of Cloud Computing**

: We will start with the definition of what cloud computing is and
  motivate why it is important to not only know technologies such as
  AI or ML or Databases. We present you with evidence that Clouds are
  absolutely relevant to todays technologies. We see furthermore a
  trend to utilize AI and ML services on in the cloud. Technologies
  such as virtual machine and containers and Function as a Service are
  essential to the repertoire of a modern Cloud or Data
  engineer. There is more than ML ... :relaxed:


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

: :o2: This chapter also includes information on how to achieve this with
  `eve`, but this framework is no longer supported. In a future
  version of the document we will remove this eve section.

**GraphQL**

: In this chapter we will introduce you to GraphQL which allows you to
  access data through a query language. It allows clients to easily
  formulate queries that retrieve desired data. Restrictions to the
  queries can be formulated to download what is needed. Other features
  include a type system. Github has added in addition to its REST service
  also a GraphQL interface. YOu will have the opportunity to explore
  GraphQl while interfacing with GitHub.

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

: :o2: A new section will be added pointing you to the cloudmesh API
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

: :o2: In fact we have here two sections that need to be delineated a bit
  better which we hope we can do with your help.

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

: :o2: you will help us improving this section if you elect to conduct
  a project on comet.

: We conclude the section with letting you know how to run Tensorflow
  via singularity,

**Serverless Computing**

: Recently a new paradigm in cloud computing has been introduced. Instead
  of using virtual machines or containers functions with limited resource
  requirements are specified that can than be executed on function capable
  execution services hosted by cloud providers.

: We will introduce you to this concept and showcase you some examples of
  FaaS services and frameworks.

**Messaging Services**

: Many devices in the cloud need to communicate with each other. In this
  chapter we look into how we can provide alternatives to REST services
  that provide messaging capabilities. We will focus on MQTT which is
  often used to connect cloud edge devices between each other and the cloud.

**GO**

: Go is a programming language used by Google and has been most famously
  used to implement Kubernetes. IN this chapter we introduce you to the
  elementary features of Go, but take also a closer look on how we can
  define REST services, use OpenAPI, and interface with clouds.

**Cloud AI Services**

: As part of the class we will be exploring AI services that are offered
  as part of clouds. You will be able if interested to use them in your
  projects. YOu will be developing also as part of this class AI services
  that you develop that can be hosted in the cloud and reused by others.
  While using cross-platform specifications, clients for Java, Python,
  Scala, Go, and other programming languages will be automatically created
  for you. This will allow others to reuse your services.
