from sys import argv

d = open(argv[1]).read().splitlines()

def part1(d):
    games = []
    for game in d:
        fail = False
        gid, cubes = game.split(": ")
        gid = int(gid.split()[1])
        for cube in cubes.split("; "):
            for color in cube.split(", "):
                amnt, color = color.split()
                if color[0] == 'r' and int(amnt) > 12:
                    fail = True
                elif color[0] == 'g' and int(amnt) > 13:
                    fail = True
                elif color[0] == 'b' and int(amnt) > 14:
                    fail = True
        if not fail:
            games.append(gid)
    return sum(games)

def part2(d):
    games = []
    for game in d:
        gid, cubes = game.split(": ")
        gid = int(gid.split()[1])
        rmin,gmin,bmin = 0,0,0
        for cube in cubes.split("; "):
            for color in cube.split(", "):
                amnt, color = color.split()
                if color[0] == 'r':
                    rmin = max(rmin, int(amnt))
                elif color[0] == 'g':
                    gmin = max(gmin, int(amnt))
                elif color[0] == 'b':
                    bmin = max(bmin, int(amnt))
        games.append(rmin*gmin*bmin)
    return sum(games)

print(f"Part 1: {part1(d)}")
print(f"Part 2: {part2(d)}")
