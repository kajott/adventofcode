# [2021, Day 9: Smoke Basin](https://adventofcode.com/2021/day/9)

The input consists of a (typically) 100x100 grid of digits.

**Part 1** asks to find all local minima, i.e. all cells that are less than the surrounding cells in the four cardinal directions.

**Part 1** asks for the sizes of the three largest areas that are delimited by 9's.


## Solution Notes

For part 1, the task description already contains the implementation approach. For code golf, the usual "dictionary with complex numbers as keys" trick does the job admirably.

Part 2 adds an additional flood fill step to the mix, which I implemented by means of breadth-first search. After implementing that, I noticed that the BFS doesn't need to start at a low point; the whole idea of the flood fill is that the whole basin is filled, so the start location doesn't matter. Thus, instead of identifying low points first, a simple list of all open deeper-than-9 points in the map can be used.

* Part 1, Python: 185 bytes, <100 ms
* Part 2, Python (using low point seeds): 328 bytes, <100 ms
* Part 2, Python (using arbitrary seeds): 311 bytes, ~100 ms
