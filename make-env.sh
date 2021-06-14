#!/usr/bin/env bash
# shellcheck disable=SC2086

# install dependencies (Ubuntu)
dev_dep="entr fd-find figlet"
runtime_dep="fzf rofi dmenu"
sudo apt install -y $dev_dep $runtime_dep

# install virtualenv package
python -m pip install --user virtualenv

# destroy and recreate the environment
rm -rv ./env
python -m virtualenv env
