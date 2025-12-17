# [2019, Day 20: Donut Maze](https://adventofcode.com/2019/day/20)


## Solution Notes

Part 1 is just a simple BFS; the most challenging part is parsing the input.

Part 2 extends this to a third dimension, but is still manageable in terms of code complexity (even though I can no longer use my beloved complex numbers as coordinate representation). The problem there is that the runtime complexity is so high that naive BFS blows apart. Performing two independent BFSes from start and goal and stopping when they meet was the key to success here.

* Part 1, Python: 432 bytes, <100 ms
* Part 2, Python: 667 bytes, ~600 ms
