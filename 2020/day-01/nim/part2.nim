import os
import strutils
import sequtils
import strformat

var nums = toSeq(lines(paramStr(1))).mapit(parseInt it)
let target = 2020
# let target = 99920044

proc main(): seq =
  for i in nums:
    for j in nums:
      for k in nums:
        if i+j+k == target:
          assert i*j*k == 96047280
          return @[i, j, k, i*j*k]

var result = main()
echo fmt"{result[0]} * {result[1]} * {result[2]} = {result[3]}"
