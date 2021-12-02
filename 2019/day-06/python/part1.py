#!/usr/bin/env python

import sys

orbit_dict = set(map(lambda x: x.split(")"), open(sys.argv[1]).read().split("\n")))

print(orbit_dict)