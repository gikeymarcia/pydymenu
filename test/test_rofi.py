#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import pytest
import pydymenu
from pydymenu.system import has_bin


def test_make_rofi_object():
    assert pydymenu.rofi


def test_rofi_present():
    assert has_bin("rofi") == True


def test_rofi_absent(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(FileNotFoundError) as except_info:
        pydymenu.rofi(["one", "two", "three"])
    assert except_info.type is FileNotFoundError
