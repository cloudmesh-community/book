# Week 3: Python for Cloud Computing 

Start of Project Selection 


## Lab Activities

### Venv in python 3


```
python -m venv ~/ENV3
```

* How do you activate the virtual env in your OS? 

* How do you modify your `.bashrc` file?

* Why do you need to use `venv` for this class? 

  - This is the same answer as why people use venv?

### Anaconda

This Lab has only to be done by those useing anaconda.

* What problems may you encounter when using anaconda as python developer?

* Let us assume you use anacondaconda on your virtual machines in the cloud. Let
  us assume you start 1000 vms all using anacondaconda. What is the overhead in
  wasted space on these machines if you just wanted to use as simple
  regular python program on these VMs?
  
* How do you find out how much space is used by your program and its
  libraries?
 
* How do you switch between anaconda and regular python 3.7.4

* What is the difference between conda, miniconda, anaconda?


### Dicts

We like to remind you about dicts in python. 

Read up upon dicts and experiment with them.

* How do you merge the content of two dicts?

### f-Strings in Python 3

Python 3 provides some very nice way of using variable names as part 
of string manupulations. 

* Locate the PEP 498 and study it:
<https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498>

Try out the following

```python
test = "Gregor"
msg = f"This is a test {test}"
print (msg)
```

```python
def f(test):
    msg = f"This is a test {test}".format(**locals())
    print (msg)
```

```python
from cloudmesh.common.debug import VERBOSE
d = {"test": "Gregor"}
VERBOSE(d)
```

In one of the examples `locals()` is used. 

* WHat does loacls do?
* What does ** in the format statement do?


### Classes 

* What is self in classes?
* Why does self needs to be used in regular method definitions?
* What can I do with __init__ and why is it used?
* What is cls and @classmethods?
* WHy woudl one use @statucmethod?

### StopWatch

### Benchmark

### Computer System



### CMD5

<https://github.com/cloudmesh/cloudmesh-cmd5>

* What is the purpose of cmd5?
* Generate your own command in cmd5. Call the command

### Python Modules

* What is a setup.py file
* What is the difference between `pip install .` and `pip install -e .`
* How do I uninstall a python module?
* My python is broken, What do you do now?
