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




NumPy is a popular library on that is used by many other python
librariessuch as pandas, and SciPy. It provides simple to use array
operations for data. This helps to accass arrays in a more intuitive
fashion and introduces various matrix operations.

We provide a short introduction to Numpy.

First we import the modules needed for this introduction and abreviate
them with the `as` feature of the import statement

    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt

Now we showcase some features of Numpy.

Float Range
-----------

`arange()` is like `range()`, but for floating-point numbers.

    X = np.arange(0.2,1,.1)

    print (X)

We use this function to generate parameter space that can then be
iterated on.

    P = 10.0 ** np.arange(-7,1,1)

    print (P)

    for x,p in zip(X,P):
        print ('%f, %f' % (x, p))

Arrays
------

To create one dimensional arrays you use

    a = np.array([1, 2, 3])   

To check some properties you can use the following

    print(type(a))            # Prints "<class 'numpy.ndarray'>"

    print(a.shape)            # Prints "(3,)"

The shape indicates that in the first dimension, there are 3 elements.
To print the actual values you can use

    print(a)                  # Prints the values of the array
    print(a[0], a[1], a[2])   # Prints "1 2 3"

To change values you can use the index of the element or use any other
python method to do so. IN our example we change the first element to
`42`

    a[0] = 42                 
    print(a)                  

To create more dimensional arrays you use

    b = np.array([[1,2,3],[4,5,6]])    # Create a 2 dimensional array
    print(b.shape)                     # Prints "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

Array Operations
----------------

Let us first create some arrays with a predefined datatype

    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    print (x)

    print(y)

To add the numbers use

    print(x+y)

Other functions such as `-`, `*`, `/` behave as expected using
elementwise oerations:

    print(x-y)

    print(x*y)

    print(x/y)

To apply functions such as 'sin' make sure you use the function provided
by the numpy package such as `np.sin`. The list of functions is included
in the manual at \*
<https://docs.scipy.org/doc/numpy/reference/routines.math.html>

    print (np.sin(x))

    print (np.sum(x))

Computations can also be applied to columns and rows

    print(np.sum(x, axis=0)) # sum of each column
    print(np.sum(x, axis=1)) # sum of each row

Linear Algebra
--------------

Linear algebra methods are also provided.

    from numpy import linalg 

    A = np.diag((1,2,3))

    w,v = linalg.eig(A)

    print ('w =', w)
    print ('v =', v)

Resources
---------

*  <https://docs.scipy.org/doc/numpy/>
* <http://cs231n.github.io/python-numpy-tutorial/#numpy>
