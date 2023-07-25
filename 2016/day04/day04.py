from sys import argv
from collections import Counter


def read_data(filename):
    with open(filename) as f:
        rooms = []
        for room in f.read().splitlines():
            r = room.split("-")
            name = "-".join(r[:-1])
            id_checksum = r[-1].split("[")
            sector_id = int(id_checksum[0])
            checksum = id_checksum[1][:-1]
            rooms.append((name, sector_id, checksum))
        return rooms


def part1(d):
    total = 0
    for name, sector_id, checksum in d:
        c = Counter(name)
        del c["-"]
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        c = "".join([k for k, _ in c[:5]])
        if c == checksum:
            total += sector_id
    return total


def part2(d):
    for name, sector_id, _ in d:
        name = [
            chr((((ord(c) - 97) + sector_id) % 26) + 97) if c != "-" else " "
            for c in name
        ]
        if "northpole" in "".join(name):
            return (sector_id, "".join(name))


d = read_data(argv[1])
# print(d)
print(f"Part 1: {part1(d)}")
print(f"Part 2: {part2(d)}")
