#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

from pydymenu.system import has_bin
import pytest
from pathlib import Path


def test_has_bin():
    assert has_bin("fzf") == True
    assert has_bin("rofi") == True
    assert has_bin("") == False
    assert has_bin("printf") == True


@pytest.mark.parametrize("wrong_types", [None, {}, 127, Path.home()])
def test_has_bin_throws_value_errors(wrong_types):
    with pytest.raises(ValueError) as except_info:
        has_bin(wrong_types)
    assert except_info.type == ValueError


# vim: set foldlevel=2:
