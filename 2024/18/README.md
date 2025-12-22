# [2024, Day 18: RAM Run](https://adventofcode.com/2024/day/18)

The task operates on a 71x71 grid, with the objective to traverse it from one corner to the opposite.

The input consists of an ordered list of coordinates for (typically) 3450 obstacles in this grid.

**Part 1** asks for the shortest path with the first 1024 of the obstacles in place.

**Part 2** asks for the first obstacle in the list that would cut off the path between the two corners.


## Solution Notes

This is a plain standard BFS maze search. Part 2 can be solved with brute-force iteration in an acceptable time, but the ideal (albeit larger) solution is of course doing a binary search for the first item in the sequence where the BFS can't reach the exit any longer.

* Part 1, Python: 251 bytes, <100 ms
* Part 2, Python (brute force): 262 bytes, ~10 s
* Part 2, Python (binary search): 317 bytes, <100 ms
