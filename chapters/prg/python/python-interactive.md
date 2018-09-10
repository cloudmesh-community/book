Interactive Python
------------------

Python can be used interactively. You can enter the interactive mode by
entering the interactive loop by executing the command:

```python
$ python
```

You will see something like the following:

```python
Python 2.7.13 (default, Nov 19 2016, 06:48:10)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the prompt used by the interpreter. This is similar to bash
where commonly `$` is used.

Sometimes it is convenient to show the prompt when illustrating an
example. This is to provide some context for what we are doing. If you
are following along you will not need to type in the prompt.

This interactive python process does the following:

-   *read* your input commands

-   *evaluate* your command

-   *print* the result of evaluation

-   *loop* back to the beginning.

This is why you may see the interactive loop referred to as a **REPL**:
**R**ead-**E**valuate-**P**rint-**L**oop.

REPL (Read Eval Print Loop)
---------------------------

There are many different types beyond what we have seen so far, such as
**dictionaries**s, **list**s, **set**s. One handy way of using the
interactive python is to get the type of a value using type():

\`\`\`python \>\>\> type(42) \<type 'int'\> \>\>\> type(hello) \<type
'str'\> \>\>\> type(3.14) \<type 'float'\>

You can also ask for help about something using help():

```python
>>> help(int)
>>> help(list)
>>> help(str)
```

Using help() opens up a help message within a pager. To navigate you can
use the spacebar to go down a page w to go up a page, the arrow keys to
go up/down line-by-line, or q to exit.

Interpreter
-----------

Although the interactive mode provides a convenient tool to test
things out you will see quickly that for our class we want to use the
python interpreter from the commandline. Let us assume the program is
called `prg.py`. Once you have written it in that file you simply can call it with

```bash
python prg.py
```

It is important to name the program with meaningful names.

Python 3 Features in Python 2
-----------------------------

In this course we want to be able to seamlessly switch between python 2
and python 3. Thus it is convenient from the start to use python 3
syntax when it is supported also in python 2. One of the most used
functions is the print statement that has in python 3 parentheses. To
enable it in python 2 you just need to import this function:

```python
>>> from __future__ import print_function, division
```

The first of these imports allows us to use the print function to output
text to the screen, instead of the print statement, which Python 2 uses.
This is simply a [design
decision](https://www.python.org/dev/peps/pep-3105/) that better
reflects Python's underlying philosophy.

Other functions such as the division also behave differently. Thus we
use

```python 
>>> from __future__ import division
```

This import makes sure that the [division
operator](https://www.python.org/dev/peps/pep-0238/) behaves in a way a
newcomer to the language might find more intuitive. In Python 2,
division / is *floor division* when the arguments are integers, meaning
that the following

```python 
(5 / 2 == 2) is True
```

In Python 3, division / is a floating point division, thus

```python 
(5 / 2 == 2.5) is True
```
