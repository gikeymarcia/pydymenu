#!/usr/bin/env bash
# Mikey Garcia, @gikeymarcia

env=./env
if [ -d $env ]; then
    rm -rf $env
fi
python -m pip install --user virtualenv
python -m virtualenv $env
