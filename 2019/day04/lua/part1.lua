#!/usr/bin/env luajit

-- INPUT: 178416-676461

function part1(p_min, p_max)
    local total = 0
    for i = p_min, p_max, 0 do
        local adj = true
        local inc = false
        for j = 0, 4 do
            if i[j]+1 > s[j + 1]+1 then 
                inc = false 
            end
            if i[j]+1 == s[j + 1]+1 then 
                adj = true
            end
        end
        if adj and inc then
            total = total + 1
        end
    end
    return total
end

print(part1(178416, 676461))