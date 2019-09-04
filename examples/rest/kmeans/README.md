#Steps 

- install swagger plugin for PyCharm 

- Declare the API using the OpenAPI 3.0.0 spec 

- Install  openapi-generator-cli for OpenAPI 3.0 code generation 
https://openapi-generator.tech/docs/installation.html

- generate the python code
```
openapi-generator-cli generate -i ~/git/rest-py-test/service.yaml -g python-flask -o ~/git/rest-py-test/flaskConn 
```

- make the changes in the flaskConn/open_api_server/controllers/default_controller.py 



- upload file 

curl -X POST "http://localhost:8080/api/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "body=@/home/niranda/Desktop/file.txt;type=text/plain"

curl -X POST "http://localhost:8080/api/download" -H "accept: text/plain" -H "Content-Type: application/json" -d "{\"id\":\"11111\"}"

openapi-generator-cli generate -i ~/git/rest-py-test/api.yaml -g python-flask -o ~/git/rest-py-test/flaskConn



python -m openapi_server

