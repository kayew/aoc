#!/usr/bin/env python3

import sys

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # "cid" not needed as it is optional

passports = [f for f in open(sys.argv[1], 'r').read().split("\n\n")]

valid = 0

for field in passports:
    d = {}
    for b in field.split():
        k, v = b.split(":")
        d[k] = v

    invalid = False
    for req in required_fields:
        if req not in d.keys():
            invalid = True

    if not invalid:
        valid += 1

print(valid)
