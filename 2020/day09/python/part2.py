#!/usr/bin/env python3

import sys

data = [int(x.strip()) for x in open(sys.argv[1], "r").readlines()]

step = int(sys.argv[2])

def find_invalid(step, data):
    for i in range(step, len(data)):
        found = False
        for j in range(i-step, i):
            for k in range(i-step, i):
                if data[i] == data[k] + data[j]:
                    found = True
        if not found:
            return data[i]

invalid_num = find_invalid(step, data)

s = []

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if sum(data[i:j+1]) == invalid_num:
            for x in data[i:j+1]:
                s.append(x)
            break
        if sum(data[i:j+1]) > invalid_num:
            break

s.sort()
print(s[0]+s[-1])
