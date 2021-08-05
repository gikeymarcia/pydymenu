#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import subprocess as sp
from sys import path as sys_path
from typing import Union, List

from pydymenu.console import console
from pydymenu.system import has_bin, newline_joined_bytestream, process_stdout


def fzf(
    items: List[str],
    prompt: Union[str, None] = None,
    multi: bool = False,
    case_sensitive: bool = False,
    preview: Union[str, None] = None,
) -> Union[List[str], None]:
    """Take list of strings and returns selection list or None."""
    if not has_bin("fzf"):
        err_msg = f"Could not locate `fzf` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _fzf_dict = {
        "prompt": prompt,
        "multi": multi,
        "case_sensitive": case_sensitive,
        "preview": preview,
    }
    return _run_fzf_with_list(items, **_fzf_dict)


def _run_fzf_with_list(menu_entries: List[str], **kwargs) -> Union[None, List[str]]:
    options = process_fzf_opts(kwargs)
    _fzf_process = sp.run(
        ["fzf"] + options,
        input=newline_joined_bytestream(menu_entries),
        stdout=sp.PIPE,
    )
    # console.log(f"{_fzf_process = }")
    return process_stdout(_fzf_process)


def process_fzf_opts(options_dict: dict) -> List[str]:
    """Takes a dictionary of fzf options and returns the command line flags."""

    def get(key: str):
        """Return a dict value from options_dict or None if missing."""
        return options_dict.get(key, None)

    flags = []
    if prompt := get("prompt"):
        flags.extend(["--prompt", prompt])
    # mutli-select
    multi = "--multi" if get("multi") else "--no-multi"
    flags.append(multi)
    if get("case_sensitive"):
        flags.append("+i")
    else:
        flags.append("-i")
    if prev := get("preview"):
        flags.extend(["--preview", prev])
    return flags


# vim: foldlevel=5:
