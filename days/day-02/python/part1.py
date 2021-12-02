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
    if move[0] == 'forward':
        xPos += int(move[1])
    elif move[0] == 'up':
        depth -= int(move[1])
    elif move[0] == 'down':
        depth += int(move[1])

print(f"Part 1: {xPos*depth}")