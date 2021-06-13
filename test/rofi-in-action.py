#!/usr/bin/env python
import pydymenu
from sample_data import options

print("TESTING ROFI")

# Simple
rofi = pydymenu.rofi(options())

# prompt
# rofi = pydymenu.rofi(options(), prompt="Who can help guide the way? ")

# multi True
# fzf = pydymenu.fzf(options(), prompt="Who can help guide the way? ", multi=True)

# multi False
# fzf = pydymenu.fzf(options(), prompt="Who can help guide the way? ", multi=False)

# fzf = pydymenu.fzf(options(), multi=True)

print(rofi)
