
def parse(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in f.readlines()]
    
def part1():
    return sum(parse('input.txt'))

print(part1())

def part2():
    seen = {0}
    total = 0
    while True:
        for num in parse("input.txt"):
            total += num
            if total in seen:
                return total
            seen.add(total)


print(part2())