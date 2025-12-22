# [2023, Day 10: Pipe Maze](https://adventofcode.com/2023/day/10)

The input consists of a (typically) 140x140 grid, filled with the characters '|', '-', 'L', 'J', 'F', '7', denoting the directions and bends of pipes, '.' (empty space), and exactly one 'S' (start position). The start position is part of one large loop of pipes. There are other pipes present in the input, but these do not form loops.

**Part 1** asks for the distance to the farthest point in the loop, starting at `S` and going along the pipes.

**Part 2** asks for the area of the enclosed space _inside_ the loop, not accounting for any outside space.


## Solution Notes

Part 1 is relatively simple: Try walking the path in all four directions from the starting position; only two of the four directions will result in a loop, and the other ones will have an open end. The map can easily be represented as a dictionary, with complex numbers for coordinates.

Part 2 is a little more involved and it can be tricky to get the conditions exactly right, especially the "slip through between adjacent parallel pipes" rule. A simple way to solve it is representing the map as an image in double resolution and "flood-fill" it; however, this is not terribly efficient and a lot of code.

My approach is slightly different: While tracing through the loop, keep track of all coordinates of the loop itself (A) and the left (B) and right (C) neighbors in traversal direction. Then use B and C as seeds for a flood-fill operation, with A as boundaries. One of those fills will spill outside the map; this is the wrong one. The other one will eventually stabilize with a finite area, and this is the solution.

Eight days later, I revisited the puzzle again, because [for reasons](../18), I learned about the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's law](https://en.wikipedia.org/wiki/Pick%27s_theorem), which, in combination, make the entire task shockingly simple, fast, and short.

* Part 1, Python: 343 bytes, <100 ms
* Part 2, Python (flood fill): 529 bytes, ~300 ms
* Part 2, Python (shoelace/Pick): 396 bytes, <100 ms
