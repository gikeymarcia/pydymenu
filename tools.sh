#!/usr/bin/env bash
# Mikey Garcia, @gikeymarcia

function _rm_virtual_env () {
    local venv_dir="$1"
    _print_banner remove virtual env
    if [ -d  "$venv_dir" ]; then
        rm -rv "$venv_dir"
    fi
}

function _clean_environment() {
    local venv_dir="$1"
    _rm_virtual_env "$venv_dir"
    create_venv "$venv_dir"
    enter_the_dojo "$venv_dir"
}

function _enter_venv() {
    local venv_dir="$1"
    local activator="${venv_dir}/bin/activate"
    if [ ! -f "$activator" ]; then
        echo "Could not find activator at ${activator}"
    else
        _print_banner enter the dojo
        source "$activator"
    fi
}

function _install_requirements() {
    python -m pip install --upgrade pip
    python -m pip install -r ./requirements_dev.txt
    python -m pip list
}

function enter_the_dojo(){
    local venv_dir="$1"
    _enter_venv "$venv_dir"
    _install_requirements
}

function _print_banner() {
    figlet "$@" | lolcat
    sleep 0.4
}

function create_venv (){
    _print_banner create virtual env
    $(which python3) -m pip install --user virtualenv
    $(which python3) -m virtualenv "$1"
}

function _smart_loader () {
    # If the virtual environment isn't configured create it, otherwise enter
    local venv_dir="$1"
    [ ! -d "$venv_dir" ] && create_venv "$venv_dir"
    enter_the_dojo "$venv_dir"
}

function _build_project () {
    _clean_environment "$2"
    # remove old builds
    rm -rv "${1}/build" && rm -rv "${1}/dist"
    python ./setup.py sdist bdist_wheel     # build source archive and wheel
    tar tzf dist/*tar.gz                    # display tar contents
    twine check dist/*                      # check render on PyPi

    if [ -z "$3" ]; then
        echo "choose either: 'test' or 'pypi' to upload build."
    elif [ "$3" == "test" ]; then
        # upload to test.pypi.org
        twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    elif [ "$3" == "pypi" ]; then
        # to upload to PyPi
        twine upload dist/*
    fi
}

function _continuous_testing() {
    # TODO check for the apps and install if needed
    _print_banner "Test Driven Development!"
    python -m pytest -v "$1"
    while true; do
        fdfind -e py | entr -rndp python -m pytest -v "$1"
        sleep 0.5
    done
}

clear
# set important variables then use _smart_loader
virtual_env_dir=$(realpath "./env")
project_dir=$(realpath ".")
_smart_loader "$virtual_env_dir"

function dojo () {
    if [ -z "$1" ]; then
        echo -e "COMMANDS:\n"
        echo new -- create a clean new development virtual environment
        echo req -- install requirements into current environment
        echo smart -- run the smart loader for quickest development
        echo test -- run continuous test driven development using pytest
        echo build -- make a build and check it for pypi render
        echo build test -- make a build and upload it to test.pypi.org
        echo build pypi -- make a build and upload it to pypi.org
    elif [ "$1" == "new" ]; then
        _clean_environment "$virtual_env_dir"
    elif [ "$1" == "req" ]; then
        _enter_venv "$virtual_env_dir" && _install_requirements "$virtual_env_dir"
    elif [ "$1" == "smart" ]; then
        _smart_loader "$virtual_env_dir"
    elif [ "$1" == "test" ]; then
        _continuous_testing "$project_dir"
    elif [ "$1" == "build" ]; then
        _build_project "$project_dir" "$virtual_env_dir" "$2"
        # dojo build
        # dojo build test
        # dojo build pypi
    fi
}

