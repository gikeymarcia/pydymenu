import argparse

import pydymenu
from pydymenu.console import console
from pydymenu.demo_data import list_options

parser = argparse.ArgumentParser(
    prog="python -m pydymenu",
    description="pydymenu demonstration: preview pydymenu options in action.",
)
group = parser.add_mutually_exclusive_group()
group.add_argument("--fzf", help="select options using fzf", action="store_true")
group.add_argument("--rofi", help="select options using rofi", action="store_true")

args = parser.parse_args()

select = False
if args.fzf:
    console.log("fzf mode", style="title")
    select = pydymenu.fzf(
        list_options,
        prompt="Choose with fzf: ",
        multi=True,
        preview="echo {} | sed -E 's/[aeiou]//g' | figlet",
    )
elif args.rofi:
    console.log("rofi mode", style="title")
    select = pydymenu.rofi(
        list_options,
        prompt="Choose with rofi: ",
        multi=True,
    )
else:
    args = parser.parse_args(["--help"])
if select is not False:
    console.log(f"{select = }")
    console.log(f"{type(select) = }")
