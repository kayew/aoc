#!/usr/bin/env python

import sys
from copy import deepcopy

OPADD = 1
OPMULTIPLY = 2
OPHALT = 99

def interpret_intcode(noun, verb, num):
    i = 0

    num[1] = noun
    num[2] = verb

    while True:
        one = num[i + 1]
        two = num[i + 2]
        three = num[i + 3]
        if num[i] == OPADD:
            num[three] = num[one] + num[two]
            i += 4
        elif num[i] == OPMULTIPLY:
            num[three] = num[one] * num[two]
            i += 4
        elif num[i] == OPHALT:
            break
        else:
            return("?")
    return num[0]

def find_value():
    num = [int(i) for i in open(sys.argv[1], "r").read().split(',')]
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            if interpret_intcode(noun, verb, deepcopy(num)) == 19690720:
                return 100 * noun + verb

print("Solution: " + str(find_value()))