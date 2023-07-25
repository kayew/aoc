#!/usr/bin/env lua5.4

local function _split(str, on, set)
    local ret = {};
    local s, e;
    while str:find(on) do
        s, e = str:find(on);
        local result = str:sub(0, s - 1);
        if set then
                ret[result] = "";
        else
                table.insert(ret, result);
        end
        str = str:sub(e + 1);
    end
    if set then
        ret[str] = "";
    else
        table.insert(ret, str);
    end
    return ret;
end

local total = 0
local letterMatch = nil
local f = io.input(arg[1])
for line in f:lines() do
    letterMatch = 0
    local param = _split(line:gsub(":","")," ")
    local passIndex = _split(param[1], "-")
    local targetLetter = param[2]
    local password = param[3]

    if password:sub(passIndex[1],passIndex[1]) == targetLetter then
        letterMatch = letterMatch + 1
    end
    if password:sub(passIndex[2],passIndex[2]) == targetLetter then
        letterMatch = letterMatch + 1
    end

    if letterMatch == 1 then
        total = total + 1
    end

end 
print(total)
f:close()
