# Dockerfile {#sec:docker-file}

In order for us to build containers, we need to know what is in the
container and how to create an image representing a container. To do
this a convenient specification format called `Dockerfile` can be
used. Once a `Dockerfile` is created, we can build images from it

We showcase here the use of a dockerfile on a simple example using a
REST service.

This example is copied from the official docker documentation hosted
at

* <https://docs.docker.com/get-started/part2/#publish-the-image>

## Specification

It is best to start with an empty directory in which we create a
Dockerfile.

```bash
local$ mkdir ~/cloudmesh/docker
local$ cd ~/cloudmesh/docker
```

Next, we create an empty file called `Dockerfile`

```bash
local$ touch Dockerfile
```

We copy the following contents into the Dockerfile and after that
create a simple REST service

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
```

We also create a `requirements.txt` file that we need for installing the
necessary python packages

    Flask


The example application we use here is a student info served via a
RESTful service implemented using python flask.
It is stored in the file app.py

```python
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


To build the container image, we can use the following command:

```bash
local$ docker build -t students .
```

To run the service open a new window and cd into the directory where
you code is located. Now say

```bash
local$ docker run -d -p 4000:80 students
```

Your docker container will run and you can visit it by using the
command

```bash
local$ curl http://localhost:4000/student/albert
```

To stop the container do a

```bash
local$ docker ps
```

and locate the id of the container, e.g., 2a19776ab812, and then run this

```bash
local$ docker stop 2a19776ab812
```

To delete the docker container image, you must first stop all instances
using it and then remove the image. You can see the images with the
command


```bash
local$ docker images
```

Then you can locate all containers using that image while looking in
the IMAGE column or using a simple fgrep in case you have many
images. Stop the containers using that image and then you can say


```bash
local$ docker rm 74b9b994c9bd
```

while the number is the container id

Once you killed all containers using that image, you can remove the
image with the `rmi` command.

```bash
local$ docker rmi 8b3246425402
```

## References

The reference documentation about docker files can be found at

* <https://docs.docker.com/engine/reference/builder/>

