# [2016, Day 19: An Elephant Named Joseph](https://adventofcode.com/2016/day/19)


## Solution Notes

Part 2 is constructed in such a way that naive solutions fall apart in terms of runtime performance. Regardless of whether an array or a list is used, complexity is always O(n²) -- you just get to choose whether item deletion or list pointer advancement kills you. A C implementation doesn't help much either.

The salvaging trick is to use a list and keep the half-way pointer around: Move it with deletions, and on every second turn, move it an additional element. This makes a C implementation near-instantaneous (so much so that there's no discernible difference between using optimization or not; at least not when compile times are factored in) and a Python implementation bearable.

* Part 1, Python: 131 bytes, ~1.5 s
* Part 2, Python: 166 bytes, ~8 s
* Part 2, C: 276 bytes, ~100 ms
