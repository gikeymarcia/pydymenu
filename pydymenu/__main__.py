#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

import argparse
from pathlib import Path

from pydymenu import fzf, rofi
from pydymenu.console import console
from pydymenu.demo_data import gen_options
from rich.syntax import Syntax

parser = argparse.ArgumentParser(
    prog="python -m pydymenu",
    description="Try pydymenu in either --fzf or --rofi mode.",
)
group = parser.add_mutually_exclusive_group()
group.add_argument("--fzf", help="Select using fzf", action="store_true")
group.add_argument("--rofi", help="Select using rofi", action="store_true")

args = parser.parse_args()
# console.log(args)

if args.fzf:
    fzf_selection = fzf(
        gen_options,
        prompt="Choose with fzf: ",
        multi=True,
        preview="echo {} | sed -E 's/[aeiou]//g' | figlet",
    )
    # show code sample
    console.print("FZF mode (sample code)\n", style="title")
    demo_file = Path(__file__).parent / "demo" / "fzf.py"
    with open(demo_file, "r") as file:
        # use pygments theme: https://pygments.org/demo/#try
        example = Syntax(demo_file.read_text(), "python", theme="material")
        console.print(example)
    console.print(f"{fzf_selection = }")
elif args.rofi:
    rofi_selection = rofi(
        gen_options,
        prompt="Choose with rofi: ",
        multi=True,
    )
    # show code sample
    console.print("rofi mode (sample code)\n", style="title")
    demo_file = Path(__file__).parent / "demo" / "rofi.py"
    with open(demo_file, "r") as file:
        example = Syntax(demo_file.read_text(), "python", theme="material")
        console.print(example)
    console.print(f"{rofi_selection = }")
else:
    args = parser.parse_args(["--help"])
