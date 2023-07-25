#!/usr/bin/env python

# INPUT: 178416-676461

import sys

min_max = [int(i) for i in sys.argv[1].split('-')]

def part2(p_min, p_max):
    valid = []
    for i in range(p_min, p_max):
        s = str(i)
        inc = True
        for j in range(5):
            if s[j] > s[j + 1]:
                inc = False
        if inc:
            total_nums = {}
            for char in s:
                if char in total_nums:
                    total_nums[char] += 1
                else:
                    total_nums[char] = 1
            if 2 in total_nums.values():
                valid.append(i)
    return len(valid)
    
print(part2(min_max[0], min_max[1]))
