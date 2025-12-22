# [2022, Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4)

The input consists of (typically) 1000 pairs of ranges, with numbers in the single to double digits.

**Part 1** asks for how many pairs there are where one range fully contains the other.

**Part 2** asks for how many pairs there are where there's any overlap in the ranges.


## Solution Notes

Since the numbers are so small, this can be conveniently be solved with sets: part 1 is checking if either set is a superset of the other, and part 2 is checking if the intersection is non-empty. I ultimately rewrote the logic so that just the endpoints of the intervals are checked against each other, as that results in much more compact code.

* Part 1, Python: 118 bytes, <100 ms
* Part 2, Python: 103 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 171 bytes (assembled)
