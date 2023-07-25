#!/usr/bin/env python3

import sys

file = open(sys.argv[1], "r")
total = 0

for line in file:
    param = line.split()
    passRange = [int(x) for x in param[0].split('-')]
    targetLetter = param[1][0]
    password = param[2]

    letterMatch = password.count(targetLetter)
    if letterMatch >= passRange[0] and letterMatch <= passRange[1]:
            total += 1
            
file.close()
print(f"total: {total}")
