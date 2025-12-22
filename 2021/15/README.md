# [2021, Day 15: Chiton](https://adventofcode.com/2021/day/15)

The input consists of a (typically) 100x100 grid of digits 1 to 9. A path is to be found from the upper-left corner to the lower-right corner.

**Part 1** asks for the lowest possible sum of a path through the grid.

**Part 2** asks the same, but the grid is repeated 5 times to the right and to the bottom, with each extra copy having its digits increased by 1, wrapping 9 over to 1.


## Solution Notes

Part 1 is nicely solvable using Dynamic Programming, i.e. incrementally preparing a table with the cost of the the optimal path to each cell, coming from either above or the left.

Part 2, however, is quite tricky: What the task description and even the example dataset doesn't say is that it's perfectly possible that there's a slightly better path through the maze when going up or left at some places instead of just down or right. So, in the end, it's down to BFS or Dijkstra. Since the maze is so big, the former is horribly slow, but it gets the job done ... just barely. Dijkstra is vastly faster, but only if an efficient priority queue implementation is used. Python has one (`heapq`), but it's still quite a bit more verbose than the naive BFS implementation.

* Part 1, Python: 199 bytes, <100 ms
* Part 2, Python (BFS): 376 bytes, ~7 s
* Part 2, Python (Dijkstra): 422 bytes, ~1 s
