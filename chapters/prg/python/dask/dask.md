# Dask

Dask is a python-based parallel computing library for
analytics. Parallel computing is a type of computation in which many
calculations or the execution of processes are carried out
simultaneously. Large problems can often be divided into smaller ones,
which can then be solved concurrently.

Dask is composed of two components:

1. *Dynamic task scheduling optimized for computation.* This is
   similar to Airflow, Luigi, Celery, or Make, but optimized for
   interactive computational workloads.
2. *Big Data collections* like parallel arrays, dataframes, and lists
   that extend common interfaces like NumPy, Pandas, or Python
   iterators to larger-than-memory or distributed environments. These
   parallel collections run on top of the dynamic task schedulers.


Dask emphasizes the following virtues:

* *Familiar*: Provides parallelized NumPy array and Pandas DataFrame
  objects.
* *Flexible*: Provides a task scheduling interface for more custom
  workloads and integration with other projects.
* *Native*: Enables distributed computing in Pure Python with access
  to the PyData stack.
* *Fast*: Operates with low overhead, low latency, and minimal
  serialization necessary for fast numerical algorithms
* *Scales up*: Runs resiliently on clusters with 1000s of cores
* *Scales down*: Trivial to set up and run on a laptop in a single
  process
* *Responsive*: Designed with interactive computing in mind it
  provides rapid feedback and diagnostics to aid humans


The section is structured in a number of subsections addressing the
following topics:

Foundations: 

* an explanation of what Dask is, how it works, and how to use lower
  level primitives to set up computations. Casual users may wish to
  skip this section, although we consider it useful knowledge for all
  users.
             
Distributed Features: 

* information on running Dask on the distributed scheduler, which
  enables scale-up to distributed settings and enhanced monitoring of
  task operations. The distributed scheduler is now generally the
  recommended engine for executing task work, even on single
  workstations or laptops.
             
Collections: 

* convenient abstractions giving a familiar feel to big data.
       
       
Bags: 

* Python iterators with a functional paradigm, such as found in
  func/iter-tools and toolz - generalize lists/generators to big data;
  this will seem very familiar to users of PySpark's RDD

Array: 

* massive multi-dimensional numerical data, with Numpy functionality

Dataframe: 

* massive tabular data, with Pandas functionality


# How Dask Works

Dask is computation tool for larger-than-memory datasets, parallel
execution or delayed/background execution.

We can summarize the basics of Dask as follows:

* process data that does not fit into memory by breaking it into
  blocks and specifying task chains
* parallelize execution of tasks across cores and even nodes of a
  cluster
* move computation to the data rather than the other way around, to
  minimize communication overheads

We use for-loops to build basic tasks, Python iterators, and the Numpy
(array) and Pandas (dataframe) functions for multi-dimensional or
tabular data, respectively.

Dask allows us to construct a prescription for the calculation we want
to carry out. A module named Dask.delayed lets us parallelize custom
code. It is useful whenever our problem doesn’t quite fit a high-level
parallel object like dask.array or dask.dataframe but could still
benefit from parallelism. Dask.delayed works by delaying our function
evaluations and putting them into a dask graph. Here is a small
example:


```
from dask import delayed

@delayed
def inc(x):
    return x + 1

@delayed
def add(x, y):
    return x + y
```

Here we have used the delayed annotation to show that we want these
functions to operate lazily - to save the set of inputs and execute
only on demand.

# Dask Bag 

Dask-bag excels in processing data that can be represented as a
sequence of arbitrary inputs. We'll refer to this as "messy" data,
because it can contain complex nested structures, missing fields,
mixtures of data types, etc. The functional programming style fits
very nicely with standard Python iteration, such as can be found in
the itertools module.

Messy data is often encountered at the beginning of data processing
pipelines when large volumes of raw data are first consumed. The
initial set of data might be JSON, CSV, XML, or any other format that
does not enforce strict structure and datatypes. For this reason, the
initial data massaging and processing is often done with Python lists,
dicts, and sets.

These core data structures are optimized for general-purpose storage
and processing. Adding streaming computation with iterators/generator
expressions or libraries like itertools or toolz let us process large
volumes in a small space. If we combine this with parallel processing
then we can churn through a fair amount of data.

Dask.bag is a high level Dask collection to automate common workloads
of this form. In a nutshell

```
dask.bag = map, filter, toolz + parallel execution
```

You can create a Bag from a Python sequence, from files, from data on
S3, etc..


```
# each element is an integer
import dask.bag as db
b = db.from_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```


```
# each element is a text file of JSON lines
import os
b = db.read_text(os.path.join('data', 'accounts.*.json.gz'))
```


```
# Requires `s3fs` library
# each element is a remote CSV text file
b = db.read_text('s3://dask-data/nyc-taxi/2015/yellow_tripdata_2015-01.csv')
```

Bag objects hold the standard functional API found in projects like
the Python standard library, toolz, or pyspark, including map, filter,
groupby, etc..

As with Array and DataFrame objects, operations on Bag objects create
new bags. Call the .compute() method to trigger execution.


```
def is_even(n):
    return n % 2 == 0

b = db.from_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c = b.filter(is_even).map(lambda x: x ** 2)
c
```


```
# blocking form: wait for completion (which is very fast in this case)
c.compute()
```

For more details on Dask Bag check https://dask.pydata.org/en/latest/bag.html

# Concurrency Features

Dask supports a real-time task framework that extends Python’s
concurrent.futures interface. This interface is good for arbitrary
task scheduling, like dask.delayed, but is immediate rather than lazy,
which provides some more flexibility in situations where the
computations may evolve over time. These features depend on the second
generation task scheduler found in dask.distributed (which, despite
its name, runs very well on a single machine).

Dask allows us to simply construct graphs of tasks with
dependencies. We can find that graphs can also be created
automatically for us using functional, Numpy or Pandas syntax on data
collections. None of this would be very useful, if there weren't also
a way to execute these graphs, in a parallel and memory-aware
way. Dask comes with four available schedulers:

* `dask.threaded.get`: a scheduler backed by a thread pool
* `dask.multiprocessing.get`: a scheduler backed by a process pool
* `dask.async.get_sync`: a synchronous scheduler, good for debugging
* `distributed.Client.get`: a distributed scheduler for executing graphs on multiple machines.

Here is a simple program for dask.distributed library:


```
from dask.distributed import Client
client = Client('scheduler:port')

futures = []
for fn in filenames:
    future = client.submit(load, fn)
    futures.append(future)

summary = client.submit(summarize, futures)
summary.result()
```

For more details on Concurrent Features by Dask check
https://dask.pydata.org/en/latest/futures.html

# Dask Array 

Dask arrays implement a subset of the NumPy interface on large arrays
using blocked algorithms and task scheduling.  These behave like numpy
arrays, but break a massive job into tasks that are then executed by a
scheduler. The default scheduler uses threading but you can also use
multiprocessing or distributed or even serial processing (mainly for
debugging). You can tell the dask array how to break the data into
chunks for processing.


```
import dask.array as da
f = h5py.File('myfile.hdf5')             
x = da.from_array(f['/big-data'], chunks=(1000, 1000))
x - x.mean(axis=1).compute()
```

For more details on Dask Array check https://dask.pydata.org/en/latest/array.html

# Dask DataFrame

A Dask DataFrame is a large parallel dataframe composed of many
smaller Pandas dataframes, split along the index.  These pandas
dataframes may live on disk for larger-than-memory computing on a
single machine, or on many different machines in a
cluster. Dask.dataframe implements a commonly used subset of the
Pandas interface including elementwise operations, reductions,
grouping operations, joins, timeseries algorithms, and more. It copies
the Pandas interface for these operations exactly and so should be
very familiar to Pandas users. Because Dask.dataframe operations
merely coordinate Pandas operations they usually exhibit similar
performance characteristics as are found in Pandas. To run the
following code, save 'student.csv' file in your machine.


```
import pandas as pd                     
df = pd.read_csv('student.csv')      
d = df.groupby(df.HID).Serial_No.mean()
print(d)
```

    ID
    101     1
    102     2
    104     3
    105     4
    106     5
    107     6
    109     7
    111     8
    201     9
    202    10
    Name: Serial_No, dtype: int64
    


```
import dask.dataframe as dd
df = dd.read_csv('student.csv')
dt = df.groupby(df.HID).Serial_No.mean().compute()
print (dt)
```

    ID
    101     1.0
    102     2.0
    104     3.0
    105     4.0
    106     5.0
    107     6.0
    109     7.0
    111     8.0
    201     9.0
    202    10.0
    Name: Serial_No, dtype: float64
    

For more details on Dask DataFrame check https://dask.pydata.org/en/latest/dataframe.html

# Dask DataFrame Storage

Efficient storage can dramatically improve performance, particularly
when operating repeatedly from disk.

Decompressing text and parsing CSV files is expensive. One of the most
effective strategies with medium data is to use a binary storage
format like HDF5.


```
# be sure to shut down other kernels running distributed clients
from dask.distributed import Client
client = Client()
```

Create data if we don't have any


```
from prep import accounts_csvs
accounts_csvs(3, 1000000, 500)
```



First we read our csv data as before.

CSV and other text-based file formats are the most common storage for
data from many sources, because they require minimal pre-processing,
can be written line-by-line and are human-readable. Since Pandas'
read_csv is well-optimized, CSVs are a reasonable input, but far from
optimized, since reading required extensive text parsing.



```
import os
filename = os.path.join('data', 'accounts.*.csv')
filename
```


```
import dask.dataframe as dd
df_csv = dd.read_csv(filename)
df_csv.head()
```



HDF5 and netCDF are binary array formats very commonly used in the
scientific realm.

Pandas contains a specialized HDF5 format, HDFStore. The
dd.DataFrame.to_hdf method works exactly like the pd.DataFrame.to_hdf
method.



```
target = os.path.join('data', 'accounts.h5')
target
```


```
%time df_csv.to_hdf(target, '/data')
```


```
df_hdf = dd.read_hdf(target, '/data')
df_hdf.head()
```

For more information of Dask DataFrame Storage, click http://dask.pydata.org/en/latest/dataframe-create.html

# Links

* <https://dask.pydata.org/en/latest/>
* <http://matthewrocklin.com/blog/work/2017/10/16/streaming-dataframes-1>
* <http://people.duke.edu/~ccc14/sta-663-2017/18A_Dask.html>
* <https://www.kdnuggets.com/2016/09/introducing-dask-parallel-programming.html>
* <https://pypi.python.org/pypi/dask/>
* <https://www.hdfgroup.org/2015/03/hdf5-as-a-zero-configuration-ad-hoc-scientific-database-for-python/>
* <https://github.com/dask/dask-tutorial>
