#!/usr/bin/env python3
# Mikey Garcia, @gikeymarcia
# https://github.com/gikeymarcia/pydymenu

from random import shuffle
import time
from typing import Iterable

__all__ = ["list_options", "gen_options"]

sensemakers = [
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
    "Jimmy Dore",
    "Dave Snowden",
    "Tristan Harris",
    "Paul Stamets",
    "Daniel Schmachtenberger",
    "Peter Wang",
    "John Robb",
    "Samo Burja",
    "Tyson Yunkaporta",
    "Michael Malice",
    "Joscha Bach",
    "Michel Bauwens",
    "Yancey Strickler",
    "Hanzi Freinacht",
]


def list_to_generator(source: Iterable[str]) -> Iterable[str]:
    for i in source:
        time.sleep(0.05)
        yield i


shuffle(sensemakers)
list_options = sensemakers
gen_options = list_to_generator(sensemakers)


# vim: foldlevel=4 :
