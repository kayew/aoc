#!/usr/bin/env python3

from sys import argv
from math import cos, sin
from math import radians as toR

data = [x.strip() for x in open(argv[1]).readlines()]

x = 0
y = 0
wp = [10, 1] # x, y / EW, NS

for s in data:
    dir = s[0]
    amnt = int(s[1:])
    if dir == "N":
        wp[1] += amnt
    elif dir == "E":
        wp[0] += amnt
    elif dir == "S":
        wp[1] -= amnt
    elif dir == "W":
        wp[0] -= amnt
    elif dir == "R":
        # P2.x = P.x * cos(R) - P.y * sin(R)
        # P2.y = P.x * sin(R) + P.y * cos(R)
        x2 = (wp[0] * cos(-1 * toR(amnt))) - (wp[1] * sin(-1 * toR(amnt)))
        y2 = (wp[0] * sin(-1 * toR(amnt))) + (wp[1] * cos(-1 * toR(amnt)))
        wp[0] = x2
        wp[1] = y2
    elif dir == "L":
        x2 = (wp[0] * cos(toR(amnt))) - (wp[1] * sin(toR(amnt)))
        y2 = (wp[0] * sin(toR(amnt))) + (wp[1] * cos(toR(amnt)))
        wp[0] = x2
        wp[1] = y2
    elif dir == "F":
        x += wp[0] * amnt
        y += wp[1] * amnt


manhattan = abs(x) + abs(y)
print(f"{manhattan:.0f}")
