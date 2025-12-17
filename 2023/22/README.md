# [2023, Day 22: Sand Slabs](https://adventofcode.com/2023/day/22)


## Solution Notes

A very interesting problem that needs to be solved in multiple steps, hence I didn't go for golf straight away this time:
- First, sort the blocks by ascending minimum Z coordinate so that the falling blocks simulation works properly.
- Establish "overlaps on the X-Y plane" relationships between blocks (called `O` in the golfed code).
- Use these relationships to run the falling simulation: <br>
  For each block, find the maximum Z-height of all overlapping blocks below it, and pull it down to that height.
- Establish two more relationships, "supports" (`S`) and its reverse, "is supported by" (`R`): <br>
  A block _A_ supports a block _B_ if they overlap and _B_'s minimum Z value is _A_'s maximum Z value plus 1.
  - Note that these relationships form a directed acyclic graph of blocks supporting other blocks. All further operations are, strictly speaking, just operations on this graph.
- Solve part 1 by counting how many blocks only support blocks for which they are not the only support.
- For part 2, perform support graph searches starting at every node (= block) and count how many blocks would be falling if this one is removed. The principle of that is not unlike a BFS: Mark blocks as falling if all of their supports are falling as well, and continue the search with the supports of the blocks that have just been marked. Blocks that have multiple supports will then automatically be revisited until all their supports have been marked (and they are in turn marked as falling too), but they will never be marked as falling if the starting block never causes all the supports to fall.

In the golf versions, the relationship dictionaries (`O`, `S`, `R`) only contain _indices_ of bricks in the global `B` array, not the brick coordinates themselves. This is due to Python lacking a nice way to use lists as keys in dictionaries and sets. (I could have used a custom class for the bricks, but that would have been even more code.)

* Part 1, Python: 498 bytes, ~800 ms
* Part 2, Python: 552 bytes, ~1 s
