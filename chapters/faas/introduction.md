# FaaS

## Introduction

FaaS or Function as a service is a new paradim in cloud computing that
is gaining popularity recently. FaaS is also known as Serverless
Computing to some. While the name Serverless implies that no servers
are involved this is not true.  So FaaS would be a better term to
describe this technology. FaaS is built around functions and
events. Functions are generally stateless and are executed within
isolated containers. The execution of the functions can be thought of
as an event driven model. A program or application in FaaS consist of
a set of functions and a set of events or triggers that invoke or
activate those functions. A function activation can result in another
function activation as a result.

Generally FaaS specifies a set of constraints on what a function can
be. The constraints include storage constraints such as a maximum size
for the function, maximum memory allowed, execution time, etc. The
exact constraints differ from provider to provider. AWS Lambda is
considered as one of first FaaS offerings. Now most cloud providers
offer their own version of FaaS. Several popular FaaS providers are
listed next.

## Serverless Computing

In Serverless Computing, servers are still there, its just that we
dont need to manage them.

Another advantage of going serverless is that you no longer need to
keep a server running all the time. The *server* suddenly appears when
you need it, then disappears when you’re done with it. Now you can
think in terms of functions instead of servers, and all your business
logic can now live within these functions.

## Faas provider

* [AWS Lambda](https://aws.amazon.com/lambda)[@aws-amazon-lambda]
* [Azure Functions](https://azure.microsoft.com/en-us/services/functions)[@azure-serverless-computing]
* [IBM Cloud Functions](https://cloud.ibm.com/functions/)[@ibm-cloud-functions]
* [Google Cloud Functions](https://cloud.google.com/functions)[@google_cloud_functions]
* [Iron.io](https://www.iron.io)[@iron_io]
* [Webtask.io](https://webtask.io)[@webtask_io]

Other than the providers there are also several open source FaaS
offerings that are available to be used. One of the most complete and
popular open source option would be Apache OpenWhisk, which was
developed by IBM and later open sourced. IBM currently deploys
OpenWhisk in IBM cloud and offers it as a IBM Cloud functions.

* [OpenWhisk](https://github.com/apache/incubator-openwhisk)[@openwhisk]
* [Funktion](https://github.com/funktionio/funktion) [@funktion]
* [Iron Functions](https://github.com/iron-io/functions)[@iron_functions]
* [Kubeless](https://github.com/kubeless/kubeless)[@kubeless]
* [Fission](https://github.com/fission/fission)[@fission]
* [FaaS-netes](https://github.com/alexellis/faas-netes)[@faas-netes]


There are many articles and tutorials online that provide very good
information regarding FaaS. Given next are some such resources that provide
introductions and some example usecase's of FaaS

## Resources

* <https://stackify.com/function-as-a-service-serverless-architecture>[@function_as_a_service]
* <https://en.wikipedia.org/wiki/Serverless_computing>[@serverless_computing]
* <https://azure.microsoft.com/en-us/overview/serverless-computing>[@azure_serverless_computing]
* <https://aws.amazon.com/serverless>[@aws-amazon-serverless]
* <https://aws.amazon.com/lambda>[@aws-amazon-lambda]
* <https://www.infoworld.com/article/3093508/cloud-computing/what-serverless-computing-really-means.html>
* <https://techbeacon.com/aws-lambda-serverless-apps-5-things-you-need-know-about-serverless-computing>
* <https://blog.alexellis.io/introducing-functions-as-a-service>

## Usage Examples

* <https://aws.amazon.com/solutions/case-studies/netflix-and-aws-lambda>
* <https://blog.alexellis.io/first-faas-python-function>
