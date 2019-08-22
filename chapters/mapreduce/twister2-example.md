# Twister2 Examples

Twister documentation lists several examples[@www-twister2-examples] that users can leverage to better understand the
Twister2 API's. Currently there are several Communication API examples and Task API examples available in the Twister2
documentation. In this section we will go through how an example can be executed with Twister2.

## Submitting a Job
In order to run an example users need to submit the example to Twister2 using the `twister` command. This command
is found inside the bin directory of the distribution.


Here is a description of the command

```bash
twister2 submit cluster job-type job-file-name job-class-name [job-args]
```

* submit is the command to execute
* cluster which resource manager to use, i.e. standalone, kubernetes, this should be the name of the configuration directory for that particular resource manager
* job-type at the moment we only support jar
* job-file-name the file path of the job file (the jar file)
* job-class-name name of the job class with a main method to execute

Here is an example command
```bash
./bin/twister2 submit standalone jar examples/libexamples-java.jar edu.iu.dsc.tws.examples.task.ExampleTaskMain -itr 80 -workers 4 -size 1000 -op "allgather" -stages 8,1
```

In this command, cluster is standalone and has program arguments.

For this exercise we are using the standlone mode to submit a job. However Twister2 does support Kubernetes, Mesos,
Slurm and Nomad resource schedulers if users want to submit jobs to larger cluster deployments.

## Batch WordCount Example


In this section we will run a batch word count example from Twister2. This example only uses communication layer and resource scheduling layer. The threads are managed by the user program.

The example code can be found in

`twister2/examples/src/java/edu/iu/dsc/tws/examples/basic/batch/wordcount/`

When we install Twister2, it will compile the examples. Lets go to the installation directory and run the example.

```bash
cd bazel-bin/scripts/package/twister2-dist/
./bin/twister2 submit standalone jar examples/libexamples-java.jar edu.iu.dsc.tws.examples.batch.wordcount.WordCountJob
```

This will run 4 executors with 8 tasks. So each executor will have two tasks. At the first phase, the 0-3 tasks running
in each executor will generate words and after they are finished, 5-8 tasks will consume those words and create a count.
