# [2019, Day 25: Cryostasis](https://adventofcode.com/2019/day/25)


## Solution Notes

This is a proper text adventure, so I started to solve it like one does: mapping out the maze with pen and paper, learning the hard way which objects are dangerous and which aren't. At the Security Checkpoint, it became clear that it's not just the number of carried objects that's important, but the exact combination. So I hard-coded the path to visit all rooms and pick up all items into my (non-golf) program and had it then try out all 2^n combinations (which fortunately isn't an issue at n=8).

This is, of course, no general solution, and not even a nicely golfable one. So I sat down later and added DFS-based maze exploration code that picks up all non-dangerous items along the way. It's not an optimal solution in terms of steps required, as the DFS returns to the starting position and the path to the Security Checkpoint has to be walked again afterwards, but it's much simpler this way, so I don't care.

* Part 1, Python: 1106 bytes, ~6 s
