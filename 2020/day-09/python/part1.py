#!/usr/bin/env python3

import sys

data = [int(x.strip()) for x in open(sys.argv[1], "r").readlines()]

step = int(sys.argv[2])

for i in range(step, len(data)):
    found = False
    for j in range(i-step, i):
        for k in range(i-step, i):
            if k!=j and data[i] == data[k] + data[j]:
                found = True
    if not found:
        print(i, data[i])
