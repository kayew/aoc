#!/usr/bin/env python3

import sys

num = [int(i) for i in open(sys.argv[1], 'r').read().split("\n")]
target = 2020
# target = 99920044

def part1():
    for i in num:
        for j in num:
            if i + j == target:
                assert i*j == 970816
                return [i, j, i*j]

result = part1()
print(f"{result[0]} * {result[1]} = {result[2]}")