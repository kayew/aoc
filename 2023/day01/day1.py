from sys import argv
import re

num = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def digit_calibration(d):
    out = [[c for c in line if c.isdigit()] for line in d]
    return sum([int(x[0]+x[-1]) for x in out])

def letter_calibration(d):
    regex = r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))" 
    match = [[num[letter] if not letter.isdigit() else letter for letter in re.findall(regex, n)] for n in d]
    # match = [re.findall(regex, n) for n in d]
    # for dig in match:
    #     for i in range(len(dig)):
    #         if not dig[i].isdigit():
    #             dig[i] = num[dig[i]]
    return sum([int(x[0]+x[-1]) for x in match])
    
d = open(argv[1]).read().splitlines()
print(f"Part 1: {digit_calibration(d)}")
print(f"Part 2: {letter_calibration(d)}")
