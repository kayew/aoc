#!/usr/bin/env python

import sys
from copy import deepcopy

data = [x.strip().split() for x in open(sys.argv[1]).readlines()]
data_copy = deepcopy(data)
surrounding = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
total = 0

def count_seat(seat_map, i, j, char):
    total = 0
    for x in surrounding:
        try:
            current_pos = seat_map[i + x[0]][j + x[1]]
            if current_pos == char:
                total += 1
        except IndexError:
            continue
    return total

def change_seat(seat_map, i, j):
    if seat_map[i][j] == "L":
        count = count_seat(seat_map, i, j, "#")
        if count == 0:
            return "#"
    elif seat_map[i][j] == "#":
        count = count_seat(seat_map, i, j, "L")
        if count >= 4:
            return "L"
    else:
        return seat_map[i][j]

while True:
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = change_seat(data_copy, i, j)
    if data == data_copy:
        break
        # else:
        #     data_copy[i][j] = change_seat(data_copy, i, j)

print(data)

