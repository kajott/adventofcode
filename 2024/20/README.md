# 2024, Day 20: Race Condition


## Solution Notes

Being a maze puzzle with an interesting twist. What the "cheats" in part 1 basically do is allowing a step size of 2 exactly once during traversal. (While it would be theoretically possible to walk around a corner during a cheat, this would only have a benefit if there were diagonally adjacent walls in the input, which isn't the case.) In part 2 this gets generalized a bit, and as the example highlights, it allows to jump from one point to any other point within a Manhattan distance of 20 or less.

This problem seems like the ideal candidate for something like Dijkstra's algorithm. I tried that, and after reading the instructions properly (specifically, that a unique cheat is identified by start position _and_ end position; easy to miss, but crucial!), I had a nice solution for the example, but it was extremely slow on the actual input. After quite some tuning, I got the correct result for part 1 using 10 minutes of CPU time and 20 GiB of RAM, but that's obviously not a feasible approach.

Thinking about it a bit further, I had a much simpler idea: Since the cheat can be activated only once, the parts before and after activating it are just normal path searches. Those can be precomputed easily &ndash; in the absence of a cheat, there's only one shortest path from any point to the exit, or from the start to that point; furthermore, we don't need the paths themselves, but only their lengths. Since these lengths always add up to the length `m` of the single path through the maze, one of the two half-path precomputations can be omitted: if the distance from `S` to a point `P` is known (`dist(S,P)`), the distance from `P` to `E` is `dist(P,E) = m - dist(S,P)`. The total length `l` of a path from `S` up to point `P`, then cheating for `x` cycles, arriving at point `Q` and finally going to `E` is thus `l = dist(S,P) + x + m - dist(S,Q)`. Since only the amount of _savings_ is relevant, this would be `d = m - l`, which simplifies to `d = dist(S,Q) - dist(S,P) - x`. Note that the term `m` is completely eliminated, and with it any dependence on the end position. This may be surprising, but it's consistent with the observation that the start and end points are always at the very ends of the path.

The results can be found by checking all possible cheats for all positions `P` in the maze and checking if `d >= 100` for them. The possible cheats for part 1 simply put `Q` two positions left, right, above and below `P` for part 1, or form a diamond-shaped area for part 2.

* Part 1, Python: 283 bytes, ~6 s
* Part 2, Python: 362 bytes, ~10 s
