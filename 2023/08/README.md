# 2023, Day 8: Haunted Wasteland


## Solution Notes

Part 1 is nearly trivial, part 2 is the interesting thing here. Brute force doesn't help, it's really all about finding the cycles and computing where they overlap. This is helped **a lot** by a few (certainly deliberate) properties of the input data:
- Each start node leads to exactly one end node, i.e. the cycles are completely disjoint and don't overlap.
- The number of steps required to reach an end node again is equal to the number of steps required to each it the first time.
- This number is the product of the instruction sequence length and some prime number.

These three properties combined allow a simple and very fast solution.

* Part 1, Python: 202 bytes, <100 ms
* Part 2, Python: 238 bytes, <100 ms
