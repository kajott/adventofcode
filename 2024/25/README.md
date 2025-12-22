# [2024, Day 25: Code Chronicle](https://adventofcode.com/2024/day/25)

The input describes the shape of (typically) 500 "locks" and "keys", each represented as a densely populated 5x7 grid.

The task is to determine how many lock-and-key pairs fit together without overlapping.


## Solution Notes

A simple implement-as-described task, in theory. In practice, all that quibble about locks vs. keys and pin heights is just a red herring, and the actual task is simply to check all pairs of patterns for collisions at any of the `#` spots.

* Part 1, Python: 165 bytes, ~250 ms
