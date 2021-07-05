import argparse
import pydymenu
from pydymenu.console import console
from pydymenu.demo_data import options

parser = argparse.ArgumentParser(
    description="pydymenu demonstration: preview pydymenu options in action.",
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--fzf",
    "-f",
    help="select options using fzf",
    action="store_true",
)
group.add_argument(
    "--rofi",
    "-r",
    help="select options using rofi",
    action="store_true",
)

args = parser.parse_args(["--rofi"])
console.log(args, log_locals=True)

if args.fzf:
    console.log("FZF MODE", style="title")
    select = pydymenu.fzf(options, prompt="", multi=True)
    console.log(f"{type(select) = }")
    console.log(f"{select = }")
elif args.rofi:
    console.log("rofi mode", style="title")
    select = pydymenu.rofi(options, prompt="Choose your weapon ", multi=True)
    console.log(f"{select = }")
    console.log(f"{type(select) = }")
