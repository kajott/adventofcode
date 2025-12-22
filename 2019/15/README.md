# [2019, Day 15: Oxygen System](https://adventofcode.com/2019/day/15)

This puzzle uses the Intcode virtual machine that has been fully specified in [day 9](../09), and which is going to be used a lot during AoC 2019.

The input for this task consists of an Intcode core dump of (typically) 1050 words.

The program controls an agent that operates in a 2D maze. It runs a loop that inputs a movement command in any of the four cardinal directions, executes it and reports whether it hit a wall and couldn't execute the move (0), moved successfully (1) or hit the goal (2).

**Part 1** asks for the length of the shortest path from the initial position to the goal.

**Part 2** asks for the amount of time steps required for a complete flood fill of the entire maze, starting at the goal.


## Solution Notes

Both parts really ask for a BFS maze traversal, but there's a caveat: since the maze can only be queried through the stateful Intcode program, only DFS is easily possible. Fortunately, the maze is constructed in a way that a properly implemented DFS works just fine for part 1.

I say "properly implemented", because my initial implementation was *not* perfect and walked some paths multiple times, causing it to find a sub-optimal path to the target. Thus, I had to add a BFS as a second step anyway, which made part 2 quite simple to implement.

While recoding the solution in golf form, I fixed my DFS bug and don't require a BFS for part 1 any longer. Moreover, I removed the "relative base" functionality from the Intcode interpreter, as it's not used by the program.

* Part 1, Python: 665 bytes, ~300 ms
* Part 2, Python: 773 bytes, ~300 ms
