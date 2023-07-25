const std = @import("std");
const print = std.debug.print;
const allocator = std.heap.page_allocator;

fn parse() ![]usize {
    const input = @embedFile("day01_input.txt");

    var max = std.ArrayList(usize).init(allocator);

    var data_it = std.mem.split(u8, input, "\n\n");

    while (data_it.next()) |elf| {
        var calories = std.mem.split(u8, elf, "\n");
        var sum: usize = 0;
        while (calories.next()) |cals| {
            if (cals.len == 0) continue;
            var cals_val = try std.fmt.parseInt(usize, cals, 10);
            sum += cals_val;
        }
        try max.append(sum);
    }

    var sorted = max.toOwnedSlice();

    std.sort.sort(usize, sorted, {}, std.sort.desc(usize));

    return sorted;
}

fn part1(input: []usize) !usize {
    return input[0];
}

fn part2(input: []usize) !usize {
    return input[0] + input[1] + input[2];
}

pub fn main() !void {
    const d = try parse();
    print("Part 1: {any}\nPart 2: {any}", .{ part1(d), part2(d) });
}
