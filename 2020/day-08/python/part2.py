#!/usr/bin/env python3

import sys

data = [x.strip() for x in open(sys.argv[1], "r").readlines()]

def execute(d):
    acc = 0
    visited_pos = set()
    i = 0

    while i not in visited_pos and i < len(d):
        ins = d[i][:3]
        amt = int(d[i][4:])
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

    return i, acc

def switch_op(inst, swap, inst_list):
    for j in [i for i in range(len(inst_list)) if inst_list[i][:3] == inst]:
        inst_list[j] = inst_list[j].replace(inst, swap)
        i, acc = execute(inst_list)
        inst_list[j] = inst_list[j].replace(swap, inst)
        if i == len(inst_list):
            return acc

for x in [("jmp", "nop"), ("nop", "jmp")]:
    print(switch_op(x[0], x[1], data))
