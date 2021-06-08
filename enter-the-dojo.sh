#!/usr/bin/env bash

figlet "enter the dojo"
ls -l

source env/bin/activate
python -m pip install -r ./requirements_dev.txt
python -m pip list
