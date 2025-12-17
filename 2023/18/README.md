# [2023, Day 18: Lavaduct Lagoon](https://adventofcode.com/2023/day/18)


## Solution Notes

Part 1 can be solved using the same approach I took initially for [2023/10](../10): Use *three* sets of complex numbers, one for the main path and two for the left and right neighbor fields in order of traversal. Those are then used as seeds for a BFS-based flood fill algorithm; one of the seeds will spill outside the map, and the other eventually fills the entire loop. The sizes of the resulting sets is the answer. Easy.

For very obvious reasons, this doesn't work for part 2, at least not without modifications. After toying around a lot with scanline-based approaches which ultimately all failed, I went another route: Coordinate compression. All possible X and Y coordinates are collected and then mapped to smaller ones in increments of 2. The spaces inbetween are columns and rows of some inflated size that reflects the distance between the adjacent original coordinates. In other words, the huge grid is reduced to a much smaller grid with uneven weights, but that only matters for the final area computation; everything else can be done just as in part 1, except with tuples instead of complex numbers due to frequent component access.

A few hours later, I learned about another approach: using a combination of the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's law](https://en.wikipedia.org/wiki/Pick%27s_theorem), it's possible to compute the resulting area directly from the polygon's vertex coordinates using almost trivial math. This approach is so ridiculously simple that the entire solution now fits into three lines, and it doesn't even flinch when confronted with part 2's huge coordinates. The solutions for parts 1 and 2 only differ in the parser, and part 1 even ends up being two bytes _larger_ than part 2 because the directions need to be looked up in a dictionary instead of being computable with a few simple formulas.

* Part 1, Python (BFS filling): 340 bytes, ~150 ms
* Part 2, Python (BFS filling + coordinate compression): 699 bytes, ~400 ms
* Part 1, Python (shoelace/Pick): 176 bytes, <100 ms
* Part 2, Python (shoelace/Pick): 174 bytes, <100 ms
