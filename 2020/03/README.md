# [2020, Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

The input consists of a (typically) 30x320 grid populated with objects. The grid repeats infinitely in horizontal direction.

**Part 1** asks how many objects are encountered when going through the grid row by row, with the X position increasing by 3 with every row.

**Part 2** asks for four additional rules (X increments of 1, 5 and 7, and also one scenario with an X increment of 1, but a Y increment of 2).


## Solution Notes

This is essentially just adding together 0's and 1's in a regular grid.

* Part 1, Python: 100 bytes, <100 ms
* Part 2, Python: 158 bytes, <100 ms
