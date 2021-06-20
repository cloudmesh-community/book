# NumPy {#s-numpy}

NumPy is a popular library that is used by many other Python
packages such as Pandas, SciPy, and scikit-learn. It provides a
fast, simple-to-use way of interacting with numerical data
organized in vectors and matrices. In this section, we will
provide a short introduction to NumPy.

## Installing NumPy

The most common way of installing NumPy, if it wasn't included
with your Python installation, is to install it via pip:

    $ pip install numpy

If NumPy has already been installed, you can update to the most
recent version using:

    $ pip install -U numpy

You can verify that NumPy is installed by trying to use it in
a Python program:

    import numpy as np

Note that, by convention, we import NumPy using the alias 'np' -
whenever you see 'np' sprinkled in example Python code, it's a
good bet that it is using NumPy.

## NumPy Basics

At its core, NumPy is a container for n-dimensional data. Typically,
1-dimensional data is called an array and 2-dimensional data is called
a matrix. Beyond 2-dimensions would be considered a multidimensional
array. Examples, where you'll encounter these dimensions, may include:

* 1 Dimensional: time-series data such as audio, stock prices, or a single observation in a dataset.
* 2 Dimensional: connectivity data between network nodes, user-product
  recommendations, and database tables.
* 3+ Dimensional: network latency between nodes over time, video
  (RGB+time), and version-controlled datasets.

All of these data can be placed into NumPy's array object, just
with varying dimensions.

## Data Types: The Basic Building Blocks

Before we delve into arrays and matrices, we will start with
the most basic element of those: a single value. NumPy can
represent data utilizing many different standard datatypes such
as uint8 (an 8-bit **u**signed **int**eger), float64 (a 64-bit
float), or str (a string). An exhaustive listing can be found at:

* <https://docs.scipy.org/doc/numpy-1.15.0/user/basics.types.html>

Before moving on, it is important to know about the tradeoff
made when using different datatypes. For example, a uint8 can
only contain values between 0 and 255. This, however, contrasts
with float64 which can express any value from +/- 1.80e+308. So
why wouldn't we just always use float64s? Though they allow us
to be more expressive in terms of numbers, they also consume
more memory. If we were working with a 12-megapixel image,
for example, storing that image using uint8 values would require
3000 * 4000 * 8 = 96 million bits, or 91.55 MB of memory. If we
were to store the same image utilizing float64, our image would
consume 8 times as much memory: 768 million bits or 732.42 MB.
It is important to use the right data type for the job to avoid
consuming unnecessary resources or slowing down processing.

Finally, while NumPy will conveniently convert between datatypes,
one must be aware of overflows when using smaller data types.
For example:

    a = np.array([6], dtype=np.uint8)
    print(a)
    >>>[6]
    a = a + np.array([7], dtype=np.uint8)
    print(a)
    >>>[13]
    a = a + np.array([245], dtype=np.uint8)
    print(a)
    >>>[2]

In this example, it makes sense that 6+7=13. But how does
13+245=2? Put simply, the object type (uint8) simply ran out of
space to store the value and wrapped back around to the beginning.
An 8-bit number is only capable of storing 2^8, or 256, unique values.
An operation that results in a value above that range will 'overflow'
and cause the value to wrap back around to zero. Likewise, anything
below that range will 'underflow' and wrap back around to the end.
In our example, 13+245 became 258, which was too large to store in 8
bits and wrapped back around to 0 and ended up at 2.

NumPy will, generally, try to avoid this situation by dynamically
retyping to whatever datatype will support the result:

    a = a + 260
    print(test)
    >>>[262]

Here, our addition caused our array, 'a', to be upscaled to use
uint16 instead of uint8. Finally, NumPy offers convenience functions
akin to Python's range() function to create arrays of sequential
numbers:

    X = np.arange(0.2,1,.1)
    print(X)
    >>>array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], dtype=float32)

We can use this function to also generate parameters spaces that can
be iterated on:

    P = 10.0 ** np.arange(-7,1,1)
    print(P)

    for x,p in zip(X,P):
        print('%f, %f' % (x, p))

## Arrays: Stringing Things Together

With our knowledge of datatypes in hand, we can begin to explore
arrays. Simply put, arrays can be thought of as a sequence of
values (not neccesarily numbers). Arrays are 1 dimensional and can
be created and accessed simply:

    a = np.array([1, 2, 3])
    print(type(a))
    >>><class 'numpy.ndarray'>
    print(a)
    >>>[1 2 3]
    print(a.shape)
    >>>(3,)
    a[0]
    >>>1

Arrays (and, later, matrices) are zero-indexed. This makes it
convenient when, for example, using Python's range() function
to iterate through an array:

    for i in range(3):
        print(a[i])
    >>>1
    >>>2
    >>>3

Arrays are, also, mutable and can be changed easily:

    a[0] = 42
    print(a)
    >>>array([42, 2, 3])

NumPy also includes incredibly powerful broadcasting features. This
makes it very simple to perform mathematical operations on arrays
that also makes intuitive sense:

    a * 3
    >>>array([3, 6, 9])
    a**2
    >>>array([1, 4, 9], dtype=int32)

Arrays can also interact with other arrays:

    b = np.array([2, 3, 4])
    print(a * b)
    >>>array([ 2,  6, 12])

In this example, the result of multiplying together two
arrays is to take the element-wise product while multiplying by a
constant will multiply each element in the array by that constant.
NumPy supports all of the basic mathematical operations: addition,
subtraction, multiplication, division, and powers. It also includes
an extensive suite of mathematical functions, such as log() and max(),
which are covered later.

## Matrices: An Array of Arrays

Matrices can be thought of as an extension of arrays - rather than
having one dimension, matrices have 2 (or more). Much like arrays,
matrices can be created easily within NumPy:

    m = np.array([[1, 2], [3, 4]])
    print(m)
    >>>[[1 2]
    >>> [3 4]]

Accessing individual elements is similar to how we did it for arrays.
We simply need to pass in a number of arguments equal to the number
of dimensions:

    m[1][0]
    >>>3

In this example, our first index selected the row and the second selected
the column - giving us our result of 3. Matrices can be extending out
to any number of dimensions by simply using more indices to access
specific elements (though use-cases beyond 4 may be somewhat rare).

Matrices support all of the normal mathematial functions such as
+, -, &ast;, and /. A special note: the &ast; operator will result
in an element-wise multiplication. Using @ or np.matmul() for matrix
multiplication:

    print(m-m)
    print(m*m)
    print(m/m)

More complex mathematical functions can typically be found within
the NumPy library itself:

    print(np.sin(x))
    print(np.sum(x))

A full listing can be found at:
https://docs.scipy.org/doc/numpy/reference/routines.math.html

## Slicing Arrays and Matrices

As one can imagine, accessing elements one-at-a-time is both slow
and can potentially require many lines of code to iterate over
every dimension in the matrix. Thankfully, NumPy incorporate a very
powerful slicing engine that allows us to access ranges of elements
easily:

    m[1, :]
    >>>array([3, 4])

The ':' value tells NumPy to select all elements in the given
dimension. Here, we've requested all elements in the first row. We
can also use indexing to request elements within a given range:

    a = np.arange(0, 10, 1)
    print(a)
    >>>[0 1 2 3 4 5 6 7 8 9]
    a[4:8]
    >>>array([4, 5, 6, 7])

Here, we asked NumPy to give us elements 4 through 7 (ranges in Python
are inclusive at the start and non-inclusive at the end). We can even
go backwards:

    a[-5:]
    >>>array([5, 6, 7, 8, 9])

In the previous example, the negative value is asking NumPy to return
the last 5 elements of the array. Had the argument been ':-5', NumPy
would've returned everything BUT the last five elements:

    a[:-5]
    >>>array([0, 1, 2, 3, 4])

Becoming more familiar with NumPy's accessor conventions will allow
you write more efficient, clearer code as it is easier to read a
simple one-line accessor than it is a multi-line, nested loop when
extracting values from an array or matrix.

## Useful Functions

The NumPy library provides several convenient mathematical functions
that users can use. These functions provide several advantages
to code written by users:

* They are open source typically have multiple contributors checking
  for errors.
* Many of them utilize a C interface and will run much faster than
  native Python code.
* They're written to very flexible.

NumPy arrays and matrices contain many useful aggregating functions
such as max(), min(), mean(), etc These functions are usually able
to run an order of magnitude faster than looping through the object,
so it's important to understand what functions are available to
avoid 'reinventing the wheel.' In addition, many of the functions
are able to sum or average across axes, which make them extremely
useful if your data has inherent grouping. To return to a previous
example:

    m = np.array([[1, 2], [3, 4]])
    print(m)
    >>>[[1 2]
    >>> [3 4]]
    m.sum()
    >>>10
    m.sum(axis=1)
    >>>[3, 7]
    m.sum(axis=0)
    >>>[4, 6]

In this example, we created a 2x2 matrix containing the numbers
1 through 4. The sum of the matrix returned the element-wise addition
of the entire matrix. Summing across axis 0 (rows) returned a new array
with the element-wise addition across each row. Likewise, summing across
axis 1 (columns) returned the columnar summation.

## Linear Algebra

Perhaps one of the most important uses for NumPy is its robust support
for Linear Algebra functions. Like the aggregation functions described
in the previous section, these functions are optimized to be much faster
than user implementations and can utilize processesor level features to
provide very quick computations. These functions can be accessed very
easily from the NumPy package:

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print(np.matmul(a, b))
    >>>[[19 22]
        [43 50]]

Included in within np.linalg are functions for calculating the
Eigendecomposition of square matrices and symmetric matrices. Finally,
to give a quick example of how easy it is to implement algorithms in
NumPy, we can easily use it to calculate the cost and gradient when
using simple Mean-Squared-Error (MSE):

    cost = np.power(Y - np.matmul(X, weights)), 2).mean(axis=1)
    gradient = np.matmul(X.T, np.matmul(X, weights) - y)

Finally, more advanced functions are easily available to users via the
linalg library of NumPy as:

    from numpy import linalg

    A = np.diag((1,2,3))

    w,v = linalg.eig(A)

    print ('w =', w)
    print ('v =', v)

## NumPy Resources

* <https://docs.scipy.org/doc/numpy>
* <http://cs231n.github.io/python-numpy-tutorial/#numpy>
* <https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.linalg.html>
* <https://en.wikipedia.org/wiki/Mean_squared_error>
