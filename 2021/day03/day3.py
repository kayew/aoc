from sys import argv
import pandas as pd
import numpy as np


def read_data(filename: str) -> pd.DataFrame:
    with open(filename, "r", encoding="UTF-8") as f:
        return pd.DataFrame([list(map(lambda y: y, x.strip())) for x in f])


def part1(d: pd.DataFrame) -> int:
    res = [d[col].mode()[0] for col in d.columns]

    g = int("".join(res), 2)
    e = g ^ int("1" * len(res), 2)

    return g * e


def part2(d: pd.DataFrame) -> None:
    pass
# def part2(d: pd.DataFrame) -> int:
#     def oxygen():
#         # get most common bit of position
#         df = d.copy(deep=True)
#         curr_column = 0
#         max_column = len(df.columns)
#         while curr_column < max_column - 1:
#             mcb = df[curr_column].value_counts().index[0]
#             to_drop = df[df[curr_column] != mcb].index
#             df.drop(to_drop, inplace=True)
#             curr_column += 1

#         if len(df.index) >= 2:
#             df.drop(df[df[curr_column] != "1"].index, inplace=True)
#         res = df.to_numpy().flatten()
#         return int("".join(res), 2)

#     def co2():
#         # get least common bit of position
#         df = d.copy(deep=True)
#         curr_column = 0
#         max_column = len(df.columns)
#         while curr_column < max_column - 1:
#             lcb = df[curr_column].value_counts().index[-1]
#             to_drop = df[(df[curr_column] != lcb)].index
#             df.drop(to_drop, inplace=True)
#             curr_column += 1

#         if len(df.index) >= 2:
#             df.drop(df[df[curr_column] != "0"].index, inplace=True)
#         res = df.to_numpy().flatten()
#         return int("".join(res), 2)

#     return oxygen() * co2()


if __name__ == "__main__":
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}\nPart 2: {part2(d)}")
