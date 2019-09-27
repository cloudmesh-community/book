# Dictionaries

## Dotdict

For simple dictionaries we sometimes like to simplify the notation with a `.` instead of using the `[]`:

You can achieve this with dotdict

```python
from cloudmesh.common.dotdict import dotdict

data = {
    "name": "Gregor"
}

data = dotdict(data)
```

Now you can either call

```python
data["name"]
```

or

```python
data.name
```

This is espacially useful in if conditions as it may be easier to read and write

```python
if data.name is "Gregor":

    print("this is quite readable")
```

and is the same as

```python
if data["name"] is "Gregor":

    print("this is quite readable")
```

For more features, see API: [dotdict](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=dotdict#module-cloudmesh.common.dotdict)


## FlatDict

In some cases it is useful to be able to flatten out dictionaries that
contain dicts within dicts. For this we can use `FlatDict`.

```
from cloudmesh.common.Flatdict import FlatDict

data = {
    "name": "Gregor"
    "address": {
        "city": "Bloomington",
        "state": "IN"

    }
}

flat = FlatDict(data, sep=".")

```

This will be converted to a dict with the following structure.

```python

flat = {
    "name": "Gregor"
    "address.city": "Bloomington",
    "address.state": "IN"
}
```

With `sep` you can change the sepaerator between the nested dict
attributes. For more features, see API:
[dotdict](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=flatdict#module-cloudmesh.common.FlatDict)


## Printing Dicts

In case we want to print dicts and lists of dicts in various formats, we
have included a simple `Printer` that can print a dict in yaml, json,
table, and csv format.

The function can even guess from the passed parameters what the input format is
and uses the appropriate internal function.

A common example is 

```python
from pprint import pprint
from cloudmesh.common.Printer import Printer

data = [
    {
        "name": "Gregor",
        "address": {
            "street": "Funny Lane 11",
            "city": "Cloudville"
        }
    },
    {
        "name": "Albert",
        "address": {
            "street": "Memory Lane 1901",
            "city": "Cloudnine"
        }
    }
]


pprint(data)

table = Printer.flatwrite(data,
                          sort_keys=["name"],
                          order=["name", "address.street", "address.city"],
                          header=["Name", "Street", "City"],
                          output='table')

print(table)
```


For more features, see API: [Printer](https://cloudmesh.github.io/cloudmesh-manual/api/cloudmesh.common.html?highlight=flatdict#module-cloudmesh.common.Printer)

More examples are available in the source code as [tests](https://github.com/cloudmesh/cloudmesh-common/tree/master/tests) 
