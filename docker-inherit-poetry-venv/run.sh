#!/bin/bash

# Build base image that uses poetry
docker build -f base/Dockerfile --tag local:base base

docker run local:base

# Build override image that then uses venv used above
docker build -f override/Dockerfile --tag local:override override

docker run local:override