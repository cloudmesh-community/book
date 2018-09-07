Harp PageRank
=============

 

For this exercise you will implement PageRank on Harp framework.

Deliverables
------------

Zip your source code and output as username_harp-pagerank.zip. Please
submit this file to the Canvas Assignments page.

Evaluation
----------

The point total for this exercise is 6, where the distribution is as
follows:

-   Completeness of your code (5 points)

-   Correct output (1 point)

Prerequisites
-------------

From now on, you donot need the old VM. To avoid any conflict and
inconvenience, we have prepared a new VM (ubuntu 16.04) for you. The
link will be posted on canvas. All necessary tools/libaries such Maven,
JDK, Github, Hadoop 2.6.0, Harp are configured and ready for use.
Intellij is installed as well. You can also use your own VM. But you
will need to setup those tools/libraries by yourself. Some tutorials are
available at the harp website. Here this instruction is based on the
configurations in this new VM.

![Harp PageRank
Architecture](section/icloud/assignment/exercise7/p8){width="6cm"
height="8cm"}

HarpPageRank Implementation
---------------------------

Most of the code is completed for you and your task will be to perform
the **Compute PR** step in the above diagram. The code for this can be
found in **simplepagerank/PageRankMapper.java**

INPUT section/icloud/assignment/exercise7/computePartialPR.java

Compilation and Running
-----------------------

-   To make the modification to the code, you can use Intellij IDE or
    linux terminal. The source code is located at

    ``` {.bash language="bash"}
    /home/cc/Documents/harp/harp-tutorial-app/src/main/java/edu/iu/simplepagerank
    ```

-   To compile the code, type the following commands in terminal

    ``` {.bash language="bash"}
    $ cd $HARP_ROOT_DIR
    $ mvn clean package
    ```

-   If hadoop is not started, start hadoop by:

    ``` {.bash language="bash"}
    $ $HADOOP_HOME/sbin/start-dfs.sh
    $ $HADOOP_HOME/sbin/start-yarn.sh
    ```

    Then you can view the web UI at localhost:50070 and localhost:8088

-   We prepared the input dataset (input5K-2partitions) for you. Use the
    following command to put it to hdfs. Please note there is a \"dot\"
    at the end of the second command.

    ``` {.bash language="bash"}
    $ cd $HARP_ROOT_DIR/data/tutorial/simplepagerank
    $ hdfs dfs -put input5K-2partitions .
    ```

-   Run the program:

    ``` {.bash language="bash"}
    $ cd $HARP_ROOT_DIR
    $ hadoop jar harp-tutorial-app/target/harp-tutorial-app-1.0-SNAPSHOT.jar edu.iu.simplepagerank.HarpPageRank input5K-2partitions output5k 5000 10
    ```

    This will run PageRank against input2K-2partitions dataset. It has
    5000 URLs in total. The program will run 2 parallel map tasks for 10
    iterations. If you want to launch N map tasks, you need to divide
    the dataset into N partitions.

-   To get the output, perform the following commands to get the output
    to the Desktop. Then you can submit it to canvas.

    ``` {.bash language="bash"}
    $ hdfs dfs -get output5k /home/cc/Desktop
    ```
