#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import pydymenu
from pydymenu.demo_data import gen_options, list_options

print("TESTING FZF")

# Simple
# fzf = pydymenu.fzf(list_options)

# prompt
# fzf = pydymenu.fzf(gen_options, prompt="Who can help guide the way? ")

# # multi True
fzf = pydymenu.fzf(gen_options, prompt="Who can help guide the way? ", multi=True)

# # multi False
# fzf = pydymenu.fzf(gen_options, prompt="Who can help guide the way? ", multi=False)

# # preview
# fzf = pydymenu.fzf(list_options, prompt="who? ", multi=True, preview="figlet {}")

print(f"fzf output: {fzf}", f"type: {type(fzf)}", sep="\n")
