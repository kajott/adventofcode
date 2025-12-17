# [2019, Day 12: The N-Body Problem](https://adventofcode.com/2019/day/12)


## Solution Notes

Part 1 is quite fun, but part 2 raises the bar considerably. As the task description implies, there has to be some kind of sub-state periodicity which needs to be detected and extrapolated for the whole system. My initial attempt was to detect periodicity in each of the 24 variables independently, but that turned out to be the wrong approach. Instead, the right thing to do is decompose the system by dimension: Each axis' state is computed independently of the other axes!

For part 2, I have two solutions. The first attempt was to recycle the code from part 1, but it was rather complicated to separate the axes after running the simulation in the way part 1 did (and had to do, because the energy computation *required* cross-axis operations). I tried again and made maximum use of the whole axis separation thing: The simulations are run for each of the three dimensions in turn. This results in a much smaller and even slightly faster implementation.

The *real* fun part, though, was writing the interactive (OpenGL-based) visualizer later on :) It's rather surprising how such a simple system (let alone one operating purely on integers) can produce such smooth, yet chaotic, trajectories.

* Part 1, Python: 345 bytes, <100 ms
* Part 2, Python (derived from part 1 solution): 473 bytes, ~5 s
* Part 2, Python (full axis separation): 368 bytes, ~6 s
