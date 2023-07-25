# import pandas as pd
# import numpy as np
from sys import argv


def read_input(filename: str) -> list:
    with open(filename, 'r') as f:
        return [(d[0], int(d[1:])) for d in f.read().split(', ')]
    

def manhattan(pos: complex):
    return abs(int(pos.real)) + abs(int(pos.imag))


def part1(d: list) -> int:
    direction = 1+0j
    position = 0+0j

    TURNS = {'L': 0+1j, 'R': 0-1j}

    for dir, val in d:
        direction *= TURNS[dir]
        position += direction * val

    return manhattan(position)


def part2(d: list) -> int:
    direction = 1+0j
    position = 0+0j
    visited = {position}

    TURNS = {'L': 0+1j, 'R': 0-1j}

    for dir, val in d:
        direction *= TURNS[dir]

        for _ in range(val):
            position += direction

            if position in visited:
                return manhattan(position)
            else:
                visited.add(position)

    raise Exception('could not find')


if __name__ == '__main__':
    d = read_input(argv[1])
    # d = [(d[0], int(d[1:])) for d in 'R8, R4, R4, R8'.split(', ')]
    print(f"Part 1: {part1(d)}\nPart 2: {part2(d)}")
