#!/usr/bin/env python

import sys

lines = list(map(lambda w:w.split(','), open(sys.argv[1], "r").read().split('\n')))

wire1 = lines[0]
wire2 = lines[1]

def find_coords(wire):
    x_curr, y_curr, x_dest, y_dest = 0, 0, 0, 0
    direction = (0,0)
    points = set()
    for move in wire:

        units = int(move[1:])

        if move[0] == "R":
            x_dest += units
            direction = (1,0)
        elif move[0] == "L":
            x_dest -= units
            direction = (-1,0)
        elif move[0] == "U":
            y_dest += units
            direction = (0,1)
        elif move[0] == "D":
            y_dest -= units
            direction = (0,-1)

        while x_curr != x_dest or y_curr != y_dest:
            points.add((x_curr, y_curr))
            x_curr += direction[0]
            y_curr += direction[1]

    return points

wire1_coords = find_coords(wire1)
wire2_coords = find_coords(wire2)

intersections = wire1_coords.intersection(wire2_coords).difference({(0,0)})

manhattan = list(map(lambda point:abs(point[0]) + abs(point[1]), intersections))

print(min(manhattan))