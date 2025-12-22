# [2019, Day 20: Donut Maze](https://adventofcode.com/2019/day/20)

The input describes a (typically) 110x110 maze with a large square hole in the center. The maze is open towards some spots around the periphery (both outside and in the center),  and at each of these spots, a random 2-letter identifier is listed. There are exactly two instances of each of the spot IDs, except two that form a non-matched pair.

The marked spots are pairs of portals; the non-matched pair marks the start and end locations.

**Part 1** asks for the shortest path through the maze.

**Part 2** changes how the portals work: Instead of connecting to the same-named portal of the same maze, the inner portals of a maze connect to the outer portals of _another_ instance of the maze, bidirectionally. There's no nesting limit towards the inner portals, but the outer portals of the initial maze (not the aditional instances!) are closed, and the start/end locations are only valid at the initial maze too.

**Part 2** asks for the shortest path through this type of maze.


## Solution Notes

Part 1 is just a simple BFS; the most challenging part is parsing the input.

Part 2 extends this to a third dimension, but is still manageable in terms of code complexity (even though I can no longer use my beloved complex numbers as coordinate representation). The problem there is that the runtime complexity is so high that naive BFS blows apart. Performing two independent BFSes from start and goal and stopping when they meet was the key to success here.

* Part 1, Python: 432 bytes, <100 ms
* Part 2, Python: 667 bytes, ~600 ms
