# Create a Docker Image for processing microCT images

## How it works

- The ```Dockerfile``` creates a Docker Image based on  [slicer/slicer-notebook](https://hub.docker.com/r/slicer/slicer-notebook).
- It adds Slicer extensions

## Create a new image

First, clone the repo:

```git clone https://github.com/gabnasello/microct-env.git``` 

and run the following command to build the image (you might need sudo privileges):

```docker build --no-cache -t microct-env:latest .```

Then you can follow the instructions in the [Docker repository](https://hub.docker.com/repository/docker/gnasello/microct-env) to use the virtual environment.

Enjoy data science!