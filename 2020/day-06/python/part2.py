#!/usr/bin/env python3

import sys, string

data = [x.split() for x in open(sys.argv[1]).read().split("\n\n")]

total = 0

for q in data:
    u = set(string.ascii_lowercase)
    for c in q:
        u = u.intersection(set(c)) # or u &= set(c)
    
    total += len(u)
    
print(total)
