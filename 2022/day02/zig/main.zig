const std = @import("std");
const print = std.debug.print;
const allocator = std.heap.page_allocator;

const ROCK: usize = 1;
const PAPER: usize = 2;
const SCISSORS: usize = 3;

const WIN: usize = 6;
const DRAW: usize = 3;
const LOSE: usize = 0;

fn parse(input: []const u8) !std.ArrayList([2]u8) {
    var inp_it = std.mem.split(u8, input, "\n");
    var res = std.ArrayList([2]u8).init(allocator);

    while (inp_it.next()) |line| {
        try res.append([_]u8{ line[0], line[2] });
    }

    return res;
}

fn part1(d: std.ArrayList([2]u8)) !usize {
    var total_score: usize = 0;

    for (d.items) |game| {
        const opp = game[0];
        const you = game[1];

        total_score += switch (opp) {
            'A' => switch (you) {
                'Y' => PAPER + WIN,
                'Z' => SCISSORS + LOSE,
                else => ROCK + DRAW,
            },
            'B' => switch (you) {
                'Z' => SCISSORS + WIN,
                'X' => ROCK + LOSE,
                else => PAPER + DRAW, // y
            },
            else => switch (you) {
                'X' => ROCK + WIN,
                'Y' => PAPER + LOSE,
                else => SCISSORS + DRAW, // z
            },
        };
    }

    return total_score;
}

fn part2(d: std.ArrayList([2]u8)) !usize {
    var total_score: usize = 0;

    for (d.items) |game| {
        const opp = game[0];
        const you = game[1];

        total_score += switch (opp) {
            'A' => switch (you) {
                'X' => SCISSORS + LOSE,
                'Y' => ROCK + DRAW,
                else => PAPER + WIN,
            },
            'B' => switch (you) {
                'X' => ROCK + LOSE,
                'Y' => PAPER + DRAW,
                else => SCISSORS + WIN,
            },
            else => switch (you) {
                'X' => PAPER + LOSE,
                'Y' => SCISSORS + DRAW,
                else => ROCK + WIN,
            },
        };
    }

    return total_score;
}

pub fn main() !void {
    const input = @embedFile("day02_input.txt");
    const d = try parse(input);
    defer d.deinit();
    // print("{any}", .{d});
    print("Part 1: {any}\n", .{try part1(d)});
    print("Part 2: {any}\n", .{try part2(d)});
}
