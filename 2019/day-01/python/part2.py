#!/usr/bin/env python

""" CHALLENGE, PART 2:

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. 
Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. 

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? 
(Calculate the fuel requirements for each module separately, then add them all up at the end.)

"""

import math
import sys

def total_fuel(fuel): # recursion!
    fuels_fuel = math.floor(fuel / 3) - 2 # the fuel required for each amount of fuel
    if fuels_fuel <= 0:
        return 0 # return zero if less than zero to avoid negatives
    else:
        return fuels_fuel + total_fuel(fuels_fuel) # total together the total amount of fuel needed

with open(sys.argv[1]) as file: # same as part 1...
    lines = file.readlines()
    total = 0
    for line in lines:
        total += total_fuel(int(line)) # recursion to determine the fuel for each mass of fuel
    print(total)