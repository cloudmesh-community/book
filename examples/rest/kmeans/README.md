# Steps 

- Install swagger plugin for PyCharm 

- Declare the API using the OpenAPI 3.0.0 spec 
```yaml
openapi: 3.0.0
info:
  title: Sample Pet Store App
  description: This is a sample server for a pet store.
  termsOfService: http://example.com/terms/
  contact:
    name: API Support
    url: http://www.example.com/support
    email: support@example.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  version: 0.0.1

servers:
  - url: http://localhost:8080/kmeans

paths:
  /upload:
    post:
      summary: upload input
      operationId: kmeans.upload_file
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
        '200':
          description: successful file upload
          content:
            application/json:
              schema:
                type: object
                properties:
                  job_id:
                    type: integer
                  filename:
                    type: string

  /fit:
    post:
      summary: fit a kmeans model
      operationId: kmeans.kmeans_fit
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                job_id:
                  type: integer
                model_params:
                  type: object
                  additionalProperties: {}
      responses:
        '200':
          description: labels of the provided points
          content:
            text/csv:
              schema:
                type: string
                format: binary


  /predict:
    post:
      summary: predict on a previously built model
      operationId: kmeans.kmeans_predict
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                job_id:
                  type: string
                file:
                  type: string
                  format: binary
      responses:
        '200':
          description: successful completion
          content:
            text/csv:
              schema:
                type: string
                format: binary

```

- Install requirements.txt 
```
pip install -r requirements.txt
```

- Start the server 
```
python server.py
```

- Upload a file 
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

- Fit the kmeans model 
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

- predict using the fitted kmeans model 
```
curl -X POST "http://localhost:8080/kmeans/predict" -H "accept: text/csv" -H "Content-Type: multipart/form-data" -F "job_id=0" -F "file=@predict.csv;type=text/csv"
```
response: file 
```
1.000000000000000000e+00
0.000000000000000000e+00
```