# Steps 

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

* Upload a file 
```
curl -X POST "http://localhost:8080/kmeans/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@model.csv;type=text/csv"
```
response:
```json
{
  "filename": "model.csv", 
  "job_id": 0
}
```

* Fit the kmeans model 
```
curl -X POST "http://localhost:8080/kmeans/fit" -H "accept: text/csv" -H "Content-Type: application/json" -d "{\"job_id\":0,\"model_params\":{\"n_clusters\":3}}"
```
response: file
```
1.000000000000000000e+00
1.000000000000000000e+00
1.000000000000000000e+00
0.000000000000000000e+00
0.000000000000000000e+00
2.000000000000000000e+00
```

* Predict using the fitted kmeans model 
```
curl -X POST "http://localhost:8080/kmeans/predict" -H "accept: text/csv" -H "Content-Type: multipart/form-data" -F "job_id=0" -F "file=@predict.csv;type=text/csv"
```
response: file 
```
1.000000000000000000e+00
0.000000000000000000e+00
```