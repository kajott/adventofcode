# [2016, Day 24: Air Duct Spelunking](https://adventofcode.com/2016/day/24)


## Solution Notes

A Traveling Salesman problem with relatively few targets, but on a rather large maze. It looks like this problem is too large for pure BFS, so I didn't even try and went a different route (as did most other contestants): Use BFS to generate a distance table for each target pair and then find the shortest path through that. For the latter part, an exhaustive O(n!) search is more than acceptable, performance-wise.

* Part 1, Python: 419 bytes, <100 ms
* Part 2, Python: 425 bytes, <100 ms
