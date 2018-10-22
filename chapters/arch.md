# Architectures {#s-cloud-architectures}

---

**:mortar_board: Learning Objectives**

* Reveiew classical architectural models leading up to cloud computing.
* Review some mayor cloud architecture views.
* Visualize the NIST cloud architecture
* Discuss an architecture for multicloud frameworks.

---

While we have introduce in our introductory section a number of
definitions for cloud computing, as well as an architectural view for
clouds based on the "as a Service" model, we will look a bit closer at
other alternative views. These views are in some cases important as
they provide appropriate abstractions for more detailed
implementations.

## Evolution of Compute Architectures

We start our observation with some a depiction of some of the
important architectural models motivating the current state of
information technology services we provide in +@fig:evolution-computer-arch.
The [original figure]
(http://www.cmlab.csie.ntu.edu.tw/~jimmychad/CN2011/Readings/CloudComputingNewWine.pdf)
has been updated by von Laszewski to include the mobile computing and
the internet of things phase that is bringing rapid changes to how we
perceive and use the cloud in the near future.

![Evolution of Compute Architectures](images/compute-phase.png){#fig:evolution-computer-arch}

We define the following terminology based on the evolution of compute
architectures:


### Mainframe Computing

Mainframe computing is using the larger and more reliable computers, 
like IBM System z9, to run the critical applications, bulk data processing, 
enterprise resource planning and business transaction procesings.

Mainframe Computing refers to 

:o: This section can be contributed by a student

### PC Computing

The term PC is short for personal computer. The first PCs were
introduced by IBM to the market. PCs need an operating system such as
Windows, macOS, or Linux

PC Computing refers to

> an era where consumers predominantly used personal computers to
> conduct their work. Such computers were mostly stand alone without
> network as early networks were not available to consumers.

### Intranet and Server Computing

We refer to Intranet and Server Computing as an environment in which 

> the computers are part of an private network, also called, intranet,
> that is contained within an enterprise and later on also
> homes. Intranets are able to connect many local resources within a
> Local but also a wide area network

### Grid Computing Computing 

and its evolution is defined in
[The Grid-Idea and Its Evolution](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.61.196&rep=rep1&type=pdf). The
original definition of Grid computing has been summarise as follows:

> A computational Grid is a hardware and software infrastructure that
> provides dependable, consistent, pervasive, and inexpensive access
> to high-end computational capabilities. [@foster-book]

However, in the paper we also define that Grids were not just about
computing, but introduced an approach that through the introduction of
virtual organizations lead to the following definition

> A production Grid is a shared computing infrastructure of hardware,
software, and knowledge resources that allows the coordinated resource
sharing and problem solving in dynamic, multi-institutional virtual
organizations to enable sophisticated international scientific and
business-oriented collaborations.

This definition is certainly including services that are today offered
by the Cloud. Hence in the early days of cloud computing there was a
large debate occurring if cloud is just another term for Grid. In
[Cloud Computing and Grid Computing 360-Degree Compared]
(http://datasys.cs.iit.edu/publications/2008_GCE08_Clouds_Grids.pdf)
an analysis is conducted between the different architecture models
outlining that collective resources and connectivity protocols
introduced by the Grid community have been replaced by the cloud with
platform and unified resources.

To provide a very simple but possibly incomplete comparison, Cloud
computing integrated infrastructure such as supercomputers and other
large scale resources through unified protocols. The effort was
initially provided by research institutions but have been introduced
in business. However, with the growth of the data centers to foster
common tasks such as Web hosting, we see a clear difference:

* while the Grid was originally designed to give a few scientist access
  to the biggest agglomerated research supercomputers,
* business focused on serving originally millions of users with the
  need to run only a view data or compute services.

This certainly resulted in independent development, while cloud
computing has today consumed Grids. Tools such as the GLobus toolkit
are no longer widely used, and the development has shifted to the
support of data services only.



### Internet Computing

With the ocurance of the WWW protocols, internet commuting brought to
the consumers a global computer network providing a variety of
information and communication facilities.

Internet Computing refers to

> the infrastructure that enables sharing of data, within the WWWW community.

Internet computing also comprises early infrastructures such as AOL,
which poularized the term *you got mail*

### Cloud Computing

Cloud Computing refers to

> :o: A written section can be contributed by student

We have provided a lecture about the definition of cloud computing
previously

### Mobile Computing 


Mobile Computing refers to

> a diverse set of devices allowing users to access data and
> information from wherever they are with mobile devices such as cell
> phones or tablet computers. mobile computing is dominated by
> transmission of data, voice, and video over a network via the mobile
> device

### Internet of Things Computing

Internet of Things Computing refers to

> devices that are interconnected via the internet while they are
> embedded in *things* or common objects. The dives send and receive
> data to be integrated into a network with sensors and actuators
> reacting upon sensory and other data.


### Edge Computing

In addition, we need to point out two additional terms that we will
integrate in this image. Edge Computing and Fog Computing.  Currently
there is still some debate about what these terms are, but we will
follow the following definitions:

Edge Computing refers to

> computing conducted on the very edge of infrastructure. This means
> that data that is not needed in the data center can be calculated
> and analyzed on the edge devices instead. No interaction between
> cloud services is needed. Only the absolute required data is send to
> the cloud.

### Fog Computing

FoG Computing refers to 

> computing conducted in-between the cloud and the edge devices. This
> could be for example part of a smart network, that hosts a small set
> of analytics capabilities, so that the data does not have to travel
> back to the data center, but the edge device is not powerful enough
> to do the calculation. Thus a Fog computing infrastructure provides
> tha ability to conduct the analysis closer to the edge saving
> valuable resources while not needing to transmit all data to the
> data center although it will be analyzed


## As a Servise Architecture Model

The *as a Service* architecture was one of the earliest definition of
cloud architecture while focussing on the service aspect provided by
the cloud. the layers such as IaaS, PaaS, and SaaS provide a layered
architecture view while separating infrastructure, platform, and
services. This allows a separation of concerns typically between
infrastructure providers, platform developers, and software architects
using platforms and or infrastructure services.

The typical triangular diagram (see +@fig:iaas-triangle) is often used
to represent it.

![Infrastructure as a Service](images/architecture-iaas.png){#fig:iaas-triangle}

## Product or Functional Based Model

When we inspect prominent providers such as Amazon, Azure, and Google,
we find that on their Web pages they do provide their customers an
alternative view that is motivated by exposing numerous products to
the customers grouped by functions. Thes services are often in the
hundrest. To achieve the exposure of the products in a meaningful
fashion, they introduce a functional view motivation a functional
architecture view of the cloud.

When we analyse these functions for example for Amazon Web services we
find the following

- Compute
- Storage
- Databases
- Migration
- Networking & Content Delivery
- Developer Tools
- Management Tools
- Media Services
- Security, Identity & Compliance
- Machine Learning
- Analytics
- Mobile
- Augmented reality and Virtual Reality
- Application Integration
- Customer Engagement
- Business Productivity
- Desktop & App Streaming
- Internet of Things
- Game Development
- AWS Marketplace Software
- AWS Cost Management

From this we derive that for the initial contact to the customer the
functionality is put in foreground, rather than the distinction
between SaaS, PaaS, and IaaS. If we sort these services into the as a
Service mode we find:


- IaaS

  - Compute
  - Storage
  - Databases
  - Migration
  - Networking & Content Delivery

- PaaS
  - Developer Tools
  - Management Tools
  - Media Services
  - Security, Identity & Compliance
  - Machine Learning
  - Analytics
  - Mobile
  - Augmented reality and Virtual Reality
  - Application Integration
  - Customer Engagement
  - Business Productivity
  - Desktop & App Streaming
  - Game Development
  - AWS Marketplace Software
  - AWS Cost Management
  - Internet of Things

We observe that AWS focusses on providing infrastructure and
platformes so others can provide integrated service to its customers.

Other examples for product lists such as the one from Azure are provided in the Appendix.


## NIST Cloud Architecture

In the introduction we have extensively discussed the NIST cloud
architecture. A Nice visual representation is provided in the
following Figure.

![Visual representation of the NIST Cloud Architecture](images/nist-vis-arch.png)

Source: <https://downloads.cloudsecurityalliance.org/assets/research/security-guidance/csaguide.v3.0.pdf>

## Cloud Security Alliance Reference Architecture

The Cloud Security Alliance (CSA) is a nonprofit organization that provides a variety of security resources to institutions including guidelines, education and best practices for adoption. Based on the following guiding prinicples they published the following reference Architecture:

* Define protections that enable trust in the cloud.
* Develop cross-platform capabilities and patterns for proprietary and open-source providers.
* Will facilitate trusted and efficient access, administration and resiliency to the customer/consumer.
* Provide direction to secure information that is protected by regulations.
* The Architecture must facilitate proper and efficient identification, authentication, authorization,
administration and auditability.
* Centralize security policy, maintenance operation and oversight functions.
* Access to information must be secure yet still easy to obtain.
* Delegate or Federate access control where appropriate.
* Must be easy to adopt and consume, supporting the design of security patterns
* The Architecture must be elastic, flexible and resilient supporting multi-tenant, multi-landlord platforms
* The architecture must address and support multiple levels of protection, including network, operating
system, and application security needs.

![Cloud Security Alliance Reference Architecture](images/csa-architecture.png)
Source: <https://downloads.cloudsecurityalliance.org/initiatives/tci/TCI_Reference_Architecture_v2.0.pdf>



## Multicloud Architectures

One of the issues we see today is that it is unrealistic to assume
clouds are only provided by one vendor, or that they have all the same
interface. Each vendor is advertising their special services to
distinguish themselves from the competitors. For the end user and the
developer that projects the problem of vendor lockin. However, we need
to be aware of efforts that allow an easy of such vendor lockin while
for example providing multi cloud solutions.  Such solutions integrate
multiple vendors and technologies into a single architecture allowing
to use multiple cloud vendors at the same time.

### Cloudmesh Architecture

One of the earliest such tools is Cloudmesh.org, which is lead by von
Laszewski. The tool was developed at a time when AWS and Nimbus, and
Eucalyptus where predominant players. At that time OpenStack was just
transitioned from a NASA project to a community development.

FutureGrid ws one of the earliest academic cloud offerings to explore
the effectiveness of the different cloud infrastructure solutions. It
was clear that a unifying framework and abstraction layer was needed
allowing us to utilize the easily. In fact cloudmesh did not only
provide a REST based API, but also a commandline shell allowing to
switch between clouds with a single variable. It also provided bare
metal provisioning before OpenStack even offered it. Through an
evolution of developments the current cloudmesh architecture that
allows multicloud services is depicted in the next figure. We still
distinguish the IaaS level which included not only IaaS Abstractions,
but also Containers, and HPC services. Platforms are typically
integrad=ted through DevOps that can be hosted on the IaaS. Examples
are Hadoop, and Spark The services are exposed through a client API
hiding much of the internals to the user. A portal and application
services have successfully demonstrated the feasibility of this
approach.

![](images/arch-cloudmesh.png)

Within the hour e516 class we will be developing a modern version of
cloudmesh from the ground up by only using python 3 as implementation
language, integration of containers, and REST services based on
OpenAPI. Local data to manage the different services are hosted in a
mongo DB database and exposed through portable containers, so that a
single crosplatform environment exists as part of the project
deliverables.

Students from e516 can and are in fact expected to participate
actively on the development of Cloudmesh v4.0. In addition the OpenAPI
service specifications developed for the project will be integrated in
Volume 8 of the NIST Big data reference architecture, which is
discussed elsewhere.

The advantage of developing such an environment is that we can look at
various aspects of cloudcomputing while demonstrating integrated use patterns.

## Resources

* <http://www.lifl.fr/iwaise12/presentations/tata.pdf>
* <https://media.amazonwebservices.com/AWS_Cloud_Best_Practices.pdf>
* <http://staff.polito.it/alessandro.mantelero/cloud_computing/Sun_Wp2009.pdf>
* <https://resources.sei.cmu.edu/asset_files/Presentation/2010_017_001_23337.pdf>
* <https://www.oracle.com/technetwork/articles/entarch/orgeron-top-10-cloud-1957407.pdf>
* <http://www.oracle.com/technetwork/topics/entarch/oracle-wp-cloud-ref-arch-1883533.pdf>
* <https://pdfs.semanticscholar.org/cecd/c193b73ec1e7b42d132b3c340e6dd348d3f4.pdf>
