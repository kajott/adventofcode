# 2024, Day 20: Race Condition

The Historians are quite pixelated again. This time, a massive, black building looms over you - you're [right outside](../../2017/24) the CPU!

While The Historians get to work, a nearby program sees that you're idle and challenges you to a _race_. Apparently, you've arrived just in time for the frequently-held _race condition_ festival!

The race takes place on a particularly long and twisting code path; programs compete to see who can finish in the _fewest picoseconds_. The winner even gets their very own [mutex](https://en.wikipedia.org/wiki/Lock_\(computer_science\))!

## Part 1

They hand you a _map of the racetrack_ (your puzzle input). For example:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

The map consists of track (`.`) - including the _start_ (`S`) and _end_ (`E`) positions (both of which also count as track) - and _walls_ (`#`).

When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down, left, or right; each such move takes _1 picosecond_. The goal is to reach the end position as quickly as possible. In this example racetrack, the fastest time is `84` picoseconds.

Because there is only a single path from the start to the end and the programs all go the same speed, the races used to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to _cheat_.

The rules for cheating are very strict. _Exactly once_ during a race, a program may _disable collision_ for up to _2 picoseconds_. This allows the program to _pass through walls_ as if they were regular track. At the end of the cheat, the program must be back on normal track again; otherwise, it will receive a [segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault) and get disqualified.

So, a program could complete the course in 72 picoseconds (saving _12 picoseconds_) by cheating for the two moves marked `1` and `2`:

    ###############
    #...#...12....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

Or, a program could complete the course in 64 picoseconds (saving _20 picoseconds_) by cheating for the two moves marked `1` and `2`:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...12..#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

This cheat saves _38 picoseconds_:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...#...#
    ###.####1##.###
    #...###.2.#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

This cheat saves _64 picoseconds_ and takes the program directly to the end:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..21...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

Each cheat has a distinct _start position_ (the position where the cheat is activated, just before the first move that is allowed to go through walls) and _end position_; cheats are uniquely identified by their start position and end position.

In this example, the total number of cheats (grouped by the amount of time they save) are as follows:

*   There are 14 cheats that save 2 picoseconds.
*   There are 14 cheats that save 4 picoseconds.
*   There are 2 cheats that save 6 picoseconds.
*   There are 4 cheats that save 8 picoseconds.
*   There are 2 cheats that save 10 picoseconds.
*   There are 3 cheats that save 12 picoseconds.
*   There is one cheat that saves 20 picoseconds.
*   There is one cheat that saves 36 picoseconds.
*   There is one cheat that saves 38 picoseconds.
*   There is one cheat that saves 40 picoseconds.
*   There is one cheat that saves 64 picoseconds.

You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible, you'll need a list of the best cheats. _How many cheats would save you at least 100 picoseconds?_

Your puzzle answer was `1452`.

## Part 2

The programs seem perplexed by your list of cheats. Apparently, the two-picosecond cheating rule was deprecated several milliseconds ago! The latest version of the cheating rule permits a single cheat that instead lasts at most _20 picoseconds_.

Now, in addition to all the cheats that were possible in just two picoseconds, many more cheats are possible. This six-picosecond cheat saves _76 picoseconds_:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #1#####.#.#.###
    #2#####.#.#...#
    #3#####.#.###.#
    #456.E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

Because this cheat has the same start and end positions as the one above, it's the _same cheat_, even though the path taken during the cheat is different:

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S12..#.#.#...#
    ###3###.#.#.###
    ###4###.#.#...#
    ###5###.#.###.#
    ###6.E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds (but can still only end when the program is on normal track). Any cheat time not used is lost; it can't be saved for another cheat later.

You'll still need a list of the best cheats, but now there are even more to choose between. Here are the quantities of cheats in this example that save _50 picoseconds or more_:

*   There are 32 cheats that save 50 picoseconds.
*   There are 31 cheats that save 52 picoseconds.
*   There are 29 cheats that save 54 picoseconds.
*   There are 39 cheats that save 56 picoseconds.
*   There are 25 cheats that save 58 picoseconds.
*   There are 23 cheats that save 60 picoseconds.
*   There are 20 cheats that save 62 picoseconds.
*   There are 19 cheats that save 64 picoseconds.
*   There are 12 cheats that save 66 picoseconds.
*   There are 14 cheats that save 68 picoseconds.
*   There are 12 cheats that save 70 picoseconds.
*   There are 22 cheats that save 72 picoseconds.
*   There are 4 cheats that save 74 picoseconds.
*   There are 3 cheats that save 76 picoseconds.

Find the best cheats using the updated cheating rules. _How many cheats would save you at least 100 picoseconds?_

Your puzzle answer was `999556`.

## Solution Notes

Being a maze puzzle with an interesting twist. What the "cheats" in part 1 basically do is allowing a step size of 2 exactly once during traversal. (While it would be theoretically possible to walk around a corner during a cheat, this would only have a benefit if there were diagonally adjacent walls in the input, which isn't the case.) In part 2 this gets generalized a bit, and as the example highlights, it allows to jump from one point to any other point within a Manhattan distance of 20 or less.

This problem seems like the ideal candidate for something like Dijkstra's algorithm. I tried that, and after reading the instructions properly (specifically, that a unique cheat is identified by start position _and_ end position; easy to miss, but crucial!), I had a nice solution for the example, but it was extremely slow on the actual input. After quite some tuning, I got the correct result for part 1 using 10 minutes of CPU time and 20 GiB of RAM, but that's obviously not a feasible approach.

Thinking about it a bit further, I had a much simpler idea: Since the cheat can be activated only once, the parts before and after activating it are just normal path searches. Those can be precomputed easily &ndash; in the absence of a cheat, there's only one shortest path from any point to the exit, or from the start to that point; furthermore, we don't need the paths themselves, but only their lengths. Since these lengths always add up to the length `m` of the single path through the maze, one of the two half-path precomputations can be omitted: if the distance from `S` to a point `P` is known (`dist(S,P)`), the distance from `P` to `E` is `dist(P,E) = m - dist(S,P)`. The total length `l` of a path from `S` up to point `P`, then cheating for `x` cycles, arriving at point `Q` and finally going to `E` is thus `l = dist(S,P) + x + m - dist(S,Q)`. Since only the amount of _savings_ is relevant, this would be `d = m - l`, which simplifies to `d = dist(S,Q) - dist(S,P) - x`. Note that the term `m` is completely eliminated, and with it any dependence on the end position. This may be surprising, but it's consistent with the observation that the start and end points are always at the very ends of the path.

The results can be found by checking all possible cheats for all positions `P` in the maze and checking if `d >= 100` for them. The possible cheats for part 1 simply put `Q` two positions left, right, above and below `P` for part 1, or form a diamond-shaped area for part 2.

* Part 1, Python: 283 bytes, ~5 s
* Part 2, Python: 362 bytes, ~6 s
