# [2019, Day 1: The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1)

The input consists of (typically) 100 5-to-6-digit numbers.

**Part 1** asks for the sum of `floor(x/3)-2` for each number `x` in the input.

**Part 2** asks the same, but the formula shall be evaluated repeatedly until the result becomes zero or negative, and all the intermediate results shall be added up too.


## Solution Notes

A straightforward starter: Summing values after doing some light math on them, with some slight recursion in part 2.

* Part 1, Python: 48 bytes, <100 ms
* Part 2, Python: 80 bytes, <100 ms
