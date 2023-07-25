#!/usr/bin/env python

import sys

OPADD = 1
OPMULTIPLY = 2
OPIN = 3
OPOUT = 4
OPJIT = 5
OPJIF = 6
OPLT = 7
OPEQ = 8
OPHALT = 99

OPIN_DEF_INP = 5

num = list(map(int, open(sys.argv[1], "r").read().split(',')))

i = 0   # pointer

while True:
    three = num[i + 3]
    complete = num[i]

    op = complete % 100
    complete = int(complete / 100)
    m1 = complete % 10

    value_1 = None
    if m1 == 0:
        value_1 = num[num[i + 1]]
    elif m1 == 1:
        value_1 = num[i + 1]
    else:
        break

    if op == OPADD or op == OPMULTIPLY or op == OPLT or op == OPEQ:
        
        value_1 = None
        if m1 == 0:
            value_1 = num[num[i + 1]]
        elif m1 == 1:
            value_1 = num[i + 1]
        else:
            break

        complete = int(complete / 10)
        m2 = complete % 10
        value_2 = None

        if m2 == 0:
            value_2 = num[num[i + 2]]
        elif m2 == 1:
            value_2 = num[i + 2]
        else:
            break

        result = None
        if op == OPADD:
            result = value_1 + value_2
        elif op == OPMULTIPLY:
            result = value_1 * value_2
        elif op == OPLT:
            if value_1 < value_2:
                result = 1
            else:
                result = 0  
        else:
            if value_1 == value_2:
                result = 1
            else:
                result = 0
        i += 4
        num[three] = result
    elif op == OPIN:
        num[num[i + 1]] = OPIN_DEF_INP
        i += 2

    elif op == OPOUT:

        value_1 = None
        if m1 == 0:
            value_1 = num[num[i + 1]]
        elif m1 == 1:
            value_1 = num[i + 1]
        else:
            print("FUCK!")
            break
        print(value_1)
        i += 2

    elif op == OPJIT or op == OPJIF:

        value_1 = None
        if m1 == 0:
            value_1 = num[num[i + 1]]
        elif m1 == 1:
            value_1 = num[i + 1]
        else:
            break

        complete = int(complete / 10)
        m2 = complete % 10
        value_2 = None

        if m2 == 0:
            value_2 = num[num[i + 2]]
        elif m2 == 1:
            value_2 = num[i + 2]
        else:
            break 
        
        if op == OPJIT:
            if value_1 != 0:
                i = value_2
            else:
                i += 3
        else:
            if value_1 == 0:
                i = value_2
            else:
                i += 3
    elif op == OPHALT:
        break
    else:
        print(op)