from os import paramStr
import strutils, strformat, sugar, algorithm

let data = collect(newSeq):
  for x in lines(paramStr(1)):
    x.multiReplace(("F", "0"), ("B", "1"), ("L", "0"), ("R", "1"))
var sID = newSeq[int](0)

proc part1(d: seq[int]): int =
  return d[^1]

proc part2(d: seq[int]): int =
  for x in d[0]..d[^1]:
    if x notin d:
      return x

for line in data:
  var
    fRow = parseBinInt(line[0..^4])
    fCol = parseBinInt(line[^3..^1])

  sID.add(fRow * 8 + fCol)

sort(sID)

echo fmt"Part 1: {part1(sID)}", "\n", fmt"Part 2: {part2(sID)}"
