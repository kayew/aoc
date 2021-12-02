#!/usr/bin/env python3

import sys
from collections import defaultdict

adapter_list = sorted([0] + [int(x.strip()) for x in open(sys.argv[1], "r").readlines()])

highest = adapter_list[-1] + 3
adapter_list.append(highest)

combos = defaultdict(lambda: 0)
combos[0] = 1

for x in adapter_list:
    combos[x] += combos[x - 1] + combos[x - 2] + combos[x - 3]

print(combos[max(combos)])
