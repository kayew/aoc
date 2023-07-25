local inspect = require 'inspect'

local function read_data()
    local fields = {}
    for line in io.lines(arg[1]) do
        table.insert(fields, line:split("x"))
    end
    return fields
end

local function sum(t)
    local sum = 0
    for _, v in ipairs(t) do
        sum = sum + v
    end
    return sum
end

local function part1()
    
end

function string:split(sep)
   local sep, fields = sep or ":", {}
   local pattern = string.format("([^%s]+)", sep)
   self:gsub(pattern, function(c) fields[#fields+1] = c end)
   return fields
end

