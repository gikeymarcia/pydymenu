#!/usr/bin/env bash
# Mikey Garcia, @gikeymarcia
# meant to be sourced before returning to development

figlet "enter the dojo"
ls -l

source env/bin/activate
python -m pip install -r ./requirements_dev.txt
python -m pip list
