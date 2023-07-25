from sys import argv

d = {}
with open('day21_input.txt', 'r') as l_f:
    for lines in l_f.readlines():
        line = lines.strip().split(': ')
        d[line[0]] = line[1]
    # print(d)

known_d = {}

for k, v in d.copy().items():
    try:
        known_d[k] = int(v)
        d.pop(k)
    except ValueError:
        continue



