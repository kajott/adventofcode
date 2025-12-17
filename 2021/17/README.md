# 2021, Day 17: Trick Shot


## Solution Notes

The shot simulation part is quite simple, the question is how to guess valid initial velocities. Fortunately, the solution space is small enough that an exhaustive search over the full range is acceptable. For part 2, it's imperative that every possible solution is taken into account, including those with negative initial `y` velocities in general and direct shots at the lower-right corner of the target area in particular.

* Part 1, Python: 232 bytes, ~500 ms
* Part 2, Python: 216 bytes, ~1 s
* Part 1+2, Python: 250 bytes, ~1 s
