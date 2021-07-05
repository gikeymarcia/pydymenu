#!/usr/bin/env python3
from random import shuffle
import time

__all__ = ["options", "gen_opts"]

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

shuffle(sensemakers)
options = sensemakers


def gen_opts(source: list):
    for i in source:
        time.sleep(0.15)
        yield i


# vim: foldlevel=4 :
