#!/usr/bin/env python
import pydymenu

print("TESTING USAGE")

my_opts = ["Jordan Hall", "Bret Weinstein", "Jim Rutt", "John Vervaeke"]

# Simple
# fzf = pydymenu.fzf(my_opts)
# print(f"single:\n{fzf}")

# prompt
# fzf = pydymenu.fzf(my_opts, prompt="which? ")

# multi True
# fzf = pydymenu.fzf(my_opts, prompt="which? ", multi=True)

# multi False
# fzf = pydymenu.fzf(my_opts, prompt="which? ", multi=False)

many = pydymenu.fzf(my_opts, multi=True)
