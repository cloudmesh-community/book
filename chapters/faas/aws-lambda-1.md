# AWS Lambda - 1

## Introduction

AWS Lambda is considered as one of the earliest FaaS implementations
made available to end users. AWS Lambda provides a rich set of
features that can be leveraged by users to build programs and
applications on top of the FaaS framework. AWS Lambda supports many
event types that developers can use to orchestrate their FaaS
applications. And in line with the FaaS model AWS Lambda only charges
users for actual execution time of the functions. For example if you
host and deploy a function on AWS Lambda and only execute it for 1
minute every day you will only be charged for the 1 minute execution
time.

AWS does not share how the internals of AWS Lambda work in detail but
as with any general FaaS framework it should be leveraging various
container technologies underneath. You can get a better understanding
on how the internals of a FaaS framework is organized by looking at
the [OpenWhisk Section](openwhisk.md)

## AWS Lambda Features

AWS Lambda provides many features that allows the creation of an FaaS
application straight forward. An FaaS application normally consist of
a set of functions and a set of events that activate or invoke those
functions. AWS Lambda supports several programing languages that allow
developers to develop the function they require in any of the
programming languages that are supported. The following list show the
programming languages that are currently supported by AWS Lambda for
function creation.

* Node.js (JavaScript)
* Python
* Java (Java 8 compatible)
* C# (.NET Core)
* Go

Other than the functions the most important requirement for a good
FaaS framework is a rich set of function invocation methods which
allow users to tie together different events that happen in the echo
system with the FaaS application. In this regard AWS Lambda supports
many event sources, mainly from the AWS echo system. AWS documentation
provides a complete list of supported event sources at
[AWS Lambda event sources](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html).
For example a developer can configure an function to be invoked when a
S3 bucket is updated, or configure an function to be invoked based on
inputs received by Amazon Alexa, etc.

:o: use also bibtex

## Understanding Function limitations

Before you start working on FaaS frameworks it is important to
understand the limitations and restrictions that are applied to
functions. The limits and restrictions discussed in the section are
applicable to most FaaS frameworks but the exact values may differ
based on the FaaS vendor. However the reason for most of the
limitations are to maintain performance requirements. We will discuss
several major limits below. For a complete list of limits in AWS
Lambda please refer to the limits documentation
[AWS Lambda Function Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)

:o: use also bibtex

### Execution Time

AWS Lambda limits the execution length of a function. Currently it is
set to 15 minutes but was set at 300s previously, so the function
limits have and may change with time. Other FaaS provides have
different values for execution time limits, but in general each FaaS
provider does define a execution time limit

### Function size

AWS Lambda also sets several memory and storage limits for
functions. Currently the maximum memory allocated to a function is
3008MB and the maximum allocated storage space is 512MB. However it is
good to keep in mind that monetary charge for function execution
increases with the amount of memory that is specified for the
function.

## Understanding the free Tier 

If new users want to experiment with AWS lambda, AWS does provide a
free tier for AWS Lambda, which include 1 million function invocations
per month. You can find a more detailed description of the free tier
in the AWS docs
[AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

:o: use also bibtex
 
## Writing your fist Lambda function

With the GUI interface it is relatively easy to try out your first
Serverless function with AWS Lambda. Please follow the steps defined
at
[How to run your first AWS Lambda function in the cloud](../iaas/aws/aws-lambda.md#how-to-run-your-first-aws-lambda-function-in-the-cloud---example)

:o: use also bibtex
