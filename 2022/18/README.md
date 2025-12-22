# [2022, Day 18: Boiling Boulders](https://adventofcode.com/2022/day/18)

The input consists of (typically) 2200 1-to-2-digit 3D coordinates, describing the positions of 1x1x1 cubes in 3D space.

**Part 1** asks for the surface area of the entire object, not counting the surfaces of neighboring cubes.

**Part 2** asks the same, but excluding the surface area of any enclosed inner space, i.e. space that's completely surrounded by cubes.


## Solution Notes

This is a relatively easy task: Count how many of the eight neighbors of each block are air, and that's already it for part 1. Part 2 requires filling the space with (BFS-generated) "confirmed air" first, but is otherwise near-identical. The fact that the inputs only use a 20x20x20 grid is very helpful here - if the space was much larger, clusters of rock would need to be identified first in order to still be runtime-efficient.

* Part 1, Python: 153 bytes, <100 ms
* Part 2, Python: 262 bytes, ~150 ms
