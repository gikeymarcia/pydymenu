#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

__author__ = "Mikey Garcia, @gikeymarcia"

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


class fzf:
    def __init__(self, prompt=None, args=None):
        self.prompt = Menu.resolve_prompt(prompt)
        self.available = has_bin("fzf")

    def _fzf_as_grep(self, collection, query: str):
        collection = Menu._is_iterable(collection)
        newline_sep = "\n".join(collection)
        printf = sp.Popen(["printf", f"{newline_sep}"], stdout=sp.PIPE)
        dummy_fzf = sp.Popen(["fzf", "-f", query], stdin=printf.stdout, stdout=sp.PIPE)
        head_proc = sp.Popen(["head", "-n1"], stdin=dummy_fzf.stdout, stdout=sp.PIPE)
        return head_proc.communicate()[0].decode("utf-8")

    def __call__(self, items=None, grep_query=None):
        if type(grep_query) is str:
            return self._fzf_as_grep(items, grep_query)
        else:
            items = Menu._is_iterable(items)
            fzf_proc = sp.Popen(
                ["fzf", f"--prompt={self.prompt}", "--ansi"],
            )
            print(f"output: {fzf_proc}\n" f"output: {type(fzf_proc)}")
            print(f"items: {items}\n")
            print(f"dir(fzf_proc): {dir(fzf_proc)}\n")


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
            iterator = iter(unknown_iterablity_obj)
        except TypeError:
            raise TypeError(
                "Must send an iterable object.\n"
                f"Recieved object of type: {type(unknown_iterablity_obj)}"
            )
        else:
            return unknown_iterablity_obj


# vim: foldlevel=5:
