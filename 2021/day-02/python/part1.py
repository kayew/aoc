#!/usr/bin/env python3

from sys import argv

data = [f.split() for f in open(argv[1]).read().split('\n')]

"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""

xPos = 0
depth = 0

for move in data:
    dir = int(move[1])
    if move[0] == 'forward':
        xPos += dir
    elif move[0] == 'up':
        depth -= dir
    elif move[0] == 'down':
        depth += dir

print(f"Part 1: {xPos*depth}")