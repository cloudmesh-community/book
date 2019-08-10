# StopWatch

Often you find yourself in a situation where you like to measure the
time between two events. We provide a simple  `StopWatch` that allows
you not only to measure a number of times, but also to print them out in
a convenient format.

```python
from cloudmesh.common.StopWatch import StopWatch
import os

watch = StopWatch()

watch.start("test")
os.sleep(1)
watch.stop("test")

print (watch["test"])
```

To print them, you can aslo use

```python
Stopwatch.benchmark.print()
```