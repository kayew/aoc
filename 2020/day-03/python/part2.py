#!/usr/bin/env python3

import sys

data = [x.strip() for x in open(sys.argv[1], 'r').readlines()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # right, down
# right = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 54, 64]
# down = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 47]
# slopes = [(x,y) for x in right for y in down]

numRows = len(data)  # changes between the example and actual input
numCols = len(data[0])  # ^

# m = y2 - y1 / x2 - x1 -> basically y/x

totalTrees = 1

def solve(slope: tuple) -> int:
    trees = 0
    x = 0
    for y in range(0, numRows, slope[1]):  # -> step right by factor of right 
        if data[y][x] == '#':  # this is not a 2d array, it is checking the y and x-axis for a "tree"
            trees += 1
        x = (x + slope[0]) % numCols  # allow for "looping" around on the x-axis
    return trees

for s in slopes:
    totalTrees *= solve(s)  # pass each set of slopes into solve and mul the results 

print(totalTrees)
