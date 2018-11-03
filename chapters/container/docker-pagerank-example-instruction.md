# Docker Pagerank

PageRank is a popular example algorithm used to display the ability of big data applications to run parallel tasks. This
example will show how the docker hadoop image can be used to execute the Pagerank example which is available in
 `/cloudmesh/examples/pagerank`

## Use the automated script

We make the steps of compiling java source, archiving class files,
load input files and run the program into one single script. To
execute it with the input file:
PageRankDataGenerator/pagerank5000g50.input.0, using 5000 urls and 1
iteration:

```bash
$ cd /cloudmesh/examples/pagerank
$ ./compileAndExecHadoopPageRank.sh PageRankDataGenerator/pagerank5000g50.input.0 5000 1
```

Result will look like

```bash
output.pagerank/part-r-00000
```

The head of the result will look like 

```bash
head output.pagerank/part-r-00000
```
```bash
0	2.9999999999999997E-5
1	2.9999999999999997E-5
2	2.9999999999999997E-5
3	2.9999999999999997E-5
4	2.9999999999999997E-5
5	2.9999999999999997E-5
6	2.9999999999999997E-5
7	2.9999999999999997E-5
8	2.9999999999999997E-5
9	2.9999999999999997E-5
```
## Compile and run by hand

If one wants to generate the java class files and archive them as the
previous exercise, one could use the following code (which is actually
inside compileAndExecHadoopPageRank.sh)

```bash
export HADOOP_CLASSPATH=`$HADOOP_PREFIX/bin/hadoop classpath`
mkdir /cloudmesh/examples/pagerank/dist
$ find /cloudmesh/examples/pagerank/src/indiana/cgl/hadoop/pagerank/ \
   -name "*.java"|xargs  javac -classpath $HADOOP_CLASSPATH \
   -d /cloudmesh/examples/pagerank/dist
$ cd /cloudmesh/examples/pagerank/dist
$ jar -cvf HadoopPageRankMooc.jar -C . .
```

Load input files to HDFS

```bash
$ export PATH=$PATH:/$HADOOP_PREFIX/bin
$ cd /cloudmesh/examples/pagerank/
$ hadoop fs -mkdir input.pagerank
$ hadoop fs -put PageRankDataGenerator/pagerank5000g50.input.0 input.pagerank
```

* Run program with the [PageRank Inputs File Directory][PageRank Output Directory][Number of Urls][Number Of Iterations]

```bash
$ hadoop jar dist/HadoopPageRankMooc.jar indiana.cgl.hadoop.pagerank.HadoopPageRank input.pagerank output.pagerank 5000 1
```
        
Result

```bash
$ hadoop fs -cat output.pagerank/part-r-00000
```		
