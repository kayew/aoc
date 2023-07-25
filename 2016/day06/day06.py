import pandas as pd
from sys import argv


def read_data(filename: str):
    with open(filename, 'r') as f:
        return pd.DataFrame([list(map(lambda y: y, x.strip())) for x in f])
    

def part1(d: pd.DataFrame):
    res = []

    for col in d.columns:
        res.append(d[col].value_counts().index[0])

    return "".join(res)


def part2(d: pd.DataFrame):
    res = []

    for col in d.columns:
        res.append(d[col].value_counts().index[-1])

    return "".join(res)


if __name__ == '__main__':
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
