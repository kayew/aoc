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

local function repeats(s,c)
    local _,n = s:gsub(c,"")
    return n
end

local total = 0
local f = io.input(arg[1])
for line in f:lines() do
    local param = _split(line:gsub(":","")," ") -- had to peek for this one
    local passRange = _split(param[1], "-")
    local targetLetter = param[2]
    local password = param[3]

    local letterMatch = repeats(password, targetLetter)
    if letterMatch >= tonumber(passRange[1]) and letterMatch <= tonumber(passRange[2]) then
        total = total + 1
    end
end 
print(total)
f:close()
