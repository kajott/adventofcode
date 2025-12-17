# 2018, Day 22: Mode Maze


## Solution Notes

Part 1 is refreshingly simple; the only special thing about it is that one needs to be familiar with modulo arithmetic, and read the fine print about how the inner cells are computed.

Part 2 is quite different: On the surface, it's a normal pathfinding puzzle, but after lots of tinkering around, it turns out that it's actually **3D** pathfinding: X, Y and current tool. With that knowledge, the implementation becomes rather straightforward again.

I have two versions: A straightforward BFS implementation, and another version that strictly decomposes the tool changing and moving steps. The latter version turned out smaller and three times faster.

* Part 1, Python: 279 bytes, <100 ms
* Part 2, Python (simple): 614 bytes, ~10 s
* Part 2, Python (optimized): 601 bytes, ~4 s
