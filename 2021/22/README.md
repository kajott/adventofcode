# [2021, Day 22: Reactor Reboot](https://adventofcode.com/2021/day/22)


## Solution Notes

Part 1 starts deceptively simple: Managing a 1M-cell grid is nothing out of the ordinary and well within the grasp of even the most trivial implementations. Part 2's task, then, is exactly what one would expect: the coordinate range limit is removed, and suddenly it's more like 10^16 cells ... theoretically. Since there are just `N` "commands" in the input, there can be only `2N` different coordinates per axis, and everything inbetween those can only be all-on or all-off. This kind of "compression" reduces the problem size for part 2's example (which is 60 lines) to 120^3, not even twice as large as part 1, and equally easy to solve. That approach of course also works for the actual input.

... Except it doesn't, at least not really. It turns out that at 420 lines, the grid size is already at ~600M cells. The code *does* produce the correct result, but it takes the better part of an hour to do so. So this is clearly not what the AoC author had in mind as the preferred solution!

The true solution is really to do it the hard way: Have a list of filled cubes (actually cuboids), and every time a new cube is added, all cubes that intersect it are first split into subcubes along all (up to six) intersecting coordinates. All subcubes that are completely located inside the cube that is to be added can then be safely discarded (their volume is accounted for in the other subcubes), and the new cube can be added to the list if it's set to be `on`. Phew! It takes some patience and planning to get every implementation detail right, but in the end, this can be done in less than 100 lines of code and 3 seconds of runtime without code golf. For the golf version, I sacrificed a lot of performance for size, mainly by doing things in a sub-optimal order, but I'm nevertheless quite satisfied with the result.

* Part 1, Python: 254 bytes, ~2 s
* Part 2, Python (naive approach with coordinate compression): 425 bytes, ~40 min
* Part 2, Python (cube-splitting approach): 402 bytes, ~15 s
