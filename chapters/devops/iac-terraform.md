# Infrastructure as Code (IaC) - Terraform


## Learning Objectives


* Introduction to IaC and listing of IaC Tools
* Introduction to Terraform
* Basic Terraform Script to create an EC2 instance and Terraform commands
* Another Simple Terraform script - Docker
* Further Reading

## Introduction to IaC 


IaC(Infrastructure as Code), from the book Amazon Webservices in Action [@awsinactionbook]), is 
> the process of using a high level programming language to control IT
> systems -- servers, databases, networks, and so on." 

The infrastructure can be created, configured and destroyed "by means of code rather than
using physical hardware configuration, and interactive configuration tools." [@WikipediaInfraAsCode001].  

From the book "Amazon Web Services in Action" by Wittig [@awsinactionbook], using a script or a declarative description has
the following advantages 
> 
> * Consistent usage
> * Dependencies are handled
> * Replicable
> * Customizable
> * Testable
> * Can figure out updated state
> * Minimizes human failure
> * Documentation for your infrastructure 


IaC solves the problem of *environment drift*, that used to lead to the infamous
"but it works on my machine" kind of errors that are difficult to
trace. Sam Guckenheimer [@WhatisIaC002] writes that "
> IaC guarantees Idempotence -- known/predictable end state --  irrespective of starting
> state. Idempotency is achieved by either automatically configuring an
> existing target or by discarding the existing target and recreating a
> fresh environment.
"

IaC tools that are cloud specific are
Amazon AWS - AWS CloudFormation
Google Cloud - Cloud Deployment Manager
Microsoft Azure - Azure Resource Manager
OpenStack - Heat

From the book "Terraform - Up and Running" by Yevgeniy Brikman [@terraformuprunningbook], there are" 
> 4 broad categories of IaC tools
> * Ad hoc scripts: Any shell, Python, Perl, Lua scripts that are written
> * Configuration management tools: Chef, Puppet, Ansible, SaltStack
> * Server templating tools: Docker, Packer, Vagrant
> * Server provisioning tools: Terraform, Heat, CloudFormation, Cloud Deployment Manager, Azure Resource Manager
> 
> Chef and Ansible encourage a procedural style, while Terraform,
> CloudFormation, SaltStack, Puppet and Heat encourage a more declarative style.  
"

## Introduction to Terraform

Terraform is from HashiCorp. The tool is written in Go, and so are the
modules. Since most cloud providers have APIs and support for Go,
modules have been written for most providers.  The script of Terraform
is called HCL(HashiCorp Configuration Language) is similar to
YAML. Many code editors and IDEs have support for syntax highlighting
and even refactoring.  Terraform is a single binary, and runs the
generated script remotely -- without any master-slave configuration, or
without any agents.

The basic Terraform project script is a TF file (`.tf`). Other files you
could encounter are plan file`(.tfplan`), or a state file (`.tfstate`).

## Basic Terraform Script and commands


A basic script could look like this. Create this script in a project
folder.

```
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "myec2instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

The pre-condition to running this script would be

1. Create an AWS account
2. From IAM, get the access key and secret key, and plug them into this script.
3. Having the terraform binary downloaded, and uncompressed.

The steps to run this script are as follows:

```
cmd> terraform init
cmd> terraform plan -out CREATmyec2.tfplan
cmd> terraform apply CREATmyec2.tfplan
```
Now, your EC2 section in the AWS console should show the EC2 instance.

```
cmd> terraform plan -destroy -out DESTmyec2.tfplan
cmd> terraform apply DESTmyec2.tfplan
```

These steps would destroy the EC2 instance.

Let's walk through the basic script to help understand the overall working of Terraform.

The 2 main sections of the script are *Provider* and *Resource*.
*Providers* could be cloud providers -- including all the major ones -
AWS, Google Cloud, Azure, Alibaba, DigitalOcean, Oracle, API end
points -- for example GitHub, GitLab, DNS, Databases -- MySQL,
PostgreSQL, infrastructure components like Docker, Kubernetes,
VMWare. 

*Resources* section has the resources that the *Providers*
manage.

When you run ```terraform init```, the relevant modules specified in
the "Providers" and "Resources" are downloaded, and your project
workspace  -- folder or directory -- is initialized. All the dependent
resource information is also downloaded.

The ```terraform plan``` command plans out all the infrastructure
components and displays it. The dynamic properties and values to be
assigned will be listed as `<computed>`.  It is often advisable to save
the plan file. The plan file is a binary file, and is not human
readable.

In the next step, you can ```terraform apply``` the plan file. When
you confirm the creation of the resources, terraform spawns multiple
background jobs in parallel to create the infrastructure.

From now onwards, it would be a repeated set of steps of plan and
apply, until you get the infrastructure right.

To destroy the resources you created, again run ```terraform plan```
but this time with ```-destroy``` and save the plan. In the next
step, apply the saved plan, and watch the resource being shutdown and
terminated from the AWS console.

Some of the inputs mentioned in the script can be converted into
variables. Use of variables helps with modularizing code, avoiding
repeating values, and improves security. For added security, the
access key and secret key could be accessed as environment variables.

### What is State?

When you run ```terraform apply```, a state file(.tfstate) is
created. Though it is human readable, it is not advisable to edit it
by hand. Since it is plain text and may contain secret information,
it is also not advisable to check this file into a version repository
like Git. The book "Terraform - Up and Running" [@terraformuprunningbook] advises to
add the .terraform, `.tfstate` and `.tfstate.backup` to `.gitignore` file. A
shared, encrypted, and protected storage -- like S3 -- is often the best
location for these files.

### How Terraform deals with "environment drift"?

```terraform refresh``` refreshes the state file to the updated
real-world infrastructure that may have changed after it was
instantiated.

### How to I find out what is the current stored state?

```terraform show``` will display a human readable state output


## Another Simple Terraform script - Docker


Here is a simple Terraform script with Docker with nginx from Brian Shumate [@TerraformDockerGist]

```
# Configure Docker provider and connect to the local Docker socket

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Create an Nginx container

resource "docker_container" "nginx" {
  image = "${docker_image.nginx.latest}"
  name  = "enginecks"
  ports {
    internal = 80
    external = 80
  }
}

resource "docker_image" "nginx" {
  name = "nginx:latest"
}
```

Save this file as `dockng.tf` in another project folder/directory. Make
sure docker is installed.

Run the same set of commands as before

``` terraform init 
terraform plan -out CREATmydocng.tfplan 
terraform apply CREATmydocng.tfplan 
```


This will create a docker container with nginx, visible when you run ```docker ps -a```. 

When you open a browser, and navigate to `http://localhost`, you should see the nginx start page.

To destroy the container, run these commands using the same PLAN-APPLY

```
terraform plan -destroy -out DESTmydocng.tfplan
terraform apply DESTmydocng.tfplan
```

## Further Reading


A more complex example of Terraform is given in the AWS RedShift
section of the book.

Terraform is really powerful, expressive, and versatile. We have
explored some features and the basic workflow of usage.  Please see
books and resources like the "Terraform Up and Running" [@terraformuprunningbook] for more real-world
advice on IaC, structuring Terraform code and good deployment practices.

:o: we do not need to mention authors and publishers please fix throughout the paper. The citation is good enough. YOust do a bulleted list, but explain what you would find in it if needed.

Another resource for IaC is the book "Infrastructure as Code" [@iacbook].


