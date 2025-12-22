# [2024, Day 4: Ceres Search](https://adventofcode.com/2024/day/4)

The input consists of a (typically) 140x140 grid of the letters `A`, `M`, `S` and `X`.

**Part 1** asks how many times the word `XMAS` appears in the grid, in any direction, including reversed and diagonal.

**Part 2** asks how many times a quincunx consisting of the letters `MAS` in both diagonals appears in the grid.


## Solution Notes

A very simple task, and part 2 is actually even simpler than part 1. The nice thing is that there are again many ways to implement it: A 2D array of characters is fine, but so is a flat coordinate-to-character mapping. I ended up with my usual complex numbers as coordinate representation.

* Part 1, Python: 180 bytes, ~300 ms
* Part 2, Python: 172 bytes, <100 ms
