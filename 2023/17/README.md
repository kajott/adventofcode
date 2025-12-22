# [2023, Day 17: Clumsy Crucible](https://adventofcode.com/2023/day/17)

The input consists of a (typically) 140x140 grid of digits that specify the cost of traversing each cell. The goal is to go from the upper-left corner to the lower-right corner of the grid.

Motion is restricted: Backwards motion is not allowed, and after going three steps in any direction, a 90-degree turn must be made.

**Part 1** asks for the lowest-cost path through the grid.

**Part 2** asks the same, but changes the motion criteria: between two 90-degree turns, between 4 and 10 steps must be made into the current direction.


## Solution Notes

The task is very obviously an ideal fit for [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), but it's really, really finicky to get the conditions exactly right. Allow too long or too short runs? Wrong answer. Overread the small remark that the goal has to be reached after at least 4 forward moves as well in part 2? Tough luck. Allowed turning too early at the beginning in part 2? Sorry. (All of these bit me hard!)

Regarding my golf solution, I'm actually surprised how well it could be minimized. I'm exploiting Python's variable scoping rules in ways no professional code ever should, but for code golf, it's fine. <br>
Also note that I couldn't use complex numbers here, because implementing Dijkstra's algorithm basically _requires_ use of the `heapq` module, which in turn insists that elements in the queue are sortable, which complex numbers are not.

* Part 1, Python: 350 bytes, ~1.5 s
* Part 2, Python: 367 bytes, ~5 s
