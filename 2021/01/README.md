# 2021, Day 1: Sonar Sweep


## Solution Notes

A simple first puzzle. The low-pass filter for part 2 can be either implemented as an intermediate processing step, or directly while comparing (by having a four-element sliding window instead of just three elements), which leads to shorter code.

* Part 1, Python: 68 bytes, <100 ms
* Part 2, Python: 92 bytes, <100 ms
