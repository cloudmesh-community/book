# Report List

TBD. table

Here we summarize the Projects and teams. Place the document in your github folder under project/report.md. Please make sure to use proper markdown and not githubs common mark. Once the reports are created they will at one point also show up in the proceedings.

## CLOUD STORAGE-STORAGE-LOCAL PROJECTS

| HID	| Status |	Names |	Project| 
| ---- | ---- | ---- | ---- |
| 160 | approved |	Shreyans |	Azure to Google Cloudmesh Storage Provider for Virtual Directories: see cloudmesh-storage to start. develop OpenAPI REST services for it|
| 152 | approved | Pratibha	| Google to/form AWS: Cloudmesh Storage Provider for Virtual Directories: see cloudmesh-storage to start. develop OpenAPI REST services for it| 
| 162	| approved | Shivani | Oracle to/from ? Storage Service (Residential) 534, (see: cloudmesh-storage), Provide a REST service for it based on OpenAPI that uses the cloudmesh API you develop. see also Python, implement virtual directory from local first |
| 155	| approved | Ketan	| Azure to/form AWS blob Storage Service, (see: cloudmesh-storage), Provide a REST service for it based on OpenAPI that uses the cloudmesh API you develop. |
| all |	 | |  if this works technically we should be able to coppy between all clouds as we have all services for each cloud and each speaks the same protocol |



CLOUDMESH COMPUTE PROJECTS


HID	Status	Name	Project
fa19-516-162	approved	Shivani	516: Oracle Compute Service (Residential), see also Python
165	approved	Zhi	Google Compute Service, gregor will set up new repo for this, you can start identifying python API and implement functions to list images, flavors, start vms upload keys and security groups, once repo is set up you need to start uploading your contributions on weekly basis
170	approved	Chenxu	Azure Cloudmesh Compute - The secgroup command is not working, extensive testing needs to be done. As this project is mostly finished, you will compare the performance from Azure with other clouds such as OpenStack, AWS, and possibly Oracle, and Google once they become available. You would help improve any of the missing clouds once secgroup is done (Oracle, Google). IT is best to start right away with this and learn how to start vms in Azure.
169	approved	Harsh	Developing Cloudmesh interfaces for Google Cloud Platform. The two cloud implementation to be demonstrated using GCP and AWS
PI PROJECTS


HID	Status	Name	Project
fa19-516-148	approved, started	Sub, Gregor	Federated Kubernetes Cluster with Raspberry PI
fa19-516-158
fa19-516-150	approved, started	Daivik
Akshay	Raspberry Pi Cloud Cluster for Spark
Raspberry Pi Cloud Cluster for Hadoop
DATABASE ABSTRACTION PROJECTS

HID	Status	Name	Project
fa19-516-147	approved	Harsha	Abstract database management on Multicloud environments for the NIST Big Data Reference Architecture AWS, Azure
141	approved	Bala, Mani	Abstract database management on Multicloud environments for the NIST Big Dara Refernce Architecture AWS, Azure, Mongo, SQL

NIST BigDataInterface reference implementation for data base absractions on 2 clouds with 2 differnt technologies, one is a SQL based the othe is a NoSQPL based (mongo)


OTHER PROJECTS


HID	Status	Names	Project
fa19-516-167


approved

Bill	Cloudmesh Virtual Directory Life Cycle Service, This needs to run on 2 clouds + locally. 
TTL = time to live is one, attribute for lifecycle management. Bi9ll explained this is more than ttl.

fa19-516-166	approved	Brian Funk	Cloudmesh Frugal with AWS, Azure, and Google Cloud.
fa19-516-159

Austin Zebrowski	

Apache Airflow data pipelining between HDFS and Amazon Redshift

fa19-516-171	Please review	Jagadesh	
PLEASE ADD TITLE
https://github.com/cloudmesh-community/fa19-516-171/blob/master/project/report.md

fa19-516-144
fa19-516-172	needs input from student and clarification	
Andrew Holland
Nayeem	
Introduce Encryption Functionality for Cloudmesh Configuration File

161


approved	Jim Nelson	Batch Processing using Kubernetes and Cloudmesh
batch processing - of r programs - virtual cluster for batch
processing r programs in kubernetes / vms cloudmesh may help.
gregor suggests to use kubernetes to do batch jobs on it. Possibly cloudmeh-flow would help, but we do the jobs on cubernetes, while the bactch jobs are formulated as workflows.
153, 164	approved, started	Anish, Siddhesh	Hadoop/Spark Cluster abstraction layer - dynamically changing available machines/storage available to hadoop/spark instances using orchestration tool and command line
174		Sahithi	R
151	approved	Qiwei Liu, Yanting, Chenxu	Cloudmesh Cloud AI Services.
140	approved, but some details are missing	Mohamed Elfateh	Cognitive Response Simulation using Cloudmesh Cloud AI Services
146, 163	Needs Review	John Hoerr, Kenneth Jones	
Serverless API Performance Analysis


fa19-516-168		Deepak Deopura	
https://github.com/cloudmesh-community/fa19-516-168/tree/master/project
AWS to/from Azure data transfer using APIs. -Extended version can be push data in SQL base warehouse (for example snowflake warehouse. It may be out of scope for now for this project purpose.
#pin