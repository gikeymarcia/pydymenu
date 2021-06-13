#!/usr/bin/env python
import pydymenu
from sample_data import options

print("TESTING FZF")

# Simple
fzf = pydymenu.fzf(options())

# prompt
# fzf = pydymenu.fzf(options(), prompt="Who can help guide the way? ")

# multi True
# fzf = pydymenu.fzf(options(), prompt="Who can help guide the way? ", multi=True)

# multi False
# fzf = pydymenu.fzf(options(), prompt="Who can help guide the way? ", multi=False)

# fzf = pydymenu.fzf(options(), multi=True)

print(fzf)
