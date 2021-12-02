import os
import strutils
import sequtils
import strformat

var total = 0
var letterMatch = 0

proc part1(): int =
  total = 0
  for line in lines(paramStr(1)):
    var param = line.split()
    var passRange = param[0].split("-").mapIt(parseInt it)
    var targetLetter = param[1][0]
    var password = param[2]

    var letterMatch = count(password, targetLetter)
    if letterMatch >= passRange[0] and letterMatch <= passRange[1]:
      total += 1
  return total

proc part2(): int =
  total = 0
  for line in lines(paramStr(1)):
    letterMatch = 0
    var param = line.split()
    var passIndex = param[0].split("-").mapIt(parseInt it)
    var targetLetter = param[1][0]
    var password = param[2]

    if password[passIndex[0]-1] == targetLetter:
      letterMatch += 1
    if password[passIndex[1]-1] == targetLetter:
      letterMatch += 1

    if letterMatch == 1:
      total += 1
  return total

echo fmt"Part 1: {part1()}, Part 2: {part2()}"
