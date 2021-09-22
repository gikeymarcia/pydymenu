#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from typing import Protocol, List, Union, Iterable


class Menu(Protocol):
    def __init__(
        self,
        items: Iterable[str],
        prompt: str,
        multi: bool,
        case_sensitive: bool,
        **kwargs
    ):
        raise NotImplementedError

    def select(self) -> Union[List[str], None]:
        raise NotImplementedError
