#!/usr/bin/env bash
figlet "continous TDD"
while true; do
    fd -e py | entr -rcd python -m pytest -vvv .
    sleep 1
done
