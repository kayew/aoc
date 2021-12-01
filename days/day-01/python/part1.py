#!/usr/bin/env python3

from sys import argv

sonar = [int(f) for f in open(argv[1], 'r').read().split()]
total = 0
last = 0

for i in range(len(sonar)-1):
    if sonar[i+1] > sonar[i]:
        total += 1

print(total)