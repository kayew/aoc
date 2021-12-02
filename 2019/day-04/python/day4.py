import sys

def part1():
    min_max = [int(i) for i in sys.argv[1].split('-')]
    p_min = min_max[0]
    p_max = min_max[1]

    total = 0
    for i in range(p_min, p_max):
        s = str(i)
        adj = False
        inc = True
        for j in range(5):
            if s[j] > s[j + 1]:
                inc = False
            if s[j] == s[j + 1]:
                adj = True
        if adj and inc:
            total += 1
    return total

def part2():
    min_max = [int(i) for i in sys.argv[1].split('-')]
    p_min = min_max[0]
    p_max = min_max[1]

    valid = []
    for i in range(p_min, p_max):
        s = str(i)
        inc = True
        for j in range(5):
            if s[j] > s[j + 1]:
                inc = False
        if inc:
            total_nums = {}
            for char in s:
                if char in total_nums:
                    total_nums[char] += 1
                else:
                    total_nums[char] = 1
            if 2 in total_nums.values():
                valid.append(i)
    return len(valid)

print("Part 1: " + str(part1()) + "\n" + "Part 2: " + str(part2()))