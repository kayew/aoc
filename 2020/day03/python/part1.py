#!/usr/bin/env python3

import sys

data = [x.strip() for x in open(sys.argv[1], 'r').readlines()]

slope = (3, 1)  # right, down

numRows = len(data)  # changes between the example and actual input
numCols = len(data[0])  # ^

# m = y2 - y1 / x2 - x1 -> basically y/x

trees = 0
x = 0

for y in range(0, numRows, slope[1]):  # -> step right by factor of right (in this case, step right by a factor)
    if data[y][x] == '#':  # this is not a 2d array, it is checking the y and x-axis for a "tree"
        trees += 1
    x = (x + slope[0]) % numCols  # allow for "looping" around on the x-axis
    
print(f"trees: {trees}")
