from sys import argv
from collections import Counter


def read_data(filename):
    with open(filename, 'r') as f:
        return [x for x in f.readline()]


def part1(d):
    count = Counter(d)
    return count['('] - count[')']


def part2(d):
    count = 0
    floor = 0

    for dir in d:
        if floor == -1:
            break
        match dir:
            case '(':
                floor += 1
            case ')':
                floor -= 1
            case _:
                pass
        count += 1

    return count


if __name__ == '__main__':
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
