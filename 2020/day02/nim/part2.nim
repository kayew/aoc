import os
import strutils
import sequtils

var total = 0
var letterMatch = 0

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

echo total
