#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import pydymenu
import pytest
from pydymenu.fzf import process_fzf_opts


def test_missing_fzf_error(monkeypatch):
    monkeypatch.setenv("PATH", "")
    with pytest.raises(FileNotFoundError) as except_info:
        pydymenu.fzf(["one"])
    assert except_info.type is FileNotFoundError


@pytest.mark.parametrize(
    "opt_dict, flags",
    [
        ({}, ["--no-multi", "-i"]),
        ({"prompt": None}, ["--no-multi", "-i"]),
        ({"prompt": "go larry!"}, ["--prompt", "go larry!", "--no-multi", "-i"]),
        ({"case_sensitive": True}, ["--no-multi", "+i"]),
        ({"multi": True}, ["--multi", "-i"]),
        ({"multi": True, "case_sensitive": True}, ["--multi", "+i"]),
        (
            {"preview": "git diff HEAD -- {}"},
            ["--no-multi", "-i", "--preview", "git diff HEAD -- {}"],
        ),
        (
            {"preview": "git diff HEAD -- {}", "multi": True},
            ["--multi", "-i", "--preview", "git diff HEAD -- {}"],
        ),
    ],
)
def test_process_fzf_opts(opt_dict, flags):
    assert process_fzf_opts(opt_dict) == flags


# vim: set foldlevel=2:
