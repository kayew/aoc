import os,strutils,sequtils
from strformat import fmt

let sonar: seq[int] = paramStr(1).lines.toSeq.mapit(parseInt it)
var total: int = 0

for i in 0 ..< sonar.len()-1:
  if sonar[i+1] > sonar[i]:
    total+=1

echo fmt"Part 1: {total}"
