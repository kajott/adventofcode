# [2023, Day 17: Clumsy Crucible](https://adventofcode.com/2023/day/17)


## Solution Notes

The task is very obviously an ideal fit for [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), but it's really, really finicky to get the conditions exactly right. Allow too long or too short runs? Wrong answer. Overread the small remark that the goal has to be reached after at least 4 forward moves as well in part 2? Tough luck. Allowed turning too early at the beginning in part 2? Sorry. (All of these bit me hard!)

Regarding my golf solution, I'm actually surprised how well it could be minimized. I'm exploiting Python's variable scoping rules in ways no professional code ever should, but for code golf, it's fine. <br>
Also note that I couldn't use complex numbers here, because implementing Dijkstra's algorithm basically _requires_ use of the `heapq` module, which in turn insists that elements in the queue are sortable, which complex numbers are not.

* Part 1, Python: 350 bytes, ~1.5 s
* Part 2, Python: 367 bytes, ~5 s
