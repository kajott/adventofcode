# 2020, Day 9: Encoding Error


## Solution Notes

The sheer number of combinations that need to be tested for a brute-force solution might sound high at first, but it's in fact much less than a million combinations in total, so even though we're dealing with O(n^3) here, it's not really an issue.

As the problem description already states, part 2 is (almost) a true superset of part 1. (In fact, a combined solution would just use an additional `print` statement.)

* Part 1, Python: 144 bytes, ~150 ms
* Part 2, Python: 227 bytes, ~250 ms
