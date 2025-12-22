# [2020, Day 10: Adapter Array](https://adventofcode.com/2020/day/10)

The input consists of (typically) 100 1-to-3-digit numbers.

A valid sequence of numbers is defined as starting with 0, ending with the maximum of all numbers in the input plus 3, and with every number inbetween being one from the input, and being 1 to 3 higher than its predecessor.

**Part 1** asks to arrange _all_ numbers of the input into a valid sequence, and gather statistics of how often each increment appears in the sequence.

**Part 2** asks how many valid sequences there can be.


## Solution Notes

Part 1 is almost trivial: Sort the numbers, generate differences, and that's it.

Part 2, however, requires significantly more thought. A search algorithm obviously won't cut it (and I'm very grateful that the problem text hints to this already, saving me a lot of time!). The solution here is to recognize that the number of possibilities to connect the adapters is some kind of a pseudo-Fibonacci sequence: To get to joltage N, there are as many possibilities as there are to get to joltages N-3 to N-1 if there is a suitable adapter in the bag. With this piece of the puzzle in place, everything becomes pretty straightforward.

* Part 1, Python: 104 bytes, <100 ms
* Part 2, Python: 137 bytes, <100 ms
