# Kubeless 

:o: add bibtex

## Introduction

Kubeless is an Serverless or FaaS framework that has been developed as a 
Kubernetes native framework. Kubeless is designed using services and features 
that are provided natively on the Kubernetes framework. It uses Kubernetes 
Custom Resource Definition to define functions 

## Programing model

Similar to other serverless frameworks, the programming model of Kubeless is 
an event-driven model. The two main components that need to be understood and
functions and events. Kubeless currently supports 3 types of functions 
runtimes Python, NodeJS and Ruby. These runtimes can be used to create and
deploy functions. For each function an event type is defined which specifies 
the type of trigger for the event. Kubless currently supports 3 types of 
triggers which are, HTTP based, scheduled and event-based (pubsub). 

## System Architecture

The system architecture is based completely on Kubernetes primitives which were
discussed to some extent in the previous section. The Kubless architecture 
has 3 main components, Functions API, Kubeless-controller, and Kafka. 
Additionally, they provide Kubeless command-line client which can be used to 
perform CRUD operations for function more easily. 

The Functions API provides a REST Endpoint to create, read, update and delete
functions. This is developed as a Kubernetes Custom Resource Definitions 
(CRD). CRD is an extension point provided by Kubernetes that can be used to 
create custom resources. A custom resource exposes a REST endpoint and makes 
it available as any other REST API that is embedded with Kubernetes. Once 
created, Functions custom resource exposes the REST API that can be used for 
function CRUD operations. The Kubeless-controller is a custom controller that
is deployed with the Kubernetes installation. This controller continuously 
monitors invocations that occur at the functions REST API and performs the 
required tasks according to the invocation. For example, if the invocation 
is for a function creation, the controller will create a Deployment for the
function and a Service to expose the function. The Deployment will contain 
information on what runtime the function is intended to use, therefore the 
deployment will make sure to spin up Pods which will host containers of that 
runtime when a function execution is requested. Kafka is deployed within the 
Kubernetes installation as an event source which can be used to trigger the 
functions.

Because the container image that is used to execute the function is generic, 
it does not have any specific dependencies that are required by the function 
and the function code itself. These two need to be injected into the Pod when
the Pod is created. For the application logic/function code, Kubless uses a 
configuration resource provided by Kubernetes API named ConfigMap. The code 
segment is attached to the ConfigMap which can be read from within a Pod once
the Pod is created. In order to install all the required dependencies, another
Kubernetes resource named Init containers are utilized. Init containers are a 
special kind of container which can be configured to run when a Pod is 
created. Kubernetes also guarantees that all init containers specified for
a Pod will run till completion before the application containers ( in this 
case function container) are executed. Kubless runs an init container which 
will install all the required dependencies for the function before invoking
the function. The function dependencies must be specified at function creation
 time.
