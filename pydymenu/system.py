#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from shutil import which
from typing import Iterable, List


def missing_binary(binary_name: str) -> bool:
    """Tests whether a binary is missing from the system"""
    if isinstance(binary_name, str):
        return False if which(binary_name) else True
    else:
        raise ValueError("This function only accepts string inputs.")


def newline_joined_bytestream(menu_items: Iterable[str]) -> bytes:
    """Takes an Iterable[str] and returns a bytestream suitable for standard in

    Joins all strings with '\n' then encodes as a utf-8 bytestream.
    Good for subprocess.run(input=) use
    """
    line_return, new_line = "\r", "\n"

    def ready_to_join(list_item: str) -> str:
        if new_line in list_item or line_return in list_item:
            err = f"Newlines not allowed within items. Found in\n{list_item}"
            raise ValueError(err)
        else:
            return list_item

    return "\n".join([ready_to_join(i) for i in menu_items]).encode("utf-8")


def command_input(_: List[str]) -> List[str]:
    """Run a shell command and get a result suitable for pydymenu input.

    For example:
    pydymenu.fzf(
        command_input(["find", Path.home(), "-name", "*.mp3"]),
        prompt="Which mp3(s) do you want?",
        multi=True
    )
    """
    # TODO make this
    raise NotImplementedError


__all__ = ["newline_joined_bytestream", "missing_binary"]
