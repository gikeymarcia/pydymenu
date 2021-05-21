#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

__author__ = "Mikey Garcia, @gikeymarcia"

import pydymenu
from pydymenu import fzf as fuzzy


def test_fzf_creation():
    fzf = pydymenu.fzf()
    print(type(fzf))
    print(type(pydymenu))
    assert fzf() == "running"
