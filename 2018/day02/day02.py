from collections import Counter
from sys import argv
from itertools import product

def read_data(filename):
    with open(filename, 'r') as local_file:
        return [x.strip() for x in local_file.readlines()]


def part1(d):
    match_2 = 0
    match_3 = 0
    for line in d:
        c = Counter(line).values()
        found_2, found_3 = False, False
        for vals in c:
            match vals:
                case 3 if not found_3:
                    match_3 += 1
                    found_3 = True
                case 2 if not found_2:
                    match_2 += 1
                    found_2 = True
                case _:
                    continue
    return match_2*match_3


def part2(d):
    for id1, id2 in product(d, d):
        diffs = 0
        for i, chars in enumerate(zip(id1, id2)):
            if chars[0] != chars[1]:
                if diffs > 1:
                    break
                else:
                    diffs += 1
        if diffs == 1:
            return id1[:(i//2)] + id2[-(i//2):]


data = read_data(argv[1]) 
# print(data)
print(f"Part 1: match_2 * match_3 = {part1(data)}")
print(f"Part 2: {part2(data)}")
