# OVERVIEW {#sec:book-overview}

---

![](images/learning.png) **Learning Objectives**

* Gain an overview of what currently is in this book
* Review the high-level goals
* Be aware that this book is not complete and is worked on as we speak
* Be aware to check out the book on a weekly basis to stay up to date
* Be aware that additional material is distributed in separate books 
  such as Linux, Python, and Writing in Markdown.
* Be aware that books you may purchase may already be outdated by the 
  time you order them.

---



In this book, we provide many chapters that will allow you to quickly
and easily get knowledge in cloud computing on theoretical and practical
levels. To reduce the size of the online books, we have split them up in
a number of topical books that you will be using as part of this class.

We expect that you pick up the material discussed in these books as
needed. Our main books include:

* [Linux for Cloud Computing](https://laszewski.github.io/book/linux/) [@las19linux]

  This book Gives an elementary overview of Linux features we will use.

* [Python for Cloud Computing](https://laszewski.github.io/book/python/) [@las19python]

  This book Gives an elementary overview of Python features we will use.

* [Scientific Writing with Markdown](https://laszewski.github.io/book/writing/) [@las19writing]

  This book Gives an elementary overview of Markdown features we will use.


The main book discusses aspects around clouds and is published at

* [Cloud Computing](https://laszewski.github.io/book/cloud/) [@las19technologies]

The book contains the following content:

**Definition of Cloud Computing**

: We start with the definition of what cloud computing is and
  motivate why it is vital to not only know technologies such as
  AI or ML or Databases. We present you with evidence that Clouds are
  absolutely relevant to today's technologies. We see furthermore a
  trend to utilize AI and ML services in the cloud. Technologies
  such as virtual machines and containers and Function as a Service are
  essential to the repertoire of a modern Cloud or Data
  engineer. There is more than ML ... :relaxed:


**Data Center**

: This chapter explains to you why we need cloud
  data centers, how a cloud data center look likes and which environmental
  the impact such data centers have.

**Architecture**

: This chapter introduces you to the basic architectural features and designs of cloud computing. We discuss architectures for
  IaaS, and contrast it to other architectures. We discuss the
  NIST definition of the cloud and the Cloud Security Alliance
  Reference Architecture. We discuss the multi-cloud architecture
  introduced by Cloudmesh as well as the Big Data Reference
  Architecture.

**REST**

: This chapter introduces you to a way on how to define services in the cloud that you can easily access via language-independent
  client APIs. It will introduce you to the fundamental concepts of
  REST. We will, more importantly, introduce you to OpenAPI that allows you to specify REST services via a specification document so you can create APIs and clients form the document automatically. We will showcase you how to do that with `flask`.

: We showcase you on a top-rated service such as GitHub how to
  easily interface with REST services in Python.

**GraphQL**

: In this chapter, we introduce you to GraphQL, which allows you to access data through a query language. It allows clients to easily
  formulate queries that retrieve desired data. Restrictions to the queries can be formulated to download what is needed. Other features
  include a type system. Github has added in addition to its REST service
  also a GraphQL interface. You have the opportunity to explore
  GraphQl while interfacing with GitHub.

**Hypervisors**

: Virtualization is one of the important technologies that started the cloud revolution. It provides the basic underlying principles for
  the development and adoption of clouds. The concept, although old
  and already used in the early days of computing, has recently been
  exploited to lead to better utilization of servers as part of data
  centers, but also the local desktops.

: In this chapter, we introduce you to the basic concepts and distinguish
  the various forms of virtualization.

: We list virtualization frameworks such as Libvirt, Qemu, KVM, Xen,
  and Hyper-V. Dependent on your hardware, you are encouraged to experiment with one or more of them.

**IaaS**

: In the IaaS chapter, we review many of the services
  offered by providers usch as AWS, Azure, Google, and OpenStack that
  is used by some academic clouds such as Chameleon cloud.

: In addition, we introduce you to elementary command-line tools and
  programs to access this infrastructure.

: In this section, we provide you with information about
  multi-cloud management with Cloudmesh which makes it extremely easy to
  switch between and use services from multiple clouds.

: Important to note is that the appendix contains very useful
  information that augments this section. This includes a more detailed
  list of services for some IaaS providers as well as information on
  how to use chameleon cloud which has been adapted by us for this
  chapter.


**Map/Reduce**

: In this chapter, we discuss the background of Mapreduce along with 
  Hadoop and its core components. We also introduce Spark to you in this 
  section.

: You will be presented on how you can use the systems on a single
  resource so you can explore them more easily, but we will also let
  you know how to install them on a cluster in principal.

: We conclude this section with some important Map/Reduce frameworks
  used as part of the larger Map/Reduce ecosystem such as AWS Elastic
  Map/Reduce (AWS EMR). This also includes a discussion about Twister2
  which is a version of Map/Reduce that could perform even faster than
  Spark.

**Container**

: In the container chapter, we introduce you to the basic concepts of a container and delineate it from virtual machines as we have introduced you earlier. We start the chapter with an introduction to Docker and then introduce you to how to manage clusters capable of running many containers with the help of docker swarm and
  Kubernetes.  To showcase you its use on other PaaS and applications,
  we even show you how to run Hadoop with Docker as well as how to conduct a PageRank analysis.  Kubernetes is discussed in its own section.

: As many academic datacenters do run queuing systems, we will also
  showcase Singularity allowing you to use containers within a batch
  queuing system.

: We conclude the section with letting you know how to run Tensorflow
  via singularity,

**Serverless Computing**

: Recently a new paradigm in cloud computing has been introduced. Instead
  of using virtual machines or containers functions with limited resource
  requirements have specified that can then be executed on functions capable
  execution services hosted by cloud providers.

: We introduce you to this concept and showcase you some examples of
  FaaS services and frameworks.

**Messaging Services**

: Many devices in the cloud need to communicate with each other. In 
  this chapter, we look into how we can provide alternatives to REST services that provide messaging capabilities. We focus on MQTT, which is
  often used to connect cloud edge devices between each other and the cloud.

**GO**

: Go is a programming language used by Google and has been used to 
  implement Kubernetes. In this chapter, we introduce you to the
  elementary features of Go and also take a closer look at how we can
  define REST services, use OpenAPI, and interface with clouds.

**Cloud AI Services**

: As part of the class, we explore AI services that are 
  hosted in clouds and offered as service.
  If interested, you can use them in your projects. As part of this class
  you can develop AI services which can be hosted 
  in the cloud and reused by others.
  While using cross-platform specifications, clients for Java, Python,
  Scala, Go, and other programming languages will be automatically created
  for you. This will allow others to reuse your services.
