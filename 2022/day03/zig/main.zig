const std = @import("std");
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
const allocator = gpa.allocator();
const print = std.debug.print;

fn determine_priority(i: u8) usize {
    if (std.ascii.isLower(i)) {
        return (i - 'a') + 1;
    } else {
        return (i - 'A') + 27;
    }
}

fn p1_parse(input: []const u8) !std.ArrayList([2]std.AutoHashMap(u8, void)) {
    var res = std.ArrayList([2]std.AutoHashMap(u8, void)).init(allocator);
    var lines = std.mem.split(u8, input, "\n");

    while (lines.next()) |line| {
        const left = line[0..(line.len / 2)];
        const right = line[(line.len / 2)..line.len];
        var left_set: std.AutoHashMap(u8, void) = std.AutoHashMap(u8, void).init(allocator);
        for (left) |c| {
            try left_set.put(c, {});
        }
        var right_set: std.AutoHashMap(u8, void) = std.AutoHashMap(u8, void).init(allocator);
        for (right) |c| {
            try right_set.put(c, {});
        }
        try res.append([2]std.AutoHashMap(u8, void){ left_set, right_set });
    }

    return res;
}

fn part1(d: std.ArrayList([2]std.AutoHashMap(u8, void))) !usize {
    var sum: usize = 0;
    for (d.items) |hms| {
        var left: std.AutoHashMap(u8, void) = hms[0];
        var right: std.AutoHashMap(u8, void) = hms[1];
        var left_it = left.keyIterator();
        while (left_it.next()) |k| {
            if (right.contains(k.*)) {
                sum += determine_priority(k.*);
            }
        }
    }

    return sum;
}

fn p2_parse(input: []const u8) !std.ArrayList(std.AutoHashMap(u8, void)) {
    var res = std.ArrayList(std.AutoHashMap(u8, void)).init(allocator);
    var lines = std.mem.split(u8, input, "\n");

    while (lines.next()) |line| {
        var hs = std.AutoHashMap(u8, void).init(allocator);
        for (line) |c| {
            try hs.put(c, {});
        }
        try res.append(hs);
    }

    return res;
}

fn part2(d: std.ArrayList(std.AutoHashMap(u8, void))) !usize {
    var sum: usize = 0;
    var elves = d.items;

    for (0..(elves.len - 2)) |i| {
        const elf1: std.AutoHashMap(u8, void) = elves[i+0];
        const elf2: std.AutoHashMap(u8, void) = elves[i+1];

        var elf1_ki = elf1.keyIterator();
        var insct1 = std.AutoHashMap(u8, void).init(allocator);
        defer insct1.deinit();
        while (elf1_ki.next()) |k| {
            if (elf2.contains(k.*)) {
                try insct1.put(k.*, {});
            }
        }

        const elf3: std.AutoHashMap(u8, void) = elves[i+2];
        var insct1_ki = insct1.keyIterator();
        while (insct1_ki.next()) |k| {
            if (elf3.contains(k.*)) {
                sum += determine_priority(k.*);
            }
        }

    }
    return sum;
}

pub fn main() !void {
    const input = @embedFile("day03_input.txt");
    const d1 = try p1_parse(input);
    print("Part 1: {d}\n", .{try part1(d1)});
    const d2 = try p2_parse(input);
    print("Part 2: {d}\n", .{try part2(d2)});
}

test "example" {
    const input = @embedFile("day03_example.txt");
    const d1 = try p1_parse(input);
    try std.testing.expect(try part1(d1) == 157);
    const d2 = try p2_parse(input);
    try std.testing.expect(try part2(d2) == 133);
}
