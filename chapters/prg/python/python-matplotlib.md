# Plotting with matplotlib


A brief overview of plotting with matplotlib along with examples is
provided. First matplotlib must be installed, which can be accomplished
with pip install as follows:

```bash
pip install matplotlib
```

We will start by plotting a simple line graph using built in numpy
functions for sine and cosine. This first step is to import the proper
libraries shown below.

```python
import numpy as np
import matplotlib.pyplot as plt
```

Next we will define the values for the x axis, we do this with the
linspace option in numpy. The first two parameters are the starting and
ending points, these must be scalars. The third parameter is optional and
defines the number of samples to be generated between the starting and
ending points, this value must be an integer. Additional parameters for
the linspace utility can be found here:

```python
x = np.linspace(-np.pi, np.pi, 16)
```

Now we will use the sine and cosine functions in order to generate y
values, for this we will use the values of x for the argument of both
our sine and cosine functions i.e. $cos(x)$.

```python
cos = np.cos(x)
sin = np.sin(x)
#cos, sin = np.cos(x), np.sin(x) will produce the same as the above
#two lines
```

You can display the values of the three parameters we have defined by
typing them in a python shell.

```python
x
array([-3.14159265, -2.72271363, -2.30383461, -1.88495559, -1.46607657,
    -1.04719755, -0.62831853, -0.20943951, 0.20943951, 0.62831853,
    1.04719755, 1.46607657, 1.88495559, 2.30383461, 2.72271363,
    3.14159265])
```

Having defined x and y values we can generate a line plot and since we
imported matplotlib.pyplot as plt we simply use plt.plot.

```python
plt.plot(x,cos)
```

We can display the plot using plt.show() which will pop up a figure
displaying the plot defined.

```python
plt.show()
```

Additionally we can add the sine line to out line graph by entering the
following.

```python
plt.plot(x,sin)
```

Invoking plt.show() now will show a figure with both sine and cosine
lines displayed. Now that we have a figure generated it would be useful
to label the x and y axis and provide a title. This is done by the
following three commands below:

```python
plt.xlabel("X - label (units)")
plt.ylabel("Y - label (units)")
plt.title("A clever Title for your Figure")
```

Along with axis labels and a title another useful figure feature may be
a legend. In order to create a legend you must first designate a label
for the line, this label will be what shows up in the legend. The label
is defined in the initial plt.plot(x,y) instance, below is an example.

```python
plt.plot(x,cos, label="cosine")
```

Then in order to display the legend the following command is issued:

```python
plt.legend(loc='upper right')
```

The location is specified by using upper or lower and left or right.
Naturally all these commands can be combined and put in a file with the
.py extension and run from the command line.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 16)
cos = np.cos(x)
sin = np.sin(x)
plt.plot(x,cos, label="cosine")
plt.plot(x,sin, label="sine")

plt.xlabel("X - label (units)")
plt.ylabel("Y - label (units)")
plt.title("A clever Title for your Figure")

plt.legend(loc='upper right')

plt.show()
```

An example of a bar chart is preceded below using data from
 [\[T:fast-cars\]](#T:fast-cars){reference-type="ref"
reference="T:fast-cars"}.

```python
import matplotlib.pyplot as plt

x = [' Toyota Prius', 'Tesla Roadster ', ' Bugatti Veyron', ' Honda Civic ', ' Lamborghini Aventador ']
horse_power = [120, 288, 1200, 158, 695]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, horse_power, color='green')
plt.xlabel("Car Model")
plt.ylabel("Horse Power (Hp)")
plt.title("Horse Power for Selected Cars")

plt.xticks(x_pos, x)

plt.show()
```

You can customize plots further by using plt.style.use(), in python 3.
If you provide the following command inside a python command shell you
will see a list of available styles.

```python
print(plt.style.available)
```

An example of using a predefined style is shown below.

```python
plt.style.use('seaborn')
```

Up to this point we have only showcased how to display figures through
python output, however web browsers are a popular way to display
figures. One example is Bokeh, the following lines can be entered in a
python shell and the figure is outputted to a browser.

```python
from bokeh.io import show
from bokeh.plotting import figure

x_values = [1, 2, 3, 4, 5]
y_values = [6, 7, 2, 3, 6]

p = figure()
p.circle(x=x_values, y=y_values)
show(p)
```
