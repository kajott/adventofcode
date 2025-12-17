# [2020, Day 10: Adapter Array](https://adventofcode.com/2020/day/10)


## Solution Notes

Part 1 is almost trivial: Sort the numbers, generate differences, and that's it.

Part 2, however, requires significantly more thought. A search algorithm obviously won't cut it (and I'm very grateful that the problem text hints to this already, saving me a lot of time!). The solution here is to recognize that the number of possibilities to connect the adapters is some kind of a pseudo-Fibonacci sequence: To get to joltage N, there are as many possibilities as there are to get to joltages N-3 to N-1 if there is a suitable adapter in the bag. With this piece of the puzzle in place, everything becomes pretty straightforward.

* Part 1, Python: 104 bytes, <100 ms
* Part 2, Python: 137 bytes, <100 ms
