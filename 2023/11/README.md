# [2023, Day 11: Cosmic Expansion](https://adventofcode.com/2023/day/11)

The input consists of a (typically) 140x140 grid, sparsely populated with objects.

The grid has to be pre-processed by duplicating every row and column that does not contain any objects.

**Part 1** asks for the sum of distances between each pair of objects after this pre-processing step.

**Part 2** asks the same, but the pre-processing adds not just two, but one million copies of each empty row and column to the grid.


## Solution Notes

For part 1, actually duplicating the affected rows and columns in the map data is feasible; for part 2, though, it's obviously not. There, a sensible approach is building a translation table from raw map coordinates into expanded coordinates, separately for each dimension. To my surprise, this method even saved a few extra bytes on part 1!

* Part 1, Python (duplicating rows and columns): 310 bytes, <100 ms
* Part 1, Python (coordinate translation): 307 bytes, <100 ms
* Part 2, Python (coordinate translation): 315 bytes, <100 ms
