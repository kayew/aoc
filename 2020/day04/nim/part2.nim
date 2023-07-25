from os import paramStr
import tables
import strutils
import nre except toSeq

let
  passports = paramStr(1).string.readfile.split("\n\n")
  valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  valid_units = ["cm", "in"]

var valid: int = 0

for field in passports:
  var d = initTable[string, string]()
  for b in field.split():
    var kv = b.split(":")
    d[kv[0]] = kv[1]

  try:
    if parseInt(d["byr"]) notin 1920..2002: continue
    if parseInt(d["iyr"]) notin 2010..2020: continue
    if parseInt(d["eyr"]) notin 2020..2030: continue

    var
      hgt = d["hgt"]
      unit = hgt[^2..^1]
      num = parseInt(hgt[0..^3])

    if unit notin valid_units:
      continue

    if (unit == "cm") and (num notin 150..193):
      continue

    if (unit == "in") and (num notin 59..76):
      continue

    if nre.match(d["hcl"], re"#([0-9a-f]{6})").isNone or len(d["hcl"]) != 7:
      continue

    if d["ecl"] notin valid_ecl:
      continue

    if nre.match(d["pid"], re"[0-9]{9}").isNone or len(d["pid"]) != 9:
      continue
  except:
    continue

  inc(valid)

echo valid
