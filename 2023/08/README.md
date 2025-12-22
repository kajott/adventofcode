# [2023, Day 8: Haunted Wasteland](https://adventofcode.com/2023/day/8)

The input consists of (typically) 750 assignments of a random three-letter node identifier to two other node identifiers, plus a sequence of (typically) 280 left/right directions. The sequence is cyclic, i.e. it is to be interpreted as if it repeats infinitely.

**Part 1** asks for the number of steps between a specific starting node, following the left/right instruction sequence to choose the next node at any junction, until it arrives at a specific stop node.

**Part 2** asks for the number of steps when starting at a certain set of nodes _simultaneously_ and following the sequence until *all* simultaneous iterations arrive at a certain set of stop nodes.


## Solution Notes

Part 1 is nearly trivial, part 2 is the interesting thing here. Brute force doesn't help, it's really all about finding the cycles and computing where they overlap. This is helped **a lot** by a few (certainly deliberate) properties of the input data:
- Each start node leads to exactly one end node, i.e. the cycles are completely disjoint and don't overlap.
- The number of steps required to reach an end node again is equal to the number of steps required to each it the first time.
- This number is the product of the instruction sequence length and some prime number.

These three properties combined allow a simple and very fast solution.

* Part 1, Python: 202 bytes, <100 ms
* Part 2, Python: 238 bytes, <100 ms
