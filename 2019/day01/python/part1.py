#!/usr/bin/env python

""" CHALLENGE:

Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement. 
To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

"""

import math
import sys

with open(sys.argv[1]) as file:     # open the input as "file"
    lines = file.readlines()    # set file.readlines() as the lines to loop through
    total = 0   # the total we want
    for line in lines:
        total += math.floor((int(line) / 3)) - 2 #   calculate total for each line
    print(total) #   print our total fuel