#!/usr/bin/python3

from ev3dev.ev3 import *

# Play a small song
Sound.play_song((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h')
)).wait()