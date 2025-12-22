# [2021, Day 12: Passage Pathing](https://adventofcode.com/2021/day/12)

The input describes an undirected graph with (typically) 30 edges. Node mostly have random 2-letter names, some lowercase ("small"), some uppercase ("large"). Two nodes are named "start" and "end".

**Part 1** asks how many different paths there are from start to end, whereby small nodes may only be visited at most once.

**Part 2** asks the same, but exactly one small node may be visited *twice*.


## Solution Notes

Depth-First Search is an adequate base algorithm for this puzzle. The restriction that certain nodes must not be visited twice is quite important and _must_ be implemented directly in the visitor function, otherwise the DFS will blow up on loops in the graph, which are present in all inputs.

The only thing that part 2 does is altering the constraint a bit. To implement that efficiently, I opted to add a second parameter to the visitor function, simply counts the number of double visits to smaller caves. Visiting a cave that would bring that number to 2 or higher is then just not allowed.

* Part 1, Python: 220 bytes, <100 ms
* Part 2, Python: 258 bytes, ~1 s
