# [2016, Day 22: Grid Computing](https://adventofcode.com/2016/day/22)


## Solution Notes

Part 2 is a pure smoke and mirrors affair. What looks like a typical BFS problem quickly blows apart because of the sheer problem size. The problem can only be reasonably solved by ~~cheating~~ making use of some specific properties of the input data, some of which are hinted at in the puzzle description:

* There's indeed only three types of nodes: Those which are somewhat full, those which are too big to be moved (and can thus be regarded as "walls" while traversing the grid), and exactly one empty node which is basically the "cursor".
* The normal nodes' capacity and fill level are chosen so that they really are totally transparent: their minimum capacity is less than their maximum fill level, so there's never a situation where data can't be moved from one node into the empty one.
* For all users, the "wall"-type nodes form a single line; specifically, a barrier that's at some `y` position between the empty node and the top of the grid, and extend from some `x` position (which is generally left of the cursor) up to the right edge.

In other words, the whole stuff about capacities is just a red herring. In the end, it's a simple sliding puzzle that can (only?) be solved by exploiting this and walking through the grid with the "cursor" (i.e. the empty node):

* Go up until the barrier.
* Go left until the end of the barrier.
* Go up.
* Go right. The final move to the right pushes the target data one grid cell left.
* Circle around to move the target data left, one grid cell at a time. Each cell takes 5 moves (down, left, left, up, right).

The whole thing fits into a trivial formula with only the grid width, initial cursor position and barrier start `x` coordinate as inputs. (The `y` position of the barrier doesn't even matter, as is cancels out in the formula.)

* Part 1, Python: 142 bytes, ~200 ms
* Part 2, Python: 181 bytes, <100 ms
