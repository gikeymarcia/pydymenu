#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import pydymenu
from pydymenu.demo_data import gen_options, list_options

print("TESTING ROFI")

# Simple
# rofi = pydymenu.rofi(list_options)

# prompt
# rofi = pydymenu.rofi(gen_options, prompt="Who can help guide the way? ")

# multi True
rofi = pydymenu.rofi(
    list_options,
    prompt="Who can help guide the way? ",
    multi=True,
)

# multi False
# rofi = pydymenu.rofi(options, prompt="Who can help guide the way? ", multi=False)

# case sensitive
# rofi = pydymenu.rofi(
#     options,
#     prompt="Who can help guide the way? ",
#     multi=True,
#     case_sensitive=True,
# )

print(f"Rofi output: {rofi}", f"type: {type(rofi)}", sep="\n")
