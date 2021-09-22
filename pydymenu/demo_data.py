#!/usr/bin/env python3
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
]


def list_to_generator(source: Iterable[str]) -> Iterable[str]:
    for i in source:
        time.sleep(0.01)
        yield i


shuffle(sensemakers)
list_options = sensemakers
gen_options = list_to_generator(sensemakers)


# vim: foldlevel=4 :
