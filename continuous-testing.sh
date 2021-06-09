#!/usr/bin/env bash
figlet "continous TDD"
while true; do
    fd -e py | entr -rpcd python -m pytest .
done
