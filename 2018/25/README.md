# 2018, Day 25: Four-Dimensional Adventure


## Solution Notes

4D coordinates may sound scary at first, but the task is actually independent of the input's dimensionality, so it's nothing to worry about. The only surprise here is that one can not simply add points to constellations one at a time, as later points may join two hitherto distinct constellations together. Still, the problem size is small enough to brute-force through it.

* Part 1, Python: 271 bytes, ~7 s
