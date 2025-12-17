# 2020, Day 7: Handy Haversacks


## Solution Notes

Relatively simple topological reduction operations: Part 1 requires a set; part 2 requires a sum. Parsing and building data structures is again the main task here. For part 1, it makes sense to construct a reverse mapping from contained bags to containing bags, contrary to how the input rules are formulated.

* Part 1, Python: 202 bytes, <100 ms
* Part 2, Python: 212 bytes, <100 ms
