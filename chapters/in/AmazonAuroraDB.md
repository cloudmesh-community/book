# Amazon Aurora DB {#s-Amazon-aurora-db}

---

**:mortar_board: Learning Objectives**

* Learn about AWS Aurora DB
* Features and Benefits
* Pricing
* How to provision Aurora database

---

Amazon Aurora is an on-cloud relational database offering from AWS 
that aims to offer the performance and reliability of traditional 
enterprise databases combined with cost-effectiveness of open source 
databases.

Aurora comes as an SaaS offering in RDS suite offered by Amazon.

## Amazon Aurora Features and Benefits

### Compatible Databases

Currently, Aurora is compatible with MySQL and PostGreSQL Databases.
It provides a wrapper to provision these open source databases and manage
them for high availaibility.
This allows users to provision these open source databases through Amazon 
and still use existing code, tools and drivers with little change. 

### High Performance

Aurora offers upto 5 times the throughput of a standard MySQL database 
and 3 times throughput of standard PostGreSQL. All this is offered at a
price point which 1/10th of a commerical database.

### Scalability

Aurora allows users to scale up and down the databases to smaller or larger 
sized servers based on the dynamic business needs to match the required
compute power.
There is also a serverless offering where AWS to manages the scaling of 
compute requirements.
Aurora also adds additional storage as needed upto 64TB per instance as 
the data grows.

### High Availability and Durability

Aurora DB offers multi AZ option to make the data replicated across more 
than one availability zone making the resilient to failures. 
Data can be backuped to Amazon S3 to enable point in time recovery in case
of errors.

### High Performance through Read Replicas

Aurora DB offers to create upto 15 low latency Read Reaplica nodes for a 
database which allows for high performance. One can have writer node to 
write data into the database and use the Read Replica nodes ofr query data. 


### Fully Managed

Aurora comes as part of RDS suite where Amazon manages the database 
management actvities like hardware provisioning, set up and configuration,
software patching, database backups and performance monitoring.

### Security

Aurora allows to secure the data at rest and and in transit by using keys
through Key Management Service. Databases can also be made part of VPC 
and secured using private subnets and security groups. 
Database encryption can be enabled at the time of database creation which
means that the data, backups, snapshots and replicas is also encrypted.

### Parallel Query for Analytical Queries

This feature allows users to run analytical queries on the database without 
the need to copy the data into another system to not impact the system performance.
Aurora offloads the query to the CPU nodes in its storage layer allowing 
transactional and analytical loads alongside each other.

### Performance Monitoring

Aurora provides Performance Insight as a database performance tuning and
monitoring feature that can be enabled on the database for additional cost.
It allows to visualize the loads to identify performance issues. 

### Support for Migration

Amazon provides tools for migrating existing MySQL and PostgreSQL to Aurora.
AWS Database Migration Service is provided as a service to migrate from commerical
databases into Aurora.

## Amazon Aurora Pricing

Amazon Aurora pricing is determined by various factors:
* Type and Size of database instance
* Storage and IO
* Backup Storage
* Data Transfer

For detailed pricing refer AWS Aurora Pricing documentation  
[AWS Aurora Pricing](https://aws.amazon.com/rds/aurora/pricing/).

## How to provision Aurora database

To be added.
