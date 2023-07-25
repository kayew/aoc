from sys import argv


def read_data(filename):
    with open(filename, 'r') as f:
        return [x.split() for x in f]


def part1(d: list[list[str]]):
    valid = 0

    for passphrase in d:
        if len(passphrase) == len(set(passphrase)):
            valid += 1

    return valid


def part2(d: list[list[str]]):
    valid = 0

    for passphrase in d:
        anagrams = [''.join(sorted(word)) for word in passphrase]
        if len(anagrams) == len(set(anagrams)):
            valid += 1

    return valid


if __name__ == '__main__':
    d = read_data(argv[1])

    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
