#!/usr/bin/env python3

import sys
import re

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # "cid" not needed as it is optional
valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_units = ["cm", "in"]

passports = [f for f in open(sys.argv[1], 'r').read().split("\n\n")]

valid = 0

for field in passports:
    d = {}
    for b in field.split():
        k, v = b.split(":")
        d[k] = v

    try:
        if not (1920 <= int(d["byr"]) <= 2002):
            continue
        if not (2010 <= int(d["iyr"]) <= 2020):
            continue
        if not (2020 <= int(d["eyr"]) <= 2030):
            continue

        if d["hgt"][-2:] not in valid_units:
            continue

        hgt = int(d["hgt"][:-2])

        if (d["hgt"][-2:] == "cm") and not (150 <= hgt <= 193):
            continue
        if (d["hgt"][-2:] == "in") and not (59 <= hgt <= 76):
            continue

        if not re.match(r"#([0-9a-f]{6})", d["hcl"]):
            continue

        if d["ecl"] not in valid_ecl:
            continue

        if len(d["pid"]) != 9:
            continue
    except:
        continue

    valid += 1

print(valid)
