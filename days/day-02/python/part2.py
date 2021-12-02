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
    if move[0] == 'forward':
        xPos += int(move[1])
        depth += aim * int(move[1])
    elif move[0] == 'up':
        aim -= int(move[1])
    elif move[0] == 'down':
        aim += int(move[1])

print(f"Part 2: {xPos*depth}")