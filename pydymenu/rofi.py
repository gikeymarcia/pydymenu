#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import subprocess as sp
from sys import path as sys_path
from typing import Union

from pydymenu.console import console
from pydymenu.system import has_bin, newline_joined_bytestream, process_stdout


def rofi(
    menu_entries: list[str],
    prompt: Union[str, None] = None,
    case_sensitive: bool = False,
    multi: bool = False,
):
    if not has_bin("rofi"):
        err_msg = f"Could not locate `rofi` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _rofi_dict = {
        "prompt": prompt,
        "case_sensitive": case_sensitive,
        "multi": multi,
    }
    return _run_rofi_with_list(menu_entries, **_rofi_dict)


def _run_rofi_with_list(menu_entries: list[str], **kwargs):
    options = process_rofi_opts(**kwargs)
    _rofi_process = sp.run(
        ["rofi", "-dmenu"] + options,
        input=newline_joined_bytestream(menu_entries),
        stdout=sp.PIPE,
    )
    return process_stdout(_rofi_process)


def process_rofi_opts(**kwargs: dict) -> list[str]:
    rofi_flags = []
    # prompt (default " > ")
    if not (prompt := kwargs["prompt"]):
        rofi_flags.extend(["-p", " > "])
    else:
        rofi_flags.extend(["-p", prompt])
    # case sensitive (default False)
    if kwargs["case_sensitive"]:
        rofi_flags.append("-case-sensitive")
    else:
        rofi_flags.append("-i")
    # multi-select (default False)
    if kwargs["multi"]:
        rofi_flags.append("-multi-select")
    return rofi_flags


def rofi_select(sel_list: list[str], prompt: str = "Choose: "):
    "Takes a list and uses rofi to return a selection."
    pipe_delim = "|".join(sel_list)
    opts = sp.Popen(["printf", pipe_delim], stdin=sp.PIPE, stdout=sp.PIPE)
    rofi = sp.Popen(
        ["rofi", "-dmenu", "-i", "-sep", "|", "-p", prompt],
        stdin=opts.stdout,
        stdout=sp.PIPE,
    )
    out, _ = rofi.communicate()
    selection = out.decode("utf-8").strip()
    return None if selection == "" else selection


# vim: foldlevel=5:
