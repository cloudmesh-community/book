# StopWatch

Often you find yourself in a situation where you like to measure the
time between two events. We provide a simple  `StopWatch` that allows
you not only to measure a number of times, but also to print them out in
a convenient format.

```python
from cloudmesh.common.StopWatch import StopWatch
import os


StopWatch.start("test")
os.sleep(1)
StopWatch.stop("test")

print (StopWatch.get("test"))
```

To print them, you can aslo use

```python
Stopwatch.benchmark.print()
```

For more features, please seee [StopWatch](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=stopwatch#module-cloudmesh.common.StopWatch)