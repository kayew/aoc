#!/usr/bin/env python3

from sys import argv

data = [x.strip() for x in open(argv[1]).readlines()]

x = 0
y = 0
facing = 90

for s in data:
    dir = s[0]
    amnt = int(s[1:])
    if dir == "N":
        y += amnt
    elif dir == "E":
        x += amnt
    elif dir == "S":
        y -= amnt
    elif dir == "W":
        x -= amnt
    elif dir == "L":
        facing -= amnt
        facing %= 360
    elif dir == "R":
        facing += amnt
        facing %= 360
    elif dir == "F":
        if facing == 0:
            y += amnt
        elif facing == 90:
            x += amnt
        elif facing == 180:
            y -= amnt
        elif facing == 270:
            x -= amnt

print(abs(x) + abs(y))
