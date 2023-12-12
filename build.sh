#!/bin/bash

REGISTRY=registry.k3s.kippel.de:5000
IMAGE=/development/flask/simple-quiz
TAG=v0.9

cache=''
[[ x$1 == x-no ]] && { cache='--no-cache'; }

docker build --progress=plain $cache -t ${REGISTRY}${IMAGE}:${TAG} . 
docker push ${REGISTRY}${IMAGE}:${TAG} 

exit 0

