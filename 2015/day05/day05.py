from sys import argv


def read_data(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f]


def part1(d):
    naughty = 0
    vowels = set('aeiou')
    bad = ['ab', 'cd', 'pq', 'xy']
    def double(s): return any(a == b for a, b in zip(s, s[1:]))

    for ns in d:
        if any(x in ns for x in bad):
            naughty += 1
        elif not double(ns):
            naughty += 1
        elif len(vowels & set(ns)) < 3:
            naughty += 1

    return len(d) - naughty


def part2(d):
    pass


if __name__ == '__main__':
    d = read_data(argv[1])
    # print(d)
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
