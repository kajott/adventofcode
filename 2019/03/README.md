# [2019, Day 3: Crossed Wires](https://adventofcode.com/2019/day/3)

The input consists of two sets of (typically) 300 2D movement instructions, each describing one of the four cardinal directions and a length.

The task is about executing these movement instructions and keeping a trace of grid cells visited. Both traces start at the origin, and intersections of the traces are examined in particular.

**Part 1** asks for the location of the intersection that's closest to the origin.

**Part 2** asks for the intersection with the minimal sum of path lengths across both traces.


## Solution Notes

A fun puzzle with 2D grids that can be solved using sets and dictionaries.

* Part 1, Python: 210 bytes, ~150 ms
* Part 2, Python: 214 bytes, ~150 ms
