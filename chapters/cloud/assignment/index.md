Assignments :o:
===========

Assignment 0 - Identify Technologies
------------------------------------

Assignment 0 will require you to identify the different software
tools/technologies included in the given attachment and then group them
into the correct layer of categories as indicated on the left-hand side
of the slide.

This homework is worth 5 points.

-   pptx \<files/assignment\_0.pptx\>

Project 1
---------

You will need to complete the source code and write a report. Zip your
work into a file with the name username\_project1.zip (replace
'username' with your Group Contact member's username) and submit the
following:

-   Complete source code

-   

    A document with the following details:

    :   -   Transformation of data during the computations, i.e. data
            type of key, value

        -   The data structure used to transfer between Map and Reduce
            phases

        -   How the data flow happens through disk and memory during the
            computation

Only one submission per group is required for Project 1. It is due time
at 11:59 pm on Feburary 5.

-   Project 1 \<files/project1.pdf\>

-   Input Data \<files/project1\_input\_data.txt\>

Project 2
---------

You are required to turn in the following items in a zip file
(username\_HadoopPageRank.zip) in this assignment:

-   The source code of Hadoop PageRank you implemented.

-   

    Technical report (username\_HadoopPageRank\_report.docx) that contains:

    :   -   The description of the main steps and data flow in your
            program.

        -   The output file (username\_HadoopPageRank\_output.txt) which
            contains the first 10 urls along with their ranks.

-   Project 2 \<files/project2.pdf\>

Project 3
---------

Project 3 asks you to implement a bioinformatics application using
Hadoop (Map only) MapReduce framework and write a report about the data
flow and your observations of the program.

You are required to turn in the following items in a zip file
(username\_HadoopBlast.zip) in this assignment:

-   The source code of Hadoop Blast you implemented.

-   Technical report (username \_HadoopBlast\_report.docx) that answers
    the following questions. - What is Hadoop Distributed Cache and how
    is it used in this program? - Write the two lines that put and get
    values from Distributed cache. Also include the method and class
    information. - In previous projects we used Hadoop's TextInputFormat
    to feed in the file splits line by line to map tasks. In this
    program, however, we want to feed in a whole file to a single map
    task. What is the technique used to achieve this? Also, briefly
    explain what are the key and value pairs you receive as input to a
    map task and what methods are responsible for producing these
    pairs? - Do you think this particular implementation will work if
    the input files are larger than the default HDFS block size? Briefly
    explain why. \[Hint: you can test what will happen by concatenating
    the same input file multiple times to create a larger input file in
    the resources/blast\_input folder\] - If you wanted to extend this
    program such that all output files will be concatenated into a
    single file, what key and value pairs would you need to emit from
    the map task? Also, how would you use these in the reduce that you
    would need to add?

-   The 4 output FASTA files -- celllines\_1.fa to celllines\_4.fa.

Points will be reduced (maximum 0.5 points) if the filename or directory
structure are different from instructed above.

The point total for this project is 3, where the distribution is as
follows:

-   Completeness of your code and output (1 points)

-   Correctness of written report (2 points)

-   Project 3 \<files/project3.pdf\>

Project 4
---------

Zip your source code and report in a file named username\_project4.zip

The point total for this project is 1.5, where the distribution is as
follows:

-   Correctness of your code and output (1 points)

-   Completeness of written report (0.5 points)

Before you start this project, you need to complete the Project4
Prerequisite\<files/project4\_pre.pdf\> first. The submission folder for
it will be published before the lab session.

-   Project 4 \<files/project4.pdf\>

-   Project 4 Prerequisite \<files/project4\_pre.pdf\>

Project 5
---------

Write an HBase FreqIndexBuilder program to build an inverted index table
which has the unique term's occurrences in all documents from the
clueWeb09 dataset. Zip your source code, results and report in a file
named username\_project5.zip. Submit this file to the Canvas submission
page.

-   Complete source code

-   A written report describing the main steps

The point total for this project is 3, where the distribution is as
follows:

-   Completeness of your code and output (2 points)

-   Correctness of written report (1 points)

-   Project 5 \<files/project5.pdf\>

Project 6
---------

After having familiarized yourself with the "HBase Building an Inverted
Index" homework and "PageRank algorithms" homework, you are ready to use
these applications to test the search engine function from the packaged
executable.

### Deliverables

Zip your source code, library, and results in a file named
[](mailto:username@test-search-engine.zip). Please submit this file to
the Canvas Assignments page.

### Evaluation

The point total for this project is 6, where the distribution is as
follows:

-   Completeness of your code (5 points)

-   Correct output (1 points)

-   Project 6 \<files/project6.pdf\>

Project 7
---------

The goal of this project is to familiarize yourself with the concept of
map-collective applications. Harp is similar to MapReduce in terms of
programming with the exception that it provides collective communication
support across map tasks.

Zip your source code and output as username\_harp-pagerank.zip. Please
submit this file to the Assignments page.

The point total for this project is 6, where the distribution is as
follows:

-   Completeness of your code (5 points)

-   Correct output (1 point)

We prepared a new VM for project7 and project8. Please download it from
[here](https://drive.google.com/file/d/0B2iFsq4CY1DteHhJUEk5cDNJajQ/view).

-   Project 7 \<files/project7.pdf\>

-   [VirtualBox VM
    Download](https://drive.google.com/file/d/0B2iFsq4CY1DteHhJUEk5cDNJajQ/view)

Do not copy and paste commands from pdf files. Please type them

:   manually. Special characters cause problems in executing commands in
    a terminal.

Project 8
---------

Zip your source code and report as username\_mbkmeans.zip.

The point total for this project is 6, where the distribution is as
follows: - Completeness of your code (5 points) - In the report,
describe your implementation and the output. (1 points)

You can get up to 4 bonus points based on your extra efforts.

-   Project 8 \<files/project8.pdf\>
