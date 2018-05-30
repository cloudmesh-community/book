# QuickStart to PageRank

This assignment provides a PageRank tutorial running on Docker Hadoop. 

## Description
	  
PageRank calculates a numerical value for each element of a hyperlinked set of
webpages, which reflects the probability that a random surfer will access that
page. The process of PageRank can be understood as a Markov Chain which
requires iterative calculations to converge. An iteration of PageRank
calculates the new access probability for each webpage based on values
calculated in the previous iteration. The process will repeat until the number
of current iterations is bigger than predefined maximum iterations, or the
Euclidian distance between rank values in two subsequent iterations is less
than a predefined threshold that controls the accuracy of the output results.

## Docker Run

`sudo docker run -it lee212/e222:pagerank /etc/bootstrap.sh -bash`

Note that it may take several minutes for the first time, 1) to download docker image, and 2) to start hadoop components.

Example output message during this step is like:

### Docker Image Download
```
Unable to find image 'lee212/e222:pagerank' locally
latest: Pulling from lee212/e222
b253335dcf03: Pull complete
a3ed95caeb02: Pull complete
69623ef05416: Pull complete
77c1cad6eb69: Pull complete
...
ed6629089518: Extracting [==================================================>]  1.875kB/1.875kB
36a49c5cc0d9: Download complete
ed6629089518: Extracting [==================================================>]  1.875kB/1.875kB
ed6629089518: Pull complete
36a49c5cc0d9: Pull complete
e6a7899cd72b: Pull complete
ad5d02f614c9: Pull complete
66900b7f4ab7: Pull complete
Digest: sha256:1a13cf4a98a22ecf26d35787ed5a50fc420e8051bd7e90780d8588165151627d
Status: Downloaded newer image for lee212/e222:pagerank
```

### Hadoop Start
```
/
Starting sshd:                                             [  OK  ]
Starting namenodes on [2a9a1710278c]
2a9a1710278c: starting namenode, logging to /usr/local/hadoop/logs/hadoop-root-namenode-2a9a1710278c.out
localhost: starting datanode, logging to /usr/local/hadoop/logs/hadoop-root-datanode-2a9a1710278c.out
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop/logs/hadoop-root-secondarynamenode-2a9a1710278c.out
starting yarn daemons
starting resourcemanager, logging to /usr/local/hadoop/logs/yarn--resourcemanager-2a9a1710278c.out
localhost: starting nodemanager, logging to /usr/local/hadoop/logs/yarn-root-nodemanager-2a9a1710278c.out
```

## Run PageRank

The script is provided which uploads an input file to HDFS and runs Hadoop with PageRank (jar) program.

```
cd /cloudmesh/pagerank
./compileAndExecHadoopPageRank.sh PageRankDataGenerator/pagerank5000g50.input.0 5000 1
```

### Sample Output

```
*********************************************
*           Hadoop PageRank                 *
*********************************************
Hadoop CreateGraph starts...

18/03/12 12:00:45 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
18/03/12 12:00:46 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
18/03/12 12:00:46 INFO input.FileInputFormat: Total input paths to process : 1
18/03/12 12:00:47 INFO mapreduce.JobSubmitter: number of splits:1
18/03/12 12:00:47 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1520870421399_0001
18/03/12 12:00:48 INFO impl.YarnClientImpl: Submitted application application_1520870421399_0001
18/03/12 12:00:48 INFO mapreduce.Job: The url to track the job: http://2a9a1710278c:8088/proxy/application_1520870421399_0001/
18/03/12 12:00:48 INFO mapreduce.Job: Running job: job_1520870421399_0001
18/03/12 12:00:54 INFO mapreduce.Job: Job job_1520870421399_0001 running in uber mode : false
18/03/12 12:00:54 INFO mapreduce.Job:  map 0% reduce 0%
18/03/12 12:00:58 INFO mapreduce.Job:  map 100% reduce 0%
18/03/12 12:01:04 INFO mapreduce.Job:  map 100% reduce 100%
18/03/12 12:01:06 INFO mapreduce.Job: Job job_1520870421399_0001 completed successfully
18/03/12 12:01:06 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=145879
                FILE: Number of bytes written=521589
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=84861
                HDFS: Number of bytes written=119747
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=1
                Launched reduce tasks=1
                Data-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=2313
                Total time spent by all reduces in occupied slots (ms)=3130
                Total time spent by all map tasks (ms)=2313
                Total time spent by all reduce tasks (ms)=3130
                Total vcore-seconds taken by all map tasks=2313
                Total vcore-seconds taken by all reduce tasks=3130
                Total megabyte-seconds taken by all map tasks=2368512
                Total megabyte-seconds taken by all reduce tasks=3205120
        Map-Reduce Framework
                Map input records=5000
                Map output records=5000
                Map output bytes=135865
                Map output materialized bytes=145879
                Input split bytes=114
                Combine input records=0
                Combine output records=0
                Reduce input groups=5000
                Reduce shuffle bytes=145879
                Reduce input records=5000
                Reduce output records=5000
                Spilled Records=10000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=34
                CPU time spent (ms)=2800
                Physical memory (bytes) snapshot=442843136
                Virtual memory (bytes) snapshot=1502584832
                Total committed heap usage (bytes)=402653184
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=84747
        File Output Format Counters
                Bytes Written=119747
Hadoop PageRank starts...

Hadoop PageRank iteration 0...

18/03/12 12:01:06 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
18/03/12 12:01:06 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
18/03/12 12:01:06 INFO input.FileInputFormat: Total input paths to process : 1
18/03/12 12:01:07 INFO mapreduce.JobSubmitter: number of splits:1
18/03/12 12:01:07 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1520870421399_0002
18/03/12 12:01:07 INFO impl.YarnClientImpl: Submitted application application_1520870421399_0002
18/03/12 12:01:07 INFO mapreduce.Job: The url to track the job: http://2a9a1710278c:8088/proxy/application_1520870421399_0002/
18/03/12 12:01:07 INFO mapreduce.Job: Running job: job_1520870421399_0002
18/03/12 12:01:14 INFO mapreduce.Job: Job job_1520870421399_0002 running in uber mode : false
18/03/12 12:01:14 INFO mapreduce.Job:  map 0% reduce 0%
18/03/12 12:01:24 INFO mapreduce.Job:  map 67% reduce 0%
18/03/12 12:01:27 INFO mapreduce.Job:  map 100% reduce 0%
18/03/12 12:01:37 INFO mapreduce.Job:  map 100% reduce 100%
18/03/12 12:01:39 INFO mapreduce.Job: Job job_1520870421399_0002 completed successfully
18/03/12 12:01:39 INFO mapreduce.Job: Counters: 49
        File System Counters
                FILE: Number of bytes read=113840018
                FILE: Number of bytes written=170989795
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=119861
                HDFS: Number of bytes written=133890
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=1
                Launched reduce tasks=1
                Data-local map tasks=1
                Total time spent by all maps in occupied slots (ms)=11041
                Total time spent by all reduces in occupied slots (ms)=5883
                Total time spent by all map tasks (ms)=11041
                Total time spent by all reduce tasks (ms)=5883
                Total vcore-seconds taken by all map tasks=11041
                Total vcore-seconds taken by all reduce tasks=5883
                Total megabyte-seconds taken by all map tasks=11305984
                Total megabyte-seconds taken by all reduce tasks=6024192
        Map-Reduce Framework
                Map input records=5000
                Map output records=3350000
                Map output bytes=50220000
                Map output materialized bytes=56920006
                Input split bytes=114
                Combine input records=0
                Combine output records=0
                Reduce input groups=5000
                Reduce shuffle bytes=56920006
                Reduce input records=3350000
                Reduce output records=5000
                Spilled Records=10050000
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=320
                CPU time spent (ms)=16540
                Physical memory (bytes) snapshot=457768960
                Virtual memory (bytes) snapshot=1530519552
                Total committed heap usage (bytes)=411041792
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=119747
        File Output Format Counters
                Bytes Written=133890
Hadoop CleanUptResults starts...

18/03/12 12:01:39 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
18/03/12 12:01:39 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
18/03/12 12:01:39 INFO input.FileInputFormat: Total input paths to process : 1
18/03/12 12:01:40 INFO mapreduce.JobSubmitter: number of splits:1
18/03/12 12:01:40 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1520870421399_0003
18/03/12 12:01:40 INFO impl.YarnClientImpl: Submitted application application_1520870421399_0003
18/03/12 12:01:40 INFO mapreduce.Job: The url to track the job: http://2a9a1710278c:8088/proxy/application_1520870421399_0003/
########################################################
#   Hadoop PageRank Job take 76.28 sec.
########################################################
```

## Result 

The script also downloaded result files from HDFS to your local directory.
```
head output.pagerank/part-r-00000
0       2.9999999999999997E-5
1       2.9999999999999997E-5
2       2.9999999999999997E-5
3       2.9999999999999997E-5
4       2.9999999999999997E-5
```
