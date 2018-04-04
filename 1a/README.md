# Docker Build

In this file you find a docker file which pulls down a python based image and runs a webserver with hello world

## Docker Commands

Implement the following commands and check te reference guide of docker to see what the options are of the different commands

* [Build](https://docs.docker.com/engine/reference/commandline/build/)
* [Run](https://docs.docker.com/engine/reference/commandline/run/)
* [Images](https://docs.docker.com/engine/reference/commandline/images/)
* [PS](https://docs.docker.com/engine/reference/commandline/ps/)

```
docker build -t "xxx" .
docker run -it -p 5000:5000 xxx
```