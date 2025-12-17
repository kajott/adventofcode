# [2020, Day 20: Jurassic Jigsaw](https://adventofcode.com/2020/day/20)


## Solution Notes

This is a highly complex task, not because it's hard to understand or requires specific, complicated algorithms; no, it's just the sheer amount of things that need to be done:
- input parsing
- generation of all 8 mirrored and rotated tile variants
- extracting the edges
- doing some statistics over the edges and how often they are used to solve part 1
- implement some kind of search to assemble the puzzle
- "render" the puzzle in a full bitmap without edges
- create 8 mirrored/tiled versions of _that_ again
- search for the "sea monster" pattern

The full-bitmap and monster search parts are textbook examples for situations where sets of complex numbers are really useful.

Puzzle assembly is surprisingly easy. The tile edges are unique, so there's always a fitting tile without any ambiguity. My initial "non-golf" version starts with one of the edge tiles that were already detected during part 1, and goes on in raster-scan order from there. For the golf version, I used a more straightforward depth-first search instead. It starts at _any_ tile, because absolute coordinates don't matter here.

A nice observation for part 1 is that generating the mirrored and tiled variants isn't even necessary, because the only interesting thing is the edges -- and these are simply the edges of all four sides of the tile _and_ their mirrored copies.

* Part 1, Python: 347 bytes, <100 ms
* Part 2, Python: 879 bytes, ~150 ms
