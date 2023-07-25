from sys import argv
from numpy.lib.stride_tricks import sliding_window_view


def read_input(filename: str) -> list:
    with open(filename, "r") as f:
        return [
            list(map(lambda x: int(x.strip()), li.strip().split()))
            for li in f.readlines()
        ]


def part1(d: list) -> int:
    res = 0

    for tri in d:
        x,y,z = sorted(tri)
        if (x + y > z):
            res += 1

    return res
    # return sum([1 for tri in d if sum(sorted(tri)[:2]) > max(tri)])

def part2(d: list) -> int:
    res = 0
    for i in range(0, len(d), 3):
        for j in range(len(d[i])):
            x,y,z = sorted([d[i][j], d[i+1][j], d[i+2][j]])
            if x + y > z:
                res += 1
    return res


if __name__ == "__main__":
    d = read_input(argv[1])
    # print(d[:6])
    # # nd = list(zip(*d))[0]
    # # v = sliding_window_view(nd, 3, 1)
    # # print(v[:3])
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
    # for tri in zip(*d):
    #     print(tri)
