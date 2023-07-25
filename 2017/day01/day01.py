d = None

with open("day01_input.txt") as local_file:
    # read integer from file
    d = [int(x) for x in local_file.readline()]

l = len(d)

# Part 1
# part1 = 0
# for i in range(l):
#     if d[i] == d[(i + 1) % l]:
#         part1 += d[i]

print(f"Part 1: {sum(d[i] for i in range(l) if d[i] == d[(i+1) % l])}")

# Part 2
# part2 = 0
# for i in range(l):
#     if d[i] == d[(i + l // 2) % l]:
#         part2 += d[i] 

# print("Part 2: {}".format(part2))

print(f"Part 2: {sum(d[i] for i in range(l) if d[i] == d[(i+l // 2) % l])}")
