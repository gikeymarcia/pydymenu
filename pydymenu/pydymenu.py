#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

from shutil import which
import subprocess as sp


def has_bin(binary_name):
    if type(binary_name) is str:
        if which(binary_name):
            return True
        else:
            return False
    else:
        return False


def fzf(list_of_items, prompt=None, multi=False):
    _fzf_dict = {
        "prompt": prompt,
        "multi": multi,
    }
    return _run_fzf_with_list(list_of_items, **_fzf_dict)


def _run_fzf_with_list(list_of_items, **kwargs):
    options = process_opts(kwargs)
    _fzf_process = sp.run(
        ["fzf"] + options,
        input=newline_joined_bytestream(list_of_items),
        stdout=sp.PIPE,
    )
    return process_stdout(_fzf_process, multi=kwargs["multi"])


def process_stdout(completed_process, multi=False):
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
    line_return, new_line = "\r", "\n"

    def ready_to_join(list_item):
        if new_line in list_item or line_return in list_item:
            err = f"Newlines not allowed within items. Found in\n{list_item}"
            raise ValueError(err)
        else:
            return str(list_item)

    strings = [ready_to_join(i) for i in menu_items]
    return "\n".join(strings).encode("utf-8")


def process_opts(options_dict):
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


class Menu:
    def __init__(self):
        self.menu_options = {
            "fzf": has_bin("fzf"),
            "rofi": has_bin("rofi"),
            "dmenu": has_bin("dmenu"),
        }

    def present(self):
        return self.menu_options

    @staticmethod
    def resolve_prompt(prompt):
        if prompt is None:
            return " > "
        elif type(prompt) is str:
            return prompt
        else:
            raise TypeError(
                f"Incompatible prompt given:{prompt}\n"
                f"type: {type(prompt)}\n"
                "expected a string"
            )

    @staticmethod
    def _is_iterable(unknown_iterablity_obj):
        try:
            _ = iter(unknown_iterablity_obj)
        except TypeError:
            raise TypeError(
                "Must send an iterable object.\n"
                f"Recieved object of type: {type(unknown_iterablity_obj)}"
            )
        else:
            return unknown_iterablity_obj


# vim: foldlevel=5:
