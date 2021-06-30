#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

from shutil import which
import subprocess as sp
from sys import path as sys_path
from typing import Union


def has_bin(binary_name: str) -> bool:
    binary = str(binary_name)
    return True if which(binary) else False


def fzf(
    list_of_items: list[str],
    prompt: Union[str, None] = None,
    multi: bool = False,
    case_sensitive: bool = False,
) -> Union[str, list[str], None]:
    if not has_bin("fzf"):
        err_msg = f"Could not locate `fzf` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _fzf_dict = {
        "prompt": prompt,
        "multi": multi,
        "case_sensitive": case_sensitive,
    }
    return _run_fzf_with_list(list_of_items, **_fzf_dict)


def _run_fzf_with_list(list_of_items: list[str], **kwargs):
    options = process_fzf_opts(kwargs)
    _fzf_process = sp.run(
        ["fzf"] + options,
        input=newline_joined_bytestream(list_of_items),
        stdout=sp.PIPE,
    )
    return process_stdout(_fzf_process, multi=kwargs["multi"])


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


def process_stdout(
    completed_process, multi: bool = False
) -> Union[str, list[str], None]:
    """Takes a completed process object and returns selected value(s)

    If multi=True returns a list, Otherwise return a string.
    If no selection is made returns None
    """
    if completed_process.returncode != 0:
        return None
    output_list = completed_process.stdout.decode().strip().split("\n")
    # standard_err = completed_process.stderr
    # print(standard_out)
    # print(output_list)
    if multi:
        return output_list
    else:
        return output_list[0]


def newline_joined_bytestream(menu_items) -> bytes:
    """Takes a list and returns a bytestream suitable for standard in

    Converts all values to str before joining with newlines and encoding
    as a utf-8 bytestream. Good for sending to input= for subprocess.run()
    """
    line_return, new_line = "\r", "\n"

    def ready_to_join(list_item: str) -> str:
        if new_line in list_item or line_return in list_item:
            err = f"Newlines not allowed within items. Found in\n{list_item}"
            raise ValueError(err)
        else:
            return str(list_item)

    strings = [ready_to_join(i) for i in menu_items]
    return "\n".join(strings).encode("utf-8")


def rofi(
    list_of_items: list[str],
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
    return _run_rofi_with_list(list_of_items, **_rofi_dict)


def _run_rofi_with_list(list_of_items: list[str], **kwargs):
    options = process_rofi_opts(**kwargs)
    _rofi_process = sp.run(
        ["rofi", "-dmenu"] + options,
        input=newline_joined_bytestream(list_of_items),
        stdout=sp.PIPE,
    )
    return process_stdout(_rofi_process, multi=kwargs["multi"])


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
