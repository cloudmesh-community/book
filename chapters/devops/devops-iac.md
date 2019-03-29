# Infrastructure as Code (IaC)

:o: document does not reflect separation between IaC and terraform as discussed in meeting

## Learning Objectives

:o: se how we do objectives in other documents  emoji and lines are missing

---

**:mortar_board: Learning Objectives**

* Introduction to IaC 
* How IaC is related to DevOps
* How IaC different from Configuration Management Tools, and how is it related
* Listing of IaC Tools
* Further Reading


---

## Introduction to IaC 


IaC(Infrastructure as Code), from the book Amazon Webservices in Action [@awsinactionbook]), is 

> the process of using a high level programming language to control IT
> systems -- servers, databases, networks, and so on." 

The infrastructure can be created, configured and destroyed "by means of code rather than
using physical hardware configuration, and interactive configuration tools." [@WikipediaInfraAsCode001].  

From the book "Amazon Web Services in Action" by Wittig [@awsinactionbook], using a script or a declarative description has
the following advantages 
 
> * Consistent usage
> * Dependencies are handled
> * Replicable
> * Customizable
> * Testable
> * Can figure out updated state
> * Minimizes human failure
> * Documentation for your infrastructure 


## How IaC is related to DevOps


DevOps has the following key practices
* Automated Infrastructure
* Automated Configuration Management, including Security
* Shared version control between Dev and Ops
* Continuous Build - Integrate - Test - Deploy
* Continuous Monitoring and Observability

The first 2 practices - Automated Infrastructure and Automated Configuration Management - can be satisfied by many IaC tools.

According to [@terraformuprunningbook], there are
" 
> 4 broad categories of such tools
> * Ad hoc scripts: Any shell, Python, Perl, Lua scripts that are written
> * Configuration management tools: Chef, Puppet, Ansible, SaltStack
> * Server templating tools: Docker, Packer, Vagrant
> * Server provisioning tools: Terraform, Heat, CloudFormation, Cloud Deployment Manager, Azure Resource Manager
> 
> Chef and Ansible encourage a procedural style, while Terraform,
> CloudFormation, SaltStack, Puppet and Heat encourage a more declarative style.  
"


## How IaC tools are different from Configuration Management Tools

Configuration Management tools make use of scripts to achieve a state. IaC tools maintain state and metadata created in the past. 

However, the big difference is the state achieved by running procedural code or scripts may be different from state when it was created because  
 * Ordering of the scripts determines the state. If the order changes, state will differ. Also, issues like waiting time required for resources to be created, modified or destroyed have to be correctly dealt with.
 * Version changes in procedural code are inevitable, and will lead to a different state. 

IaC or declarative tools do suffer from inflexibility related to expressive scripting language.

Sometimes IaC tools are also called Orchestration tools, but that label is misleading.

Typical workflow includes running Configuration Management tool scripts after running IaC tools.


## Listing of IaC Tools

IaC tools that are cloud specific are
Amazon AWS - AWS CloudFormation
Google Cloud - Cloud Deployment Manager
Microsoft Azure - Azure Resource Manager
OpenStack - Heat

Terraform is not a cloud specific tool, and is multi-vendor. It has got good support for all the clouds, however, Terraform scripts are not portable across clouds.


## Advantages of IaC


IaC solves the problem of *environment drift*, that used to lead to the infamous
"but it works on my machine" kind of errors that are difficult to
trace. According to [@WhatisIaC002]

> "IaC guarantees Idempotence -- known/predictable end state --  irrespective of starting
> state. Idempotency is achieved by either automatically configuring an
> existing target or by discarding the existing target and recreating a
> fresh environment."



## Further Reading


Please see books and resources like the "Terraform Up and Running" [@terraformuprunningbook] for more real-world
advice on IaC, structuring Terraform code and good deployment practices.

:o: we do not need to mention authors and publishers please fix throughout the paper. The citation is good enough. YOust do a bulleted list, but explain what you would find in it if needed.

A good resource for IaC is the book "Infrastructure as Code" [@iacbook].
