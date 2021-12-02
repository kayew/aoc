from os import paramStr
import strutils

type SetType = char or byte or bool or int16 or uint16 or enum
proc toSet[T: SetType](ar: openArray[T]): set[T] =
  for x in ar:
    result.incl(x)

let data = paramStr(1).string.readfile.split("\n\n")

var total = 0

for q in data:
  var u: set[char] = {'a'..'z'}
  for c in q.split():
    u = u * c.toSet

  total += len(u)

echo total
