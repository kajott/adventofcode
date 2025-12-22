# [2022, Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8)

The input consists of a (typically) 100x100 grid of digits that specify the heights of a tree in each cell.

**Part 1** asks how many different trees can be seen from any side of the grid, where any tree of height X occludes any other tree of height X and below in the viewing direction.

**Part 2** asks for the position of the tree from which the highest number of other trees can be seen in each of the four cardinal directions.


## Solution Notes

Following the instructions precisely is key here; the most notable detail that can be tricky to get right (and especially hard to golf properly) is that there are _two_ different stopping conditions for the visibility check and score computation loops: It has to stop *after* a large tree has been hit, but *before* the edge of the map.

* Part 1, Python: 220 bytes, <100 ms
* Part 2, Python: 224 bytes, <100 ms
