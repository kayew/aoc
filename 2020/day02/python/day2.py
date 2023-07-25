#!/usr/bin/env python3

import sys

def part1():
    total = 0
    file = open(sys.argv[1], "r")
    for line in file:
        param = line.split()
        passRange = [int(x) for x in param[0].split('-')]
        targetLetter = param[1][0]
        password = param[2]

        letterMatch = password.count(targetLetter)
        if letterMatch >= int(passRange[0]) and letterMatch <= int(passRange[1]):
                total += 1
    file.close()
    return total

def part2():
    total = 0
    file = open(sys.argv[1], "r")
    for line in file:
        letterMatch = 0
        param = line.split()
        passIndex = [int(x) for x in param[0].split('-')]
        targetLetter = param[1][0]
        password = param[2]

        if password[passIndex[0]-1] == targetLetter:
            letterMatch += 1
        if password[passIndex[1]-1] == targetLetter:
            letterMatch += 1

        if letterMatch == 1:
            total += 1
    file.close()
    return total

print(f"Part 1: {part1()}, Part 2: {part2()}")
