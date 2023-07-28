const std = @import("std");
const print = std.debug.print;
const Allocator = std.mem.Allocator;

const Elf = struct {
    min: usize,
    max: usize,

    fn init(input: []const u8) Elf {
        var fields = std.mem.tokenize(u8, input, "-");
        return Elf{
            .min = std.fmt.parseInt(usize, fields.next().?, 10) catch unreachable,
            .max = std.fmt.parseInt(usize, fields.next().?, 10) catch unreachable,
        };
    }

    fn contains(self: Elf, other: Elf) bool {
        return (self.min >= other.min and self.max <= other.max) or (other.min >= self.min and other.max <= self.max);
    }

    fn overlap(self: Elf, other: Elf) bool {
        return self.min <= other.max and other.min <= self.max;
    }
};

fn parse(allocator: Allocator, input: []const u8) ![][2]Elf {
    var result = std.ArrayList([2]Elf).init(allocator);
    defer result.deinit();
    var lines = std.mem.tokenize(u8, input, ",\n");
    while (lines.next()) |line| {
        var elf1 = Elf.init(line);
        var elf2 = Elf.init(lines.next().?);
        const elves: [2]Elf = .{ elf1, elf2 };
        try result.append(elves);
    }
    return result.toOwnedSlice();
}

fn part1(d: [][2]Elf) !usize {
    var result: usize = 0;

    for (d) |elves| {
        if (elves[0].contains(elves[1]) or elves[1].contains(elves[0])) {
            result += 1;
        }
    }

    return result;
}

fn part2(d: [][2]Elf) !usize {
    var result: usize = 0;
    for (d) |elves| {
        if (elves[0].overlap(elves[1])) {
            result += 1;
        }
    }
    return result;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const input = @embedFile("day04_input.txt");
    const d = try parse(allocator, input);
    defer allocator.free(d);
    print("{d}\n", .{try part1(d)});
    print("{d}\n", .{try part2(d)});
}
