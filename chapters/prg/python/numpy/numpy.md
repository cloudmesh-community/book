# Numpy {#s-numpy}

NumPy is a popular library that is used by many other Python
packages such as Pandas, SciPy, and scikit-learn. It provides a
simple-to-use and fast way of interacting with numerical data
organized in vectors and matrices. In this section, we will
provide a short introduction to NumPy.

Installing NumPy
-----------
The most common way of installing NumPy, if it wasn't included
with your Python installation, is to install it via pip:

    pip install numpy

If NumPy has already been installed, you can update to the most
recent version using:

    pip install -U numpy
    
You can verify that NumPy is installed by trying to use it in
a Python program:
    
    import numpy as np

Note that, by convention, we import NumPy using the alias 'np' - 
whenever you see 'np' sprinkled in example Python code, it's a
good bet that it is using NumPy.

NumPy Basics
-----------
At its core, NumPy is a container for n-dimensional data. Typically,
1-dimensional data is called an array and 2-dimensional data is called
a matrix. Beyond 2-dimenions would be considered a multidimensional
array. Examples where you'll encounter these dimenions may include:

* 1 Dimensional: time series data such as audio, stock prices, or
a single observation in a dataset.
* 2 Dimensional: a single color channel in an image (e.g. red) or 
a dataset containing more than one observation, or 
* 3+ Dimensional: images composed of multiple channels (e.g. RGB,
CMYK, etc.) or video (RGB+time).

All of these data can be placed into NumPy's array object, just
with varying dimensions.

Data Types: The Basic Building Blocks
-----------
Before we delve into arrays and matrices, we'll start off with
the most basic element of those: a single value. NumPy can
represent data utilizing many different standard datatypes such
as uint8 (an 8-bit **u**signed **int**eger), float64 (a 64-bit
float), or str (a string). An exhaustive listing can be found at:

https://docs.scipy.org/doc/numpy-1.15.0/user/basics.types.html

Before moving on, it's important to know about the tradeoff
made when using different datatypes. For example, a uint8 can
only contained values between 0 and 255. This, however, constrats
with float64 which can express any value from +/- 1.80e+308. So
why wouldn't we just always use float64s? Though they allow us
to be more expressive in terms of numbers, they also consume
more memory. If we were working with a 12 megapixel image,
for example, storing that image using uint8 values would require
3000 * 4000 * 8 = 96 million bits, or 91.55 MB of memory. If we
were to store the same image utilizing float64, our image would
consume 8 times as much memory: 768 million bits or 732.42 MB.
It's important use the right datatype for the job to avoid
consuming unneccessary resources or slowing down processing.

Finally, while NumPy will convenient convert between datatypes,
one must be aware of overflows when using smaller datatypes.
For example:

    test = np.array([6], dtype=np.uint8)
    print(test)
    >>>[6]
    test = test + np.array([7], dtype=np.uint8)
    print(test)
    >>>[13]
    test = test + np.array([245], dtype=np.uint8)
    print(test)
    >>>[2]

From the above, it makes sense that 6+7=13. But how does 
13+245=2? Put simply, the object type (uint8) simply ran out of
space to store the value and wrapped back around to the beginning.
An 8-bit number is only capable of storing 2^8, or 255, unique values.
An operation that results in a value above that range will 'overflow'
to cause the value to wrap back around to zero. Likewise, anything
below that range will 'underflow' and wrap back around to the beginning.
In our example, 13+245 became 258, which was too large to store in 8
bits and wrapped back around to 0 and ended up at 2.

NumPy will, generally, try to avoid this situation by dynamically
retyping to whatever datatype will support the result:

    test = test + 260
    print(test)
    >>>[262]

Here, our addition caused our 'test' array to be upscaled to use
uint16 instead of uint8.

Arrays: Stringing Things Together
-----------
With our knowledge of datatypes in hand, we can begin to explore
arrays. Simply put, arrays can be thought of as a sequence of
values (not neccesarily numbers). Arrays are 1 dimensional and can
be created and accessed simply:

    example = np.array([1, 2, 3])
    print(example)
    >>>[1 2 3]
    example[0]
    >>>1

Arrays (and, later, matrices) are zero-indexed. This makes it
convenient, for example, when using Python's range() function to
iterate through an array:

    for i in range(3):
        print(example[i])
    >>>1
    >>>2
    >>>3

NumPy also includes incredibly powerful broadcasting features. This
makes it incredibly simple to perform mathematical functions on arrays
that, also, make intuitive sense:

    example * 3
    >>>array([3, 6, 9])
    example**2
    >>>array([1, 4, 9], dtype=int32)
    
Arrays can also interact with other arrays:
    
    other_example = np.array([2, 3, 4])
    example * other_example
    array([ 2,  6, 12])

In the above, we can see that the result of multiplying together two
arrays is to take the element-wise product while multiplying by a
constant will multiply each element in the array by that constant.
NumPy supports all of the basic mathematical operations: addition,
subtraction, multiplication, division, and powers. It also includes
an extensive suite of mathematical functions, such as log() and max(),
which are covered later.

Matrices: An Array of Arrays
----------------
Matrices can be thought of as an extension of arrays - rather than
having one dimension, matrices have 2 (or more). Much like arrays,
matrices can be created easily within NumPy:

    matrix = np.array([[1, 2], [3, 4]])
    print(matrix)
    >>>[[1 2]
    >>> [3 4]]

Accessing individual elements is similar to how we did it for arrays.
We simply need to pass in a number of arguments equal to the number
of dimensions:

    matrix[1][0]
    >>>3

In the above, our first index selected the row and the second selected
the column - giving us our result of 3. Matrices can be extending out
to any number of dimensions by simply using more indices to access
specific elements (though use-cases beyond 4 may be somewhat rare).

Slicing Arrays and Matrices
----------------
As one can imagine, accessing elements one-at-a-time is both slow
and can potentially require many lines of code to iterate over
every dimension in the matrix. Thankfully, NumPy incorporate a very
power slicing engine that allows us to access ranges of elements 
easily:

    matrix[1, :]
    >>>array([3, 4])

The ':' value tells NumPy to simply select all elements in the given
dimension. Here, we've requested all elements in the first row. We
can also use indexing to request elements within a given range:

    long_array = np.arange(0, 10, 1)
    print(long_array)
    >>>[0 1 2 3 4 5 6 7 8 9]
    long_array[4:8]
    >>>array([4, 5, 6, 7])
   
In the above, we asked NumPy to give us elements 4 through 7 (ranges
in Python are inclusive at the start and non-inclusive at the end). We
can even go backwards:

    long_array[-5:]
    >>>array([5, 6, 7, 8, 9])
    
In the above example, we're asking NumPy to give us the last 5 elements
of our array. Had we done ':-5', we would've requested everything BUT
the last five elements:

    long_array[:-5]
    >>>array([0, 1, 2, 3, 4])
    
Becoming more familiar with NumPy's accessor conventions will allow
you write more efficient, clearer code as it is easier to read a
simple one-line accessor than it is a multi-line, nested loop when
extracting values from an array or matrix.

Useful Functions
----------------


Linear Algebra
----------------

Resources
---------

* <https://docs.scipy.org/doc/numpy/>
* <http://cs231n.github.io/python-numpy-tutorial/#numpy>
