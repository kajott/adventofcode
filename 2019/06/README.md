# [2019, Day 6: Universal Orbit Map](https://adventofcode.com/2019/day/6)


## Solution Notes

Some classic operations on a directed acyclic graph (DAG), a.k.a. a tree. The important trick for the second part is to find the "common ancestor" of the `YOU` and `SAN` nodes and then just add the subgraph depths together.

* Part 1, Python: 113 bytes, <100 ms
* Part 2, Python: 165 bytes, <100 ms
