#!/usr/bin/env python3

from sys import argv

sonar = [int(f) for f in open(argv[1], 'r').read().split()]

def part1(sonar_data):
    total = 0
    for i in range(len(sonar_data)-1):
        if sonar_data[i+1] > sonar_data[i]:
            total += 1
    return total

def part2(sonar_data):
    new_sonar = []
    for i in range(len(sonar_data)-2):
        sliding_sum = sonar_data[i] + sonar_data[i+1] + sonar_data[i+2]
        new_sonar.append(sliding_sum)
    return part1(new_sonar)

print(f"Part 1: {part1(sonar)}, Part 2: {part2(sonar)}")
