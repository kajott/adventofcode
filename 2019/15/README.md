# [2019, Day 15: Oxygen System](https://adventofcode.com/2019/day/15)


## Solution Notes

Both parts really ask for a BFS maze traversal, but there's a caveat: since the maze can only be queried through the stateful Intcode program, only DFS is easily possible. Fortunately, the maze is constructed in a way that a properly implemented DFS works just fine for part 1.

I say "properly implemented", because my initial implementation was *not* perfect and walked some paths multiple times, causing it to find a sub-optimal path to the target. Thus, I had to add a BFS as a second step anyway, which made part 2 quite simple to implement.

While recoding the solution in golf form, I fixed my DFS bug and don't require a BFS for part 1 any longer. Moreover, I removed the "relative base" functionality from the Intcode interpreter, as it's not used by the program.

* Part 1, Python: 665 bytes, ~300 ms
* Part 2, Python: 773 bytes, ~300 ms
