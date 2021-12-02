from os import paramStr
import tables
import strutils
from sequtils import toSeq

let
  required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  passports = paramStr(1).string.readfile.split("\n\n")

var valid: int = 0

for field in passports:
  var d = initTable[string, string]()
  for b in field.split():
    var kv = b.split(":")
    d[kv[0]] = kv[1]

  var invalid = false
  for req in required_fields:
    if req notin toSeq(d.keys):
      invalid = true

  if not invalid:
    valid += 1

echo valid
