# AWS DocumentDB (hid: sp19-516-134)

---

**:mortar_board: Learning Objectives**

* Learn about AWS Document DB
* Components
* Features and Benefits
* Pricing
* How to provision Document database
* How to connect to Document Database

---

AWS Document DB is a fully managed service with compatibility with
Mongo DB. Mongo DB application code can be run here with same drivers
and tools. A cluster needs to be created for using AWS document DB. It
can contain zero or more databases instances and a attached volume for
managing data for the cluster. The storage is replicated to multiple
availablity zones with each having its own copy.

Components:

1. Instances - There could be upto 16 instances which do the reading
   and writing data from storage volume. Primary and Replica are the
   two types of instances. Only one Primary instances is permitted
   which is used to read and write to the volume. Replica is used only
   for read operation and can be used to placed in multiple availbaility
   zones to increase the cluster availibility. Instances can be bought up
   and terminated as desired. Compute capacity can be scaled independent
   of storage.

2. Cluster Volumes - Volume can store upto 64 TB of data replicated
   across availability zones.
   
## Amazon DocumentDB Features and Benefits

* *MongoDB-compatible*: Implemented using the Apache 2.0 open source 
  MongoDB 3.6 API by emulating the responses that a MongoDB client 
  expects from a MongoDB server. This allows you to use your existing 
  MongoDB drivers and tools with Amazon DocumentDB.
  
* *Highly available*: Designed for 99.99% availability with six copies 
  of data across three AWS Availability Zones (AZs). Switchs to read 
  replica in the event of a failure–typically in less than 30 seconds.
  Data is automatically backed up in S3 for 35 days.
  
* *Performance at scale*: It uses a distributed, fault-tolerant, 
  self-healing storage system that auto-scales up to 64 TB per database 
  cluster. Reduces database I/O by writing only database changes to 
  the storage layer
  
* *Highly secure*: Provides multiple levels of security for your database, 
  including network isolation using Amazon VPC, encryption at rest using
  keys you create and control through AWS Key Management Service (KMS), 
  and encryption-in-transit using Transport Layer Security (TLS). 
  
* *Fully managed*: Automatically and continuously monitors and backs up 
   your database to Amazon S3, enabling point-in-time recovery 
   (up to the second for the last 35 days). Integrates with Amazon CloudWatch, 
   so you can monitor over 20 key operational metrics for your database 
   instances via the AWS Management Console.
  
##  AWS Document database Pricing

