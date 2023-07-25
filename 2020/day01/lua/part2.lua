#!/usr/bin/env lua5.4

local function parseInput()
    local num = {}
    for str in io.lines(arg[1]) do
        num[#num+1] = tonumber(str)
    end
    return num
end

local num = parseInput()
local target = 2020
-- local target = 99920044

local function part2()
    for i=1, #num do
        for j=1, #num do
            for k=1, #num do
                if num[i] + num[j] + num[k] == target then
                    return {num[i], num[j], num[k], num[i] * num[j] * num[k]}
                end
            end
        end
    end
end

local result = part2()
print("Part 2: "..result[1].." * "..result[2].." * "..result[3].." = "..result[4])
