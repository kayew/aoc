#!/usr/bin/env python3

from sys import argv

sonar = [int(f) for f in open(argv[1], 'r').read().split()]
new_sonar = []
total = 0

for i in range(len(sonar)-2):
    sliding_sum = sonar[i] + sonar[i+1] + sonar[i+2]
    new_sonar.append(sliding_sum)

for i in range(len(new_sonar)-1):
    if new_sonar[i+1] > new_sonar[i]:
        total += 1

print(total)
