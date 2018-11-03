#!/bin/bash

if [ $# -ne 3 ]; then
    echo 1>&2 Usage: [PageRank Inputs File Directory][Number of Urls][Number Of Iterations]
    echo "e.g. ./compileAndExecHadoopPageRank.sh PageRankDataGenerator/pagerank5000g50.input.0 5000 1"
    exit -1
fi

if [ -f dist/HadoopPageRankMooc.jar ]
then
    echo "jar is reaty to run a program!"
else
    echo "jar not found, compling now!"
    export HADOOP_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`
	mkdir /cloudmesh/examples/pagerank/dist
	find /cloudmesh/examples/pagerank/src/indiana/cgl/hadoop/pagerank/ -name "*.java"|xargs  javac -classpath $HADOOP_CLASSPATH -d /cloudmesh/examples/pagerank/dist
	cd dist
	jar -cvf HadoopPageRankMooc.jar -C . .
	cd ..
fi

# run pageRank

export PATH=$PATH:/$HADOOP_HOME/bin
hadoop fs -mkdir input.pagerank
hadoop fs -put $1 input.pagerank
hadoop jar dist/HadoopPageRankMooc.jar indiana.cgl.hadoop.pagerank.HadoopPageRank input.pagerank output.pagerank $2 $3

# capture the standard output
rm -rf output.pagerank
hadoop fs -get output.pagerank .

echo "PageRank Finished execution, see results in output.pagerank/ directory."
