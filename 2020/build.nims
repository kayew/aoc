#!/usr/bin/env nim
import strformat, os
exec(fmt"nim c -d:danger --opt:speed --gc:arc {commandLineParams()[1]}")