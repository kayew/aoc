from sys import argv


def read_data(filename: str) -> list:
    with open(filename, 'r') as f:
        return [x.split() for x in f]


def process(register, d):
    def read(val):
        try:
            return int(val)
        except ValueError:
            return register[val]
    
    i = 0

    while i < len(d):
        inst = d[i]
        match inst[0]:
            case 'cpy':
                x = inst[1]
                y = inst[2]
                register[y] = read(x)
            case 'inc':
                x = inst[1]
                register[x] += 1
            case 'dec':
                x = inst[1]
                register[x] -= 1
            case 'jnz':
                x = inst[1]
                y = inst[2]
                if read(x) != 0:
                    i += read(y)
                    i -= 1
            case _:
                break
        i += 1

def part1(d: list) -> int:
    register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    process(register, d)

    return register['a']


def part2(d: list) -> int:
    register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    process(register, d)

    return register['a']


if __name__ == '__main__':
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}\nPart 2: {part2(d)}")
