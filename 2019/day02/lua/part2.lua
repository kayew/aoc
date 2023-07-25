local OPADD = 1
local OPMULTIPLY = 2
local OPHALT = 99

function table.clone(org)
    return {table.unpack(org)}
end

function interpret_intcode(noun, verb, num)

    num[2] = noun
    num[3] = verb

    local i = 1

    while true  do
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
    return num[1]
end

function find_value()
    local num = {}
    for str in io.lines(arg[1])():gmatch("%d+") do
        num[#num+1] = tonumber(str)
    end
    for noun = 0, 99, 1 do
        for verb = 0, 99, 1 do
            if interpret_intcode(noun, verb, table.clone(num)) == 19690720 then
                return 100 * noun + verb
            end
        end
    end
end

print("Solution: " .. find_value())