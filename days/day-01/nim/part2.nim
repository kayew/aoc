import os,strutils,sequtils
from strformat import fmt

let sonar: seq[int] = paramStr(1).lines.toSeq.mapit(parseInt it)

var
  total: int = 0
  newSonar: seq[int] = @[]

for i in 0 ..< sonar.len()-2:
  var slidingSum = sonar[i] + sonar[i+1] + sonar[i+2]
  newSonar.add(slidingSum)

for i in 0 ..< newSonar.len()-1:
  if newSonar[i+1] > newSonar[i]:
    total += 1

echo fmt"Part 2: {total}"