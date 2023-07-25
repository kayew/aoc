from sys import argv
import array as arr

def read_data(filename: str) -> arr.array:
    with open(filename, "r", encoding="UTF-8") as f:
        return arr.array("i", [int(x) for x in f])
        # return np.array([int(x) for x in f])

def part1(d) -> int:
    # result = 0
    # for i in range(len(d)-1):
    #     if d[i] < d[i+1]:
    #         result += 1
    # return result
    return sum(d[i] < d[i + 1] for i in range(len(d) - 1))


def part2(d) -> int:
    nd = [d[i] + d[i-1] + d[i-2] for i in range(len(d) - 2)]
    return part1(nd)


d = read_data(argv[1])
print(f"Part 1: {part1(d)}")
print(f"Part 2: {part2(d)}")
