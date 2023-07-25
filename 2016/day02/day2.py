from sys import argv

def read_input(filename) -> list:
    with open(filename, "r") as f:
        return [list(li.strip()) for li in f]

def part1(d: list):
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    x, y = 1, 1
    code = []
    for line in d:
        for c in line:
            match c:
                case 'U':
                    x = max(x-1, 0)
                case 'D':
                    x = min(x+1, 2)
                case 'L':
                    y = max(y-1, 0)
                case 'R':
                    y = min(y+1, 2)
                case _:
                    continue
        code.append(keypad[x][y])
    return ''.join(map(str, code))

def part2(d):
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]
    x, y = 2, 0
    code = []
    for line in d:
        for c in line:
            match c:
                case 'U':
                    x = max(x-1, 0) if keypad[max(x-1, 0)][y] else x
                case 'D':
                    x = min(x+1, 4) if keypad[min(x+1, 4)][y] else x
                case 'L':
                    y = max(y-1, 0) if keypad[x][max(y-1, 0)] else y
                case 'R':
                    y = min(y+1, 4) if keypad[x][min(y+1, 4)] else y
                case _:
                    continue
        code.append(keypad[x][y])
    return ''.join(map(str, code))


d = read_input(argv[1])
print(f"Part 1: {part1(d)}")
print(f"Part 2: {part2(d)}")

