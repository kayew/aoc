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
            t.append(i[2:].split(" bag")[0])
            d[k] = t
        else:
            d[k] = []
            continue

def can_contain(bag_name):
    total = 0
    for sb in d:
        total += check_sub_bag(sb, bag_name)
    return total

def check_sub_bag(sub, bag_name):
    total = 0
    if sub == bag_name:
        return 1
    for l in d[sub]:
        if l == bag_name: 
            total += 1
        else:
            ans = check_sub_bag(l, bag_name)
            if ans > 0:
                return ans
    return total

print(can_contain("shiny gold")-1)
