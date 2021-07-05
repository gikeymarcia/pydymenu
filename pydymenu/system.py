#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/

from shutil import which
from subprocess import CompletedProcess
from typing import Union


def has_bin(binary_name: str) -> bool:
    if type(binary_name) is str:
        return True if which(binary_name) else False
    else:
        raise ValueError("This function only accepts string inputs.")


def process_stdout(proc: CompletedProcess) -> Union[list[str], None]:
    """Takes a completed process object and returns selected value(s).

    If no selection is made returns None
    """
    if proc.returncode != 0:
        return None
    return proc.stdout.decode().strip().split("\n")


def newline_joined_bytestream(menu_items: list[str]) -> bytes:
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
            return list_item

    strings = [ready_to_join(i) for i in menu_items]
    return "\n".join(strings).encode("utf-8")
