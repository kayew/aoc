#!/usr/bin/env python3
with open("input.txt") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        total += int(line)
    print(total)