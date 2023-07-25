from sys import argv


def read_data(filename: str) -> list[tuple[str, int]]:
    with open(argv[1], "r", encoding="UTF-8") as f:
        a = [lst.strip().split(" ") for lst in f.readlines()]
        return list(map(lambda x: (x[0], int(x[1])), a))


def part1(a) -> int:
    d: dict[str, list[int]] = {"forward": [], "down": [], "up": []}
    for dir, val in a:
        d[dir].append(val)

    x_pos = sum(d["forward"])
    y_pos = sum(d["down"]) - sum(d["up"])

    return x_pos * y_pos


def part2(a) -> int:
    aim = 0
    x_pos = 0
    y_pos = 0
    for dir, val in a:
        match dir:
            case "forward":
                x_pos += val
                y_pos += aim * val
            case "down":
                aim += val
            case "up":
                aim -= val
            case _:
                pass
    return x_pos * y_pos


if __name__ == "__main__":
    a = read_data(argv[1])
    # print(a)
    print(f"Part 1: {part1(a)}\nPart 2: {part2(a)}")
