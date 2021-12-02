from os import paramStr
import sugar, strutils, strformat

let data = collect(newSeq):
  for x in lines(paramStr(1)):
    x.strip()

var
  acc = 0
  visited_pos: set[uint16] = {}
  i = 0

while (i.uint16 notin visited_pos) and (i < len(data)):
  var
    ins = data[i][0..2]
    amt = parseInt(data[i][4..^1])
  case ins:
  of "acc":
    visited_pos.incl(i.uint16)
    acc += amt
    i += 1
  of "jmp":
    visited_pos.incl(i.uint16)
    i += amt
    continue
  of "nop":
    i += 1
    continue
  else: discard

echo fmt"acc: {acc}"
