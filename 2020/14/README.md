# 2020, Day 14: Docking Data


## Solution Notes

The basic idea for both parts is that the tri-state mask has to be decomposed into an "AND part" and an "OR part". For part 2, there's an additional iteration over all the 2^(number of X'es) combinations.

* Part 1, Python: 179 bytes, <100 ms
* Part 2, Python: 292 bytes, ~150 ms
