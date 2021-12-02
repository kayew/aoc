#!/usr/bin/env python3

from sys import argv

data = [f.split() for f in open(argv[1]).read().split('\n')]

"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
"""

xPos = 0
depth = 0
aim = 0

for move in data:
    dir = int(move[1])
    if move[0] == 'forward':
        xPos += dir
        depth += aim * dir
    elif move[0] == 'up':
        aim -= dir
    elif move[0] == 'down':
        aim += dir

print(f"Part 2: {xPos*depth}")