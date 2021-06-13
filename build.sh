#!/usr/bin/env bash

# enter development environment
source ./enter-the-dojo.sh

# remove old builds
rm -rf ./build/
rm -rf ./dist/

# build source archive and wheel
python ./setup.py sdist bdist_wheel

# display tar contents
tar tzf dist/pydymenu-*tar.gz

# to upload to PyPi
# twine upload dist/*
