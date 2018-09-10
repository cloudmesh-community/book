# Using Kubernetes on FutureSystems

This section introduces you on how to use the Kubernetes cluster
on FutureSystems.  Currently we have deployed kubernetes on our
cluster called *echo*.


## Getting Access

You will need an account on FutureSystems and upload the ssh key to
the FutureSystems portal from the computer from which you want to
login to echo. To verify, if you have access try to see if you can log
into india.futuresystems.org. You need to be a member of a valid
FutureSystems project.

If you have verified that you have access to the india, you can now try
to login to the kubernetes cluster head node with the same username
and key:

At this time we ask you to use the following IP address to communicate
with echo via its head node:

    149.165.150.85

To login to echo use the command

    ssh FS_USERNAME@149.165.150.85

where FS_USERNAME is the username you have on futureSystems.

**NOTE: If you have access to india but not the kubernetes software, your 
project may not have been authorized to access the kubernetes cluster.
Send a ticket to FutureSystems ticket system to request this.**

Once you are logged in to the kubernetes cluster head node, try to run:

    kubectl get pods

This will let you know if you have access to kubernetes and verifies
if the kubectl command works for you. Naturally it will also list the pods.

## Example Use

The following command runs an image called nginx with two replicas:

    kubectl run nginx --replicas=2 --image=nginx --port=80

As a result of this one deployment was created, and two PODs are
created and started. To see the deployment, please use the command


    kubectl get deployment

This will result in the following output

    NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
    nginx     2         2         2            2           7m


To see the pods please use the command

    kubectl get pods

This will result in the following output

    NAME                   READY STATUS  RESTARTS AGE
    nginx-7587c6fdb6-4jnh6 1/1   Running 0        7m
    nginx-7587c6fdb6-pxpsz 1/1   Running 0        7m

If we want to see more detailed information we cn use the command

    kubectl get pods -o wide

```
NAME                   READY STATUS  RESTARTS AGE IP        NODE
nginx-75...-4jnh6 1/1   Running 0        8m  192.168.56.2   e003
nginx-75...-pxpsz 1/1   Running 0        8m  192.168.255.66 e005
```

Please note the IP address field. Now if we try to access the nginx
homepage with wget (or curl)


    wget 192.168.56.2

we see the following output:


    --2018-02-20 14:05:59--  http://192.168.56.2/
    Connecting to 192.168.56.2:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 612 [text/html]
    Saving to: 'index.html'
    
    index.html    100%[=========>]     612  --.-KB/s    in 0s
    
    2018-02-20 14:05:59 (38.9 MB/s) - 'index.html' saved [612/612]


It verifies that the specified image was running, and it is accessible
from within the cluster.

Next we need to start thinking about how we
access this web server from outside the cluster. We can explicitly
exposing the service with the following command

    kubectl expose deployment nginx --type=NodePort --name=999-nginx-ext

We will see the response

    service "nginx-external" exposed

To find the exposed ip addresses, we simply issue the command
    
    kubectl get svc

We se something like this

    NAME          TYPE      CLUSTER-IP    EXTERN PORT(S)      AGE
                                          AL-IP
    kubernetes    ClusterIP 10.96.0.1     <none> 443/TCP      8h
    999-nginx-ext NodePort  10.96.183.189 <none> 80:30275/TCP 6s

please note that we have given a unique name.

---

For IU students:

You could use your username or if you use one of our classes your
hid. The number part will typically be sufficient.  For class users
that do not use the hid in the name we will terminate all instances
without notification. In addition, we like you explicitly to add
"-ext" to every container that is exposed to the internet. Naturally
we want you to shut down such services if they are not in use. Failure
to do so may result in termination of the service without notice, and
in the worst case revocation of your privileges to use *echo*.

---

In our example you will find the port on which our service is exposed
and remapped to. We find the port **30275** in the value
**80:30275/TCP** in the ports column for the running container.

Now if we visit this URL, which is the public IP of the head node
followed by the exposed port number

    http://149.165.150.85:30275

you should see the 'Welcome to nginx' page.

## Exercises

E.kubernetes.fs.1:

> Explore more complex service examples.

E.kubernetes.fs.2:

> Explore constructing a complex web app with multiple services.

E.kubernetes.fs.3:

> Define a deployment with a yaml file declaratively.
