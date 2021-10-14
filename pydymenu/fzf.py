#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from typing import Iterable, List, Optional

from pydymenu.exceptions import MissingProgram
from pydymenu.menu import Menu
from pydymenu.system import missing_binary, stream_to_stdin


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

    def process_opts(self) -> List[str]:
        """Turn selected options into List[str] of `fzf` flags."""
        prompt = ["--prompt", self.prompt]
        multi = "--multi" if self.multi else "--no-multi"
        case = "+i" if self.case_sensitive else "-i"
        if self.preview:
            return prompt + [multi, case, "--preview", self.preview]
        else:
            return prompt + [multi, case]

    def select(self) -> Optional[List[str]]:
        """Run `fzf` selector on given items."""
        output: Optional[str] = stream_to_stdin(self.items, self.command)
        if output is None:
            return None
        else:
            return [line for line in output.split("\n") if len(line) > 0]


def fzf_func(
    items: Iterable[str],
    prompt: str = None,
    multi: bool = False,
    case_sensitive: bool = False,
    preview: str = None,
) -> Optional[List[str]]:
    """Launches a `fzf` process and returns either List[str] or None."""
    fuzzy_finder = FzfProtocol(
        items=items,
        prompt=prompt,
        multi=multi,
        case_sensitive=case_sensitive,
        preview=preview,
    )
    return fuzzy_finder.select()


# vim: foldlevel=1:
