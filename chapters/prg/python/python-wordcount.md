# Word Count with Parallel Python

We will demonstrate Python's `multiprocessing` API for parallel
computation by writing a program that counts how many times each word in
a collection of documents appear.

## Generating a Document Collection

Before we begin, let us write a script that will generate document
collections by specifying the number of documents and the number of
words per document. This will make benchmarking straightforward.

To keep it simple, the vocabulary of the document collection will
consist of random numbers rather than the words of an actual language:

    '''Usage: generate_nums.py [-h] NUM_LISTS INTS_PER_LIST MIN_INT MAX_INT DEST_DIR

    Generate random lists of integers and save them 
    as 1.txt, 2.txt, etc.

    Arguments:
       NUM_LISTS      The number of lists to create.
       INTS_PER_LIST  The number of integers in each list.
       MIN_NUM        Each generated integer will be >= MIN_NUM.
       MAX_NUM        Each generated integer will be <= MAX_NUM.
       DEST_DIR       A directory where the generated numbers will be stored.

    Options:
      -h --help
    '''

    from __future__ import print_function
    import os, random, logging
    from docopt import docopt


    def generate_random_lists(num_lists, 
                              ints_per_list, min_int, max_int):
        return [[random.randint(min_int, max_int) \
            for i in range(ints_per_list)] for i in range(num_lists)]


    if __name__ == '__main__':
       args = docopt(__doc__)
       num_lists, ints_per_list, min_int, max_int, dest_dir = [
          int(args['NUM_LISTS']),
          int(args['INTS_PER_LIST']),
          int(args['MIN_INT']),
          int(args['MAX_INT']),
          args['DEST_DIR']
       ]

       if not os.path.exists(dest_dir):
          os.makedirs(dest_dir)

       lists = generate_random_lists(num_lists, 
                                     ints_per_list, 
                                     min_int, 
                                     max_int)
       curr_list = 1
       for lst in lists:
          with open(os.path.join(dest_dir, '%d.txt' % curr_list), 'w') as f:
         f.write(os.linesep.join(map(str, lst)))
      curr_list += 1
       logging.debug('Numbers written.')

Notice that we are using the
[docopt](https://pypi.python.org/pypi/docopt) module that you should be
familiar with from the Section [Python DocOpts](#s-python-docopts} to make the script easy to run from the command line.

You can generate a document collection with this script as follows:

    python generate_nums.py 1000 10000 0 100 docs-1000-10000

## Serial Implementation

A first serial implementation of wordcount is straightforward:

    '''Usage: wordcount.py [-h] DATA_DIR

    Read a collection of .txt documents and count how many times each word
    appears in the collection.

    Arguments:
      DATA_DIR  A directory with documents (.txt files).

    Options:
      -h --help
    '''

    from __future__ import division, print_function
    import os, glob, logging
    from docopt import docopt

    logging.basicConfig(level=logging.DEBUG)


    def wordcount(files):
       counts = {}
       for filepath in files:
          with open(filepath, 'r') as f:
         words = [word.strip() for word in f.read().split()]
         for word in words:
            if word not in counts:
               counts[word] = 0
            counts[word] += 1
       return counts


    if __name__ == '__main__':
       args = docopt(__doc__)
       if not os.path.exists(args['DATA_DIR']):
          raise ValueError('Invalid data directory: %s' % args['DATA_DIR'])

       counts = wordcount(glob.glob(os.path.join(args['DATA_DIR'], '*.txt')))
       logging.debug(counts)

## Serial Implementation Using map and reduce

We can improve the serial implementation in anticipation of parallelizing
the program by making use of Python's `map` and `reduce` functions.

In short, you can use `map` to apply the same function to the members of
a collection. For example, to convert a list of numbers to strings, you
could do:

    import random
    nums = [random.randint(1, 2) for _ in range(10)]
    print(nums)
    [2, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    print(map(str, nums))
    ['2', '1', '1', '1', '2', '2', '2', '2', '2', '2']

We can use reduce to apply the same function cumulatively to the items
of a sequence. For example, to find the total of the numbers in our
list, we could use `reduce` as follows:

    def add(x, y): 
        return x + y

    print(reduce(add, nums))
    17

We can simplify this even more by using a lambda function:

    print(reduce(lambda x, y: x + y, nums))
    17

You can read more about [Python's lambda function in the
docs](https://docs.python.org/2.7/tutorial/controlflow.html#lambda-expressions).

With this in mind, we can reimplement the wordcount example as follows:

    '''Usage: wordcount_mapreduce.py [-h] DATA_DIR

    Read a collection of .txt documents and count how
    many times each word
    appears in the collection.

    Arguments: 
       DATA_DIR  A directory with documents (.txt files).

    Options:
       -h --help
    '''

    from __future__ import division, print_function
    import os, glob, logging
    from docopt import docopt

    logging.basicConfig(level=logging.DEBUG)

    def count_words(filepath):
       counts = {}
       with open(filepath, 'r') as f:
          words = [word.strip() for word in f.read().split()]

      for word in words:
         if word not in counts:
            counts[word] = 0
         counts[word] += 1
      return counts


    def merge_counts(counts1, counts2):
       for word, count in counts2.items():
          if word not in counts1:
         counts1[word] = 0
      counts1[word] += counts2[word]
       return counts1


    if __name__ == '__main__':
       args = docopt(__doc__)
       if not os.path.exists(args['DATA_DIR']):
          raise ValueError('Invalid data directory: %s' % args['DATA_DIR'])

          per_doc_counts = map(count_words,
                               glob.glob(os.path.join(args['DATA_DIR'],
                               '*.txt')))
       counts = reduce(merge_counts, [{}] + per_doc_counts)
       logging.debug(counts)

## Parallel Implementation

Drawing on the previous implementation using `map` and `reduce`, we can
parallelize the implementation using Python's `multiprocessing` API:

    '''Usage: wordcount_mapreduce_parallel.py [-h] DATA_DIR NUM_PROCESSES

    Read a collection of .txt documents and count, in parallel, how many
    times each word appears in the collection.

    Arguments:
       DATA_DIR       A directory with documents (.txt files).
       NUM_PROCESSES  The number of parallel processes to use.

    Options:
       -h --help
    '''

    from __future__ import division, print_function
    import os, glob, logging
    from docopt import docopt
    from wordcount_mapreduce import count_words, merge_counts
    from multiprocessing import Pool

    logging.basicConfig(level=logging.DEBUG)

    if __name__ == '__main__':
       args = docopt(__doc__)
       if not os.path.exists(args['DATA_DIR']):
          raise ValueError('Invalid data directory: %s' % args['DATA_DIR'])
       num_processes = int(args['NUM_PROCESSES'])

       pool = Pool(processes=num_processes)

       per_doc_counts = pool.map(count_words,
                                 glob.glob(os.path.join(args['DATA_DIR'],
                                 '*.txt')))
       counts = reduce(merge_counts, [{}] + per_doc_counts)
       logging.debug(counts)

## Benchmarking

To time each of the examples, enter it into its own Python file
and use Linux's `time` command:

```bash
$ time python wordcount.py docs-1000-10000
```

The output contains the real run time and the user run time. real is
wall clock time - time from start to finish of the call. user is the
amount of CPU time spent in user-mode code (outside the kernel) within
the process, that is, only actual CPU time used in executing the
process.

## Excersises

E.python.wordcount.1:

> Run the three different programs (serial, serial w/ map and reduce,
> parallel) and answer the following questions:
> 
> 1. Is there any performance difference between the different versions
>    of the program?
> 2. Does user time significantly differ from real time for any of the
>    versions of the program?
> 3. Experiment with different numbers of processes for the parallel
>    example, starting with 1. What is the performance gain when you goal
>    from 1 to 2 processes? From 2 to 3? When do you stop seeing
>    improvement? (this will depend on your machine architecture)


## References

* [Map, Filter and Reduce](http://book.pythontips.com/en/latest/map_filter.html)
* [multiprocessing API](https://docs.python.org/2/library/multiprocessing.html)
