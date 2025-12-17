# 2022, Day 12: Hill Climbing Algorithm


## Solution Notes

A rather basic pathfinding puzzle that can be solved nicely using BFS. Thanks to the relatively small problem size, even a "simplified" BFS that doesn't keep track of visited nodes is sufficient. (A naive DFS, though, is not, and will explode on the actual input.)

It may not be obvious for part 1 (and, thruth be told, I didn't realize it either), but with hindsight from part 2 it turns out that it's beneficial to perform the DFS "in reverse", i.e. *not* determine the shortest path from start to any point in the grid, but determine the shortest path from any point to the end. This way, part 2 becomes trivial and is just an additional `print` statement; that's why I put both parts into the same file. (It's not a huge deal if the BFS is implemented the wrong way round though; it's just that runtime increases from "not even blinking an eye" to 1.5 seconds or so.)

Note that my golf version directly uses the ASCII codes of the input as the height values. It even keeps the linefeeds as one (*very* low - height 10 instead of 97 to 122) valid column. In terms of the puzzle, these turn into locations that could theoretically be climbed down into, but there's no way up from them, so they don't affect overall pathfinding much.

* Parts 1+2, Python: 312 bytes, <100 ms
