# [2021, Day 15: Chiton](https://adventofcode.com/2021/day/15)


## Solution Notes

Part 1 is nicely solvable using Dynamic Programming, i.e. incrementally preparing a table with the cost of the the optimal path to each cell, coming from either above or the left.

Part 2, however, is quite tricky: What the task description and even the example dataset doesn't say is that it's perfectly possible that there's a slightly better path through the maze when going up or left at some places instead of just down or right. So, in the end, it's down to BFS or Dijkstra. Since the maze is so big, the former is horribly slow, but it gets the job done ... just barely. Dijkstra is vastly faster, but only if an efficient priority queue implementation is used. Python has one (`heapq`), but it's still quite a bit more verbose than the naive BFS implementation.

* Part 1, Python: 199 bytes, <100 ms
* Part 2, Python (BFS): 376 bytes, ~7 s
* Part 2, Python (Dijkstra): 422 bytes, ~1 s
