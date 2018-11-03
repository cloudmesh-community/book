# Amazon Kinesis Data streams :hand:

Comment: This section needs to be improved

We provide high level overview on Amazon Kinesis and focus on an example that details setting up Amazon Kinesis data stream.
Amazon kinesis is used to collect and process large streams of data records in a real time. Amazon kinesis data streams application reads data from a Kinesis data stream as records. Kinesis applications can use the kinesis client libraries and they can run on Amazon EC2 instances.

## Components of Kinesis Data Streams

- Kinesis Data Streams
- Data Records
- Producers
- Consumers

## High Level Components Description

The Producers continually push data to Kinesis data streams and the consumers process the data in real time. Consumers are any applications running on Amazon EC2, can store their results on AWS service such as Amazon dynamo DB, Amazon Redshift, Amazon S3.

## Amazon Kinesis Limitations

Note the following constraints in using Amazon Kinesis Streams 
- The maximum  data blob size  (the data payload before Base64-encoding) in a record is 1 megabyte (MB).
- One shard can be a maximum of 1000 PUT records/second.
- By default, data streams collected are accessible up to 24 hours. However, by enabling extended data retention, data can be available up to 7 days. 

## Setting up for Amazon Kinesis Data Streams

To use Amazon Kinesis Data Streams you need to do the following steps

- Setup the AWS account
- Download libraries and tools
  - Amazon Kinesis API reference is the basic set of operations that kinesis data streams supports
  - The AWS SDKs based on your preference language of development like Java, .NET , Python and etc.
  - The Kinesis client library provides easy-to-use programing model for processing data.
  - The AWS command line interface supports kinesis data streams. The AWS CLI enables you to control multiple AWS services from command the command line and automate them through the scripts

## Create Kinesis

Step1 - Login to AWS and create the Kinesis data streams
A Kinesis stream is an ordered sequence of data records. To add data to a Kinesis stream, configure producers using the Streams PUT API or the Amazon Kinesis Producer Library (KPL).

Step2 – Click the create stream and fill the required fields such as stream name and number of shared and then click on create button.
 

![AWS CreateKenesisStream](images/CreateKinesisStream.png?raw=true)

![AWS DataStreamDetails](images/DataStreamDetails.png?raw=true)
 

Step3 – Set up users on kinesis stream. Create new users and assign a policy to each user.

Step4 – Connect your application to Amazon kinesis

## Features of Amazon Kinesis

Amazon Kinesis has the following features:

* Flat learning curve − Kinesis is easy to use. Just create an AWS stream endpoint from AWS console and start pushing data in. It does not require setting up of complex software and infrastructure which can be hard to maintain and manage.
* Up-to-date processing of high throughput data − It can collect data at any time, at any scale and provide analysis right away when you need it enabling you to respond to an incoming information immediately.
* Low-Cost − there are no upfront fees and you pay only as you use.
* Seamless integration with Amazon ecosystem− It can be easily integrated with Amazon services like Amazon S3, Redshift, and Amazon DynamoDB.
* Build custom applications − Amazon Kinesis provides application programming interfaces to easily build applications on top of the Kinesis platform to meet specific needs of the business.
