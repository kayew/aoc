#!/usr/bin/env luajit

function part1()
    local file = io.lines(arg[1])
    local total = 0
    for line in file do
        total = total + math.floor(line / 3) - 2
    end
    return total
end

--=======================
-- PART 2
--=======================


function total_fuel(fuel)
    local fuels_fuel = math.floor(fuel / 3) - 2
    if fuels_fuel <= 0 then
        return 0
    else 
        return fuels_fuel + total_fuel(fuels_fuel)
    end
end

function part2()
    local file = io.lines(arg[1])
    local total = 0
    for line in file do
        total = total + total_fuel(line)
    end
    return total
end

print("Part 1: " .. part1() .. "\n" .. "Part 2: " .. part2())