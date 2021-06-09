#!/usr/bin/env python
import pydymenu
from random import shuffle

print("TESTING USAGE")
my_opts = [
    "Jordan Hall",
    "Bret Weinstein",
    "Jim Rutt",
    "John Vervaeke",
    "Jamie Wheal",
    "The Stoa",
    "Jonathan Pageau",
    "Jordan Peterson",
    "Joe Rogan",
    "Sam Harris",
    "Terrence McKenna",
    "Rupert Spira",
    "Curt Jaimungal",
    "Daryl Davis",
    "Aaron Mate",
    "Abby Martin",
    "Lex Fridman",
    "Glenn Loury",
    "David Fuller",
    "Ken Wilber",
    "Yoga with Adrienne",
]
shuffle(my_opts)

# Simple
# fzf = pydymenu.fzf(my_opts)

# prompt
fzf = pydymenu.fzf(my_opts, prompt="Who can help guide the way? ")

# multi True
# fzf = pydymenu.fzf(my_opts, prompt="Who can help guide the way? ", multi=True)

# multi False
# fzf = pydymenu.fzf(my_opts, prompt="Who can help guide the way? ", multi=False)

# fzf = pydymenu.fzf(my_opts, multi=True)

print(fzf)
