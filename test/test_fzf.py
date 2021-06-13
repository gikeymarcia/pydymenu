#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import pydymenu
import pytest


def test_has_bin():
    assert pydymenu.has_bin("fzf") == True
    assert pydymenu.has_bin(None) == False
    assert pydymenu.has_bin("") == False
    assert pydymenu.has_bin("printf") == True


def test_missing_fzf_error(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(FileNotFoundError) as except_info:
        pydymenu.fzf(["one"])
    assert except_info.type is FileNotFoundError


# vim: set foldlevel=2:
