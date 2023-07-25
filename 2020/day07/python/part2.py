#!/usr/bin/env python3

import sys

# fmt: off
data = [x.strip().split(" bags contain ") for x in open(sys.argv[1]).readlines()]

d = {}

for b in data:
    d[b[0]] = b[1].split(", ")

for k,v in d.items():
    t = []
    for i in v:
        if i[0] != "n":
            t.append((int(i[0]), i[2:].split(" bag")[0]))
            d[k] = t
        else:
            d[k] = []
            continue

def get_total_bag(bag):
    total = 1
    if bag in d:
        for i in d[bag]:
            total += i[0] * get_total_bag(i[1])
    return total

print(get_total_bag("shiny gold")-1)
