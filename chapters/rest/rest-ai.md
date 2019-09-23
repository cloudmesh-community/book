# REST AI services Example {#sec:restai-kmeans}

This is a more involved example which uses OpenAPI 3.0 specification to invoke 
[![Video](images/video.png) K-means Clustering](https://www.youtube.com/watch?v=aGRdp4TKc4c&list=PLy0VLh_GFyz9fRbuhUS59rUThN_G1VCdX&index=2) 
routine in scikit-learn [@scik2]. Scikit-learn k-means user-guide can be found 
Scikit-learn K-Means package [@scikitlearn-kmeans].  

This involves the following. 

* Upload a file with points to create the k-means clustering model.
* Method to call scikit-learn KMeans module 
* Upload a file with points that need to be predicted and return a file 
  with the predicted cluster IDs. 
* Additionally, scikit-learn KMeans module provides routines to get the cluster 
  centers, labels, etc. which can also be exposed as REST services.   

To create the REST services, we would be using OpenAPI 3.0 REST service via
 introspection.  

## Service Endpoints/ Paths 

###  Path *kmeans/upload* 

A POST request with a file containing points to create the k-means clustering
 model. POST content would be *multipart/form-data*.  


For an example consider the following 6 points in XY dimensions,

```
1, 2
1, 4
1, 0
10, 2
10, 4
10, 0 
```

Curl command: 

```bash
$ curl -X POST "http://localhost:8080/kmeans/upload" \
        -H "accept: application/json" \ 
        -H "Content-Type: multipart/form-data" \ 
        -F "file=@model.csv;type=text/csv"
```

Service implementation would look like this. File content will be received as a 
[*werkzeug.datastructures.FileStorage*](https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.FileStorage) 
object in *Flask*, which can be used to stream into the filesystem. Backend
 keeps two dicts to map Job ID to file and vise-versa (*inputs* and *inputs_r*). 
 
```python
def upload_file(file=None):
    filename = file.filename

    in_file = INPUT_DIR + '/' + filename
    if not os.path.exists(in_file):
        file.save(in_file)  # save the input file

    if in_file not in inputs_r:
        job_id = len(inputs)
        inputs.update({job_id: in_file})
        inputs_r.update({in_file: job_id})
    else:
        job_id = inputs_r[in_file]

    return jsonify({'job_id': job_id, 'filename': filename})
```

If the request is successful, a *JSON* will be returned with the file name and 
the associated job ID. Job ID can be considered ID that would connect, inputs to 
the models and the predicted outputs. 

```
{
  "filename": "model.csv", 
  "job_id": 0
}
```

### Path *kmeans/fit*

A POST request with a *JSON* body containing Job ID and model parameters that 
need to passed on to the scikit-learn KMeans model initialization such as, 
number of clusters (n_clusters), maximum iterations (max_iter), etc. 

Example:

```
{
  "job_id": 0,
  "model_params": {
    "n_clusters": 3
  }
}
```

curl command:

```bash
$ curl -X POST "http://localhost:8080/kmeans/fit" \
        -H "accept: text/csv" \
        -H "Content-Type: application/json" \
        -d "{\"job_id\":0,\"model_params\":{\"n_clusters\":3}}"
```
  
 Service implementation looks like this. POST request body will be populated as 
 a dict and passed on to the method by  Flask (*body*). Once the model is 
 fitted, it will be put into a in memory dict (*models*) against its Job ID. 
 Labels will be written to disk as a file, and the content will be returned as a 
 CSV. 
  
 ```python
def kmeans_fit(body):
    print(body)

    job_id = body['job_id']

    if job_id not in inputs or not os.path.exists(inputs[job_id]):
        abort(500, "input file missing for job id " + str(job_id))
        return
    in_file = inputs[job_id]

    X = np.genfromtxt(in_file, delimiter=",")  # create the model

    params = dict(default_model_params)
    params.update(body['model_params'])

    kmeans = KMeans(**params).fit(X)

    models.update({job_id: kmeans})  # add the model in to the dict

    labels = OUTPUT_DIR + "/" + str(job_id) + ".labels"
    np.savetxt(labels, kmeans.labels_, delimiter=",")

    return send_file(labels)
```
  
The response CSV file will be returned with the corresponding labels for the 
input points. 

 ```
1.000000000000000000e+00
1.000000000000000000e+00
1.000000000000000000e+00
0.000000000000000000e+00
0.000000000000000000e+00
2.000000000000000000e+00
```
 
 ### Path *kmeans/predict* 
 
 A POST request with a file containing the points to be predicted and the 
 corresponding Job ID as *multipart/form-data*. 
 
 ```
job_id=0
```

Points to be predicted 

```
0, 0
12, 3
```

curl command:

```bash
$ curl -X POST "http://localhost:8080/kmeans/predict" \
        -H "accept: text/csv" \
        -H "Content-Type: multipart/form-data" \ 
        -F "job_id=0" \
        -F "file=@predict.csv;type=text/csv"
```

Service implementation looks like this. Note that there is a strange behavior in 
*Flask* with *Connextion* where the file content will be passed on to the
 *file* object as a [*werkzeug.datastructures.FileStorage*](https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.FileStorage) 
object but the Job ID is passed as a dict to *body* object.  

```python
def kmeans_predict(body, file=None):
    job_id = int(body['job_id'])

    if job_id in models:
        p_file = OUTPUT_DIR + '/' + str(job_id) + '.p'
        file.save(p_file)

        p = np.genfromtxt(p_file, delimiter=',')  # read the predictions

        result = models[job_id].predict(p)

        print(result)

        res_file = OUTPUT_DIR + "/" + str(job_id) + ".out"
        np.savetxt(res_file, result, delimiter=",")

        return send_file(res_file)

    else:
        abort(500, "model not found for job id " + str(job_id))
        return
```


The response would send out the corresponding labels of the passed points as a 
CSV file. 

```
1.000000000000000000e+00
0.000000000000000000e+00
```

## Files

Files of this example can be found 
[here](https://github.com/cloudmesh-community/book/tree/master/examples/rest/kmeans).

* Open API 3 service definitions - 
  [api.yaml](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/api.yaml)
* Flask server - 
  [server.py](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/server.py) 
* Kmeans service implementation - 
  [kmeans.py](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/kmeans.py)
* Python requirements - 
  [requirements.txt](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/requirements.txt)
* Example files 
  [model.csv](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/model.csv) 
  and 
  [predict.csv](https://github.com/cloudmesh-community/book/blob/master/examples/rest/kmeans/predict.csv) 


## Running the example 

* Go to the example directory. 
* Activate the Python3 venv used for *Cloudmesh* 
* Install requirements.txt 

```bash
$ pip install -r requirements.txt
```

* Start the server 

```bash
$ python server.py
```

* Upload a file 

```bash 
$ curl -X POST "http://localhost:8080/kmeans/upload" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@model.csv;type=text/csv"
```

* Fit the kmeans model 

```bash
$ curl -X POST "http://localhost:8080/kmeans/fit" \
    -H "accept: text/csv" \
    -H "Content-Type: application/json" \
    -d "{\"job_id\":0,\"model_params\":{\"n_clusters\":3}}"
```

* Predict using the fitted kmeans model 

```bash
$ curl -X POST "http://localhost:8080/kmeans/predict" \
    -H "accept: text/csv" \
    -H "Content-Type: multipart/form-data" \
    -F "job_id=0" \
    -F "file=@predict.csv;type=text/csv"
```

* Additionally, you can access the Swagger UI for *kmeans* service in your Flask 
  server from [here](http://localhost:8080/kmeans/ui/)

## Notes

* Above services can easily be combined together in the backend to accept a 
  model file, together with a prediction input 
* File and to return the predicted output file (synchronous operation). But 
  usually, we can expect AI jobs to be long running, hence the services would 
  need to be handled asynchronously. 
* Additionally, once a model is fitted, users should be able to reuse the model 
  for multiple predictions. Hence it is sensible to separate out model fitting 
  and predictions into separate services.        


