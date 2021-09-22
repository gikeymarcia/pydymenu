#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import pytest

import pydymenu
from pydymenu.demo_data import gen_options, list_options
from pydymenu.exceptions import MissingProgram


def test_missing_fzf_error(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(MissingProgram) as except_info:
        pydymenu.fzf(["one"])
    assert except_info.type is MissingProgram


@pytest.mark.parametrize(
    "kwargs, flags",
    [
        ({}, ["--prompt", " > ", "--no-multi", "-i"]),
        ({"prompt": None}, ["--prompt", " > ", "--no-multi", "-i"]),
        ({"prompt": "go larry!"}, ["--prompt", "go larry!", "--no-multi", "-i"]),
        ({"case_sensitive": True}, ["--prompt", " > ", "--no-multi", "+i"]),
        ({"multi": True}, ["--prompt", " > ", "--multi", "-i"]),
        ({"multi": True, "case_sensitive": True}, ["--prompt", " > ", "--multi", "+i"]),
        (
            {"preview": "git diff HEAD -- {}"},
            ["--prompt", " > ", "--no-multi", "-i", "--preview", "git diff HEAD -- {}"],
        ),
        (
            {"preview": "git diff HEAD -- {}", "multi": True},
            ["--prompt", " > ", "--multi", "-i", "--preview", "git diff HEAD -- {}"],
        ),
    ],
)
def test_flag_calculation(kwargs, flags):
    fzf = pydymenu.FzfProtocol(gen_options, **kwargs)
    assert (fzf.flags) == flags


# vim: set foldlevel=2:
