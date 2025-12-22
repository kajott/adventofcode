# [2020, Day 24: Lobby Layout](https://adventofcode.com/2020/day/24)

The input consists of (typically) 315 lines of 11 to 22 movement directions in any of the six cardinal directions of a hexagonal grid. Each line describes a path of movement, starting from one common cell. The cell at the end of the path is flipped from "off" to "on" or vice-versa.

**Part 1** asks how many cells are in the "on" state after executing all instructions.

**Part 2** asks to simulate 10 time steps of a cellular automaton, starting with the initial state from part 1. At each time steps, "on" cells with 0 or more than 2 "on" cells in their neighborhood shall turn "off", and "off" cells with exactly 2 "on" cells in their neighborhood shall turn "on".


## Solution Notes

Hexagonal grids are always a bit cumbersome to work with, but the tasks are simple enough to make it worthwhile. In the end, I used a tried-and-true representation with dictionaries and sets of complex numbers.

After part 1, I was half expecting part 2 to be something like "the black tiles form letters, please read them", but instead it's a cellular automaton. This makes the puzzle a little less exciting, but it's still fun.

* Part 1, Python: 186 bytes, <100 ms
* Part 2, Python: 402 bytes, ~2 s
