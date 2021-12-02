#!/usr/bin/env lua5.4

local function parse(inp)
    local num = {}
    for str in io.lines(inp) do
        num[#num+1] = str
    end
    return num
end

local data = parse(arg[1])
local slope = {3, 1}

local numRows = #data
local numCols = string.len(data[1])

local trees = 0
local x = 0

for y=1,numRows,slope[2] do
    if data[y]:sub(x+1, x+1) == '#' then
        trees = trees + 1
    end
    x = (x + slope[1]) % numCols
end

print("trees "..trees)
