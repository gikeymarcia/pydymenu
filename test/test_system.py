#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from pydymenu.system import missing_binary
import pytest
from pathlib import Path


def test_has_bin():
    assert missing_binary("fzf") == False
    assert missing_binary("rofi") == False
    assert missing_binary("") == True
    assert missing_binary("printf") == False


@pytest.mark.parametrize("wrong_types", [None, {}, 127, Path.home()])
def test_missing_binary_throws_value_errors(wrong_types):
    with pytest.raises(ValueError) as except_info:
        missing_binary(wrong_types)
    assert except_info.type == ValueError


# vim: set foldlevel=2:
