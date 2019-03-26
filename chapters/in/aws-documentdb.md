# AWS DocumentDB (hid: sp19-516-134)

---

**:mortar_board: Learning Objectives**

* Learn about AWS Document DB
* Features and Benefits
* Components
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
