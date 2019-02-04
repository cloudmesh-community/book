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
Now that NumPy is installed and imported, we can begin to use it.




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
