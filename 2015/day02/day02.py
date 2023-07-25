from sys import argv


def read_data(filename: str) -> list[list[int]]:
    with open(filename, 'r') as f:
        return [list(map(lambda y: int(y), x.strip().split('x'))) for x in f]


def part1(d: list[list[int]]) -> int:
    # total = 0
    # for l, w, h in d:
    #     sq = [2*l*w, 2*w*h, 2*h*l]
    #     total += sum(sq) + (min(sq)//2)
    # return total
    return sum(
         sum([2*l*w, 2*w*h, 2*h*l])+ (min([2*l*w, 2*w*h, 2*h*l])//2) for l, w, h in d
    )

def part2(d) -> int:
    # total = 0
    # for l,w,h in d:
    #     peri = [2*(l+w), 2*(w+h), 2*(h+l)]
    #     cubic = l*w*h
    #     total += min(peri) + cubic
    # return total
    return sum(min([2*(l+w), 2*(w+h), 2*(h+l)]) + (l*w*h) for l, w, h in d)


if __name__ == '__main__':
    d = read_data(argv[1])
    print(f"Part 1: {part1(d)}")
    print(f"Part 2: {part2(d)}")
