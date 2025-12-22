# [2022, Day 15: Beacon Exclusion Zone](https://adventofcode.com/2022/day/15)

The input consists of (typically) 25 pairs of a "sensor" and a "beacon" each, both represented by signed 7-digit 2D coordinates. Around each sensor, there is a diamond-shaped zone that touches its associated beacon; in that zone, no other beacon can be located. (In other words, there's no beacon that's closer to a sensor's associated beacon in Manhattan metric.)

**Part 1** asks for the number of positions that can not contain a beacon at a specific row of the map.

**Part 2** asks for the one position in a certain rectangular region of the map where a beacon could be located that's not associated to any sensor.


## Solution Notes

This task is interesting in that there are many different ways to solve it that all work, but most of them are too inefficient to be feasible, especially in part 2. For part 1, simple sets of X coordinates at the queried Y position work fine; using some kind of representation that can encode and intersect individual ranges efficiently would be much faster, but also a lot more code. I used this approach for part 2 initially, but since part 2 queries 4 million times the rows compared to part 1, it's quite slow and very memory-hungry.

There are, however, quite a few strategies to make the search more efficient:
- The elusive beacon must be on the intersection of the boundaries of at least four scanners to be unique; anything less than four, and it would be a line. (By "boundary", I mean the diamond that's _one larger_ that the scanner range.) I implemented a solution based on this approach in a scratchpad, but without any further optimizations, it's no better than the naive coordinate range scan.
- The contributing boundaries need to be laid out in a special way: There need to be (at least) two that share a boundary in diagonal (`\`) direction and (at least) two others that share a boundary in anti-diagonal (`/`) direction. Sharing a boundary means that the Manhattan distance between the scanners must be the sum of the boundary radii (which, in turn, are the scanner range plus 1, so the total difference is the sum of scanner ranges plus 2). <br> For all contest inputs (but, interestingly, not the example input), it seems that there are exactly two pairs of such scanners, so we can deem it safe to use this as a heuristic.
- After identifying the four relevant scanners, intersecting the boundaries of those is sufficient. An analytical solution would be ideal, but this exceeds my grasp of maths.
- To speed up the intersection process (and, in my case just as important, save a lot of code), it's sufficient to just examine one of the four lines of each sensor's boundary diamond, specifically the line facing the sought-after sensor. <br> But wait, that's a catch-22, right? We don't know the beacon's position yet! That's right, but what we _do_ know is that it needs to be somewhere inside the quadrilateral formed by the scanner's centers. A coarse approximation of the beacon position is absolutely sufficient for that, and the centroid of the quadrilateral can be used for that.

With all these optimizations applied, part 2 becomes reasonably small and quick.

* Part 1, Python (set of coordinates): 200 bytes, ~1 s
* Part 2, Python (coordinate ranges): 379 bytes, ~3 min, 7 GiB RAM
* Part 2, Python (heuristics and boundary intersection): 340 bytes, ~1.5 s
