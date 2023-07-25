from os import paramStr
from algorithm import sort
import sugar, strutils, sequtils

let 
  data = collect(newSeq):
    for x in lines(paramStr(1)):
      parseInt(x.strip())
  step = parseInt(paramStr(2))

proc find_invalid(step: int, data: seq[int]): int = 
  for i in step ..< data.len:
    var found = false
    for j in (i - step) ..< i:
      for k in (i - step) ..< i:
        if k!=j and data[i] == data[k] + data[j]:
          found = true
    if not found:
      return data[i]

let invalid_num = find_invalid(step, data)

var s = newSeq[int](0)

for i in 0 ..< data.len:
  for j in i+1 ..< data.len:
    if data[i ..< j+1].foldl(a+b) == invalid_num:
      for x in data[i ..< j+1]:
        s.add(x)
    if data[i ..< j+1].foldl(a+b) > invalid_num:
      break

s.sort
echo s[0]+s[^1]
