# Introduction to Mapreduce {#s-mapreduce}


In this section we discuss about the background of Mapreduce along
with Hadoop and core components of Hadoop.

We start out our section with a review of the python lambda expression
as well as the map function.  Understanding these concepts is helpful
for our overall understanding of map reduce.

So before you watch the video, we encourage you to learn Sections
{#s-python-lambda} and {#s-python-map}.

Now that you have a basic understanding of the map function we
recommend to watch our videos about mapreduce, hadoop and spark which
we provide within this chapter.

[:clapper: Map Reduce, Hadoop, and Spark (19:02) Hadoop A](https://drive.google.com/file/d/1CmtoDDio-CYT9g4bsjclVfukA5TsIc8n/view?usp=sharing)


MapReduce is a programming technique or processing capability which
operates in a cluster or a grid on a massive data set and brings out
reliable output. It works on essentially two main functions – map()
and reduce().  MapReduce processes large chunks of data so its highly
beneficial to operate in multi-threaded fashion meaning parallel
processing. MapReduce can also take advantage of data locality so that
we do not loose much on communication of data from place to another.

## MapReduce Algorithm

MapReduce can operate on a filesystem, which is an unstructured data
or a database, a structured data and these are the following three
stages of its operation:

1. Map – This method processes the very initial data set. Generally,
   the data is in file format which can be stored in HDFS (Hadoop File
   System). Map function reads the data line by line and creates
   several chunks of data and that is again stored in HDFS. This
   broken set of data is in key/value pairs. So in multi-threaded
   environment, there will be many worker nodes operating on the data
   using this map() function and write this intermediate data in form
   of key/value to temporary data storage.
2. Shuffle – In this stage, worker nodes will shuffle or redistribute
   the data in such a way that there is only one copy for each key.
3. Reduce – This function always comes at last and it works on the
   data produced by map and shuffle stages and produces even smaller
   chunk of data which is used to calculate output.(see
   +@fig:mapreduce_diagram)

![MAPREDUCE_DIAGRAM :o:](images/mapreduce_diagram.png){#fig:mapreduce_diagram}

          

 The Shuffle operation is very important here as that is mainly
responsible for reducing the communication cost.  The main advantage
of using MapReduce algorithm is that it becomes very easy to scale up
data processing just by adding some extra computing nodes. Building up
map and reduce methods are sometimes nontrivial but once done, scaling
up the applications is so easy that it is just a matter of changing
configuration. Scalability is really big advantage of MapReduce model.
In the traditional way of data processing, data was moved from nodes
to the master and then the processing happens in master machine. In
this approach, we lose bandwidth and time on moving data to master and
parallel operation cannot happen. Also master can get over-burdened
and fail.  In MapReduce approach, Master node distributes the data to
the slave machines which are in themselves a processing unit. So all
slaves process the data in parallel and the time taken to process the
data is reduced tremendously. (see +@fig:mapreduce_master_slave)

![MAPREDUCE_MATER_SLAVE :o:](images/mapreduce_master_slave.png){#fig:mapreduce_master_slave}

 


### MapReduce Example: Word Count

Let us understand MapReduce by an example. For example: we have a text
file as Sample.txt as Cat, Bear, Camel, Bird, Cat, Bird, Camel, Cat,
Bear, Camel, Cat, Camel

1. First we divide the input into four parts so that individual nodes
   can handle the load.
2. We tokenize each word and assign weightage of value “1” to each word.
3. This way we will have a list of key-value pairs with key being the
   word and value as 1.
4. After this mapping phase, shuffling phase starts where all maps
   with same key are sent corresponding reducer.
5. Now each reducer will have a unique key and a list of values for
   each key which in this case is all 1s.
6. After that, each reducer will count the total number of 1s and
   assigns final count to each word.
7. The final output is then written to a file. (see
   +@fig:mapreduce_wordcount)

![MAPREDUCE_WORDCOUNT :o:](images/mapreduce_wordcount.png){#fig:mapreduce_wordcount}

 

Let us see an example of map() and reduce() methods in code for this
word count example.

```java
public static class Map extends Mapper<LongWritable,
                                Text,
                                Text,
                                IntWritable> {
 
   public void map(LongWritable key,
                   Text value,
                   Context context)
                   throws IOException,InterruptedException {
 
       String line = value.toString();
       StringTokenizer tokenizer = new StringTokenizer(line);
       while (tokenizer.hasMoreTokens()) {
           value.set(tokenizer.nextToken());
           context.write(value, new IntWritable(1));
       }
}           
```

Here we have created a class Map which extends Mapper from MapReduce
framework and we override map() method to declare the key/value pairs.
Next, there will be a reduce method defined inside Reduce class as
below and both input and output here is a key/value pairs:

```java
public static class Reduce extends Reducer<Text,
                                   IntWritable,
                                   Text,IntWritable> {
 
   public void reduce(Text key,
                      Iterable<IntWritable> values,
                      Context context)
     throws IOException,InterruptedException {
 
         int sum=0;
         for(IntWritable x: values) {
            sum+=x.get();
         }
         context.write(key, new IntWritable(sum));
    }
}

```

## Hadoop MapReduce and Hadoop Spark

In earlier version of Hadoop, we could use MapReduce with HDFS
directly but from 2.0 onwards, YARN(Cluster Resource Management) is
introduced which acts as a layer between MapReduce and HDFS and using
this YARN, many other BigData frameworks can connect to HDFS as
well. (see +@fig:mapreduce_hadoop_spark)

![MAPREDUCE_HADOOP_SPARK :o:](images/mapreduce_hadoop_spark.png){#fig:mapreduce_hadoop_spark}
 

There are many big data frameworks available and there is always a
question as to which one is the right one. Leading frameworks are
Hadoop MapReduce and Apache Spark and choice depends on business
needs.  Let us start comparing both of these frameworks with respect
to their processing capability.

### Apache Spark  

Apache Spark is lightning fast cluster computing framework. Spark is
in-memory system. Spark is 100 time faster than Hadoop MapReduce.

### Hadoop MapReduce

Hadoop MapReduce reads and writes on disk because of this it is a slow
system and that affects the volume of data been processed. But Hadoop
is a scalable and fault tolerant, it us good for linear processing.

### Key Differences

1. Speed Spark is lightning fast cluster computing framework and
   operates up to 100 time faster in-memory and 10 times faster than
   Hadoop on disk. In-memory processing reduces the disk read/write
   processes which are time consuming.
2. Complexity Spark is easy to use since there are many APIs available
   but for Hadoop, developers need to code the functions which makes
   it harder.
3. Application Management Spark can perform batch processing,
   interactive and Machine Learning and Streaming of data, all in the
   same cluster, which makes it a complete framework for data analysis
   whereas Hadoop is just a batch engine and it requires other
   frameworks for other tasks which makes it somewhat difficult to
   manage.
4. Real-Time Data Analysis Spark is capable of processing real time
   data with great efficiency. But Hadoop was designed primarily for
   batch processing so it cannot live data.
5. Fault Tolerance Both the systems are fault tolerant so there is no
   need to restart the applications from scratch.

