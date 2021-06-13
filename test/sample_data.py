#!/usr/bin/env python
from random import shuffle


def options():
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
    return my_opts
