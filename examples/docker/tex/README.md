# Draft: Create latex container with book checked out

## Build the image

    docker build -t cloudmesh-tex .


## Run the container in interactive mode

    docker run -it cloudmesh-tex bash


## Upload the image to dockerhub

TBD

## Test if the book can be compiled

    make pdflatex

remember this only does one pdflatex to check the syntax, not compilet the book

## Compile the entire book 

FOR THIS WE NEED TO CHNAGE THE MAKEFILE TO NOT DO REPETED COMPILES

right now we can do make, but need to do something like 

    make once

that seems a nice name - not yet working


## Running from docker hub

    docker run -it laszewski/cloudmesh-tex:0.0.1
