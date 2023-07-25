#!/usr/bin/env luajit

local OPADD = 1
local OPMULTIPLY = 2
local OPHALT = 99

local num = {}
for str in io.lines(arg[1])():gmatch("%d+") do
    num[#num+1] = tonumber(str)
end

num[2] = 12
num[3] = 2

local i = 1

while true do
    one = num[i + 1]+1
    two = num[i + 2]+1
    three = num[i + 3]+1
    if num[i] == OPADD then
        num[three] = num[one] + num[two]
        i = i + 4
    elseif num[i] == OPMULTIPLY then
        num[three] = num[one] * num[two]
        i = i + 4
    elseif num[i] == OPHALT then
        break
    end
end

print("Solution: " .. num[1])