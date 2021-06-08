#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/dotfiles

import pydymenu

__author__ = "Mikey Garcia, @gikeymarcia"

if __name__ == "__main__":
    fzf = pydymenu.fzf(prompt="ready: ", args=["-m"])
    selction = fzf(
        ["one", "two", "three", "twins", "twinkies", "cottonwood"],
    )
    print(selction)

# vim: foldlevel=2:
