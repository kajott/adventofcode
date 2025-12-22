# [2021, Day 6: Lanternfish](https://adventofcode.com/2021/day/6)

The input consists of a sequence of (typically) 300 single-digit numbers.

In every time step, all numbers are decreased. If a number goes below zero in that process, it's replaced by a 6, and an 8 is appended to the sequence.

**Parts 1 and 2** ask for the length of the sequence after 80 and 256 time steps, respectively.


## Solution Notes

Working with a _histogram_ of fish timers instead of the timer list itself not only makes the implementation much easier, it also it essential for part 2. So, if part 1 is already implemented that way, part 2 is really just substituting the constant 80 by 256, without running into any nasty surprises.

* Part 1, Python: 137 bytes, <100 ms
* Part 2, Python: 138 bytes, <100 ms
