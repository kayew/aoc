from os import paramStr
import strutils, sugar, algorithm

let data = collect(newSeq):
  for x in lines(paramStr(1)):
    x.multiReplace(("F", "0"), ("B", "1"), ("L", "0"), ("R", "1"))
var sID = newSeq[int](0)

for line in data:
  var
    fRow = parseBinInt(line[0..^4])
    fCol = parseBinInt(line[^3..^1])

  sID.add(fRow * 8 + fCol)

sort(sID)
echo sID[^1]
