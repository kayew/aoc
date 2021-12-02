#!/usr/bin/env python

import sys

OPADD = 1
OPMULTIPLY = 2
OPHALT = 99 

num = [int(i) for i in open(sys.argv[1], "r").read().split(',')]

num[1] = 12
num[2] = 2

i = 0

while True:
    one = num[i + 1]
    two = num[i + 2]
    three = num[i + 3]
    if num[i] == OPADD:
        num[three] = num[one] + num[two]
        i += 4
    elif num[i] == OPMULTIPLY:
        num[three] = num[one] * num[two]
        i += 4
    elif num[i] == OPHALT:
        break
    else:
        print("?")
        
print("Solution: " + str(num[0]))