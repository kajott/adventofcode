# [2023, Day 24: Never Tell Me The Odds](https://adventofcode.com/2023/day/24)

The input consists of (typically) 300 3D positions (15-digit) and velocities (1-to-3-digit, signed) of objects that move with constant linear velocity.

**Part 1** asks for how many of these objects would collide within a defined 2D area, disregarding the Z coordinate completely, at some point in time.

**Part 2** asks for the position (not velocity) of an additional object that would eventually collide with **all** other objects at some point in time, in full 3D, without coordinate range constraints.


## Solution Notes

This is much more of a vector algebra puzzle than a programming puzzle. Part 1 is still reasonably simple; the equations for 2D ray-ray collision are relatively easy to resolve with some pen, paper and high school math. (I had the latter, but not the former, so I took a bit longer than I would have liked to, but it wasn't too bad either.)

Part 2 is so much more complex that it took several hours for the first "actual" solutions to appear on the AoC Reddit forums; until then, everybody just shoved the problem into the [Z3 solver library](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) and let it do the hard part.

The thing that's still relatively easy to understand is that the problem is massively overconstrained, or in other words: The 300 hailstones are nothing but a big red herring, because it just takes any combination of **three** of them to solve the problem. Think of it this way: We're searching a line (the rock trajectory) that intersects with some set of other lines (the hailstone trajectories). If there's only one or two reference lines, there's an infinite number of solutions, but once a third line is added, there's only one possible line that intersects them all. (I recommend using uncooked spaghetti to visualize this.)

But anyway, even with this knowledge, how to get to a solution? It's rather complicated; I couldn't work it out myself, but a former university classmate of mine did and kindly provided a comprehensible paper scribble to me that I reworked into a [nice document](aoc2023_24_part2_math.md) that should be reasonably easy to follow. Suffice to say that it involves a lot of intuition and some cross product magic to come up with a linear system of equations with six unknowns, which are exactly the parameters of the rock trajectory. My solution thus contains a full implementation of Gaussian Elimination to get the result, which makes up the bulk of the golfed code.

Even so, my naive implementation really struggles with floating-point precision issues; any attempt to optimize it further resulted in off-by-one errors on my input, and I can easily imagine it failing with other people's inputs. However, since a solution is so quick to compute, the process can be repeated many times with different triples of hailstones (we do have a bunch of them to work with, after all!) and the most frequent solution, which is _highly_ likely to be the correct one, can be selected from the results.

* Part 1, Python: 265 bytes, ~100 ms
* Part 2, Python (single hailstone triple): 601 bytes, <100 ms
* Part 2, Python (better numerical stability): 674 bytes, <100 ms
