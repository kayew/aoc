import os
import strutils
import sequtils

var total = 0

for line in lines(paramStr(1)):
  var param = line.split()
  var passRange = param[0].split("-").mapIt(parseInt it)
  var targetLetter = param[1][0]
  var password = param[2]

  var letterMatch = count(password, targetLetter)
  if letterMatch >= passRange[0] and letterMatch <= passRange[1]:
    total += 1

echo total
