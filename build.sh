#!/usr/bin/env bash

# enter development environment
source ./enter-the-dojo.sh

# remove old builds
rm -rf ./build/
rm -rf ./dist/

# build source archive and wheel
python ./setup.py sdist bdist_wheel

# display tar contents
tar tzf dist/*tar.gz

# check render on PyPi
twine check dist/*

# upload to test.pypi.org
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# to upload to PyPi
# twine upload dist/*
