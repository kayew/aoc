#!/usr/bin/env python3

import sys

data = [x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') for x in open(sys.argv[1], "r").read().split("\n")]

sID = []

for line in data:
    fRow = int(line[:7], 2)
    fCol = int(line[-3:], 2)

    sID.append(fRow * 8 + fCol)

print(max(sID))
