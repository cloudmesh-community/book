# Simple Introspection example

## Steps 

* (Optional) Install swagger plugin for PyCharm 

* Declare the API using the OpenAPI 3.0.2 spec provided in *api.yaml*

* Activate your Python environment.

* Install requirements.txt 
```
pip install -r requirements.txt
```

* Start the server 
```
python server.py
```

* In the second terminal you run the curl call 

```bash
curl http://localhost:8080/cloudmesh/cpu
```
