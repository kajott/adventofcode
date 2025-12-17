# [2015, Day 20: Infinite Elves and Infinite Houses](https://adventofcode.com/2015/day/20)


## Solution Notes

This puzzle is all about the sum-of-divisors function. The target value is quite large, so a dumb brute-force search takes too long. I still use a brute-force approach though, but an accelerated one: First, I start at (roughly) 100,000, and second, I perform only a "sparse" check, exploiting the fact that the sum-of-divisors function is roughly increasing (though not monotonically so). A fine search then detects the actual value.

* Part 1, Python: 141 bytes, ~3 s
* Part 2, Python: 148 bytes, ~4 s
