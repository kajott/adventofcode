# [2025, Day 8: Playground](https://adventofcode.com/2025/day/8)

The input consists of (typically) 1000 5-digit 3D coordinates.

The points described by these coordinates are to be pairwise connected together into clusters, ordered by the distance of the points in a pair in ascending Euclidean metric.

**Part 1** asks for the sizes of the three largest clusters after joining the closest 1000 pairs of points.

**Part 2** asks to continue joining pairs until all points belong to the same cluster.


## Solution Notes

This task calls for some creative use of dictionaries and sets. First, a full distance matrix has to be computed and sorted (which takes surprisingly long, by the way), and then, the connections can be made. To keep track of those, I used a dictionary containing the circuit (as a set) where each box belongs into. Multiple entries in there will have the same value, and that's fine. At the end, it boils down to identifying distinct circuits.

The solution isn't perfectly amenable to code golf. It's also one of the cases where part 2 is actually shorter than part 1, as the entire evaluation step is skipped.

* Part 1, Python: 290 bytes, ~1.5 s
* Part 2, Python: 255 bytes, ~2.5 s
