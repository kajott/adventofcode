# 2016, Day 13: A Maze of Twisty Little Cubicles


## Solution Notes

A simple breadth-first search puzzle with a nice maze generator function. The algorithm runs fast enough that I could even skip the "don't re-visit already visited nodes" optimization for part 1. (For part 2, it's required, but not because of runtime, but because the visited node list is the *result*.)

* Part 1, Python: 236 bytes, <100 ms
* Part 2, Python: 253 bytes, <100 ms
