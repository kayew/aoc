#!/usr/bin/env lua5.4

local function parse(inp)
    local num = {}
    for str in io.lines(inp) do
        num[#num+1] = str
    end
    return num
end

local data = parse(arg[1])
local slopes = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

local numRows = #data
local numCols = string.len(data[1])

local totalTrees = 1

local function solve(slope)
    local trees = 0
    local x = 0
    for y=1,numRows,slope[2] do
        if data[y]:sub(x+1, x+1) == '#' then
            trees = trees + 1
        end
        x = (x + slope[1]) % numCols
    end
    return trees
end

for i=1, #slopes do
    totalTrees = totalTrees * solve(slopes[i])
end

print("total trees: ".. totalTrees)
