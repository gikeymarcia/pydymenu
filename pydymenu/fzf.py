#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import subprocess as sp
from sys import path as sys_path
from typing import Union

from pydymenu.console import console
from pydymenu.system import has_bin, newline_joined_bytestream, process_stdout


def fzf(
    items: list[str],
    prompt: Union[str, None] = None,
    multi: bool = False,
    case_sensitive: bool = False,
) -> Union[list[str], None]:
    """Take list of strings and returns selection list or None."""
    if not has_bin("fzf"):
        err_msg = f"Could not locate `fzf` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _fzf_dict = {
        "prompt": prompt,
        "multi": multi,
        "case_sensitive": case_sensitive,
    }
    return _run_fzf_with_list(items, **_fzf_dict)


def _run_fzf_with_list(menu_entries: list[str], **kwargs) -> Union[None, list[str]]:
    options = process_fzf_opts(kwargs)
    _fzf_process = sp.run(
        ["fzf"] + options,
        input=newline_joined_bytestream(menu_entries),
        stdout=sp.PIPE,
    )
    console.log(f"{_fzf_process = }")
    return process_stdout(_fzf_process)


def process_fzf_opts(options_dict: dict) -> list[str]:
    """Takes a dictionary of fzf options and returns the command line flags."""
    # print(f"opts: {options_dict}")
    fzf_flags = []
    if prompt := options_dict.get("prompt", None):
        fzf_flags.extend(["--prompt", prompt])
    # mutli-select
    multi = options_dict.get("multi", None)
    multi_mode = "--multi" if multi else "--no-multi"
    fzf_flags.append(multi_mode)
    # case sensitive (default False)
    if options_dict["case_sensitive"]:
        fzf_flags.append("+i")
    else:
        fzf_flags.append("-i")
    # TODO: preview
    # TODO: print_query
    # print(f"adds: {fzf_flags}")
    return fzf_flags


# vim: foldlevel=5:
