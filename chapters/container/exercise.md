# Exercises

E.Docker.1: MongoDB Container

> Develop a docker file that uses the mongo distribution from Dockerhub 
> and starts a MongoDB database on the regular port while communicating 
> to your container.
>
> What are the parameters on the command line that you need to define?

E.Docker.2: MongoDB Container with authentication

> Develop a MongoDB container that includes an outhenticated user. You
> must use the cloudmesh.yaml file for specifying the information for the 
> admin user and password. 
>
> 1. How do you add the user?
> 2. How do you start the container?
> 3. Showcase the use of the authentication with a simple script or pytest.

> You are allowed tou sue docker compose, but make sure you read the
> password ond username from the yaml file. YoU must not configure it by
> hand in the compose yaml file. You can use cloudmesh commands to read
> the username and password.

> ```
> cms config value cloudmesh.data.mongo.MONGO_USERNAME
> cms config value cloudmesh.data.mongo.MONGO_PASSWORD
> ```

E.Docker.3: Cloudmesh Container

> In this assignment we will explore the use of two containers. We will be
> leveraging the asisgnment E.Docker.2.
>
> First, you wil lstart the authenticated docker MongoDB container

> You will be writing an additional dockerfile, that creates cloudmesh in
> a docker container. Upon start the parameter passed to the container
> will be executed in the container. You will use the .ssh and .cloudmesh
> directory from your native file system.
>
>For hints, please look at 
>
> * <https://github.com/cloudmesh/cloudmesh-cloud/blob/master/docker/ubuntu-19.04/Dockerfile>
> * <https://github.com/cloudmesh/cloudmesh-cloud/blob/master/docker/ubuntu-19.04/Makefile>
> 
> To jump start you try 
>
> ```
> make image
> make shell
>```
>
> Explore! Understand what is done in the Makefile
>
> Questions:
> 
> 1. How would you need to modify the Dockerfile to complete it?
> 2. Whay did we outcomment the MongoDB related tasks in the Dockerfile?
> 3. How do we need to establish communication to the MongoDB container
> 4. Could docker compose help, or would it be too complicated, e.g. what 
>    if the mongo container already runs?
> 5. Why would it be dangerous to store the cloudmesh.yaml file inside 
>    the container? Hint: DockerHub.
> 6. Why should you at this time not upload images to DockerHub?



E.Docker.Swarm.1: Documentation

> Develop a section in the handbook that deploys a Docker Swarm cluster
> on a number of
> ubuntu machines. Note that this may actually be easier as docker and
> docker swarm are distributed with recent versions of ubuntu. Just in
> case we are providing a link to an effort we found to install docker
> swarm. However we have not checked it or identified if it is useful.

> * <https://rominirani.com/docker-swarm-tutorial-b67470cf8872>

E.Docker.Swarm.2: Google Compute Engine

> Develop a section that deploys a Docker Swarm cluster on Google Compute
> Engine. Note that this may actually be easier as docker and docker swarm
> are distributed with recent versions of ubuntu. Just in case we are
> providing a link to an effort we found to install docker swarm. However
> we have not checked it or identified if it is useful.

> * <https://rominirani.com/docker-swarm-on-google-compute-engine-364765b400ed>

E.SingleNodeHadoop:

> Setup a single node hadoop environment.

> This includes:

> 1. Create a Dockerfile that deploys hadoop in a container
> 2. Develop sample applications and tests to test your cluster. You can
>      use wordcount or similar.
>
> you will find a comprehensive installation instruction that sets up a
> hadoop cluster on a single node at
>
> * <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html>

E.MultiNodeHadoop:

> Setup a hadoop cluster in a distributed environment.

> This includes:

> 1. Create docker compose and Dockerfiles that deploys hadoop in kubernetes
> 2. Develop sample applications and tests to test your cluster. You can
>    use wordcount or similar.
>
> you will find a comprehensive installation instruction that sets up a
> hadoop cluster in a distributed environment at
>
> * <https://hadoop.apache.org/docs/r3.0.0/hadoop-project-dist/hadoop-common/ClusterSetup.html>
>
> You can use this set of
> instructions or identify other resources on the internet that allow the
> creation of a hadoop cluster on kubernetes. Alternatively you can use docker compose
> for this exercise.


E.SparkCluster: Documentation

> Develop a high quality section that installs a spark cluster in
> kubernetes. Test your deployment on minikube and also on Futuresystems
> echo.
>
> You may want to get inspired from the talk *Scalable Spark Deployment
> using Kubernetes*:
>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-1/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-2/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-3/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-4/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-5/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-6/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-7/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-8/>
> * <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-9/>
>
> Make sure you do not plagiarize.
