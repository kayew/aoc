import os
import sequtils
import strformat

let
  data: seq[string] = toSeq(lines(paramStr(1)))
  slopes: seq[tuple] = @[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

var
  numRows: int = len(data)
  numCols: int = len(data[0])
  totalTrees: int = 1

proc solve(slope: tuple): int =
  var trees: int = 0
  var x: int = 0
  for y in countup(0, numRows-1, slope[1]):
    if data[y][x] == '#':
      trees += 1
    x = (x + slope[0]) mod numCols
  return trees

for s in slopes:
  totalTrees *= solve(s)

echo fmt"Total Trees: {totalTrees}"
