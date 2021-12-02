from os import paramStr
import sugar, strutils

var data: seq[string] = collect(newSeq):
  for x in lines(paramStr(1)):
    x.strip()

proc execute(d: seq[string]): array[2, int] = 
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
      of "nop":
        i += 1
      else: discard

  return [i, acc]

proc switch_op(inst, swap: string, inst_list: var seq[string]): int =
  var to_switch = collect(newSeq):
    for i in 0 ..< inst_list.len:
      if inst_list[i][0..2] == inst:
        i
  for j in to_switch:
    inst_list[j] = inst_list[j].replace(inst, swap)    
    var r = execute(inst_list)
    inst_list[j] = inst_list[j].replace(swap, inst)  
    if r[0] == inst_list.len:
      return r[1]

for x in [("jmp", "nop"), ("nop", "jmp")]:
    echo switch_op(x[0], x[1], data)
