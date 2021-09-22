# !/usr/bin/env python3
#  Mikey Garcia, @gikeymarcia
#  https://github.com/gikeymarcia/pydymenu

import pytest

import pydymenu
from pydymenu.demo_data import gen_options
from pydymenu.exceptions import MissingProgram
from pydymenu.system import missing_binary


def test_make_rofi_object():
    assert pydymenu.rofi


def test_rofi_present():
    assert missing_binary("rofi") == False


def test_rofi_absent(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(MissingProgram) as except_info:
        pydymenu.rofi(["one", "two", "three"])
    assert except_info.type is MissingProgram


@pytest.mark.parametrize(
    "kwargs, flags",
    [
        ({}, ["-p", " > ", "-i"]),
        ({"prompt": None}, ["-p", " > ", "-i"]),
        ({"prompt": "go larry!"}, ["-p", "go larry!", "-i"]),
        ({"case_sensitive": True}, ["-p", " > ", "-case-sensitive"]),
        ({"multi": True}, ["-p", " > ", "-multi-select", "-i"]),
        ({"multi": True, "prompt": "do it"}, ["-p", "do it", "-multi-select", "-i"]),
        (
            {"multi": True, "case_sensitive": True},
            ["-p", " > ", "-multi-select", "-case-sensitive"],
        ),
        # TODO ignore extra args? Not sure if this matters
        # ({"preview": "git diff HEAD -- {}"}, ["-p", " > "]),
    ],
)
def test_flag_calculation(kwargs, flags):
    rofi = pydymenu.RofiProtocol(gen_options, **kwargs)
    assert (rofi.flags) == flags
