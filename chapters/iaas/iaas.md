# Introduction

---

**:mortar_board: Learning Objectives**

* Review IaaS servise by prominent cloud providers.
* Understand how to write Python programs on managing virtual machines with libcloud.
* Understand how to write Python programs on managing data services with libcloud.
* Experiment with cloud providers while practially testing them. :warning: be carfull with your allocation

---

[NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) defines the term 

*Infrastructure as a Service (IaaS)* as follows:

> The capability provided to the consumer is to provision processing,
> storage, networks, and other fundamental computing resources where
> the consumer is able to deploy and run arbitrary software, which can
> include operating systems and applications. The consumer does not
> manage or control the underlying cloud infrastructure but has
> control over operating systems, storage, and deployed applications;
> and possibly limited control of select networking components (e.g.,
> host firewalls).

The key term is to *provision* fundamental computing resources. This
means a user does not have to worry about managing the hardware
allowing low level services such as the operating system or the
network fabric to be the next higher interface for the user. The
hardware fabric is managed by the cloud provider, while the operating
system level and their connectivity with each other is managed by the
user.

We distinguish the following categories of infrastructure:

* compute resources
* network resources
* storage resources

We also like to remind you that such IaaS as parts of clouds can
either be accessed public, private or in a hybrid fashion.

Within the next view section we will focus on some of the main
providers of IaaS.

This includes

* Amazon Web Services
* Azure
* Google

Additionally, we also have 

* Watson

which although provides IaaS focusses more on delivering AI platforms
and related services to the community.

On the research side wi will be focussing on

* Chameleon Cloud.

Some of the services listed provide a free small contingent of IaaS
offerings that you can use. The use of this free tier will be
sufficient to conduct thsi class.

