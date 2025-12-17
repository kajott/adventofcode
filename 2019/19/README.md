# [2019, Day 19: Tractor Beam](https://adventofcode.com/2019/day/19)


## Solution Notes

Part 1 is well solvable with brute-force iteration, though the runtime is not optimal. The surprising part is that the Intcode VM needs a full restart (including re-initializing the memory) between each query; I assumed that it runs an endless loop that repeatedly queries coordinates instead, which cost me (and many other contestants) a few minutes of debugging.

For part 2, it's clear that brute force is no longer an option. Instead, the edges of the beam need to be traced somehow; I chose the upper edge, and try to find the lowest position for which both (X,Y) and (X-99,Y+99) are in the beam.

My initial approach (expecting the coordinates to be very large) was to compute the slope of the edge, so I have a good approximation of where the upper edge's Y is for any X. Then I did a coarse search for a working X with a large step size, followed by a fine search. This works and is really fast, but it has two caveats: First, the code is quite large. Second, there are situations where a 100x100 square can be found for X-1, but not for X, i.e. the "can a square be found" function is not monotonically increasing with X. This is bad if the coarse search lands at such a local minimum; that actually happened to me until I tweaked the search parameters accordingly.

Since the coordinates turned out to be not *that* large, I tried again with a much simpler approach: Just walk along the upper edge until the square fits. This is naturally much slower, but still bearable, and it's 42 bytes smaller, so I'm fine with that.

* Part 1, Python (brute force): 494 bytes, ~3.5 s
* Part 2, Python (fast search with slope estimation): 561 bytes, ~350 ms
* Part 2, Python (edge walking): 519 bytes, ~5 s
