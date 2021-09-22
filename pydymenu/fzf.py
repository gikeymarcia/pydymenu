#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import subprocess as sp
from typing import Iterable, List, Union

from pydymenu.exceptions import MissingProgram
from pydymenu.menu import Menu
from pydymenu.system import missing_binary, newline_joined_bytestream


class FzfProtocol(Menu):
    """Implements Menu protcol for `fzf` selector.

    Takes Iterable[str] as input and returns:
        List[str]:  upon selection
        None:       when no selection is made
    """

    def __init__(
        self,
        items: Iterable[str],
        prompt: str = None,
        multi: bool = False,
        case_sensitive: bool = False,
        preview: str = None,
    ):
        self.items = items
        self.prompt = " > " if prompt is None else prompt
        self.multi = multi
        self.case_sensitive = case_sensitive
        self.preview = preview
        self.flags: List[str] = self.process_opts()
        self.command: List[str] = ["fzf"] + self.flags
        if missing_binary("fzf"):
            raise MissingProgram("Cannot find `fzf` on your system.")

    def select(self) -> Union[List[str], None]:
        """Run `fzf` selector on given items."""
        process = sp.run(
            self.command,
            input=newline_joined_bytestream(self.items),
            stdout=sp.PIPE,
        )
        output = [o for o in process.stdout.decode().split("\n") if len(o) > 0]
        return output if len(output) > 0 else None

    def process_opts(self) -> List[str]:
        """Turn selected options into List[str] of `fzf` flags."""
        prompt = ["--prompt", self.prompt]
        multi = "--multi" if self.multi else "--no-multi"
        case = "+i" if self.case_sensitive else "-i"
        if self.preview:
            return prompt + [multi, case, "--preview", self.preview]
        else:
            return prompt + [multi, case]


def fzf_func(
    items: Iterable[str],
    prompt: str = None,
    multi: bool = False,
    case_sensitive: bool = False,
    preview: str = None,
):
    """Launches a `fzf` process and returns either List[str] or None."""
    fuzzy_fider = FzfProtocol(
        items=items,
        prompt=prompt,
        multi=multi,
        case_sensitive=case_sensitive,
        preview=preview,
    )
    return fuzzy_fider.select()


# vim: foldlevel=1:
