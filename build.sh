#!/usr/bin/env bash

# enter development environment
source ./enter-the-dojo.sh

# build source archive and wheel
python ./setup.py sdist bdist_wheel
