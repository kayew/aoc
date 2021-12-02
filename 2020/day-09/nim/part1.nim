from os import paramStr
import sugar, strutils

let 
  data = collect(newSeq):
    for x in lines(paramStr(1)):
      parseInt(x.strip())
  step = parseInt(paramStr(2))

for i in step ..< data.len:
  var found = false
  for j in (i - step) ..< i:
    for k in (i - step) ..< i:
      if k!=j and data[i] == data[k] + data[j]:
        found = true
  if not found:
    echo data[i]
