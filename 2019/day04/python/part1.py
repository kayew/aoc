#!/usr/bin/env python

import sys

""" CHALLENGE:

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

How many different passwords within the range given in your puzzle input meet these criteria?

"""

# INPUT: 178416-676461

min_max = [int(i) for i in sys.argv[1].split('-')]

def part1(p_min, p_max):
    total = 0
    for i in range(p_min, p_max):
        s = str(i)
        adj = False
        inc = True
        for j in range(5):
            if s[j] > s[j + 1]:
                inc = False
            if s[j] == s[j + 1]:
                adj = True
        if adj and inc: # will increment if both are true
            total += 1
    return total
    
print(part1(min_max[0], min_max[1]))