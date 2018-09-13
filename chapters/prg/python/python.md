## Statements and Strings {#spythonlanguage}


TODO: some of the python examples assume REPL, but its better to use a
  print statement instead as more general, please fix}
Let us explore the syntax of Python. Type into the interactive loop and
press Enter:

```python
print("Hello world from Python!")
# Hello world from Python!
```

What happened: the print function was given a **string** to process. A
string is a sequence of characters. A **character** can be a alphabetic
(A through Z, lower and upper case), numeric (any of the digits), white
space (spaces, tabs, newlines, etc), syntactic directives (comma, colon,
quotation, exclamation, etc), and so forth. A string is just a sequence
of the character and typically indicated by surrounding the characters
in double quotes.

Standard output is discussed in the `../../lesson/linux/shell` lesson.

So, what happened when you pressed Enter? The interactive Python program
read the line `print ("Hello world from Python!")`, split it into the
print statement and the `"Hello world from Python!"` string, and then
executed the line, showing you the output.

Variables
---------

You can store data into a **variable** to access it later. For instance,
instead of:

```python
print('Hello world from Python!')
```

which is a lot to type if you need to do it multiple times, you can
store the string in a variable for convenient access:

```python
hello = 'Hello world from Python!'
print(hello)
# Hello world from Python!
```

Data Types
----------

### Booleans

A **boolean** is a value that indicates *truthness* of something. You
can think of it as a toggle: either "on" or "off", "one" or "zero",
"true" or "false". In fact, the only possible values of the **boolean**
(or bool) type in Python are:

-   True
-   False

You can combine booleans with **boolean operators**:

-   and
-   or


```python
print(True and True)
# True

print(True and False)
# False

print(False and False)
# False

print(True or True)
# True

print(True or False)
# True

print(False or False)
# False
```

### Numbers

The interactive interpreter can also be used as a calculator. For
instance, say we wanted to compute a multiple of 21:

```python
print(21 * 2)
# 42
```

We saw here the print statement again. We passed in the result of the
operation 21 \* 2. An **integer** (or **int**) in Python is a numeric
value without a fractional component (those are called **floating
point** numbers, or **float** for short).

The mathematical operators compute the related mathematical operation to
the provided numbers. Some operators are:

| Operator | Function |
| --- | -------------- |
| * |   multiplication |
| / |   division |
| + |   addition |
| - |   subtraction |
| ** |   exponent |

Exponentiation $x^y$ is written as x\*\*y is x to the yth power.

You can combine **float**s and **int**s:

```python
print(3.14 * 42 / 11 + 4 - 2)
# 13.9890909091

print(2**3)
# 8
```

Note that **operator precedence** is important. Using parenthesis to
indicate affect the order of operations gives a difference results, as
expected:

```python
print(3.14 * (42 / 11) + 4 - 2)
# 11.42

print(1 + 2 * 3 - 4 / 5.0)
# 6.2

print( (1 + 2) * (3 - 4) / 5.0 )
# -0.6
```

Module Management
-----------------

A module allows you to logically organize your Python code. Grouping
related code into a module makes the code easier to understand and use.
A module is a Python object with arbitrarily named attributes that you
can bind and reference. A module is a file consisting of Python code. A
module can define functions, classes and variables. A module can also
include runnable code.

### Import Statement

When the interpreter encounters an import statement, it imports the
module if the module is present in the search path. A search path is a
list of directories that the interpreter searches before importing a
module. The from...import Statement Python's from statement lets you
import specific attributes from a module into the current namespace. It
is preferred to use for each import its own line such as:

```python
import numpy
import matplotlib
```

When the interpreter encounters an import statement, it imports the
module if the module is present in the search path. A search path is a
list of directories that the interpreter searches before importing a
module.

### The from ... import Statement

Python's from statement lets you import specific attributes from a
module into the current namespace. The from ... import has the following
syntax:

```python
from datetime import datetime
```

Date Time in Python
-------------------

The datetime module supplies classes for manipulating dates and times in
both simple and complex ways. While date and time arithmetic is
supported, the focus of the implementation is on efficient attribute
extraction for output formatting and manipulation. For related
functionality, see also the time and calendar modules.

The import Statement You can use any Python source file as a module by
executing an import statement in some other Python source file.

```python
from datetime import datetime
```

This module offers a generic date/time string parser which is able to
parse most known formats to represent a date and/or time.

```python
    from dateutil.parser import parse
```

pandas is an open source Python library for data analysis that needs to
be imported.

```python
import pandas as pd
```

Create a string variable with the class start time

```python
fall_start = '08-21-2018'
```

Convert the string to datetime format

```python 
datetime.strptime(fall_start, '%m-%d-%Y') \#
datetime.datetime(2017, 8, 21, 0, 0)
```

Creating a list of strings as dates

```python
class_dates = ['8/25/2017', '9/1/2017', '9/8/2017', '9/15/2017', '9/22/2017', '9/29/2017']
```

Convert Class_dates strings into datetime format and save the list into
variable a

```python
a = [datetime.strptime(x, '%m/%d/%Y') for x in class_dates]
```

Use parse() to attempt to auto-convert common string formats. Parser
must be a string or character stream, not list.

```python
parse(fall_start)
# datetime.datetime(2017, 8, 21, 0, 0)
```

Use parse() on every element of the Class_dates string.

```python
[parse(x) for x in class_dates] 
# [datetime.datetime(2017, 8, 25, 0, 0),
#   datetime.datetime(2017, 9, 1, 0, 0),
#   datetime.datetime(2017, 9, 8, 0, 0),
#   datetime.datetime(2017, 9, 15, 0, 0),
#   datetime.datetime(2017, 9, 22, 0, 0),
#   datetime.datetime(2017, 9, 29, 0, 0)]
```

Use parse, but designate that the day is first.

```python
parse (fall_start, dayfirst=True)
# datetime.datetime(2017, 8, 21, 0, 0)
```

Create a dataframe.A DataFrame is a tabular data structure comprised of
rows and columns, akin to a spreadsheet, database table. DataFrame as a
group of Series objects that share an index (the column names).

```python
import pandas as pd
data = {
  'dates': [
    '8/25/2017 18:47:05.069722', 
    '9/1/2017 18:47:05.119994', 
    '9/8/2017 18:47:05.178768', 
    '9/15/2017 18:47:05.230071', 
    '9/22/2017 18:47:05.230071', 
    '9/29/2017 18:47:05.280592'], 
  'complete': [1, 0, 1, 1, 0, 1]} 
df = pd.DataFrame(
  data,
  columns = ['dates','complete'])
print(df)
#                  dates  complete
#  0  8/25/2017 18:47:05.069722 1
#  1   9/1/2017 18:47:05.119994 0
#  2   9/8/2017 18:47:05.178768 1
#  3  9/15/2017 18:47:05.230071 1
#  4  9/22/2017 18:47:05.230071 0
#  5  9/29/2017 18:47:05.280592 1
```

Convert `` df[`date`] `` from string to datetime

```python
import pandas as pd
pd.to_datetime(df['dates'])
# 0   2017-08-25 18:47:05.069722
# 1   2017-09-01 18:47:05.119994
# 2   2017-09-08 18:47:05.178768
# 3   2017-09-15 18:47:05.230071
# 4   2017-09-22 18:47:05.230071
# 5   2017-09-29 18:47:05.280592
# Name: dates, dtype: datetime64[ns]
```

Control Statements
------------------

### Comparison

Computer programs do not only execute instructions. Occasionally, a
choice needs to be made. Such as a choice is based on a condition.
Python has several conditional operators:

| Operator | Function |
| --- | -------------- |
| > |   greater than |
| < |  smaller than |
| == |   equals |
| != |   is not |

Conditions are always combined with variables. A program can make a
choice using the if keyword. For example:

```python
x = int(input("Guess x:"))
if x == 4:
   print('Correct!')
```

In this example, *You guessed correctly!* will only be printed if the
variable x equals to four (see table above). Python can also execute
multiple conditions using the elif and else keywords.

```python
x = int(input("Guess x:"))
if x == 4:
    print('Correct!')
elif abs(4 - x) == 1:
    print('Wrong, but close!')
else:
    print('Wrong, way off!')
```

### Iteration

To repeat code, the for keyword can be used. For example, to display the
numbers from 1 to 10, we could write something like this:

```python
for i in range(1, 11):
   print('Hello!')
```

The second argument to range, *11*, is not inclusive, meaning that the
loop will only get to *10* before it finishes. Python itself starts
counting from 0, so this code will also work:

```python
for i in range(0, 10):
   print(i + 1)
```

In fact, the range function defaults to starting value of *0*, so the
above is equivalent to:

```python
for i in range(10):
   print(i + 1)
```

We can also nest loops inside each other:

```python
for i in range(0,10):
    for j in range(0,10):
        print(i,' ',j)
```

In this case we have two nested loops. The code will iterate over the
entire coordinate range (0,0) to (9,9)

Datatypes
---------

### Lists

see: <https://www.tutorialspoint.com/python/python_lists.htm>

Lists in Python are ordered sequences of elements, where each element
can be accessed using a 0-based index.

To define a list, you simply list its elements between square brackets
'\[\]':

```python
names = [
  'Albert',
  'Jane',
  'Liz',
  'John',
  'Abby']
# access the first element of the list
names[0]
# 'Albert'
# access the third element of the list
names[2] 
# 'Liz'
```

You can also use a negative index if you want to start counting elements
from the end of the list. Thus, the last element has index *-1*, the
second before last element has index *-2* and so on:

```python
# access the last element of the list
names[-1] 
# 'Abby'
# access the second last element of the list
names[-2] 
# 'John'
```

Python also allows you to take whole slices of the list by specifying a
beginning and end of the slice separated by a colon

```python
# the middle elements, excluding first and last
names[1:-1] 
# ['Jane', 'Liz', 'John']
```

As you can see from the example above, the starting index in the slice
is inclusive and the ending one, exclusive.

Python provides a variety of methods for manipulating the members of a
list.

You can add elements with append':

```python
names.append('Liz')
names
# ['Albert', 'Jane', 'Liz',
#  'John', 'Abby', 'Liz']
```

As you can see, the elements in a list need not be unique.

Merge two lists with 'extend':

```python
names.extend(['Lindsay', 'Connor'])
names
# ['Albert', 'Jane', 'Liz', 'John',
#  'Abby', 'Liz', 'Lindsay', 'Connor']
```

Find the index of the first occurrence of an element with 'index':

```python 
names.index('Liz') \# 2
```

Remove elements by value with 'remove':

```python
names.remove('Abby')
names
# ['Albert', 'Jane', 'Liz', 'John',
#  'Liz', 'Lindsay', 'Connor']
```

Remove elements by index with 'pop':

```python
names.pop(1)
# 'Jane'
names
# ['Albert', 'Liz', 'John',
#  'Liz', 'Lindsay', 'Connor']
```

Notice that pop returns the element being removed, while remove does
not.

If you are familiar with stacks from other programming languages, you
can use insert and 'pop':

```python
names.insert(0, 'Lincoln')
names
# ['Lincoln', 'Albert', 'Liz',
#  'John', 'Liz', 'Lindsay', 'Connor']
names.pop()
# 'Connor'
names
# ['Lincoln', 'Albert', 'Liz',
#  'John', 'Liz', 'Lindsay']
```

The Python documentation contains a [full list of list operations]().

To go back to the range function you used earlier, it simply creates a
list of numbers:

```python
range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(2, 10, 2)
# [2, 4, 6, 8]
```

### Sets

Python lists can contain duplicates as you saw above:

```python
names = ['Albert', 'Jane', 'Liz',
         'John', 'Abby', 'Liz']
```

When we do not want this to be the case, we can use a
[set](https://docs.python.org/2/library/stdtypes.html#set):

```python
unique_names = set(names)
unique_names
# set(['Lincoln', 'John', 'Albert', 'Liz', 'Lindsay'])
```

Keep in mind that the *set* is an unordered collection of objects, thus
we can not access them by index:

```python
unique_names[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   TypeError: 'set' object does not support indexing
```

However, we can convert a set to a list easily:

```python
unique_names = list(unique_names) 
unique_names [`Lincoln', `John', `Albert', `Liz', `Lindsay']
unique_names[0]
# `Lincoln'
```

Notice that in this case, the order of elements in the new list matches
the order in which the elements were displayed when we create the set.
We had

`set(['Lincoln', 'John', 'Albert', 'Liz', 'Lindsay'])`

and now we have

`['Lincoln', 'John', 'Albert', 'Liz', 'Lindsay'])`

You should not assume this is the case in general. That is, do not make
any assumptions about the order of elements in a set when it is
converted to any type of sequential data structure.

You can change a set's contents using the add, remove and update methods
which correspond to the append, remove and extend methods in a list. In
addition to these, *set* objects support the operations you may be
familiar with from mathematical sets: *union*, *intersection*,
*difference*, as well as operations to check containment. You can read
about this in the [Python documentation for
sets](https://docs.python.org/2/library/stdtypes.html#set).

### Removal and Testing for Membership in Sets

One important advantage of a `set` over a `list` is that **access to
elements is fast**. If you are familiar with different data structures
from a Computer Science class, the Python list is implemented by an
array, while the set is implemented by a hash table.

We will demonstrate this with an example. Let's say we have a list and a
set of the same number of elements (approximately 100 thousand):

```python
import sys, random, timeit
nums_set = set([random.randint(0, sys.maxint) for _ in range(10**5)])
nums_list = list(nums_set)
len(nums_set)
# 100000
```

We will use the [timeit](https://docs.python.org/2/library/timeit.html)
Python module to time 100 operations that test for the existence of a
member in either the list or set:

```python
timeit.timeit('random.randint(0, sys.maxint) in nums', 
              setup='import random; nums=%s' % str(nums_set), number=100)
# 0.0004038810729980469
timeit.timeit('random.randint(0, sys.maxint) in nums', 
              setup='import random; nums=%s' % str(nums_list), number=100)
# 0.398054122924804
```

The exact duration of the operations on your system will be different,
but the take away will be the same: searching for an element in a set is
orders of magnitude faster than in a list. This is important to keep in
mind when you work with large amounts of data.

### Dictionaries

One of the very important data structures in python is a dictionary also
referred to as *dict*.

A dictionary represents a key value store:

```python
person = {
  'Name': 'Albert',
  'Age': 100,
  'Class': 'Scientist'
  }
print("person['Name']: ", person['Name'])
# person['Name']:  Albert
print("person['Age']: ", person['Age'])
# person['Age']:  100
```

A convenient for to print by named attributes is

```
print("{Name} {Age}'.format(**data)) 
```
This form of printing with the format statement and a reference to data
increases readability of the print statements.


You can delete elements with the following commands:

```python
del person['Name'] # remove entry with key 'Name'
person
# {'Age': 100, 'Class': 'Scientist'}
person.clear()     # remove all entries in dict
# person
# {}
del person         # delete entire dictionary
person
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  NameError: name 'person' is not defined
```

You can iterate over a dict:

```python
person = {
  'Name': 'Albert',
  'Age': 100,
  'Class': 'Scientist'
  }
for item in person:
  print(item, person[item])

# Age 100
# Name Albert
# Class Scientist
```

### Dictionary Keys and Values

You can retrieve both the keys and values of a dictionary using the
keys() and values() methods of the dictionary, respectively:

```python
person.keys()
# ['Age', 'Name', 'Class']
person.values()
# [100, 'Albert', 'Scientist']
```

Both methods return lists. Notice, however, that the order in which the
elements appear in the returned lists (Age, Name, Class) is different
from the order in which we listed the elements when we declared the
dictionary initially (Name, Age, Class). It is important to keep this in
mind: **you cannot make any assumptions about the order in which the
elements of a dictionary will be returned by the keys() and values()
methods**.

However, you can assume that if you call keys() and values() in
sequence, the order of elements will at least correspond in both
methods. In the above example Age corresponds to 100, Name to `Albert`,
and Class to Scientist, and you will observe the same correspondence in
general as long as *keys() and values() are called one right after the
other*.

### Counting with Dictionaries

One application of dictionaries that frequently comes up is counting the
elements in a sequence. For example, say we have a sequence of coin
flips:

```python
import random
die_rolls = [
  random.choice(['heads', 'tails']) for _ in range(10)
]
# die_rolls
# ['heads', 'tails', 'heads',
#  'tails', 'heads', 'heads', 
   'tails', 'heads', 'heads', 'heads']
```

The actual list die_rolls will likely be different when you execute
this on your computer since the outcomes of the die rolls are random.

To compute the probabilities of heads and tails, we could count how many
heads and tails we have in the list:

```python
counts = {'heads': 0, 'tails': 0}
for outcome in coin_flips:
   assert outcome in counts
   counts[outcome] += 1
print('Probability of heads: %.2f' % (counts['heads'] / len(coin_flips)))
# Probability of heads: 0.70

print('Probability of tails: %.2f' % (counts['tails'] / sum(counts.values())))
# Probability of tails: 0.30
```

In addition to how we use the dictionary counts to count the elements of
coin_flips, notice a couple things about this example:

1.  We used the assert outcome in counts statement. The assert statement
    in Python allows you to easily insert debugging statements in your
    code to help you discover errors more quickly. assert statements are
    executed whenever the internal Python `__debug__` variable is set
    to True, which is always the case unless you start Python with the
    -O option which allows you to run *optimized* Python.

2.  When we computed the probability of tails, we used the built-in sum
    function, which allowed us to quickly find the total number of coin
    flips. sum is one of many built-in function you can [read about
    here](https://docs.python.org/2/library/functions.html).

Functions
---------

You can reuse code by putting it inside a function that you can call in
other parts of your programs. Functions are also a good way of grouping
code that logically belongs together in one coherent whole. A function
has a unique name in the program. Once you call a function, it will
execute its body which consists of one or more lines of code:

```python
def check_triangle(a, b, c):
return \
    a < b + c and a > abs(b - c) and \
    b < a + c and b > abs(a - c) and \
    c < a + b and c > abs(a - b)

    print(check_triangle(4, 5, 6))
```

The def keyword tells Python we are defining a function. As part of the
definition, we have the function name, check_triangle, and the
parameters of the function -- variables that will be populated when the
function is called.

We call the function with arguments 4, 5 and 6, which are passed in
order into the parameters a, b and c. A function can be called several
times with varying parameters. There is no limit to the number of
function calls.

It is also possible to store the output of a function in a variable, so
it can be reused.

```python
def check_triangle(a, b, c):
  return \
     a < b + c and a > abs(b - c) and \
     b < a + c and b > abs(a - c) and \
     c < a + b and c > abs(a - b)

    result = check_triangle(4, 5, 6)
    print(result)
```

Classes
-------

A class is an encapsulation of data and the processes that work on them.
The data is represented in member variables, and the processes are
defined in the methods of the class (methods are functions inside the
class). For example, let's see how to define a Triangle class:

```python
class Triangle(object):

  def __init__(self, length, width,
               height, angle1, angle2, angle3):
     if not self._sides_ok(length, width, height):
         print('The sides of the triangle are invalid.')
     elif not self._angles_ok(angle1, angle2, angle3):
         print('The angles of the triangle are invalid.')

     self._length = length
     self._width = width
     self._height = height

     self._angle1 = angle1
     self._angle2 = angle2
     self._angle3 = angle3

 def _sides_ok(self, a, b, c):
     return \
         a < b + c and a > abs(b - c) and \
         b < a + c and b > abs(a - c) and \
         c < a + b and c > abs(a - b)

 def _angles_ok(self, a, b, c):
     return a + b + c == 180

triangle = Triangle(4, 5, 6, 35, 65, 80)
```

Python has full object-oriented programming (OOP) capabilities, however
we can not cover all of them in a quick tutorial, so please refer to the
[Python docs on classes and
OOP](https://docs.python.org/2.7/tutorial/classes.html).

Modules
-------

Now write this simple program and save it:

```python
from __future__ import print_statement, division
print("Hello world!")
```

As a check, make sure the file contains the expected contents on the
command line:

```bash
$ cat hello.py
from __future__ import print_statement, division
print("Hello world!")
```

To execute your program pass the file as a parameter to the python
command:

```bash
$ python hello.py
Hello world!
```

Files in which Python code is stored are called **module**s. You can
execute a Python module form the command line like you just did, or you
can import it in other Python code using the import statement.

Let's write a more involved Python program that will receive as input
the lengths of the three sides of a triangle, and will output whether
they define a valid triangle. A triangle is valid if the length of each
side is less than the sum of the lengths of the other two sides and
greater than the difference of the lengths of the other two sides.:

```
"""Usage: check_triangle.py \[-h\] LENGTH WIDTH HEIGHT

Check if a triangle is valid.

Arguments:
  LENGTH     The length of the triangle.
  WIDTH      The width of the traingle.
  HEIGHT     The height of the triangle.

Options:
-h --help
"""
from __future__ import print_function, division
from docopt import docopt

if __name__ == '__main__':
  arguments = docopt(__doc__)
  a, b, c = int(arguments['LENGTH']),
            int(arguments['WIDTH']),
            int(arguments['HEIGHT'])
  valid_triangle = \
      a < b + c and a > abs(b - c) and \
      b < a + c and b > abs(a - c) and \
      c < a + b and c > abs(a - b)
  print('Triangle with sides %d, %d and %d is valid: %r' % (
      a, b, c, valid_triangle
  ))
```
      

Assuming we save the program in a file called `check_triangle.py`, we can
run it like so:

```bash
$ python check_triangle.py 4 5 6
Triangle with sides 4, 5 and 6 is valid: True
```

Let us break this down a bit.

1.  We are importing the print_function and division modules from
    python 3 like we did earlier in this tutorial. It's a good idea to
    always include these in your programs.
2.  We've defined a boolean expression that tells us if the sides that
    were input define a valid triangle. The result of the expression is
    stored in the valid_triangle variable. inside are true, and False
    otherwise.
3.  We've used the backslash symbol \\ to format are code nicely. The
    backslash simply indicates that the current line is being continued
    on the next line.
4.  When we run the program, we do the check if `__name__ ==
    '__main__'`. `__name__` is an internal Python variable that
    allows us to tell whether the current file is being run from the
    command line (value `__name__`), or is being imported by a module
    (the value will be the name of the module). Thus, with this
    statement we're just making sure the program is being run by the
    command line.
5.  We are using the docopt module to handle command line arguments. The
    advantage of using this module is that it generates a usage help
    statement for the program and enforces command line arguments
    automatically. All of this is done by parsing the docstring at the
    top of the file.
6.  In the print function, we are using [Python's string formatting
    capabilities](https://docs.python.org/2/library/string.html#format-string-syntax)
    to insert values into the string we are displaying.

## Lambda Expressions

As oppose to normal functions in Python which are defined using the `def`
keyword, lambda functions in Python are anonymous functions which do not have a
name and are defined using the `lambda` keyword. The generic syntax of a lambda
function is in form of`lambda arguments: expression`, as shown in the following
example: 

```python
greeter = lambda x: print('Hello %s!'%x)
greeter('George')
```
As you could probably guess, the result is: 

```python
>>> greeter('George')
Hello George!
```

Now consider the following examples:

```python
power2 = lambda x: x ** 2 
```
The `power2` function defined in the expression above, is equivalent to the
following definition: 

```python
def power2(x):
    return x ** 2 
```

Lambda functions are useful for when you need a function for a short period of
time. Note that they can also be very useful when passed as an argument with
other built-in functions that take a function as an argument, e.g. `filter()` and
`map()`. In the next example we show how a lambda function can be combined with
the `filer` function. Consider the array `all_names` which contains five words
that rhyme together. We want to filter the words that contain the word
`name`. To achieve this, we pass the function `lambda x: 'name' in x` as the
first argument. This lambda function returns `True` if the word `name` exists as
a sub-string in the string `x`. The second argument of `filter` function is the
array of names, i.e. `all_names`. 


```python
>>> all_names = ['surname', 'rename', 'nickname', 'acclaims', 'defame']
>>> filtered_names = list(filter(lambda x: 'name' in x, all_names))
>>> filtered_names
['surname', 'rename', 'nickname']
```

As you can see, the names are successfully filtered as we expected. 


## Generators

:o: Students can contribute this section 

## Non Blocking Threads

:o: Students can contribute this section

## Subprocess

:o: Students can contribute this section

## Queue

:o: Students can contribute this section

see:
* https://docs.python.org/3/library/queue.html

## Scheduler

:o: Students can contribute this section

see:
* https://docs.python.org/3/library/sched.html

## Python SSL

:o: Students can contribute this section

see:
* https://docs.python.org/3/library/ssl.html
* also demonstrate how you could just use supprocess ... to contarst 

