import os,strutils,sequtils,sugar
from strformat import fmt

let data = collect(newSeq):
  for x in paramStr(1).lines:
    x.split.toSeq
    
var
  xPos = 0
  depth = 0

for move in data:
  var dir = move[1].parseInt
  case move[0]:
    of "forward":
      xPos += dir
    of "up":
      depth -= dir
    of "down":
      depth += dir
    else:
      echo fmt"Unknown move: {move[0]}"
  
echo fmt"Part 1: {xPos*depth}"