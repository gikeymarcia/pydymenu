#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

from shutil import which
import subprocess as sp
from sys import path as sys_path


def has_bin(binary_name):
    binary = str(binary_name)
    return True if which(binary) else False


def fzf(list_of_items, prompt=None, multi=False):
    if not has_bin("fzf"):
        err_msg = f"Could not locate `fzf` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _fzf_dict = {
        "prompt": prompt,
        "multi": multi,
    }
    return _run_fzf_with_list(list_of_items, **_fzf_dict)


def _run_fzf_with_list(list_of_items, **kwargs):
    options = process_fzf_opts(kwargs)
    _fzf_process = sp.run(
        ["fzf"] + options,
        input=newline_joined_bytestream(list_of_items),
        stdout=sp.PIPE,
    )
    return process_stdout(_fzf_process, multi=kwargs["multi"])


def process_stdout(completed_process, multi=False):
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


def newline_joined_bytestream(menu_items):
    """Takes a list and returns a bytestream suitable for standard in

    Converts all values to str before joining with newlines and encoding
    as a utf-8 bytestream. Good for sending to input= for subprocess.run()
    """
    line_return, new_line = "\r", "\n"

    def ready_to_join(list_item):
        if new_line in list_item or line_return in list_item:
            err = f"Newlines not allowed within items. Found in\n{list_item}"
            raise ValueError(err)
        else:
            return str(list_item)

    strings = [ready_to_join(i) for i in menu_items]
    return "\n".join(strings).encode("utf-8")


def process_fzf_opts(options_dict):
    """Takes a dictionary of fzf options and returns the command line flags."""
    # print(f"opts: {options_dict}")
    fzf_flags = []
    if prompt := options_dict.get("prompt", None):
        fzf_flags.extend(["--prompt", prompt])
    # mutli-select
    multi = options_dict.get("multi", None)
    multi_mode = "--multi" if multi else "--no-multi"
    fzf_flags.append(multi_mode)
    # TODO: preview
    # TODO: print_query
    # print(f"adds: {fzf_flags}")
    return fzf_flags


def rofi(list_of_items, **kwargs):
    if not has_bin("rofi"):
        err_msg = f"Could not locate `rofi` on system path:\n{sys_path}"
        raise FileNotFoundError(err_msg)
    _rofi_dict = {
        "case_sensitive": False,
    }
    options = process_rofi_opts(**kwargs)
    _rofi_process = sp.run(
        ["rofi", "-dmenu"] + options,
        input=newline_joined_bytestream(list_of_items),
    )


def process_rofi_opts(**kwargs):
    rofi_flags = []
    if kwargs["case_sensitive"]:
        rofi_flags.append("-case-sensitive")
    else:
        rofi_flags.append("-i")
    return rofi_flags


def rofi_select(sel_list, prompt="Choose: "):
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
