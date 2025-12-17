# [2025, Day 11: Reactor](https://adventofcode.com/2025/day/11)


## Solution Notes

There's nothing special about this task: a plain DFS will do. In part 1, it doesn't even need memoization, as the relatively low result suggests.

Memoization is a must for part 2 though, and there are two principal ways to solve the puzzle with it. My first approach, which turned out to be the most size-effective, was to still search from `svr` to `out`, but keep track of the two-bit information whether `dac` and `fft` have been passed along the way. Another solution that many people use is to determine the results from all relevant sub-paths and multiply and add them together as needed. I implemented that one as well, but it doesn't give any tangible benefit compared to by initial solution.

* Part 1, Python: 131 bytes, <100 ms
* Part 2, Python (tagging): 208 bytes, <100 ms
* Part 2, Python (partial paths): 247 bytes, <100 ms
