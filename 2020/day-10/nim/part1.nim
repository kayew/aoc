from os import paramStr
from algorithm import sorted
import strutils, strformat, sequtils

var adapter_list = readFile(paramStr(1)).split.map(parseInt).sorted

var
  diff_1 = 1
  diff_3 = 0
  highest = adapter_list[^1] + 3

adapter_list.add(highest)

for i in 0 ..< adapter_list.len - 1:
  if adapter_list[i+1] - adapter_list[i] == 3:
    diff_3 += 1
  if adapter_list[i+1] - adapter_list[i] == 1:
    diff_1 += 1

echo fmt"{diff_1} * {diff_3} = {diff_3 * diff_1}"
