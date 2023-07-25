#!/usr/bin/env python3

import sys

data = [x.strip() for x in open(sys.argv[1], "r").readlines()]

acc = 0
visited_pos = set()
i = 0

while i not in visited_pos and i < len(data):
    ins = data[i][:3]
    amt = int(data[i][4:])
    if ins == "acc":
        visited_pos.add(i)
        acc += amt
        i += 1
        continue
    if ins == "jmp":
        visited_pos.add(i)
        i += amt
        continue
    if ins == "nop":
        i += 1
        continue

print(acc)
