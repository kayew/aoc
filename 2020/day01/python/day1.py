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

def part2():
    for i in num:
        for j in num:
            for k in num:
                if i+j+k == target:
                    assert i*j*k == 96047280
                    return [i, j, k, i*j*k]

result1 = part1()
result2 = part2()

print(f"Part 1: {result1[0]} * {result1[1]} = {result1[2]}")
print(f"Part 2: {result2[0]} * {result2[1]} * {result2[2]} = {result2[3]}")
