#!/usr/bin/env python
import pydymenu
from pydymenu.demo_data import options

print("TESTING ROFI")
# Simple
# rofi = pydymenu.rofi(options)

# prompt
rofi = pydymenu.rofi(options, prompt="Who can help guide the way? ")

# multi True
# rofi = pydymenu.rofi(options, prompt="Who can help guide the way? ", multi=True)

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
