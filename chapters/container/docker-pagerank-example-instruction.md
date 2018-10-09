# Docker Pagerank :o:

:o: TODO the text is incomplete

Place holder for PageRank Example in the docker hadoop section, needs
to be merged to docker-hadoop.tex

## Use the automated script

We make the steps of compiling java source, archiving class files,
load input files and run the program into one single script. To
execute it with the input file:
PageRankDataGenerator/pagerank5000g50.input.0, using 5000 urls and 1
iteration:

```bash
$ cd /cloudmesh/pagerank
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

## Compile and run by hand

If one wants to generate the java class files and archive them as the
previous exercise, one could use the following code (which is actually
inside compileAndExecHadoopPageRank.sh)

```bash
export HADOOP_CLASSPATH=`$HADOOP_PREFIX/bin/hadoop classpath`
mkdir /cloudmesh/pagerank/dist
$ find /cloudmesh/pagerank/src/indiana/cgl/hadoop/pagerank/ \
   -name "*.java"|xargs  javac -classpath $HADOOP_CLASSPATH \
   -d /cloudmesh/pagerank/dist
$ cd /cloudmesh/pagerank/dist
$ jar -cvf HadoopPageRankMooc.jar -C . .
```

Load input files to HDFS

```bash
$ export PATH=$PATH:/$HADOOP_PREFIX/bin
$ cd /cloudmesh/pagerank/
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
