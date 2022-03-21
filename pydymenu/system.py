#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import errno
from shutil import which
import subprocess as sp
from typing import Iterable, List, Optional


def missing_binary(binary_name: str) -> bool:
    """Tests whether a binary is missing from the system"""
    if isinstance(binary_name, str):
        return False if which(binary_name) else True
    else:
        raise ValueError("This function only accepts string inputs.")


def stream_to_stdin(items: Iterable[str], command: List[str]) -> Optional[str]:
    """
    Stream each Iteralbe item into the standard in for the given command.

    Each item is appended with a '\\n' and 'utf-8' encoded before streamed in.

    Uses low-level subprocess.Popen(). If the process is interrupted or
    completes with an error code the None value will be returned. Otherwise,
    the byte output of Popen.stdout is decoded into a string and returned.

    """
    process = sp.Popen(command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=None)
    stdin, stdout = process.stdin, process.stdout
    line_return, new_line = "\r", "\n"
    if process is not None and stdin is not None and stdout is not None:
        for i in items:
            if new_line in i or line_return in i:
                raise ValueError("no line breaks within an item.")
            else:
                try:
                    # write each item to standard in as a utf-8 encoded bytestream
                    stdin.write(i.encode("utf-8") + b"\n")
                    stdin.flush()
                except IOError as e:
                    if e.errno != errno.EPIPE and errno.EPIPE != 32:
                        raise
            poll_process_status = process.poll()
            if poll_process_status in [1, 2, 130]:
                # fzf returns 130 when interrupted with Ctrl+c
                return None
            elif poll_process_status == 0:
                return stdout.read().decode()
        try:
            stdin.close()
        except IOError as e:
            if e.errno != errno.EPIPE and errno.EPIPE != 32:
                raise
        if process is None or process.wait() not in [0, 1]:
            return None
        elif stdout is not None:
            return stdout.read().decode()
        else:
            return None


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


__all__ = ["missing_binary", "stream_to_stdin"]
