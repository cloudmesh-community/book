# Dictionaries

## Dotdict

For simple dictionaries we sometimes like to simplify the notation with a . instead of using the `[]`:

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

if data["name"] is "Gregor":

    print("this is quite readable")
```


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

flat = FlatDict(data)

```

This will be converted to a dict with the following structure.

```python 

flat = {
    "name": "Gregor"
    "address.city": "Bloomington",
    "address.state": "IN"
}
```

