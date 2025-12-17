# [2021, Day 20: Trench Map](https://adventofcode.com/2021/day/20)


## Solution Notes

On the surface, this is just a generic 2D cellular automaton using an arbitrary 512-bit rule for the binary 3x3 neighborhood. The nasty part is the "infinite grid" condition and that its unpleasant implications are only really exercised by the actual input, and not the example: Slots 0 and 511 have "inverting" behavior, meaning that the void outside the used part of the map toggles every iteration, having some effect on the map boundaries.

There may be direct ways to handle this kind of condition, but I didn't bother (not least because I'm trying to do some code golf here); when simulating `t` iterations, I simply extended the grid by `2*t` cells on all four edges and cut away `t` of them before computing the final tally. The latter part is important, because my sloppy implementation assumes that the void (outside of the padding area) is always `.` (never `#`), which isn't correct and thus results in a few artifacts in the padding area; that's why it has to be removed to get correct results.

Part 2 uses the same approach, just with a higher iteration count, which pushes it firmly into the "just barely acceptable" performance region. There's lots of possible way to optimize things (like dynamically extending the padding area), but I decided not to bother.

* Part 1, Python: 365 bytes, <100 ms
* Part 2, Python: 375 bytes, ~10 s
