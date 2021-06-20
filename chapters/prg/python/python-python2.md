## Python 3 Features in Python 2

In this course we want to be able to seamlessly switch between python 2
and python 3. Thus it is convenient from the start to use python 3
syntax when it is supported also in python 2. One of the most used
functions is the print statement that has in python 3 parentheses. To
enable it in python 2 you just need to import this function:

```python
from __future__ import print_function, division
```

The first of these imports allows us to use the print function to output
text to the screen, instead of the print statement, which Python 2 uses.
This is simply a 
[design decision](https://www.python.org/dev/peps/pep-3105/)
that better reflects Python's underlying philosophy.

Other functions such as the division also behave differently. Thus we
use

```python
from __future__ import division
```

This import makes sure that the 
[division operator](https://www.python.org/dev/peps/pep-0238/)
behaves in a way a
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
