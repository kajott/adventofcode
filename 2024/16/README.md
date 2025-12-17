# [2024, Day 16: Reindeer Maze](https://adventofcode.com/2024/day/16)


## Solution Notes

This is a nice twist for an otherwise unassuming pathfinding puzzle, but at the same time, it's extremely brutal. Coming up with a solution that works for the examples in part 1 is easy, but one that scales for the 20k-cell maze of the actual input is already challenging, and finding all the bugs and corner cases that are _not_ exercised in the examples can be a downright horror trip. In my case, it turns out that the order in which nodes are visited does matter: using a `set` for the unvisited states _sometimes_ doesn't work, it has to be a list. For part 2, it's crucial to have the "visited state" map not just keyed by the position, but the position _and direction_, otherwise the algorithm wouldn't find all optimal paths, only some.

The only nice thing here is that it's trivial to write a combined solution: Since part 1's result is a byproduct of computing part 2, it's more or less only a matter of an additional `print()` to output both.

* Part 1, Python: 276 bytes, ~2 s
* Part 2, Python: 347 bytes, ~3.5 s
* Parts 1+2, Python: 359 bytes, ~3.5 s
