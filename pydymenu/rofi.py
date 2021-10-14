#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from typing import Iterable, List, Optional

from pydymenu.exceptions import MissingProgram
from pydymenu.menu import Menu
from pydymenu.system import missing_binary, stream_to_stdin


class RofiProtocol(Menu):
    """Implements Menu protcol for `rofi` selector.

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
    ):
        self.items = items
        self.prompt = " > " if prompt is None else prompt
        self.multi = multi
        self.case_sensitive = case_sensitive
        self.flags: List[str] = self.process_opts()
        self.command: List[str] = [
            "rofi",
            "-dmenu",
            "-async-pre-read",
            "1",
        ] + self.flags
        if missing_binary("rofi"):
            raise MissingProgram("Cannot find `rofi` on your system.")

    def select(self) -> Optional[List[str]]:
        """Run `rofi` selector on given items."""
        output: Optional[str] = stream_to_stdin(self.items, self.command)
        if output is None:
            return None
        else:
            return [line for line in output.split("\n") if len(line) > 0]

    def process_opts(self) -> List[str]:
        """Turn selected options into List[str] of `rofi` flags."""
        prompt = ["-p", self.prompt]
        multi = ["-multi-select"] if self.multi else []
        case = ["-case-sensitive"] if self.case_sensitive else ["-i"]
        return prompt + multi + case


def rofi_func(
    items: Iterable[str],
    prompt: str = None,
    multi: bool = False,
    case_sensitive: bool = False,
):
    """Launches a `rofi` process and returns either List[str] or None."""
    rofi_selector = RofiProtocol(
        items=items,
        prompt=prompt,
        multi=multi,
        case_sensitive=case_sensitive,
    )
    return rofi_selector.select()


# vim: foldlevel=1:
