# Apache OpenWhisk {#s-openwhisk}

Apache OpenWhisk is a Function as a Service (FaaS), aka Serverless computing, platform used to execute code in response of an events via triggers by managing the infrastructure, servers and scaling. The advantage of OpenWhisk over traditional long-running VM or container approach is that there is lack of resiliency-related overhead in OpenWhisk. OpenWhisk is inherently scalable since the actions are executed on demand. OpenWhisk also helps the developers to focus only on coding by taking care of infrastructure-related tasks like monitoring and patching.

The developers provide the code written in the desired programming language for the desired action and this code will be executed in response to the events. The *triggering* can be invoked using HTTP requests or external feeds. The events invoking the triggers ranges from database modification to new variables in IoT sensors. Actions that response to these events could also range from a Python code snippet to a binary code in a container and it is as well possible to chain the actions. Note that these actions are deployed and executed instantaneously and can be invoked not only by triggers but also using the OpenWhisk API or CLI.

## OpenWhisk Workflow

OpenWhisk uses Nginx, Kafka, Docker and CouchDB as internal components. To understand the role of each of these components, let's review an action invocation trace in the system. Remember the main outcome of OpenWhisk (or Serverless architecture in general) is to execute the user's code inside the system and return the result. The workflow of the OpenWhisk is illustrated in the figure +@fig:openwhisk-workflow

![OpenWhisk workFlow](images/openwhisk_workflow.png){#fig:openwhisk-workflow}

We will review the role of each components in the OpenWhisk workflow.

### The Action and Nginx

As mentioned prior, the action is the response of the OpenWhisk to triggers. Consider the following JavaScript function:
``` Javascript
function main() {
    return { hello: 'world' };
}
```
This is the Hello World example of the OpenWhisk action where the action returns a JSON object with the key `hello` which has a value of `world`.  After saving this function in a `.js` file, e.g. `action.js` then the action could be created using the following command:
```bash
$ wsk action create HelloAction action.js
```
Then, the `HelloAction` can be invoked using:
```bash
$ wsk action invoke HelloAction --result
```
The `wsk` command is what is known as OpenWhisk CLI, which we will show how to install in the next sections.  Note that OpenWhisk's API is RESTful and fully HTTP based. In other words, the above-mentioned `wsk action` command  is basically a HTTP request equivalent to the following:
```
POST /api/v1/namespaces/$userNamespace/actions/HelloAction
Host: $openwhiskEndpoint
```
The `userNamespace` variable defines the namespace in which the `HelloAction` is put into. Accordingly, nginx is the entering point of the OpenWhisk system and it plays an important role as a HTTP server as well as a reverse proxy server, mainly used for SSL termination and HTTP request  forwarding.
### Controller: The System's Interface
We learned that nginx does not do any processing on the HTTP request except decrypting it (SSL Termination). The main processing of the request starts in the Controller. The controller plays the role of the interface for user both for actions and Create, Read, Update, and Delete (CRUD) requests, translating the user's POST request to action invocation. The controller has an essential role in OpenWhisk workflow and its role is not finished here and is partially involved in next steps as well.

### CouchDB

Naturally some notion of authentication is essentially required for the system. This authentication is performed by the Controller via CouchDB. The CouchDB instance has a specific database, namely `subjects` which contains the credentials and corresponding privileges. The credentials that corresponds to a request are verified against the `subjects` database and if the user's privileges satisfies the permissions required for the requested `HelloAction`, the action will be invoked. In our example, we are assuming that the `HelloAction` is in a namespace owned by the user, meaning that the user has the required permission to invoke the action.

After authentication and authorization using the `subjects` database, the record for the action `HelloAction` is load from `whisks` database. This record contains the code, the parameters consist of default parameters merged with user parameters, as well as the resource limits, e.g. maximum memory. The `HelloAction` record in `whisk` contains its code (listed above) and no parameters as the code does not get any parameters.

### Load Balancer

Next comes the load balancer which is technically part of the controller and it is load balancer's responsibility to check the health status of the executors, known as `Invokers`, continuously. Load balancer is aware of the available invokers and select them for the actions accordingly.

### Kafka

For a request user sends, there are two scenarios where things can go bad:

* Invocation is lost due to a crash
* Invocation has to wait for invokers to be available

Both of this scenarios can be handled with Kafka distributed messaging system. The action invocation mechanism with Kafka is as follows:

The controller "publishes" a message to Kafka. This message contains the required action and corresponding parameters and is addressed to an Invoker chosen by the controller. Kafka responds to the HTTP request of the user with an `ActivationId` which could be used later by the user to get the result. OpenWhisk supports both synchronous and asynchronous invocation models. In the former model, the user's HTTP request is terminated as the system accepts it. The latter model, known as blocking invocation, is otherwise.

### Invoker

As the heart of the OpenWhisk, the Invoker's responsibility is to invoke the action. Invoker is implemented in Scala but it uses Docker for a safe and isolated execution. For each invoked actions, a container is spawned and the code as well as the parameters are passed to it. As soon as the result is obtained, the container is terminated.

The ` Action` example is a node.js action and therefore the invoker will start a node.js container, inject our above-mentioned code to it, runs the code and gets the results, save the logs and terminates the node.js container.
### CouchDB again
The result of the Invoker is saved in another database in CouchDB, namely `activations`, under same ActivationId that was sent back to the user. The result of the `HelloAction` example containing the log in JSON format, would look like this:

```json
{
   "activationId": "31809ddca6f64cfc9de2937ebd44fbb9",
   "response": {
       "statusCode": 0,
       "result": {
           "hello": "world"
       }
   },
   "end": 1474459415621,
   "logs": [
       "2016-09-21T12:03:35.619234386Z stdout: Hello World"
   ],
   "start": 1474459415595,
}
```
Similar to the same API call used for submitting the action, we can use OpenWhisk's API to retrieve the result using the ActivationId:
```bash
wsk activation get 31809ddca6f64cfc9de2937ebd44fbb9
```

## Setting Up OpenWhisk Locally

There are several approaches to starting the OpenWhisk platform:

* Directly running the service
* Running using Kubernetes and Mesos
* Running with Vagrant using a pre-configured VM

But an easier approach is using [OpenWhisk Devtools](https://github.com/apache/incubator-openwhisk-devtools) which is purposed for local development and testing of OpenWhisk. Using OpenWhisk Devtools, you can quickly start OpenWhisk on any machine using `docker compose`. Accordingly, make sure the `docker compose` is already installed on your machine. Then to start the platform, clone the OpenWhisk Devtools and navigate to its folder, then:

```bash
$ cd docker-compose
$ make quick-start
```

Make sure you do not have any services running on the following ports otherwise the docker compose will fail starting some of the containers:

* 5984 for CouchDB
* 2181, 2888, 3888 for Zookeeper
* 9092 for Kafka
* 8888, 2551 for the Controller
* 8085 for the Invoker
* 9001 for Minio
* 6379 for Redis
* 8080, 443, 9000, 9090 for apigateway
* 8001 Kafka-UI

In case you have services running on any of the ports above, you can either stop the local services that are using these ports or alternatively you can modify the `docker-compose.yml` and change the source port number in the port number mapping. The latter option is, however, more tricky because you have to make sure the change does not affect the communication between the containers. For instance if you have `Apache` service running on Port 80, then open `docker-compose.yml`, search for the keyword `80:` to find the port mapping with source port of 80:
```bash
ports:
  - "80:80"
```
then change it to another port:
```bash
ports:
  - "8080:80"
```
After that, you should be able to run `make quick-start` successfully and then you can check the status of the running docker containers using:

```bash
$ docker ps --format "{{.ID}}: {{.Names}} {{.Image}}"
16e7746c4af1: wsk0_9_prewarm_nodejs6 openwhisk/nodejs6action:latest
dd3c4c2d4947: wsk0_8_prewarm_nodejs6 openwhisk/nodejs6action:latest
6233ae715cf7: openwhisk_apigateway_1 openwhisk/apigateway:latest
3ac0938aecdd: openwhisk_controller_1 openwhisk/controller
e1bb7272a3fa: openwhisk_kafka-topics-ui_1 landoop/kafka-topics-ui:0.9.3
6b2408474282: openwhisk_kafka-rest_1 confluentinc/cp-kafka-rest:3.3.1
9bab823a891b: openwhisk_invoker_1 openwhisk/invoker
98ebd5b4d605: openwhisk_kafka_1 wurstmeister/kafka:0.11.0.1
65a3b2a7914f: openwhisk_zookeeper_1 zookeeper:3.4
9b817a6d2c40: openwhisk_redis_1 redis:2.8
e733881d0004: openwhisk_db_1 apache/couchdb:2.1
6084aec44f03: openwhisk_minio_1 minio/minio:RELEASE.2018-07-13T00-09-07Z
```
Note that 12 containers should be up and running:
```bash
$ docker ps --format "{{.ID}}: {{.Names}} {{.Image}} | wc -l"
12
```

### Debugging quick-start

It is always possible that something goes wrong in the process of deploying the 12 dockers. If the `make quick-start` process stuck at some point, the best way to find the issue is to use the `docker ps -a` command to check which of the containers is causing the issue. Then you can try to fix the issue of that container separately. This fix could possibly happen in `docker-compose.yml` file. For instance, there was some issue with the `openwhisk/controller` docker at some point and it turns out the issue was the following line in the `docker-compose.yml`:

```bash
command: /bin/sh -c "exec /init.sh --id 0 >> /logs/controller-local_logs.log 2>&1"
```
this line is indicating that the following command should be run after the container is started:
```bash
$ /init.sh --id 0 >> /logs/controller-local_logs.log 2>&1
```
However, starting another instance of the docker image with this command outputted a `Permission Denied` error which could be fixed either by changing the logs folder permission in the docker image or container (followed by a commit) or saving the log file in another folder. In this case replacing that line with the following line would temporarily fix the issue:
```bash
command: /bin/sh -c "exec /init.sh --id 0 >> /home/owuser/controller-local_logs.log 2>&1"
```

## "Hello World" in OpenWhisk

OpenWhisk provides a command line tool called [openwhisk-cli](https://github.com/apache/incubator-openwhisk-cli) which is used for controlling the platform. As part of the `make quick-start` command that we used above for starting the platform, the account credentials will automatically be written into the configuration of the CLI. You can either install the CLI directly from the repository or install it using `linuxbrew`. Alternatively, use the binary available in this path in OpenWhisk Devtools folder:

`[PATH_TO_DEVTOOLS]/docker-compose/openwhisk-src/bin/wsk`

Running the `wsk` without any command or flag, will print its help:

```bash
~/incubator-openwhisk-devtools/docker-compose/openwhisk-src/bin$ ./wsk

        ____      ___                   _    _ _     _     _
       /\   \    / _ \ _ __   ___ _ __ | |  | | |__ (_)___| | __
  /\  /__\   \  | | | | '_ \ / _ \ '_ \| |  | | '_ \| / __| |/ /
 /  \____ \  /  | |_| | |_) |  __/ | | | |/\| | | | | \__ \   <
 \   \  /  \/    \___/| .__/ \___|_| |_|__/\__|_| |_|_|___/_|\_\
  \___\/ tm           |_|

Usage:
  wsk [command]

Available Commands:
  action      work with actions
  activation  work with activations
  package     work with packages
  rule        work with rules
  trigger     work with triggers
  sdk         work with the sdk
  property    work with whisk properties
  namespace   work with namespaces
  list        list entities in the current namespace
  api         work with APIs
```
For instance, you can get the host address using:

```bash
$ wsk property get | grep host
whisk API host		192.168.2.2
```
You can then re-invoke the built-in `Hello World` example using:
```bash
~/incubator-openwhisk-devtools/docker-compose$ make hello-world
creating the hello.js function ...
invoking the hello-world function ...
adding the function to whisk ...
ok: created action hello
invoking the function ...
invocation result: { "payload": "Hello, World!" }
{ "payload": "Hello, World!" }
creating an API from the hello function ...
ok: updated action hello
invoking:  http://192.168.2.2:9090/api/23bc46b1-71f6-4ed5-8c54-816aa4f8c502/hello/world
  "payload": "Hello, World!"
ok: APIs
Action          Verb  API Name  URL
/guest/hello     get    /hello  http://192.168.2.2:9090/api/23bc46b1-71f6-4ed5-8c54-816aa4f8c502/hello/world
deleting the API ...
ok: deleted API /hello
deleting the function ...
ok: deleted action hello
```

## Creating a custom action

We already invoked the built-in hello world action. Now, we try to build a new custom action. First create a file called `greeter.js`:
```js
function main(input) {
   return {payload:  'Hello, ' + input.user.name + ' from ' + input.user.location + '!'};
}
```
Now we can create an action called `greeter` using the `greeter.js`:
```bash
$ wsk -i action create greeter greeter.js
ok: created action greeter
```
Note that the `-i` option is to prevent the following error:
```bash
$ wsk action create greeter greeter.js
error: Unable to create action 'summer': Put https://192.168.2.2/api/v1/namespaces/guest/actions/summer?overwrite=false: x509: cannot validate certificate for 192.168.2.2 because it doesn't contain any IP SANs
Run 'wsk --help' for usage.
```
Afterwards you can get the list of actions to make sure your desired action is created:
```bash
$ wsk -i action list
actions
/guest/greeter                            private nodejs:6
```
Afterwards, we can invoke the action by passing a `json` parameter including a name and location and receive the result:

```bash
$ wsk -i action invoke -r greeter -p user '{"name": "Vafa", "location": "Indiana"}'
{
    "payload": "Hello Vafa from Indiana!"
}

```
Now we can retrieve the list of activation records:

```bash
$ wsk activation list -i
activations
976a7d02dab7460eaa7d02dab7760e9a greeter
02e0e12118af43b0a0e12118afd3b038 hello
10c2cddb0d2c4c1f82cddb0d2c1c1feb hello
```
The result of the command above is showing that the `hello` action has been invoked twice and the `greeter` action was invoked once. You can get more information about each of the activation using the `wsk -i activation get [ACTIVATION_ID]`:
```bash
$ wsk -i activation get 976a7d02dab7460eaa7d02dab7760e9a
ok: got activation 976a7d02dab7460eaa7d02dab7760e9a
{
    "namespace": "guest",
    "name": "greeter",
    "version": "0.0.1",
    "subject": "guest",
    "activationId": "976a7d02dab7460eaa7d02dab7760e9a",
    "start": 1539980284774,
    "end": 1539980284886,
    "duration": 112,
    "response": {
        "status": "success",
        "statusCode": 0,
        "success": true,
        "result": {
            "payload": "Hello Vafa from Indiana!"
        }
    },
  ...
```

Finally, after you are finished using the OpenWhisk Devtools, you can stop platform using:
```bash
~/incubator-openwhisk-devtools/docker-compose$ make destroy
Stopping openwhisk_apigateway_1      ... done
Stopping openwhisk_controller_1      ... done
Stopping openwhisk_kafka-topics-ui_1 ... done
Stopping openwhisk_kafka-rest_1      ... done
Stopping openwhisk_invoker_1         ... done
Stopping openwhisk_kafka_1           ... done
Stopping openwhisk_zookeeper_1       ... done
Stopping openwhisk_redis_1           ... done
Stopping openwhisk_db_1              ... done
Stopping openwhisk_minio_1           ... done
...
```
