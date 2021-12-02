import os
import strutils
import sequtils
import strformat

var nums = toSeq(lines(paramStr(1))).mapit(parseInt it)
let target = 2020

proc part1(): seq =
  for i in nums:
    for j in nums:
      if i+j == target:
        assert i*j == 970816
        return @[i, j, i*j]

proc part2(): seq =
  for i in nums:
    for j in nums:
      for k in nums:
        if i+j+k == target:
          assert i*j*k == 96047280
          return @[i, j, k, i*j*k]

var
  result1 = part1()
  result2 = part2()

echo fmt"Part 1: {result1[0]} * {result1[1]} = {result1[2]}"
echo fmt"Part 2: {result2[0]} * {result2[1]} * {result2[2]} = {result2[3]}"
