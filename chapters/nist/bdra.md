# NIST Big Data Referenece Architecture

One of the major technical areas in the cloud is to define
architectures that can work with Big Data. For this reason NIST has
work now for some time on identifying how to create a data
interoperability framework. The idea here is that at one point
architecture designers can pick services that they can chose to
combine them as part of their data pipeline and integrate in a
convenient fashion into their solution.

Besides just being a high level description NIST also encourages the
verification of the architecture through interface specifications,
especially those that are currently under way in Volume 8 of the
document series. You have the unique opportunity to help shape this
interface and contribute to it. We will provide you not only
mechanisms on how you theoretically can do this, but also how you
practically can contribute.

As part of your projects in 516 you will need to integrate a
significant service that you can contribute to the NIST document in
form of a specification and in form of an implementation.


# Pathway to the NIST-BDRA

The Nist Big Data Public Working Group (NBD-PWG) was established as
collaboration between industry, academia and government "to create a
consensus-based extensible Big Data Interoperability Framework (NBDIF)
which is a vendor-neutral, technology- and infrastructure-independent
ecosystem" [@www-nist-bdra]. It will be helpfule for Big Data
stakeholders such as data architects, data scientists, researchers,
implementers to integrate and utilize "the best available analytics
tools to process and derive knowledge through the use of standard
interfaces between swappable architectural components"
[@www-nist-bdra]. The NBDIF is being developed in three stages:

* Stage 1: "Identify the high-level Big Data reference architecture
key components, which are technology, infrastructure, and vendor
agnostic," [@www-nist-bdra] introduction of the Big Data Reference
Architecture (NBD-RA);
* Stage 2: "Define general interfaces between the NBD-RA components
with the goals to aggregate low-level interactions into high-level
general interfaces and produce set of white papers to demonstrate how
NBD-RA can be used" [@www-nist-bdra];
* Stage 3: "Validate the NBD-RA by building Big Data general
applications through the general interfaces.[@www-nist-bdra]"

Nist has developed the following volumes as liste in *Table: BDRA volumes* that surround the creation of the NIST-BDRA 

**Table: NIST BDRA Volumes**

| Volumes | Volume | Title |
| :---- | :---- | :--- |
| [NIST SP1500-1r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-1r1.pdf) | Volume 1| Definitions
| [NIST SP1500-2r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-2r1.pdf) | Volume 2 | Taxonomies
| [NIST SP1500-3r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-3r1.pdf) | Volume 3 | Use Cases and Requirements
| [NIST SP1500-4r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-4r1.pdf) | Volume 4 | Security and Privacy
| [NIST SP1500-5](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-5.pdf)   | Volume 5 | Reference Architectures White Paper Survey
| [NIST SP1500-6r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-6r1.pdf) | Volume 6 | Reference Architecture
| [NIST SP1500-7r1](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-7r1.pdf) | Volume 7 | Standards Roadmap
| [NIST SP1500-9](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-9.pdf)   | Volume 8 | Reference Architecture Interface (new)
| [NIST SP1500-10](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-10.pdf)  | Volume 9 | Adoption and Modernization (new)


# Big Data Characteristics and Definitions

Volume 1 of the series introduces the community to common definitions
that are used as part of the field of Big data. This includes the
analysis of characteristics such as volume, velocity, variety,
variability and the use of structures and unstructured data. As part
of the field of data science and engineering it lists a number of
areas that are to be believed to be essential including that they must
master including data structures, parallelism, metadata, flow rate,
visual communication. In addition we believe that an additional skill
set must be prevalent that allows a data engineer to deploy such
technologies onto actual systems.

We have submitted the following proposal to NIST:

> 3.3.6. Deployments:

> A significant challange exists for data engineers to develop
> architectures and their deployment implications. The volume of data
> and the processing power needed to analysis them may require many
> thousands of distributed compute resources. They can be part of
> private data centers, virtualized with the help of virtual machines
> or containers and even utilize serverless computing to focus
> integration of Big Data Function as a Service based architectures.
> As such architectures are assumed to be large community standards
> such as leveraging DevOps will be necessary for the engineers to
> setup and manage such architectures. This is especially important
> with the swift development of the field that may require rolling
> updates without interruption of the services offered.

This addition reflects the newest insight into what a data scientist
needs to know and the newest job trends that we observed.
