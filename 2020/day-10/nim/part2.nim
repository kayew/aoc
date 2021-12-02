from os import paramStr
from algorithm import sorted
import strutils, sequtils, tables

var adapter_list = readFile(paramStr(1)).split.map(parseInt).sorted

var
  highest = adapter_list[^1] + 3
  combos = [0].toCountTable # bascially defaultdict(lambda: 0)

adapter_list.add(highest)
combos[0] = 1

for x in adapter_list:
  combos[x] = combos[x - 1] + combos[x - 2] + combos[x - 3]

echo combos[highest-3]
