#!/bin/bash -lx
echo "params: $1"
cd src
serverless plugin install -n serverless-python-requirements
serverless $1