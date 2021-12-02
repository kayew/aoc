from os import paramStr
import strutils, strformat

type SetType = char or byte or bool or int16 or uint16 or enum
proc toSet[T: SetType](ar: openArray[T]): set[T] =
  for x in ar:
    result.incl(x)

let data = paramStr(1).string.readfile.split("\n\n")

proc part1(d: seq[string]): int =
  for q in data:
    var u: set[char]
    for c in q.split():
        u = u + c.toSet

    result += len(u)

proc part2(d: seq[string]): int =
  for q in data:
    var u: set[char] = {'a'..'z'}
    for c in q.split():
      u = u * c.toSet

    result += len(u)

echo &"Part 1: {part1(data)} Part 2: {part2(data)}"
