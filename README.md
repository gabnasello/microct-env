# Docker Image for processing 3D biomedical images

# Build the docker image

From the project folder, run the command below:

```bash build.sh```

# Run docker container

## Standard approach (recommended)

From the project folder, run the command below:

```docker-compose up -d```

Close the container with:

```docker-compose down```

## Alternative approach

You can run the following command:

```docker run -d -it --rm  -p 8888:8888 --volume $HOME:/home/sliceruser/work --entrypoint /bin/bash --user root --name microct gnasello/microct-env:latest```

To connect to a container that is already running ("slicer" is the container name):

```docker exec -it microct /bin/bash```

docker exec -it microct-individual /bin/bash

After use, you close the container with:

```docker rm -f microct```

# Acknowledgements

This Docker is built on [slicer/slicer-notebook](https://hub.docker.com/r/slicer/slicer-notebook)