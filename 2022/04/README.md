# 2022, Day 4: Camp Cleanup


## Solution Notes

Since the numbers are so small, this can be conveniently be solved with sets: part 1 is checking if either set is a superset of the other, and part 2 is checking if the intersection is non-empty. I ultimately rewrote the logic so that just the endpoints of the intervals are checked against each other, as that results in much more compact code.

* Part 1, Python: 118 bytes, <100 ms
* Part 2, Python: 103 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 171 bytes (assembled)
