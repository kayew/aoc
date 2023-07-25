from sys import argv


def read_data(filename):
    with open(filename, "r") as f:
        return [x for x in f.read()]


def move(movement):
    def add(position, visited):
        if position in visited:
            visited[position] += 1
        else:
            visited[position] = 1
    
    pos = (0, 0)
    visited = {pos: 1}
    for m in movement:
        match m:
            case "^":
                # north
                x, y = pos
                new_pos = (x, y + 1)
                pos = new_pos
                add(new_pos, visited)
            case "v":
                # south
                x, y = pos
                new_pos = (x, y - 1)
                pos = new_pos
                add(new_pos, visited)
            case ">":
                # east
                x, y = pos
                new_pos = (x + 1, y)
                pos = new_pos
                add(new_pos, visited)
            case "<":
                # west
                x, y = pos
                new_pos = (x - 1, y)
                pos = new_pos
                add(new_pos, visited)

    return visited


def part1(d):
    visited = move(d)
    return len(visited.keys())


def part2(d):
    santa_moves = [d[i] for i in range(0, len(d), 2)]
    robo_moves = [d[i] for i in range(1, len(d), 2)]

    visited = move(santa_moves) | move(robo_moves)

    return len(visited.keys())


if __name__ == "__main__":
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
