# Dockefile

In order for us to build containers, we need to know what is in the
container and how to create an image representing a container. To do
this a convenient specification format called `Dockerfile` can be
used. Once a `Dockerfile` is created, we can build images from it

We showcase here the use of a dockerfile on a simple example using a
REST service.

This example is copied from the officil docker documentation hosted
at

* <https://docs.docker.com/get-started/part2/#publish-the-image>

## Specification

It os best to start with an empty directory in which we create a
Dockerfile.

```console
$ mkdir ~/cloudmesh/docker
$ cd ~/cloudmesh/docker
```

Next, we create an empty file called `Dockerfile`

```console
$ touch Dockerfile
```

We copy the following contents into the Dockerfile and after that
create a simple REST service

```
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

We also create a `requirements.txt` file that we need for installing the
necessary python packages

requirements.txt

```
Flask
Eve
```

The application we install is using a Redis database and a Flask
service that includes a visit counter and returns the hostname of the
fisiting host. IT is stored in the file app.py

```
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/student/albert')
def alberts_information():
    data = {
        'firstname': 'Albert',
        'lastname': 'Zweistsein',
        'university': 'Indiana University',
        'email': 'albert@example.com'
        }
    return jsonify(**data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
```


To build the container, we can use the following command:

```
docker build -t hello .
```

To run the service open a new window and cd into the directory where
you code is located. Now say

```
docker run -d -p 4000:80 hello
``

Your docker container will run and you can visit it by using the
command

```
$ curl http://localhost:4000/student/albert
```

To stop the container do a

```
$ docker ls
```

and locate the id of the contehaine 


docker container stop 2a19776ab812


## Refernces

The refence documentation about docker files can be found at 

* <https://docs.docker.com/engine/reference/builder/>

